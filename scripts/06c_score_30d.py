"""
06c_score_30d.py — Prévision à 30 jours (ajoutée le 12/10/2026, demande d'Augustin).

Même principe que le score à 7 jours (06b_ml_score.py) : analyse technique → apprentissage → analyse des erreurs.
Différence : à 30 jours, l'historique des snapshots (depuis avril 2026) est trop court ; on apprend donc sur les
cours journaliers Binance des ~1000 derniers jours (téléchargés ici, en parallèle, et mis en cache 12 h ;
à défaut, les klines 365 j de 02_fetch_klines.py).

Chaque jour :
  1. Variables techniques par token et par jour (rangs du jour, robustes aux régimes) :
     perf 7/30/90/180 j, volatilité 30/90 j, distance au plus haut 90 j, écart aux MA50/MA200,
     tendance des volumes, taille (volume échangé), plus forte hausse sur 180 j (« déjà explosé »).
  2. Cible : faire mieux que la médiane de l'univers dans les 30 jours.
  3. Deux candidats :
       - MODÈLE appris (gradient boosting, fenêtre glissante d'un an, purge de 30 j) ;
       - RÈGLE SIMPLE « peu volatil + gros volume ».
  4. ANALYSE DES ERREURS : les deux sont testés sur les 120 derniers jours déjà mesurables (données jamais vues
     par le modèle). Le meilleur est utilisé ; s'ils sont proches, on mélange les deux.
  5. Probabilité honnête : pour chaque tranche de 10 % du classement, on affiche le taux de réussite RÉELLEMENT
     observé sur ces 120 jours (et non une sortie brute de modèle).
  6. Les prédictions du jour (top 20) sont suivies et jugées à 30 j par 13_memory.py.

Étude du 12/10/2026 (cours Binance janv. 2025 → sept. 2026, ~480 tokens, 206 dates de test, 30 j) :
  - Ce qui prédit le mieux le 30 j : la FAIBLE VOLATILITÉ (corrélation de rang −0,18) et l'absence d'explosion
    passée (−0,12). Le momentum 30 j est légèrement NÉGATIF (le top 20 momentum ne bat le marché que 39 % du temps).
  - Règle simple : top 20 bat le marché 68 % du temps (70 % puis 65 % sur les deux moitiés de la période).
    Modèle appris (régression logistique, fenêtre 1 an) : 63 %, mais meilleur classement global (corrélation 0,16).
  - ATTENTION : sur 30 j l'altcoin médiane PERD ~10 % (seuls 31 % des tokens finissent en hausse). « Battre le
    marché » veut souvent dire « perdre moins » : le top 20 de la règle a un return médian de −3 %.

Produit :
  data/computed/scores.csv            colonnes outperf_prob_30d, rank_30d, method_30d
  data/learning/model_report_30d.json méthode du jour, auto-évaluation, calibration par tranche
Si scikit-learn ou les klines manquent : rien n'est modifié (le pipeline ne casse jamais).
"""
from __future__ import annotations
import csv, json, warnings
from datetime import datetime
from common import ROOT, TODAY, COMPUTED, HISTORY, RAW, setup_logger, http_get, cache_get, cache_put

log = setup_logger("06c_score_30d")
warnings.filterwarnings("ignore")
LEARNING = ROOT / "data" / "learning"

HORIZON      = 30     # jours
TRAIN_DAYS   = 365    # fenêtre d'apprentissage (limitée par les klines disponibles)
EVAL_DAYS    = 120    # fenêtre d'auto-évaluation (dates déjà mesurables, jamais vues par le modèle testé)
TOP_N        = 20
MIN_QVOL     = 500_000  # volume médian 30 j minimum ($) pour entrer dans l'apprentissage
BLEND_MARGIN = 0.02   # écart de réussite en dessous duquel on mélange modèle et règle
KLINES_DAYS  = 1000   # historique téléchargé (max Binance par requête)
FEATS = ["r7", "r30", "r90", "r180", "vol30", "vol90", "dd90", "pma50", "pma200", "vtrend", "size", "runup180"]


def fetch_long(symbols):
    """Klines journalières longues (KLINES_DAYS) : cache 12 h, sinon téléchargement parallèle (8 requêtes à la fois)."""
    from concurrent.futures import ThreadPoolExecutor
    out = {}
    todo = []
    for s in symbols:
        c = cache_get("binance", f"klineslong_1d_{s}", max_age_hours=12)
        if c: out[s] = c.get("data", c) if isinstance(c, dict) else c
        else: todo.append(s)
    def one(s):
        try:
            d = http_get("https://data-api.binance.vision/api/v3/klines",
                         {"symbol": s, "interval": "1d", "limit": KLINES_DAYS}, timeout=20, retries=2)
            cache_put("binance", f"klineslong_1d_{s}", d)
            return s, d
        except Exception:
            return s, None
    if todo:
        with ThreadPoolExecutor(max_workers=8) as ex:
            for s, d in ex.map(one, todo):
                if d: out[s] = d
        log.info(f"Klines longues : {len(todo)} téléchargées, {len(out)} disponibles")
    return out


def load_klines(pd, symbols):
    """Clôtures et volumes ($) journaliers : klines longues si possible, sinon cache 365 j de 02_fetch_klines."""
    folder = RAW / "binance"
    long = fetch_long(symbols)
    closes, quotes = {}, {}
    for s in symbols:
        data = long.get(s)
        if not data:
            files = sorted(folder.glob(f"klines_1d_{s}_*.json"), reverse=True)
            if not files:
                continue
            try:
                j = json.loads(files[0].read_text(encoding="utf-8"))
            except Exception:
                continue
            data = j.get("data", j) if isinstance(j, dict) else j
        if not data or len(data) < 60:
            continue
        idx = pd.to_datetime([int(k[0]) for k in data], unit="ms").normalize()
        closes[s] = pd.Series([float(k[4]) for k in data], index=idx)
        quotes[s] = pd.Series([float(k[7]) for k in data], index=idx)
    if not closes:
        return None, None
    C = pd.DataFrame(closes).sort_index(); Q = pd.DataFrame(quotes).reindex(C.index)
    C = C[~C.index.duplicated(keep="last")]; Q = Q[~Q.index.duplicated(keep="last")]
    full = pd.date_range(C.index.min(), C.index.max(), freq="D")
    return C.reindex(full), Q.reindex(full)


def runup(np, C, window=180):
    """Plus forte hausse (plus haut / plus bas qui le précède − 1) sur `window` jours, pour chaque date."""
    vals = C.to_numpy(dtype=float); out = np.full(vals.shape, np.nan)
    for j in range(vals.shape[1]):
        col = vals[:, j]
        for i in range(len(col)):
            if not col[i] > 0:
                continue
            w = col[max(0, i - window):i + 1]; w = w[w > 0]
            if len(w) >= 30:
                out[i, j] = float((w / np.minimum.accumulate(w)).max() - 1)
    return out


def build(pd, np, C, Q):
    lr = np.log(C / C.shift(1))
    F = {
        "r7": C / C.shift(7) - 1, "r30": C / C.shift(30) - 1, "r90": C / C.shift(90) - 1, "r180": C / C.shift(180) - 1,
        "vol30": lr.rolling(30, min_periods=20).std(), "vol90": lr.rolling(90, min_periods=45).std(),
        "dd90": C / C.rolling(90, min_periods=30).max() - 1,
        "pma50": C / C.rolling(50, min_periods=30).mean() - 1, "pma200": C / C.rolling(200, min_periods=100).mean() - 1,
        "vtrend": Q.rolling(7, min_periods=5).mean() / Q.rolling(90, min_periods=30).mean(),
        "size": np.log1p(Q.rolling(30, min_periods=20).median()),
    }
    F["runup180"] = pd.DataFrame(runup(np, C), index=C.index, columns=C.columns)
    qmed = Q.rolling(30, min_periods=20).median()
    fwd = C.shift(-HORIZON) / C - 1
    # format long (date, token) sans DataFrame.stack, dont le comportement change selon la version de pandas
    nd, ns = C.shape
    D = pd.DataFrame({"date": np.repeat(C.index.values, ns), "symbol": np.tile(C.columns.values, nd)})
    for name, df in list(F.items()) + [("qmed", qmed), ("price", C), ("fwd", fwd)]:
        D[name] = df.reindex(index=C.index, columns=C.columns).to_numpy(dtype=float).ravel()
    D = D[D["price"] > 0].reset_index(drop=True)
    D = D[D["vol30"].notna()]                                 # au moins ~1 mois de cours
    for c in FEATS:                                           # rangs du jour (NaN conservés : le boosting sait les gérer)
        D[c] = D.groupby("date")[c].rank(pct=True) - 0.5
    elig = D["qmed"] >= MIN_QVOL
    med = D[elig].groupby("date")["fwd"].median()
    D["excess"] = D["fwd"] - D["date"].map(med)
    D["elig"] = elig
    D["rule"] = -D["vol30"].fillna(0) + D["size"].fillna(0)  # règle simple : peu volatil + gros volume
    return D


def make_model():
    from sklearn.ensemble import HistGradientBoostingClassifier
    return HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, max_iter=200,
                                          min_samples_leaf=200, random_state=0)


def evaluate(pd, np, df, col):
    """Taux de réussite du top 20 (bat la médiane), corrélation de rang et taux par tranche de 10 %."""
    beats, ics = [], []
    for _, g in df.groupby("date"):
        if len(g) < 50: continue
        beats.append(float((g.nlargest(TOP_N, col)["excess"] > 0).mean()))
        ics.append(g[col].corr(g["excess"], method="spearman"))
    pct = df.groupby("date")[col].rank(pct=True)
    dec = np.minimum((pct * 10).astype(int), 9)
    by_dec = (df["excess"] > 0).groupby(dec).mean()
    pos_dec = (df["fwd"] > 0).groupby(dec).mean()
    return {"top20_beat": float(np.mean(beats)) if beats else None, "ic": float(np.nanmean(ics)) if ics else None,
            "days": len(beats), "deciles_beat": [round(float(by_dec.get(i, np.nan)), 3) for i in range(10)],
            "deciles_up": [round(float(pos_dec.get(i, np.nan)), 3) for i in range(10)]}


def run():
    try:
        import numpy as np, pandas as pd
        import sklearn  # noqa: F401
    except ImportError as e:
        log.warning(f"scikit-learn/pandas absent ({e}) — prévision 30 j ignorée"); return
    scores_path = COMPUTED / "scores.csv"
    if not scores_path.exists():
        log.warning("Pas de scores.csv — étape ignorée"); return
    with open(scores_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    universe = [r["symbol"] for r in rows if str(r.get("outperf_prob_7d", "")).strip() != ""]  # mêmes exclusions que 06b
    C, Q = load_klines(pd, universe)
    if C is None or C.shape[1] < 100:
        log.warning(f"Klines insuffisantes ({0 if C is None else C.shape[1]} tokens) — prévision 30 j ignorée"); return
    D = build(pd, np, C, Q)
    last = D["date"].max()
    labeled = D[D["fwd"].notna() & D["elig"]].copy()
    labeled["y"] = (labeled["excess"] > 0).astype(int)
    lab_dates = sorted(labeled["date"].unique())
    if len(lab_dates) < EVAL_DAYS + 90:
        log.warning(f"Historique trop court ({len(lab_dates)} jours mesurables) — prévision 30 j ignorée"); return

    # ── analyse des erreurs : modèle entraîné AVANT la fenêtre de test, puis comparé à la règle ───
    ev_start = lab_dates[-EVAL_DAYS]
    tr_old = labeled[(labeled["date"] < ev_start - pd.Timedelta(days=HORIZON)) &
                     (labeled["date"] >= ev_start - pd.Timedelta(days=HORIZON + TRAIN_DAYS))]
    te = labeled[labeled["date"] >= ev_start].copy()
    m_old = make_model().fit(tr_old[FEATS], tr_old["y"])
    te["model"] = m_old.predict_proba(te[FEATS])[:, 1]
    te["blend"] = te.groupby("date")["model"].rank(pct=True) + te.groupby("date")["rule"].rank(pct=True)
    res = {k: evaluate(pd, np, te, k) for k in ("model", "rule", "blend")}
    mb, rb = res["model"]["top20_beat"], res["rule"]["top20_beat"]
    method = "model" if mb >= rb + BLEND_MARGIN else "rule" if rb >= mb + BLEND_MARGIN else "blend"
    log.info(f"Auto-évaluation 30 j ({res['model']['days']} jours jamais vus) : modèle {mb:.0%} / règle simple {rb:.0%} "
             f"/ mélange {res['blend']['top20_beat']:.0%} (top {TOP_N} qui bat la médiane) → méthode retenue : {method}")

    # ── modèle final, entraîné sur l'année écoulée (purge de 30 j : seulement des résultats connus) ──
    tr = labeled[labeled["date"] >= labeled["date"].max() - pd.Timedelta(days=TRAIN_DAYS)]
    model = make_model().fit(tr[FEATS], tr["y"])
    today = D[D["date"] == last].copy()
    today["model"] = model.predict_proba(today[FEATS])[:, 1]
    today["blend"] = today["model"].rank(pct=True) + today["rule"].rank(pct=True)
    today["pct"] = today[method].rank(pct=True)
    # probabilité = courbe lisse « rang du jour → taux de réussite observé » ajustée sur les 120 jours de test
    # (avant : une valeur par tranche de 10 %, donc tout le top 20 affichait exactement le même chiffre)
    from sklearn.linear_model import LogisticRegression
    te_pct = te.groupby("date")[method].rank(pct=True).to_numpy()
    calib = LogisticRegression(C=1e6, max_iter=1000).fit(np.c_[te_pct, te_pct ** 2], te["y"].to_numpy())
    tp = today["pct"].to_numpy()
    today["prob"] = np.round(100 * calib.predict_proba(np.c_[tp, tp ** 2])[:, 1], 1)
    today["rank30"] = today[method].rank(ascending=False, method="first").astype(int)
    probs = dict(zip(today["symbol"], today["prob"])); ranks = dict(zip(today["symbol"], today["rank30"]))

    # ── écriture ─────────────────────────────────────────────────────────
    fields = list(rows[0].keys()) if rows else []
    for extra in ("outperf_prob_30d", "rank_30d", "method_30d"):
        if extra not in fields: fields.append(extra)
    label = {"model": "modèle appris", "rule": "règle simple (peu volatil + gros volume)", "blend": "mélange modèle + règle"}[method]
    for r in rows:
        p = probs.get(r["symbol"])
        r["outperf_prob_30d"] = p if p is not None else ""
        r["rank_30d"] = ranks.get(r["symbol"], "")
        r["method_30d"] = label if p is not None else ""
    with open(scores_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    (HISTORY / f"scores_{TODAY}.csv").write_text(scores_path.read_text(encoding="utf-8"), encoding="utf-8")

    try:  # facteurs dominants, lisibles (régression logistique sur les mêmes variables)
        from sklearn.linear_model import LogisticRegression
        t2 = tr.dropna(subset=FEATS)
        lr = LogisticRegression(C=0.05, max_iter=2000).fit(t2[FEATS], t2["y"])
        coefs = sorted(zip(FEATS, lr.coef_[0]), key=lambda x: -abs(x[1]))
    except Exception:
        coefs = []
    top = today.sort_values("rank30").head(TOP_N)
    LEARNING.mkdir(parents=True, exist_ok=True)
    (LEARNING / "model_report_30d.json").write_text(json.dumps({
        "date": TODAY, "horizon_days": HORIZON, "target": "bat la médiane du marché à 30 j",
        "method_used_today": method, "method_label": label,
        "klines_span": [str(C.index.min().date()), str(last.date())], "tokens": int(C.shape[1]),
        "train_rows": int(len(tr)), "eval_window": [str(pd.Timestamp(ev_start).date()), str(pd.Timestamp(lab_dates[-1]).date())],
        "eval": {k: {kk: (round(vv, 3) if isinstance(vv, float) else vv) for kk, vv in v.items()} for k, v in res.items()},
        "universe_up_rate_eval": round(float((te["fwd"] > 0).mean()), 3),
        "universe_median_return_eval_pct": round(float(te.groupby("date")["fwd"].median().median() * 100), 1),
        "top_factors": [{"feature": f, "effect": round(float(c), 3)} for f, c in coefs],
        "top_today": [{"symbol": s.replace("USDT", ""), "prob": float(p)} for s, p in zip(top["symbol"], top["prob"])],
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    log.info(f"Prévision 30 j écrite ({label}) : {len(probs)} tokens, apprentissage {len(tr)} lignes")


if __name__ == "__main__":
    run()
