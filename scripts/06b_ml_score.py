"""
06b_ml_score.py — Score appris (remplace la formule manuelle de bull_prob_7d).

Tourne juste après 06_score.py. À chaque run :
  1. Relit tout l'historique data/history/scores_*.csv (+ le jour courant).
  2. Calcule le régime de marché, dont l'indice d'ALTSEASON.
  3. Entraîne un modèle (gradient boosting) qui prédit, pour chaque token,
     la probabilité de FAIRE MIEUX QUE LA MÉDIANE DU MARCHÉ dans HORIZON jours.
     → réentraîné chaque jour avec toutes les prédictions déjà mesurables :
       c'est la boucle d'apprentissage.
  4. ANALYSE DES ERREURS (depuis le 11/11/2026) : le modèle, une règle simple (« grosse cap peu volatile »)
     et leur MÉLANGE sont rejoués semaine après semaine sur les ~4 derniers mois (chaque semaine n'est prédite
     qu'avec des données antérieures). Le classement du jour = le mélange, sauf si l'un des deux fait pire que
     le hasard sur la période. La probabilité affichée = taux de réussite réellement observé à ce rang.
     Chaque méthode est aussi jugée contre BTC et en hausse absolue → data/learning/backtest_7d.json.
  5. Réécrit data/computed/scores.csv (+ le snapshot du jour dans history/).

Colonnes produites / modifiées dans scores.csv :
  outperf_prob_7d     probabilité (%) de battre la médiane du marché à 7 j
  score, bull_prob_7d = outperf_prob_7d (compatibilité dashboard / rapports)
  bull_prob_7d_legacy ancienne formule manuelle (conservée pour comparaison)
  score_model         méthode du jour (ml_blend = mélange modèle + règle ; ml_gb = modèle seul ; naive_rule = règle seule)
  pct_model_7d, pct_rule_7d  rang (0-100) du token selon le modèle seul / la règle seule
  rank_7d, avoid      rang dans le classement du jour ; avoid = fait partie des 20 derniers (« à éviter »)
  market_regime, alt_index_30d, alt_index_90d

Si scikit-learn est absent ou si les données sont insuffisantes, le script
ne touche à rien (le score reste celui de 06_score.py) : le pipeline ne casse jamais.

Recherche ayant motivé ce choix (25/09/2026, walk-forward avril→septembre 2026) :
  top 20 qui bat la médiane à 7 j — formule manuelle 41 %, ce modèle 64 %.
"""
from __future__ import annotations
import csv, json, warnings
from datetime import datetime, timedelta
from common import ROOT, TODAY, COMPUTED, HISTORY, setup_logger, is_derivative_token, tier_from_rank

log = setup_logger("06b_ml_score")
warnings.filterwarnings("ignore")
LEARNING = ROOT / "data" / "learning"

# ─────────────────────────── paramètres ────────────────────────────────────
HORIZON        = 7      # jours. Changer ici pour tester un autre horizon (3, 14…).
MIN_TRAIN_ROWS = 5000   # en dessous : pas de modèle, on garde l'ancien score
TOP_N_EVAL     = 20     # taille du "top" pour l'auto-évaluation

# ALTSEASON
# Indice = % des 100 plus grosses altcoins (hors BTC, stablecoins) qui ont fait mieux que BTC
# sur la période. Seuils classiques (indice "Altcoin Season" sur 90 j) : ≥ 75 altseason, ≤ 25 saison BTC.
ALT_SEASON_90  = 75
BTC_SEASON_90  = 25
ALT_ACTIVE_30  = 60     # indice 30 j élevé (étiquettes de régime, groupe « altseason » des leaders)
# MODE ALTSEASON ABANDONNÉ le 11/11/2026. Il mélangeait du momentum au classement (puis utilisait un modèle dédié)
# quand l'indice 30 j dépassait 60. Résultats : en réel 51 % (mode actif) contre 68 % (inactif) ; rejoué sur
# 31 jours d'altseason, le mélange momentum fait 53 % contre 57 % pour le modèle seul et 65 % pour la règle simple.
# Sur 2,6 ans de cours Binance (941 jours), un indice 30 j ≥ 75 % a été suivi d'une altcoin médiane à −18 % en
# 30 j (17 % seulement battent BTC) : un indice élevé annonce la FIN de la surperformance des altcoins, pas son
# début. Le momentum 30 j est d'ailleurs le pire signal testé (top 20 : 37 % battent la médiane à 30 j).
# → l'indice sert désormais de thermomètre (06d_market_state.py), plus à modifier le classement.

# ANALYSE DES ERREURS (walk-forward)
WF_DAYS        = 126    # nb de jours rejoués (≈ 4 mois)
WF_STEP        = 7      # le modèle testé est réentraîné toutes les semaines, uniquement sur le passé
MIN_COMPONENT  = 0.50   # un composant (modèle ou règle) sous 50 % sur la période est écarté du mélange
AVOID_N        = 20     # taille de la liste « à éviter » (bas du classement)

# LEADERS (ajouté le 29/09/2026 après l'analyse de NEAR, UNI, ZEC…)
# Le score principal vise « battre la médiane » : il est prudent et évite les tokens qui explosent
# (son top 20 ne contient que 6 % de futurs top 10 %). Les leaders forment une 2e liste, transparente :
#   perf 30 j dans le top 10 % de l'univers  ET  à moins de 5 % du plus haut 90 j.
# Backtest juin→sept. 2026 (top 20 leaders/jour, 14 j) : 19 % deviennent des top 10 % (hasard : 10 %),
#   excès moyen +3,4 %, médiane ≈ 0 → profil « loterie » hors altseason ;
#   en altseason : 67 % battent la médiane, excès médian +5,8 %, moyen +18,5 %.
#   UNI est devenu leader le 23/07, jour du départ de sa hausse de +235 %.
LEADER_PCT     = 0.90   # percentile minimum de la perf 30 j
LEADER_DIST    = 0.05   # distance max au plus haut 90 j
LEADER_MAX     = 15     # nombre max affiché

# DÉJÀ EXPLOSÉ (ajouté le 30/09/2026, idée d'Augustin : « une crypto qui a déjà explosé a moins de chances
# d'exploser à nouveau »). Vérifié sur 2 ans de cours Binance (juil. 2024 → sept. 2026, 391 tokens, 21 900 cas) :
#   hausse ≥ +100 % dans les 180 derniers jours → bat le marché à 30 j dans 40-47 % des cas (vs 53 % sinon),
#   refait +100 % en 90 j deux fois moins souvent (1-2 % vs 3,5 %). Vrai dans les deux moitiés de la période
#   et dans tous les régimes ; plus l'explosion passée est forte, plus l'effet est net.
#   Leaders (bat le marché à 7 j / 30 j) : 1re hausse 50 % / 51 % ; avec une explosion AVANT la hausse actuelle
#   (runup_prev ≥ 100 %) 43 % / 32 % → ces « 2e vagues » sont retirées de la liste des leaders.
#   Confirmé sur l'historique du projet (juin→sept. 2026) : 2e vagues 37 % à 14 j (excès moyen −15 pts),
#   1res hausses 52 % (+8 pts). En revanche, ajouté comme variable du modèle principal, ça n'apporte rien
#   (top 20 : 62,7 % → 62,0 %) : le modèle évite déjà ces tokens (seulement 6 % de son top 20). On s'en sert
#   donc pour les leaders et pour l'affichage (colonnes runup_180d_pct / already_exploded, badge 💥).
RUNUP_WINDOW   = 180    # jours regardés en arrière
RUNUP_RECENT   = 30     # runup_prev = explosion terminée avant les 30 derniers jours (≠ hausse en cours)
EXPLODED_RUNUP = 1.0    # +100 % = « a explosé »

PATS = ["uptrend", "downtrend", "macd_bullish_cross", "macd_bearish_cross", "golden_cross", "death_cross",
        "double_top_90d", "double_bottom_90d", "support_bounce", "resistance_test", "rsi_bullish_divergence",
        "rsi_bearish_divergence", "squeeze_breakout", "breakout_30d", "breakdown_30d", "bull_flag", "bear_flag"]
FEATS = ["rsi_14", "vol_30d_ann", "drawdown_90d", "dist_to_high_90d", "vol_ratio_vs_med90", "corr_btc_90d",
         "p_ma50", "p_ma200", "macd_n", "log_rank", "log_vol24", "change_24h_pct", "bull_signals", "bear_signals",
         "catalyst_score", "trend_rank", "ret_past7", "ret_past3",
         "score_momentum", "score_risk", "score_signal", "score_solidity"] + ["pat_" + p for p in PATS]
METHOD_LABEL = {"ml_blend": "mélange modèle + règle", "ml_gb": "modèle appris seul", "naive_rule": "règle simple seule"}


# ─────────────────────────── données ───────────────────────────────────────

def load_history(pd):
    frames = []
    for f in sorted(HISTORY.glob("scores_*.csv")):
        d = f.stem.replace("scores_", "")
        if len(d) != 8 or not d.isdigit():
            continue
        try:
            df = pd.read_csv(f, low_memory=False)
        except Exception as e:
            log.warning(f"Lecture {f.name} impossible : {e}"); continue
        df["date"] = pd.Timestamp(datetime.strptime(d, "%Y%m%d"))
        frames.append(df)
    return pd.concat(frames, ignore_index=True) if frames else None


def fill_missing_ranks(pd, raw):
    """Si CoinGecko a échoué un jour (< 50 % des tokens avec un rang), reprend le dernier
    rang connu de chaque token. Les rangs bougent peu d'un jour à l'autre ; sans ça, l'indice
    altseason, les tiers et la variable « taille » du modèle sont faussés (incident du 29/09/2026)."""
    r = pd.to_numeric(raw["rank_mcap"], errors="coerce") if "rank_mcap" in raw else pd.Series(float("nan"), index=raw.index)
    cov = r.notna().groupby(raw["date"]).mean()
    bad = set(cov[cov < 0.5].index)
    if not bad:
        return raw, []
    raw = raw.sort_values("date").copy()
    r = r.loc[raw.index]
    trusted = r.where(~raw["date"].isin(bad))
    carried = trusted.groupby(raw["symbol"]).ffill()
    is_bad = raw["date"].isin(bad)
    raw.loc[is_bad, "rank_mcap"] = r[is_bad].fillna(carried[is_bad])
    return raw, sorted(bad)


def is_true(s):
    return s.astype(str).str.lower().eq("true")


def shifted_prices(pd, price, offset_days, tol=2):
    """Prix à J+offset (ou J+offset±tol vers l'extérieur) pour chaque (date, symbol)."""
    idx = set(price.index)
    step = 1 if offset_days >= 0 else -1
    rows = {}
    for d in price.index:
        for e in range(tol + 1):
            t = d + pd.Timedelta(days=offset_days + step * e)
            if t in idx:
                rows[d] = price.loc[t]; break
    return pd.DataFrame(rows).T.reindex(price.index)


def runup_tables(pd, np, price):
    """Pour chaque (date, token) : la plus forte hausse (plus haut / plus bas qui le précède, − 1) sur les
    RUNUP_WINDOW derniers jours (runup_180d), et la même chose en s'arrêtant RUNUP_RECENT jours avant (runup_prev)."""
    days = ((price.index - price.index[0]) / pd.Timedelta(days=1)).astype(int).to_numpy()
    vals = price.to_numpy(dtype=float)
    run = np.full(vals.shape, np.nan); prev = np.full(vals.shape, np.nan)
    for j in range(vals.shape[1]):
        col = vals[:, j]
        for i in range(len(days)):
            if not col[i] > 0:
                continue
            m = (days >= days[i] - RUNUP_WINDOW) & (days <= days[i]) & (col > 0)
            w = col[m]
            run[i, j] = float((w / np.minimum.accumulate(w)).max() - 1)
            wp = col[m & (days <= days[i] - RUNUP_RECENT)]
            prev[i, j] = float((wp / np.minimum.accumulate(wp)).max() - 1) if len(wp) else 0.0
    return (pd.DataFrame(run, index=price.index, columns=price.columns),
            pd.DataFrame(prev, index=price.index, columns=price.columns))


def build_features(pd, np, raw, price):
    X = raw.copy()
    num = lambda c: pd.to_numeric(X[c], errors="coerce") if c in X else pd.Series(np.nan, index=X.index)
    X["p_ma50"]     = np.log(num("price") / num("ma_50"))
    X["p_ma200"]    = np.log(num("price") / num("ma_200"))
    X["macd_n"]     = num("macd_hist") / num("price")
    X["log_rank"]   = np.log1p(num("rank_mcap").fillna(2000))
    X["log_vol24"]  = np.log1p(num("vol_24h_usd"))
    X["trend_rank"] = X["trending_rank"].notna().astype(int) if "trending_rank" in X else 0
    for name, off in (("ret_past7", -7), ("ret_past3", -3)):
        past = price / shifted_prices(pd, price, off) - 1
        s = past.stack().rename(name).reset_index()
        s.columns = ["date", "symbol", name]
        X = X.merge(s, on=["date", "symbol"], how="left")
    pat = X["patterns"].fillna("") if "patterns" in X else pd.Series("", index=X.index)
    for p in PATS:
        X["pat_" + p] = pat.str.contains(p, regex=False).astype(int)
    # Normalisation en rang par jour : on compare les tokens ENTRE EUX, quel que soit le régime
    Z = X[["date", "symbol"]].copy()
    for c in FEATS:
        v = pd.to_numeric(X[c], errors="coerce") if c in X else pd.Series(np.nan, index=X.index)
        Z[c] = (v.groupby(X["date"]).rank(pct=True) - 0.5).fillna(0.0)
    return Z


def compute_regime(pd, np, raw, price):
    """Par jour : indice altseason 30 j / 90 j, perf BTC, largeur du marché."""
    rank = raw.pivot_table(index="date", columns="symbol", values="rank_mcap", aggfunc="first")
    out = {}
    past = {n: price / shifted_prices(pd, price, -n, tol=3) - 1 for n in (30, 90)}
    for d in price.index:
        r = rank.loc[d].dropna().sort_values() if d in rank.index else pd.Series(dtype=float)
        top = [s for s in r.index if s != "BTCUSDT"][:100]
        row = {}
        for n, P in past.items():
            b = P.loc[d].get("BTCUSDT", np.nan)
            v = P.loc[d, [s for s in top if s in P.columns]].dropna()
            row[f"alt_index_{n}d"] = round(float((v > b).mean() * 100), 1) if len(v) >= 20 and b == b else None
            row[f"btc_ret_{n}d"]  = round(float(b * 100), 1) if b == b else None
        g = raw[raw["date"] == d]
        ma = pd.to_numeric(g["ma_50"], errors="coerce"); p = pd.to_numeric(g["price"], errors="coerce")
        row["breadth_ma50"] = round(float((p > ma).mean() * 100), 1)
        out[d] = row
    return out


def regime_label(r: dict) -> str:
    a90, a30 = r.get("alt_index_90d"), r.get("alt_index_30d")
    if a90 is not None and a90 >= ALT_SEASON_90:
        return "Altseason"
    if a90 is not None and a90 <= BTC_SEASON_90:
        return "Saison Bitcoin"
    if a30 is not None and a30 >= ALT_SEASON_90:
        return "Altseason en formation"
    if a30 is not None and a30 >= ALT_ACTIVE_30:   # même seuil que le mode altseason du classement (unifié le 26/10/2026)
        return "Altseason modérée"
    if a30 is not None and a30 <= BTC_SEASON_90:
        return "Bitcoin domine (court terme)"
    return "Neutre"


# ─────────────────────────── modèle ────────────────────────────────────────

def make_model():
    from sklearn.ensemble import HistGradientBoostingClassifier
    return HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, max_iter=200,
                                          min_samples_leaf=200, random_state=0)


def top_beat_rate(pd, df, col):
    rates = []
    for _, g in df.groupby("date"):
        if len(g) < 50: continue
        top = g.nlargest(TOP_N_EVAL, col)
        rates.append(float((top["excess"] > 0).mean()))
    return (sum(rates) / len(rates), len(rates)) if rates else (None, 0)


def rule_score(df):
    """Règle simple : grosse capitalisation + peu volatile (variables déjà en rang du jour)."""
    return -df["vol_30d_ann"] - df["log_rank"]


def walk_forward(pd, np, train):
    """Rejoue le passé : pour chaque semaine des WF_DAYS derniers jours mesurables, entraîne le modèle sur ce qui
    précède (purge de HORIZON jours) puis prédit la semaine. Renvoie les prédictions hors échantillon."""
    dates = sorted(train["date"].unique())
    tests = dates[-WF_DAYS:]
    out = []
    for i in range(0, len(tests), WF_STEP):
        block = tests[i:i + WF_STEP]
        tr = train[train["date"] <= block[0] - pd.Timedelta(days=HORIZON)]
        if len(tr) < MIN_TRAIN_ROWS:
            continue
        te = train[train["date"].isin(block)].copy()
        te["model"] = make_model().fit(tr[FEATS], tr["y"]).predict_proba(te[FEATS])[:, 1]
        out.append(te)
    if not out:
        return None
    R = pd.concat(out, ignore_index=True)
    R["rule"] = rule_score(R)
    g = R.groupby("date")
    R["blend"] = g["model"].rank(pct=True) + g["rule"].rank(pct=True)
    return R


def evaluate_strategies(pd, np, R):
    """Par méthode : résumé + série quotidienne. Trois juges : la médiane du marché, BTC, et la hausse absolue."""
    daily = {"dates": [], "median": [], "btc": [], "up_share": []}
    strat = {k: {"beat": [], "beat_btc": [], "up": [], "basket": [], "ic": []} for k in ("model", "rule", "blend")}
    for d, g in R.groupby("date"):
        if len(g) < 50:
            continue
        btc = g["btc_fwd"].iloc[0]
        daily["dates"].append(pd.Timestamp(d).strftime("%Y%m%d"))
        daily["median"].append(round(float(g["fwd"].median()) * 100, 2))
        daily["btc"].append(round(float(btc) * 100, 2) if btc == btc else None)
        daily["up_share"].append(round(float((g["fwd"] > 0).mean()), 3))
        for k, st in strat.items():
            t = g.nlargest(TOP_N_EVAL, k)
            st["beat"].append(round(float((t["excess"] > 0).mean()), 3))
            st["beat_btc"].append(round(float((t["fwd"] > btc).mean()), 3) if btc == btc else None)
            st["up"].append(round(float((t["fwd"] > 0).mean()), 3))
            st["basket"].append(round(float(t["fwd"].mean()) * 100, 2))
            ic = g[k].corr(g["excess"], method="spearman")
            st["ic"].append(round(float(ic), 3) if ic == ic else None)
    mean = lambda v: round(float(np.mean([x for x in v if x is not None])), 3) if any(x is not None for x in v) else None
    summary = {}
    for k, st in strat.items():
        pct = R.groupby("date")[k].rank(pct=True)
        q = np.minimum((pct * 5).astype(int), 4)
        quint = (R["excess"] > 0).groupby(q).mean()
        bot = [float((g.nsmallest(AVOID_N, k)["excess"] > 0).mean()) for _, g in R.groupby("date") if len(g) >= 50]
        summary[k] = {"top20_beat": mean(st["beat"]), "top20_beat_btc": mean(st["beat_btc"]), "top20_up": mean(st["up"]),
                      "basket_ret_pct": round(float(np.mean(st["basket"])), 2), "ic": mean(st["ic"]),
                      "bottom20_beat": round(float(np.mean(bot)), 3) if bot else None,
                      "quintiles_beat": [round(float(quint.get(i, np.nan)), 3) for i in (4, 3, 2, 1, 0)]}   # Q1 = mieux classés
    summary["universe"] = {"median_ret_pct": round(float(np.mean(daily["median"])), 2),
                           "btc_ret_pct": mean([x / 1 if x is not None else None for x in daily["btc"]]),
                           "up_share": mean(daily["up_share"]),
                           "alts_beat_btc": round(float((R["fwd"] > R["btc_fwd"]).mean()), 3)}
    return summary, daily, strat


# ─────────────────────────── entrée principale ─────────────────────────────

def run():
    try:
        import numpy as np, pandas as pd
        import sklearn  # noqa: F401
    except ImportError as e:
        log.warning(f"scikit-learn/pandas absent ({e}) — score manuel conservé. "
                    f"Installer : pip install scikit-learn pandas numpy")
        return

    scores_path = COMPUTED / "scores.csv"
    if not scores_path.exists():
        log.warning("Pas de scores.csv — étape ignorée"); return
    today_df = pd.read_csv(scores_path, low_memory=False)
    today_ts = pd.Timestamp(datetime.strptime(TODAY, "%Y%m%d"))

    raw = load_history(pd)
    if raw is None:
        log.warning("Pas d'historique — étape ignorée"); return
    raw = raw[raw["date"] != today_ts]                     # le jour courant vient de scores.csv
    t = today_df.copy(); t["date"] = today_ts
    raw = pd.concat([raw, t], ignore_index=True)
    raw["price"] = pd.to_numeric(raw["price"], errors="coerce")
    raw = raw[raw["price"] > 0].drop_duplicates(["date", "symbol"], keep="last")
    raw, carried_days = fill_missing_ranks(pd, raw)
    today_ranks_carried = today_ts in carried_days
    if carried_days:
        log.warning(f"Rangs CoinGecko manquants ({len(carried_days)} jour(s), dont aujourd'hui : {today_ranks_carried}) "
                    f"→ dernier rang connu repris")
    excluded = pd.Series(False, index=raw.index)
    for c in ("stablecoin", "suspect"):
        if c in raw: excluded |= is_true(raw[c])
    deriv = pd.Series([is_derivative_token(s, b, a) for s, b, a in
                       zip(raw["symbol"], raw.get("base", raw["symbol"]), raw.get("age_days", [None] * len(raw)))],
                      index=raw.index)
    derivatives_today = sorted(raw.loc[deriv & (raw["date"] == today_ts), "symbol"].str.replace("USDT", ""))
    log.info(f"Tokens dérivés exclus (actions tokenisées, wrapped, staked) : {len(derivatives_today)}")
    carried_rank_today = dict(zip(raw.loc[raw["date"] == today_ts, "symbol"], raw.loc[raw["date"] == today_ts, "rank_mcap"]))
    raw = raw[~(excluded | deriv)]
    price = raw.pivot_table(index="date", columns="symbol", values="price", aggfunc="last").sort_index()

    # ── régime / altseason ────────────────────────────────────────────────
    regimes = compute_regime(pd, np, raw, price)
    reg_today = regimes.get(today_ts, {})
    reg_today["label"] = regime_label(reg_today)
    log.info(f"Régime : {reg_today['label']} — altseason 30j={reg_today.get('alt_index_30d')} "
             f"90j={reg_today.get('alt_index_90d')} BTC 30j={reg_today.get('btc_ret_30d')}%")

    # ── leaders (momentum 30 j + proche du plus haut 90 j) ───────────────
    past30 = price / shifted_prices(pd, price, -30, tol=3) - 1
    r30_today = past30.loc[today_ts].dropna() if today_ts in past30.index else pd.Series(dtype=float)
    today_raw = raw[raw["date"] == today_ts].set_index("symbol")
    dh_today = pd.to_numeric(today_raw["dist_to_high_90d"], errors="coerce") if "dist_to_high_90d" in today_raw else pd.Series(dtype=float)
    r30_pct = r30_today.rank(pct=True)
    runups = runup_tables(pd, np, price)
    run_today = runups[0].loc[today_ts] if today_ts in runups[0].index else pd.Series(dtype=float)
    prev_today = runups[1].loc[today_ts] if today_ts in runups[1].index else pd.Series(dtype=float)
    candidates = [s for s in r30_today.index
                  if r30_pct[s] >= LEADER_PCT and dh_today.get(s, float("nan")) < LEADER_DIST]
    second_wave = sorted(s for s in candidates if prev_today.get(s, 0) >= EXPLODED_RUNUP)
    leaders = sorted([s for s in candidates if s not in second_wave], key=lambda s: -r30_today[s])[:LEADER_MAX]
    if second_wave:
        log.info(f"Leaders écartés (déjà explosé avant la hausse actuelle) : {', '.join(s.replace('USDT', '') for s in second_wave)}")
    alt_now = (reg_today.get("alt_index_30d") or 0) >= ALT_ACTIVE_30
    leader_label = "🚀 Leader (altseason)" if alt_now else "🎲 Leader (spéculatif)"
    log.info(f"Leaders : {len(leaders)} — {', '.join(s.replace('USDT', '') for s in leaders[:8])}")

    # ── features + cible ──────────────────────────────────────────────────
    Z = build_features(pd, np, raw, price)
    fwd = shifted_prices(pd, price, HORIZON) / price - 1
    y = fwd.stack().rename("fwd").reset_index(); y.columns = ["date", "symbol", "fwd"]
    D = Z.merge(y, on=["date", "symbol"], how="left")
    D["excess"] = D["fwd"] - D.groupby("date")["fwd"].transform("median")
    D["alt30"] = D["date"].map(lambda d: (regimes.get(d) or {}).get("alt_index_30d"))
    cutoff = today_ts - pd.Timedelta(days=HORIZON)
    train = D[(D["date"] <= cutoff) & D["fwd"].notna()].copy()
    train["y"] = (train["excess"] > 0).astype(int)
    today_X = D[D["date"] == today_ts].copy()
    if len(train) < MIN_TRAIN_ROWS or today_X.empty:
        log.warning(f"Données insuffisantes ({len(train)} lignes d'entraînement) — score manuel conservé"); return

    # ── ANALYSE DES ERREURS : modèle, règle simple et mélange rejoués semaine après semaine ─────────
    btc_fwd = fwd["BTCUSDT"] if "BTCUSDT" in fwd.columns else pd.Series(np.nan, index=fwd.index)
    train["btc_fwd"] = train["date"].map(btc_fwd)
    wf_summary, wf_daily, wf_strat, calib = {}, {}, {}, None
    R = walk_forward(pd, np, train)
    method = "ml_blend"
    if R is not None and R["date"].nunique() >= 20:
        wf_summary, wf_daily, wf_strat = evaluate_strategies(pd, np, R)
        mb, rb, bb = (wf_summary[k]["top20_beat"] for k in ("model", "rule", "blend"))
        log.info(f"Analyse des erreurs ({R['date'].nunique()} jours rejoués) — top {TOP_N_EVAL} qui bat la médiane : "
                 f"modèle {mb:.0%} / règle simple {rb:.0%} / mélange {bb:.0%} ; contre BTC : "
                 f"{wf_summary['model']['top20_beat_btc']:.0%} / {wf_summary['rule']['top20_beat_btc']:.0%} / {wf_summary['blend']['top20_beat_btc']:.0%}")
        if mb < MIN_COMPONENT <= rb:
            method = "naive_rule"; log.warning(f"Modèle sous {MIN_COMPONENT:.0%} sur la période → règle simple seule")
        elif rb < MIN_COMPONENT <= mb:
            method = "ml_gb"; log.warning(f"Règle simple sous {MIN_COMPONENT:.0%} sur la période → modèle seul")
    else:
        log.warning("Historique trop court pour rejouer le passé — mélange utilisé sans calibration mesurée")

    # ── classement du jour : modèle entraîné sur tout ce qui est mesurable + règle simple ───────────
    model = make_model().fit(train[FEATS], train["y"])
    today_X["s_model"] = model.predict_proba(today_X[FEATS])[:, 1]
    today_X["s_rule"] = rule_score(today_X)
    today_X["pct_model"] = today_X["s_model"].rank(pct=True)
    today_X["pct_rule"] = today_X["s_rule"].rank(pct=True)
    col = {"ml_blend": "blend", "ml_gb": "model", "naive_rule": "rule"}[method]
    today_X["s_final"] = {"blend": today_X["pct_model"] + today_X["pct_rule"], "model": today_X["s_model"], "rule": today_X["s_rule"]}[col]
    today_X["pct"] = today_X["s_final"].rank(pct=True)
    model_name = method

    # ── probabilité honnête : taux de réussite réellement observé à ce niveau de classement ─────────
    # (courbe lisse « rang du jour → part des tokens qui ont battu la médiane », ajustée sur les jours rejoués)
    tp = today_X["pct"].to_numpy()
    if R is not None and len(R) >= MIN_TRAIN_ROWS:
        from sklearn.linear_model import LogisticRegression
        rp = R.groupby("date")[col].rank(pct=True).to_numpy()
        calib = LogisticRegression(C=1e6, max_iter=1000).fit(np.c_[rp, rp ** 2], R["y"].to_numpy())
        today_X["p_model"] = calib.predict_proba(np.c_[tp, tp ** 2])[:, 1]
        yb = (R["fwd"] > R["btc_fwd"]).astype(int).to_numpy()
        calib_btc = LogisticRegression(C=1e6, max_iter=1000).fit(np.c_[rp, rp ** 2], yb)
        today_X["p_btc"] = calib_btc.predict_proba(np.c_[tp, tp ** 2])[:, 1]
    else:
        today_X["p_model"] = 0.5 + 0.2 * (today_X["pct"] - 0.5)
        today_X["p_btc"] = np.nan
    today_X["rank7"] = today_X["s_final"].rank(ascending=False, method="first").astype(int)
    n_ranked = len(today_X)
    alt_days_train = train.loc[train["alt30"] >= ALT_ACTIVE_30, "date"].nunique()

    # ── écriture ─────────────────────────────────────────────────────────
    probs = dict(zip(today_X["symbol"], (today_X["p_model"] * 100).round(1)))
    probs_btc = dict(zip(today_X["symbol"], (today_X["p_btc"] * 100).round(1)))
    pct_m = dict(zip(today_X["symbol"], (today_X["pct_model"] * 100).round(0)))
    pct_r = dict(zip(today_X["symbol"], (today_X["pct_rule"] * 100).round(0)))
    rank7 = dict(zip(today_X["symbol"], today_X["rank7"]))
    btc_p = probs.get("BTCUSDT")
    with open(scores_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys()) if rows else []
    for extra in ("outperf_prob_7d", "bull_prob_7d_legacy", "score_model", "market_regime", "alt_index_30d", "alt_index_90d",
                  "derivative", "rank_source", "ret_30d_pct", "leader", "leader_rank", "leader_label",
                  "runup_180d_pct", "already_exploded", "beat_btc_prob_7d", "pct_model_7d", "pct_rule_7d", "rank_7d", "avoid"):
        if extra not in fields: fields.append(extra)
    for r in rows:
        r["bull_prob_7d_legacy"] = r.get("bull_prob_7d_legacy") or r.get("bull_prob_7d", "")
        r["derivative"] = is_derivative_token(r["symbol"], r.get("base"), r.get("age_days"))
        r30 = r30_today.get(r["symbol"])
        r["ret_30d_pct"] = round(float(r30) * 100, 1) if r30 is not None and r30 == r30 else ""
        r["leader"] = r["symbol"] in leaders
        r["leader_rank"] = leaders.index(r["symbol"]) + 1 if r["leader"] else ""
        r["leader_label"] = leader_label if r["leader"] else ""
        ru = run_today.get(r["symbol"])
        r["runup_180d_pct"] = round(float(ru) * 100) if ru is not None and ru == ru else ""
        r["already_exploded"] = bool(ru is not None and ru == ru and ru >= EXPLODED_RUNUP)
        r["rank_source"] = "coingecko" if r.get("rank_mcap") else ""
        if today_ranks_carried and not r.get("rank_mcap"):
            cr = carried_rank_today.get(r["symbol"])
            if cr is not None and cr == cr:
                r["rank_mcap"] = int(cr); r["tier"] = tier_from_rank(cr); r["rank_source"] = "dernier connu"
        p = probs.get(r["symbol"])
        if p is not None:
            r["outperf_prob_7d"] = p
            r["score"] = p
            r["bull_prob_7d"] = p
            r["score_model"] = model_name
            pb = probs_btc.get(r["symbol"])
            r["beat_btc_prob_7d"] = pb if pb is not None and pb == pb else ""
            r["pct_model_7d"] = int(pct_m[r["symbol"]]); r["pct_rule_7d"] = int(pct_r[r["symbol"]])
            r["rank_7d"] = int(rank7[r["symbol"]])
            r["avoid"] = bool(rank7[r["symbol"]] > n_ranked - AVOID_N)
            if btc_p is not None:
                alpha = round(p - btc_p, 1)
                r["alpha_vs_btc"] = alpha
                r["vs_btc_label"] = ("🟢 Surperforme BTC" if alpha >= 5 else "🔴 Sous-performe BTC" if alpha <= -5 else "≈ Neutre vs BTC")
        else:  # stablecoins / suspects / dérivés : hors modèle, rangés en bas
            r["outperf_prob_7d"] = ""
            r["beat_btc_prob_7d"] = r["pct_model_7d"] = r["pct_rule_7d"] = r["rank_7d"] = ""
            r["avoid"] = False
            r["score"] = 0
            r["score_model"] = "exclu_derive" if r["derivative"] else "exclu"
        r["market_regime"] = reg_today["label"]
        r["alt_index_30d"] = reg_today.get("alt_index_30d")
        r["alt_index_90d"] = reg_today.get("alt_index_90d")
    rows.sort(key=lambda r: (1 if (str(r.get("stablecoin")).lower() == "true" or r["derivative"]) else 0, -float(r.get("score") or 0)))
    with open(scores_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    (HISTORY / f"scores_{TODAY}.csv").write_text(scores_path.read_text(encoding="utf-8"), encoding="utf-8")

    # ── rapports JSON ────────────────────────────────────────────────────
    hist_reg = [{"date": d.strftime("%Y%m%d"), **v, "label": regime_label(v)} for d, v in sorted(regimes.items())]
    (COMPUTED / "market_regime.json").write_text(json.dumps(
        {"today": {"date": TODAY, **reg_today}, "history": hist_reg}, ensure_ascii=False, indent=1), encoding="utf-8")
    try:  # lecture des facteurs dominants via une régression logistique (plus lisible que le boosting)
        from sklearn.linear_model import LogisticRegression
        lr = LogisticRegression(C=0.05, max_iter=2000).fit(train[FEATS], train["y"])
        coefs = sorted(zip(FEATS, lr.coef_[0]), key=lambda x: -abs(x[1]))[:10]
    except Exception:
        coefs = []
    LEARNING.mkdir(parents=True, exist_ok=True)
    (LEARNING / "model_report.json").write_text(json.dumps({
        "date": TODAY, "horizon_days": HORIZON, "target": "bat la médiane du marché",
        "model_used_today": model_name, "method_label": METHOD_LABEL.get(model_name, model_name), "train_rows": int(len(train)),
        "train_days": int(train["date"].nunique()), "alt_days_measured": int(alt_days_train),
        "alt_mode": "abandonné le 11/11/2026 (voir 06b_ml_score.py)",
        "coingecko_ranks_missing_today": bool(today_ranks_carried),
        "derivatives_excluded": {"count": len(derivatives_today), "tokens": derivatives_today},
        "already_exploded": {"rule": f"hausse ≥ +{EXPLODED_RUNUP:.0%} sur {RUNUP_WINDOW} j",
                             "count_today": int((run_today >= EXPLODED_RUNUP).sum()),
                             "leaders_removed_second_wave": [s.replace("USDT", "") for s in second_wave]},
        "leaders": {"label": leader_label, "rule": f"perf 30 j ≥ percentile {LEADER_PCT:.0%} et ≤ {LEADER_DIST:.0%} du plus haut 90 j",
                    "tokens": [{"symbol": s.replace("USDT", ""), "ret_30d_pct": round(float(r30_today[s]) * 100, 1),
                                "dist_high_90d_pct": round(float(dh_today.get(s, 0)) * 100, 1)} for s in leaders]},
        "walk_forward": {"days": int(R["date"].nunique()) if R is not None else 0,
                         "window": [wf_daily["dates"][0], wf_daily["dates"][-1]] if wf_daily.get("dates") else [],
                         **wf_summary},
        "avoid_today": [s.replace("USDT", "") for s in today_X.sort_values("rank7").tail(AVOID_N)["symbol"]],
        "top_factors": [{"feature": f, "effect": round(float(c), 3)} for f, c in coefs],
        "regime": reg_today,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    if wf_daily.get("dates"):
        (LEARNING / "backtest_7d.json").write_text(json.dumps(
            {"date": TODAY, "horizon_days": HORIZON, "top_n": TOP_N_EVAL, "method_today": model_name,
             "note": "Chaque jour est prédit par un modèle entraîné uniquement sur des données antérieures (réentraînement hebdomadaire).",
             "summary": wf_summary, **wf_daily, "strategies": wf_strat}, ensure_ascii=False), encoding="utf-8")
    log.info(f"Score appris écrit ({model_name}) : {len(probs)} tokens, entraînement {len(train)} lignes")


if __name__ == "__main__":
    run()
