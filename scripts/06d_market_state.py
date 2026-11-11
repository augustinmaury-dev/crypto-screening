"""
06d_market_state.py — Thermomètre du marché (ajouté le 11/11/2026).

Question traitée AVANT de choisir un token : « est-ce le moment de détenir des altcoins plutôt que du Bitcoin ? »

Étude du 11/11/2026 sur ~2,6 ans de cours journaliers Binance (941 jours, ~400 tokens, mêmes klines que 06c) :
  - En moyenne, l'altcoin médiane perd ~6,5 % en 30 jours pendant que BTC gagne ~1,6 % ; seules ~30 % des altcoins
    battent BTC sur 30 jours (38 % sur 7 jours). L'adversaire à battre n'est pas « la médiane du marché », c'est BTC.
  - L'indice altseason (part des 100 altcoins les plus échangées qui ont fait mieux que BTC sur 30 j) est un
    indicateur CONTRARIEN : quand il dépasse 75 %, l'altcoin médiane a perdu ~18 % les 30 jours suivants et 17 %
    seulement ont battu BTC ; quand il est sous 25 %, la suite est la moins mauvaise (−2,6 %, 35 % battent BTC).
    Vrai sur les deux moitiés de la période (corrélation de rang −0,14 / −0,23).
  - Une largeur de marché très basse (< 10 % des tokens au-dessus de leur moyenne 50 j) n'annonce PAS de rebond
    (−7,0 % à 30 j, comme la moyenne) : l'idée « marché survendu = rebond » n'est pas confirmée.
  - Limite : seuls les tokens encore cotés aujourd'hui sont dans l'historique (les délistés manquent), donc la
    réalité des altcoins est plutôt pire que ces chiffres.

Chaque jour, ce script recalcule tout sur les klines disponibles (les chiffres se mettent à jour seuls) et écrit
data/computed/market_state.json : état du jour, taux de base, « ce qui a suivi quand l'indice était à ce niveau »,
et les séries historiques pour les graphiques du dashboard.
Si les klines manquent, rien n'est écrit (le pipeline ne casse jamais).
"""
from __future__ import annotations
import csv, json, importlib, warnings
from common import TODAY, COMPUTED, setup_logger

log = setup_logger("06d_market_state")
warnings.filterwarnings("ignore")

MIN_QVOL   = 500_000     # volume médian 30 j minimum ($) pour compter dans l'univers
MIN_TOKENS = 100         # nb minimum d'altcoins pour qu'un jour soit retenu
ALT_BINS   = [0, 25, 45, 60, 75, 100.001]          # tranches de l'indice altseason 30 j (%)
BREADTH_BINS = [0, 10, 25, 50, 75, 100.001]        # tranches de la largeur de marché (%)
HIST_DAYS  = 720         # longueur des séries envoyées au dashboard


def market_series(pd, np, C, Q):
    """Une ligne par jour : état du marché ce jour-là + ce qui s'est passé ensuite (7 j et 30 j)."""
    lr = np.log(C / C.shift(1))
    vol30 = lr.rolling(30, min_periods=20).std()
    qmed = Q.rolling(30, min_periods=20).median()
    alts = (vol30 > 0.005) & (qmed > MIN_QVOL) & C.shift(59).notna()     # ni stablecoin, ni illiquide, ≥ 60 j de cours
    if "BTCUSDT" in alts:
        alts["BTCUSDT"] = False
    ma50 = C.rolling(50, min_periods=30).mean()
    B = C["BTCUSDT"]
    S = pd.DataFrame(index=C.index)
    S["n"] = alts.sum(axis=1)
    S["breadth50"] = ((C > ma50) & alts).sum(axis=1) / (alts & ma50.notna()).sum(axis=1) * 100
    S["btc"] = B
    S["btc30"] = (B / B.shift(30) - 1) * 100
    r30 = C / C.shift(30) - 1
    top = qmed.where(alts).rank(axis=1, ascending=False) <= 100
    S["alt30"] = (r30.gt(B / B.shift(30) - 1, axis=0) & top).sum(axis=1) / (top & r30.notna()).sum(axis=1) * 100
    for h in (7, 30):
        f = C.shift(-h) / C - 1
        fb = f["BTCUSDT"]
        known = alts & f.notna()
        S[f"med{h}"] = f.where(alts).median(axis=1) * 100
        S[f"btc_f{h}"] = fb * 100
        S[f"share{h}"] = (f.gt(fb, axis=0) & alts).sum(axis=1) / known.sum(axis=1) * 100
        S[f"up{h}"] = ((f > 0) & alts).sum(axis=1) / known.sum(axis=1) * 100
        S.loc[fb.isna(), [f"med{h}", f"share{h}", f"up{h}"]] = np.nan
    return S[S["n"] >= MIN_TOKENS]


def bucket_table(pd, S, col, bins, today_value):
    out = []
    for lo, hi in zip(bins[:-1], bins[1:]):
        g = S[(S[col] >= lo) & (S[col] < hi) & S["med30"].notna()]
        g7 = S[(S[col] >= lo) & (S[col] < hi) & S["med7"].notna()]
        row = {"lo": lo, "hi": min(hi, 100), "n_days": int(len(g)),
               "current": bool(today_value is not None and lo <= today_value < hi)}
        if len(g):
            row.update(med30=round(float(g["med30"].mean()), 1), btc30=round(float(g["btc_f30"].mean()), 1),
                       share30=round(float(g["share30"].mean()), 1), up30=round(float(g["up30"].mean()), 1))
        if len(g7):
            row.update(med7=round(float(g7["med7"].mean()), 1), share7=round(float(g7["share7"].mean()), 1))
        out.append(row)
    return out


def run():
    try:
        import numpy as np, pandas as pd
    except ImportError as e:
        log.warning(f"pandas absent ({e}) — thermomètre ignoré"); return
    scores_path = COMPUTED / "scores.csv"
    if not scores_path.exists():
        log.warning("Pas de scores.csv — étape ignorée"); return
    with open(scores_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    universe = [r["symbol"] for r in rows if str(r.get("outperf_prob_7d", "")).strip() != ""]
    m30 = importlib.import_module("06c_score_30d")
    C, Q = m30.load_klines(pd, universe)           # klines longues déjà en cache (téléchargées par 06c)
    if C is None or C.shape[1] < MIN_TOKENS or "BTCUSDT" not in C:
        log.warning("Klines insuffisantes — thermomètre ignoré"); return

    S = market_series(pd, np, C, Q)
    if len(S) < 200:
        log.warning(f"Historique trop court ({len(S)} jours) — thermomètre ignoré"); return
    last = S.iloc[-1]
    f1 = lambda x: round(float(x), 1) if x == x else None
    today = {"alt30": f1(last["alt30"]), "breadth50": f1(last["breadth50"]), "btc30": f1(last["btc30"]), "n_tokens": int(last["n"])}
    M30, M7 = S[S["med30"].notna()], S[S["med7"].notna()]
    base = {"med7": f1(M7["med7"].mean()), "med30": f1(M30["med30"].mean()), "btc7": f1(M7["btc_f7"].mean()),
            "btc30": f1(M30["btc_f30"].mean()), "share7": f1(M7["share7"].mean()), "share30": f1(M30["share30"].mean()),
            "up30": f1(M30["up30"].mean()), "n_days": int(len(M30))}
    by_alt = bucket_table(pd, S, "alt30", ALT_BINS, today["alt30"])
    by_breadth = bucket_table(pd, S, "breadth50", BREADTH_BINS, today["breadth50"])
    half = len(M30) // 2
    stab = [f1(M30["alt30"].iloc[:half].corr(M30["med30"].iloc[:half], method="spearman") * 100),
            f1(M30["alt30"].iloc[half:].corr(M30["med30"].iloc[half:], method="spearman") * 100)]

    # verdict : la tranche du jour comparée au taux de base (≥ 30 jours observés dans la tranche)
    cur = next((b for b in by_alt if b["current"]), None)
    verdict = {"level": "inconnu", "title": "Pas assez de recul", "text": ""}
    if cur and cur.get("share30") is not None and cur["n_days"] >= 30:
        d = cur["share30"] - base["share30"]
        level = "moins_defavorable" if d >= 3 else "plus_defavorable" if d <= -3 else "habituel"
        title = {"moins_defavorable": "Contexte un peu moins défavorable aux altcoins que d'habitude",
                 "habituel": "Contexte habituel : BTC reste difficile à battre",
                 "plus_defavorable": "Contexte défavorable aux altcoins"}[level]
        verdict = {"level": level, "title": title,
                   "text": (f"Indice altseason à {today['alt30']:.0f} % (tranche {cur['lo']:.0f}–{cur['hi']:.0f} %). Les {cur['n_days']} jours "
                            f"passés dans cette tranche ont été suivis, sur 30 j, d'une altcoin médiane à {cur['med30']:+.1f} % "
                            f"(BTC {cur['btc30']:+.1f} %) ; {cur['share30']:.0f} % des altcoins ont battu BTC "
                            f"(moyenne toutes périodes : {base['share30']:.0f} %).")}

    H = S.tail(HIST_DAYS)
    r1 = lambda s: [None if x != x else round(float(x), 1) for x in s]
    out = {
        "date": TODAY, "span": [str(S.index[0].date()), str(S.index[-1].date())], "n_days": int(len(S)),
        "today": today, "base": base, "by_alt30": by_alt, "by_breadth50": by_breadth, "verdict": verdict,
        "alt30_vs_next30_rank_corr_halves_pct": stab,
        "caveat": "Tokens encore cotés aujourd'hui uniquement (les délistés manquent) : la réalité des altcoins est plutôt pire. "
                  "Les fenêtres de 30 j se chevauchent : ~%d périodes réellement indépendantes." % max(1, len(M30) // 30),
        "history": {"dates": [d.strftime("%Y%m%d") for d in H.index], "alt30": r1(H["alt30"]), "breadth50": r1(H["breadth50"]),
                    "btc": [None if x != x else round(float(x)) for x in H["btc"]],
                    "med30_next": r1(H["med30"]), "share30_next": r1(H["share30"])},
    }
    (COMPUTED / "market_state.json").write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    log.info(f"Thermomètre : {len(S)} jours ({out['span'][0]} → {out['span'][1]}) — indice altseason {today['alt30']} %, "
             f"largeur {today['breadth50']} % → {verdict['title']}")


if __name__ == "__main__":
    run()
