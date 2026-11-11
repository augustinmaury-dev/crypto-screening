"""
14_dashboard_data.py — Rassemble tout ce que le dashboard dessine (ajouté le 11/11/2026).

Dernière étape du pipeline. Ne calcule aucun score : lit les fichiers produits par les autres étapes et écrit
un seul fichier compact, data/computed/dashboard.json, pour les graphiques :
  - régime de marché jour par jour (06b) et thermomètre long terme (06d) ;
  - analyse des erreurs à 7 j : modèle / règle simple / mélange rejoués sur ~4 mois (06b) ;
  - SUIVI RÉEL des prédictions (13_memory) : pour chaque jour, le top 20 jugé contre trois adversaires —
    la médiane du marché, BTC, et la hausse absolue (« a-t-il monté ? ») — à 7 j et à 30 j ;
  - leaders et dossiers d'ETF suivis en réel ;
  - mini-courbes de prix (30 derniers jours) de chaque token.
Si un fichier manque, la partie correspondante est simplement absente (le pipeline ne casse jamais).
"""
from __future__ import annotations
import csv, json
from collections import defaultdict
from common import ROOT, TODAY, COMPUTED, HISTORY, setup_logger

log = setup_logger("14_dashboard_data")
LEARNING = ROOT / "data" / "learning"
SPARK_DAYS = 30


def load(path, default=None):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def price_tables():
    """{date: {symbol: prix}} pour BTC (toutes les dates) et pour tous les tokens (SPARK_DAYS dernières dates)."""
    files = sorted(f for f in HISTORY.glob("scores_*.csv") if len(f.stem) == 15)
    btc, spark = {}, defaultdict(list)
    recent = {f.stem[-8:] for f in files[-SPARK_DAYS:]}
    for f in files:
        d = f.stem[-8:]
        try:
            with open(f, encoding="utf-8") as fh:
                for r in csv.DictReader(fh):
                    s = r.get("symbol")
                    try:
                        p = float(r.get("price") or 0)
                    except ValueError:
                        continue
                    if p <= 0:
                        continue
                    if s == "BTCUSDT":
                        btc[d] = p
                    if d in recent:
                        spark[s].append(float(f"{p:.4g}"))
        except Exception as e:
            log.warning(f"{f.name} illisible : {e}")
    return btc, spark, sorted(recent)


def live_tracking(pred_log, btc, selection, h):
    """Par jour de prédiction : le panier jugé contre la médiane, contre BTC et en hausse absolue (horizon h jours)."""
    by_date = defaultdict(list)
    for p in pred_log:
        if p.get("selection") == selection and p.get(f"return_{h}d") is not None:
            by_date[p["date"]].append(p)
    out = []
    for d in sorted(by_date):
        ps = by_date[d]
        rets = [float(p[f"return_{h}d"]) for p in ps]
        exc = [float(p[f"excess_{h}d"]) for p in ps if p.get(f"excess_{h}d") is not None]
        m = ps[0].get(f"measured_{h}d")
        b = (btc[m] / btc[d] - 1) * 100 if m in btc and d in btc else None
        row = {"date": d, "n": len(ps), "method": ps[0].get("score_model") or "ancienne formule",
               "group": ps[0].get("model", ""),
               "beat_median": round(sum(1 for p in ps if p.get(f"beat_market_{h}d")) / len(ps), 3),
               "up": round(sum(1 for r in rets if r > 0) / len(rets), 3),
               "basket": round(sum(rets) / len(rets), 2),
               "median": round(sum(r - e for r, e in zip(rets, exc)) / len(exc), 2) if exc else None,
               "btc": round(b, 2) if b is not None else None,
               "beat_btc": round(sum(1 for r in rets if r > b) / len(rets), 3) if b is not None else None}
        out.append(row)
    return out


def summarize(rows, group=None):
    rows = [r for r in rows if group is None or r["group"] == group]
    if not rows:
        return None
    avg = lambda k: (lambda v: round(sum(v) / len(v), 3) if v else None)([r[k] for r in rows if r.get(k) is not None])
    return {"days": len(rows), "predictions": sum(r["n"] for r in rows), "beat_median": avg("beat_median"),
            "beat_btc": avg("beat_btc"), "up": avg("up"), "basket": avg("basket"), "median": avg("median"), "btc": avg("btc"),
            "basket_beats_btc": (lambda v: round(sum(v) / len(v), 3) if v else None)(
                [1 if r["basket"] > r["btc"] else 0 for r in rows if r.get("btc") is not None]),
            "from": rows[0]["date"], "to": rows[-1]["date"]}


def run():
    pred_log = load(LEARNING / "prediction_log.json", []) or []
    btc, spark, spark_dates = price_tables()
    out = {"generated": TODAY}

    reg = load(COMPUTED / "market_regime.json", {}) or {}
    out["regime"] = {"today": reg.get("today", {}),
                     "history": [{k: h.get(k) for k in ("date", "alt_index_30d", "alt_index_90d", "btc_ret_30d", "breadth_ma50", "label")}
                                 for h in reg.get("history", [])]}
    ms = load(COMPUTED / "market_state.json")
    if ms: out["market_state"] = ms
    bt = load(LEARNING / "backtest_7d.json")
    if bt: out["backtest_7d"] = bt
    m7 = load(LEARNING / "model_report.json", {}) or {}
    m7.pop("derivatives_excluded", None)
    out["model_7d"] = m7
    out["model_30d"] = load(LEARNING / "model_report_30d.json", {}) or {}
    cal = load(LEARNING / "calibration.json", {}) or {}
    out["calibration_live"] = (cal.get("horizons", {}) or {}).get("7", {})

    # suivi réel : top 20 à 7 j et à 30 j
    live7 = live_tracking(pred_log, btc, "top20", 7)
    live30 = live_tracking(pred_log, btc, "top20_30d", 30)
    out["live_7d"] = {"daily": live7, "summary_learned": summarize(live7, "Modèle appris"), "summary_legacy": summarize(live7, "Ancienne formule"),
                      "summary_blend": summarize([r for r in live7 if r["method"] == "ml_blend"])}
    out["live_30d"] = {"daily": live30, "summary": summarize(live30)}
    lead = live_tracking(pred_log, btc, "leaders", 14)
    out["leaders_live"] = {"daily": [r for r in lead if r["date"] >= "20260929"], "summary": summarize([r for r in lead if r["date"] >= "20260929"])}

    # dossiers d'ETF (un point par dépôt)
    etf = []
    for p in pred_log:
        if p.get("selection") == "etf":
            etf.append({"date": p.get("etf_date") or p["date"], "symbol": p["symbol"].replace("USDT", ""), "form": p.get("etf_form"),
                        "kind": p.get("etf_kind"), "entity": (p.get("etf_entity") or "").split("  (CIK")[0].strip(),
                        "live": (p.get("etf_date") or "") >= "2026-09-29",
                        "excess_7d": p.get("excess_7d"), "excess_14d": p.get("excess_14d"), "return_7d": p.get("return_7d")})
    out["etf_events"] = sorted(etf, key=lambda e: e["date"])

    out["spark"] = {"dates": spark_dates, "prices": {s: v for s, v in spark.items() if len(v) >= 5}}

    path = COMPUTED / "dashboard.json"
    path.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    log.info(f"dashboard.json écrit ({path.stat().st_size // 1024} Ko) : {len(live7)} jours suivis à 7 j, {len(live30)} à 30 j, "
             f"{len(etf)} dépôts d'ETF, {len(out['spark']['prices'])} mini-courbes")


if __name__ == "__main__":
    run()
