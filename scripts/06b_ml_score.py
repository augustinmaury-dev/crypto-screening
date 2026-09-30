"""
06b_ml_score.py — Score appris (remplace la formule manuelle de bull_prob_7d).

Tourne juste après 06_score.py. À chaque run :
  1. Relit tout l'historique data/history/scores_*.csv (+ le jour courant).
  2. Calcule le régime de marché, dont l'indice d'ALTSEASON.
  3. Entraîne un modèle (gradient boosting) qui prédit, pour chaque token,
     la probabilité de FAIRE MIEUX QUE LA MÉDIANE DU MARCHÉ dans HORIZON jours.
     → réentraîné chaque jour avec toutes les prédictions déjà mesurables :
       c'est la boucle d'apprentissage.
  4. En altseason, adapte le classement (voir section ALTSEASON).
  5. Réécrit data/computed/scores.csv (+ le snapshot du jour dans history/).

Colonnes produites / modifiées dans scores.csv :
  outperf_prob_7d     probabilité (%) de battre la médiane du marché à 7 j
  score, bull_prob_7d = outperf_prob_7d (compatibilité dashboard / rapports)
  bull_prob_7d_legacy ancienne formule manuelle (conservée pour comparaison)
  score_model         modèle utilisé ce jour-là (ml_gb, ml_gb+alt_blend, ml_gb+alt_model, legacy)
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
FALLBACK_BEAT  = 0.45   # si le top 20 du modèle bat la médiane moins de 45 % du temps sur 5 semaines → règle simple
                        # (marge sous 50 % pour ne pas basculer sur du bruit : le modèle est tombé à ~35-40 %
                        #  pendant 2 semaines lors du changement de régime mi-août, puis est remonté à 55-65 %)

# ALTSEASON
# Indice = % des 100 plus grosses altcoins (hors BTC, stablecoins) qui ont fait mieux que BTC
# sur la période. Seuils classiques (indice "Altcoin Season" sur 90 j) : ≥ 75 altseason, ≤ 25 saison BTC.
ALT_SEASON_90  = 75
BTC_SEASON_90  = 25
ALT_ACTIVE_30  = 60     # régime alt "actif" à court terme (utilisé pour adapter le score)
ALT_MOMENTUM_W = 0.25   # poids du momentum mélangé au modèle en régime alt (testé : 61,5 % → 66 % sur 10 jours)
MIN_ALT_DAYS   = 30     # nb de jours alt mesurés nécessaires pour entraîner un modèle dédié à l'altseason

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
MOMENTUM_FEATS = ["p_ma50", "ret_past7", "rsi_14"]
# Calibration : le boosting est trop sûr de lui (hors échantillon, quand il annonce 75 % la réalité est ~67 %).
# On ramène les probabilités vers 50 % : p = 0.5 + k·(p_brut − 0.5), k mesuré chaque jour sur les 5 dernières semaines.
DEFAULT_SHRINK = 0.55   # valeur mesurée le 25/09/2026 (juin→septembre)


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

    # ── auto-évaluation hors échantillon : entraîne sur le passé, teste sur les 5 dernières semaines ─
    split = cutoff - pd.Timedelta(days=35)
    tr_old = train[train["date"] < split - pd.Timedelta(days=HORIZON)]
    te_new = train[train["date"] >= split].copy()
    oos = {}
    if len(tr_old) >= MIN_TRAIN_ROWS and not te_new.empty:
        m = make_model().fit(tr_old[FEATS], tr_old["y"])
        te_new["p"] = m.predict_proba(te_new[FEATS])[:, 1]
        te_new["naive"] = -te_new["vol_30d_ann"] - te_new["log_rank"]
        oos["model_top20_beat"], oos["days"] = top_beat_rate(pd, te_new, "p")
        oos["naive_top20_beat"], _ = top_beat_rate(pd, te_new, "naive")
        xc = te_new["p"] - 0.5
        if float((xc ** 2).sum()) > 0:
            oos["shrink_k"] = float(np.clip((xc * (te_new["y"] - 0.5)).sum() / (xc ** 2).sum(), 0.2, 1.0))
        log.info(f"Auto-évaluation 5 dernières semaines : modèle {oos['model_top20_beat']:.0%} "
                 f"/ règle simple {oos['naive_top20_beat']:.0%} (top {TOP_N_EVAL} qui bat la médiane)")

    # ── modèle principal, entraîné sur tout ce qui est mesurable ──────────
    model = make_model().fit(train[FEATS], train["y"])
    today_X["p_model"] = model.predict_proba(today_X[FEATS])[:, 1]
    model_name = "ml_gb"

    # Garde-fou : si le modèle perd récemment contre le hasard, on passe à la règle simple
    if oos.get("model_top20_beat") is not None and oos["model_top20_beat"] < FALLBACK_BEAT:
        log.warning(f"Modèle sous {FALLBACK_BEAT:.0%} sur les dernières semaines → règle simple (grosses caps peu volatiles)")
        naive = -today_X["vol_30d_ann"] - today_X["log_rank"]
        today_X["p_model"] = 0.5 + 0.2 * (naive.rank(pct=True) - 0.5)
        model_name = "naive_fallback"

    # ── ALTSEASON ────────────────────────────────────────────────────────
    # En altseason, les règles changent : la prime aux grosses caps peu volatiles disparaît
    # et le momentum redevient payant. Deux niveaux :
    #   a) assez de jours alt mesurés (≥ MIN_ALT_DAYS) → modèle entraîné UNIQUEMENT sur ces jours ;
    #   b) sinon → mélange prudent du modèle avec un score momentum (ALT_MOMENTUM_W).
    a30 = reg_today.get("alt_index_30d")
    alt_days_train = train.loc[train["alt30"] >= ALT_ACTIVE_30, "date"].nunique()
    if a30 is not None and a30 >= ALT_ACTIVE_30 and model_name == "ml_gb":
        if alt_days_train >= MIN_ALT_DAYS:
            alt_tr = train[train["alt30"] >= ALT_ACTIVE_30]
            alt_model = make_model().fit(alt_tr[FEATS], alt_tr["y"])
            today_X["p_model"] = alt_model.predict_proba(today_X[FEATS])[:, 1]
            model_name = "ml_gb+alt_model"
        else:
            mom = today_X[MOMENTUM_FEATS].mean(axis=1).rank(pct=True)
            base = today_X["p_model"].rank(pct=True)
            blended_rank = (1 - ALT_MOMENTUM_W) * base + ALT_MOMENTUM_W * mom
            # on garde l'échelle de probabilité du modèle, réordonnée selon le mélange
            probs = today_X["p_model"].sort_values().values
            today_X["p_model"] = probs[(blended_rank.rank(method="first").astype(int) - 1).values]
            model_name = "ml_gb+alt_blend"
        log.info(f"Régime alt actif (indice 30j = {a30}) → {model_name} "
                 f"({alt_days_train}/{MIN_ALT_DAYS} jours alt mesurés pour un modèle dédié)")

    # ── calibration des probabilités ─────────────────────────────────────
    k = oos.get("shrink_k", DEFAULT_SHRINK)
    today_X["p_model"] = 0.5 + k * (today_X["p_model"] - 0.5)
    log.info(f"Calibration : probabilités ramenées vers 50 % (k = {k:.2f})")

    # ── écriture ─────────────────────────────────────────────────────────
    probs = dict(zip(today_X["symbol"], (today_X["p_model"] * 100).round(1)))
    btc_p = probs.get("BTCUSDT")
    with open(scores_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys()) if rows else []
    for extra in ("outperf_prob_7d", "bull_prob_7d_legacy", "score_model", "market_regime", "alt_index_30d", "alt_index_90d",
                  "derivative", "rank_source", "ret_30d_pct", "leader", "leader_rank", "leader_label",
                  "runup_180d_pct", "already_exploded"):
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
            if btc_p is not None:
                alpha = round(p - btc_p, 1)
                r["alpha_vs_btc"] = alpha
                r["vs_btc_label"] = ("🟢 Surperforme BTC" if alpha >= 5 else "🔴 Sous-performe BTC" if alpha <= -5 else "≈ Neutre vs BTC")
        else:  # stablecoins / suspects / dérivés : hors modèle, rangés en bas
            r["outperf_prob_7d"] = ""
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
        {"today": {"date": TODAY, **reg_today}, "history": hist_reg[-120:]}, ensure_ascii=False, indent=1), encoding="utf-8")
    try:  # lecture des facteurs dominants via une régression logistique (plus lisible que le boosting)
        from sklearn.linear_model import LogisticRegression
        lr = LogisticRegression(C=0.05, max_iter=2000).fit(train[FEATS], train["y"])
        coefs = sorted(zip(FEATS, lr.coef_[0]), key=lambda x: -abs(x[1]))[:10]
    except Exception:
        coefs = []
    LEARNING.mkdir(parents=True, exist_ok=True)
    (LEARNING / "model_report.json").write_text(json.dumps({
        "date": TODAY, "horizon_days": HORIZON, "target": "bat la médiane du marché",
        "model_used_today": model_name, "calibration_k": round(float(k), 3), "train_rows": int(len(train)),
        "train_days": int(train["date"].nunique()), "alt_days_measured": int(alt_days_train),
        "min_alt_days_for_alt_model": MIN_ALT_DAYS,
        "coingecko_ranks_missing_today": bool(today_ranks_carried),
        "derivatives_excluded": {"count": len(derivatives_today), "tokens": derivatives_today},
        "already_exploded": {"rule": f"hausse ≥ +{EXPLODED_RUNUP:.0%} sur {RUNUP_WINDOW} j",
                             "count_today": int((run_today >= EXPLODED_RUNUP).sum()),
                             "leaders_removed_second_wave": [s.replace("USDT", "") for s in second_wave]},
        "leaders": {"label": leader_label, "rule": f"perf 30 j ≥ percentile {LEADER_PCT:.0%} et ≤ {LEADER_DIST:.0%} du plus haut 90 j",
                    "tokens": [{"symbol": s.replace("USDT", ""), "ret_30d_pct": round(float(r30_today[s]) * 100, 1),
                                "dist_high_90d_pct": round(float(dh_today.get(s, 0)) * 100, 1)} for s in leaders]},
        "oos_last_5_weeks": {k: (round(v, 3) if isinstance(v, float) else v) for k, v in oos.items()},
        "top_factors": [{"feature": f, "effect": round(float(c), 3)} for f, c in coefs],
        "regime": reg_today,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    log.info(f"Score appris écrit ({model_name}) : {len(probs)} tokens, entraînement {len(train)} lignes")


if __name__ == "__main__":
    run()
