"""
13_memory.py — Mémoire cumulative du projet.

Génère et met à jour chaque jour :
  - data/learning/pattern_history.json  (évolution des hit_rates jour par jour)
  - data/learning/prediction_log.json   (prédictions passées et leurs résultats)
  - data/learning/project_memory.md     (mémoire complète pour dialoguer avec le projet)
"""
from __future__ import annotations
from common import ROOT, TODAY, COMPUTED, HISTORY, setup_logger
import csv, json
from datetime import datetime, timedelta, timezone
from pathlib import Path

log = setup_logger("13_memory")

LEARNING   = ROOT / "data" / "learning"
SCORE_THRESHOLD  = 70   # score minimum pour enregistrer une prédiction
# bull_prob_7d est une prédiction à 7 jours → on la juge à 7 jours.
# 14 jours est mesuré en complément.
OUTCOME_HORIZONS = (7, 14)
MAIN_HORIZON     = 7
SNAPSHOT_TOLERANCE = 2  # si le snapshot J+H manque, on accepte J+H+1 ou J+H+2
MAX_PENDING_AGE  = 30   # une prédiction non mesurable après 30 j (token délisté…) est abandonnée
MAX_JOURNAL_DAYS = 30   # jours de journal conservés
CALIB_BUCKETS = [(20, 35), (35, 45), (45, 50), (50, 55), (55, 60), (60, 65), (65, 70), (70, 81)]

BULL_PATS = {
    "breakout_30d", "rsi_bullish_divergence", "golden_cross",
    "macd_bullish_cross", "double_bottom_90d", "bull_flag",
    "uptrend", "support_bounce", "hammer_4h", "bullish_engulfing_4h",
    "morning_star_4h", "squeeze_breakout",
}
BEAR_PATS = {
    "breakdown_30d", "rsi_bearish_divergence", "death_cross",
    "macd_bearish_cross", "double_top_90d", "bear_flag",
    "downtrend", "resistance_test", "shooting_star_4h",
    "bearish_engulfing_4h", "evening_star_4h",
}


# ─────────────────────────── helpers ───────────────────────────────────────

def load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default

def save_json(path: Path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def load_scores_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        with open(path, encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except Exception:
        return []

def date_n_ago(n: int) -> str:
    return (datetime.now(timezone.utc) - timedelta(days=n)).strftime("%Y%m%d")

def fmt_date(d: str) -> str:
    """20260812 → 12 août 2026"""
    try:
        dt = datetime.strptime(d, "%Y%m%d")
        mois = ["jan","fév","mar","avr","mai","jun","jul","août","sep","oct","nov","déc"]
        return f"{dt.day} {mois[dt.month-1]} {dt.year}"
    except Exception:
        return d

def trend_arrow(history: list[dict], lookback: int = 7) -> str:
    """Flèche de tendance : hit_rate actuel vs il y a ~7 snapshots.
    (La comparaison jour à jour était toujours ≈ 0 car le hit_rate est cumulatif.)"""
    if len(history) < 2:
        return "→"
    ref = history[-1 - min(lookback, len(history) - 1)]
    delta = history[-1]["hit_rate"] - ref["hit_rate"]
    if delta > 0.02:  return "📈"
    if delta < -0.02: return "📉"
    return "→"


# ─────────────────────── 1. Pattern history ────────────────────────────────

def update_pattern_history(weights: dict) -> dict:
    """Ajoute un snapshot quotidien des hit_rates dans pattern_history.json."""
    history = load_json(LEARNING / "pattern_history.json", {})

    for pat, data in weights.items():
        hr = data.get("hit_rate_14d")
        n  = data.get("samples", 0)
        if hr is None:
            continue
        if pat not in history:
            history[pat] = []
        # évite les doublons pour aujourd'hui
        if not history[pat] or history[pat][-1]["date"] != TODAY:
            history[pat].append({"date": TODAY, "hit_rate": round(hr, 4), "samples": n})
        # garde max 365 jours
        history[pat] = history[pat][-365:]

    save_json(LEARNING / "pattern_history.json", history)
    return history


# ─────────────────────── 2. Prediction log ─────────────────────────────────
#
# Correctif du 25/09/2026 — l'ancienne version :
#   - gardait seulement les 300 dernières prédictions en attente, alors qu'il y en a
#     50 à 75 par jour → elles étaient effacées au bout de ~5 jours, avant d'atteindre
#     l'horizon de 14 jours. Résultat : 0 prédiction jamais mesurée.
#   - mesurait une prédiction "7 jours" à 14 jours, avec le prix du jour (pas celui de J+H).
#
# Nouvelle version :
#   - aucune limite en nombre ; une prédiction en attente n'est abandonnée qu'après
#     MAX_PENDING_AGE jours (ex. token délisté) ;
#   - mesure à 7 j (horizon de bull_prob_7d) ET à 14 j, avec le prix du snapshot
#     historique J+H (data/history/scores_YYYYMMDD.csv) ;
#   - compare aussi à la médiane de l'univers ce jour-là ("bat le marché") pour
#     séparer la qualité du signal de la tendance générale ;
#   - backfill : reconstruit automatiquement les prédictions passées à partir de
#     data/history/ (toutes les dates où bull_prob_7d existe).

_snapshot_cache: dict[str, dict | None] = {}

def load_snapshot(date_str: str) -> dict | None:
    """{symbol: row} pour un snapshot historique, avec cache."""
    if date_str not in _snapshot_cache:
        path = HISTORY / f"scores_{date_str}.csv"
        rows = load_scores_csv(path)
        _snapshot_cache[date_str] = {r["symbol"]: r for r in rows} if rows else None
    return _snapshot_cache[date_str]

def shift_date(d: str, n: int) -> str:
    return (datetime.strptime(d, "%Y%m%d") + timedelta(days=n)).strftime("%Y%m%d")

def _fnum(x) -> float | None:
    try:
        v = float(x)
        return v if v == v else None  # NaN → None
    except (TypeError, ValueError):
        return None

def _is_excluded(row: dict) -> bool:
    return str(row.get("stablecoin", "")).lower() == "true" or str(row.get("suspect", "")).lower() == "true"

def _median(vals: list[float]) -> float:
    s = sorted(vals); n = len(s)
    if n == 0: return 0.0
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2

_median_cache: dict[tuple, float | None] = {}

def universe_median_return(d0: str, d1: str) -> float | None:
    """Return médian (%) de tout l'univers (hors stablecoins/suspects) entre deux snapshots."""
    key = (d0, d1)
    if key not in _median_cache:
        s0, s1 = load_snapshot(d0), load_snapshot(d1)
        if not s0 or not s1:
            _median_cache[key] = None
        else:
            rets = []
            for sym, r in s0.items():
                if _is_excluded(r) or sym not in s1: continue
                p0, p1 = _fnum(r.get("price")), _fnum(s1[sym].get("price"))
                if p0 and p1 and p0 > 0:
                    rets.append((p1 / p0 - 1) * 100)
            _median_cache[key] = _median(rets) if rets else None
    return _median_cache[key]

def find_outcome_snapshot(date: str, horizon: int) -> str | None:
    """Date du snapshot utilisé pour mesurer J+horizon (tolérance de quelques jours)."""
    for extra in range(SNAPSHOT_TOLERANCE + 1):
        d = shift_date(date, horizon + extra)
        if d > TODAY:
            return None
        if load_snapshot(d):
            return d
    return None

def history_dates() -> list[str]:
    return sorted(p.stem.replace("scores_", "") for p in HISTORY.glob("scores_*.csv"))

def make_prediction(date: str, row: dict) -> dict:
    score = float(row.get("score") or 0)
    return {
        "date":           date,
        "symbol":         row.get("symbol", ""),
        "score":          score,
        "bull_prob":      float(_fnum(row.get("bull_prob_7d")) or score),
        "alpha_vs_btc":   float(_fnum(row.get("alpha_vs_btc")) or 0),
        "vs_btc_label":   row.get("vs_btc_label", ""),
        "price_at":       float(_fnum(row.get("price")) or 0),
        "patterns":       row.get("patterns", ""),
        "catalyst_flags": row.get("catalyst_flags", ""),
        "exit_risk":      int(_fnum(row.get("exit_risk")) or 0),
    }

def measure(p: dict) -> bool:
    """Remplit les résultats manquants (7 j et 14 j). Retourne True si quelque chose a changé."""
    changed = False
    for h in OUTCOME_HORIZONS:
        if p.get(f"return_{h}d") is not None:
            continue
        d_out = find_outcome_snapshot(p["date"], h)
        if not d_out:
            continue
        snap = load_snapshot(d_out) or {}
        row = snap.get(p["symbol"])
        p_now, p0 = _fnum(row.get("price")) if row else None, p.get("price_at") or 0
        if not p_now or p0 <= 0:
            continue
        ret = (p_now / p0 - 1) * 100
        med = universe_median_return(p["date"], d_out)
        p[f"return_{h}d"]      = round(ret, 2)
        p[f"excess_{h}d"]      = round(ret - med, 2) if med is not None else None
        p[f"correct_{h}d"]     = ret > 0
        p[f"beat_market_{h}d"] = (ret > med) if med is not None else None
        p[f"measured_{h}d"]    = d_out
        changed = True
    # Champs historiques (compatibilité dashboard) = horizon principal
    if p.get(f"return_{MAIN_HORIZON}d") is not None and p.get("measured_date") is None:
        p["return_pct"]    = p[f"return_{MAIN_HORIZON}d"]
        p["correct"]       = p[f"correct_{MAIN_HORIZON}d"]
        p["measured_date"] = p[f"measured_{MAIN_HORIZON}d"]
        snap = load_snapshot(p["measured_date"]) or {}
        p["price_outcome"] = _fnum((snap.get(p["symbol"]) or {}).get("price"))
    p.setdefault("price_outcome", None); p.setdefault("return_pct", None)
    p.setdefault("correct", None);       p.setdefault("measured_date", None)
    return changed

def update_prediction_log(today_scores: list[dict]) -> list[dict]:
    """
    1. Backfill : ajoute les prédictions (score >= SCORE_THRESHOLD) de tous les snapshots
       historiques qui ne sont pas encore dans le log (+ celles d'aujourd'hui).
    2. Mesure les résultats à 7 j et 14 j dès que le snapshot correspondant existe.
    3. Abandonne les prédictions impossibles à mesurer après MAX_PENDING_AGE jours.
    """
    log_path = LEARNING / "prediction_log.json"
    pred_log: list[dict] = load_json(log_path, [])
    existing_keys = {(p["date"], p["symbol"]) for p in pred_log}

    # ── 1. Nouvelles prédictions : snapshots historiques + aujourd'hui ─────
    new_count = 0
    sources = [(d, list((load_snapshot(d) or {}).values())) for d in history_dates()]
    sources.append((TODAY, today_scores))
    for date, rows in sources:
        if not rows or "bull_prob_7d" not in rows[0]:
            continue  # snapshots antérieurs à l'introduction de bull_prob_7d
        for row in rows:
            if _is_excluded(row):
                continue
            if float(_fnum(row.get("score")) or 0) < SCORE_THRESHOLD:
                continue
            key = (date, row.get("symbol", ""))
            if key in existing_keys:
                continue
            pred_log.append(make_prediction(date, row))
            existing_keys.add(key)
            new_count += 1
    log.info(f"Nouvelles prédictions enregistrées (backfill inclus) : {new_count}")

    # ── 2. Mesure des résultats ────────────────────────────────────────────
    updated = sum(1 for p in pred_log if measure(p))
    log.info(f"Prédictions mises à jour avec un résultat : {updated}")

    # ── 3. Nettoyage : seulement les prédictions trop vieilles ET jamais mesurées
    cutoff = shift_date(TODAY, -MAX_PENDING_AGE)
    before = len(pred_log)
    pred_log = [p for p in pred_log if p.get("measured_date") is not None or p["date"] >= cutoff]
    if len(pred_log) < before:
        log.info(f"Prédictions abandonnées (non mesurables après {MAX_PENDING_AGE} j) : {before - len(pred_log)}")

    pred_log.sort(key=lambda p: (p["date"], p["symbol"]))
    save_json(log_path, pred_log)
    return pred_log


# ─────────────────────── 2b. Calibration de bull_prob_7d ───────────────────

def _spearman(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    if n < 10: return 0.0
    def ranks(v):
        order = sorted(range(n), key=lambda i: v[i]); r = [0.0] * n
        i = 0
        while i < n:  # rangs moyens pour les ex aequo
            j = i
            while j + 1 < n and v[order[j + 1]] == v[order[i]]: j += 1
            for k in range(i, j + 1): r[order[k]] = (i + j) / 2
            i = j + 1
        return r
    rx, ry = ranks(xs), ranks(ys)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return num / den if den else 0.0

def compute_calibration() -> dict:
    """
    Juge bull_prob_7d sur TOUT l'univers (pas seulement les tokens >= 70) :
    pour chaque (date, token) historique, return réel à 7 j et 14 j.
    Répond à : "quand je dis 70 %, est-ce que ça monte 70 % du temps ?"
    et "est-ce que les tokens bien notés font mieux que les autres ?".
    Sauvegardé dans data/learning/calibration.json.
    """
    result = {"generated_date": TODAY, "horizons": {}}
    dates = [d for d in history_dates() if (load_snapshot(d) and "bull_prob_7d" in next(iter(load_snapshot(d).values())))]
    for h in OUTCOME_HORIZONS:
        obs = []  # (bull_prob, return, excess, date)
        for d in dates:
            d_out = find_outcome_snapshot(d, h)
            if not d_out: continue
            s0, s1 = load_snapshot(d), load_snapshot(d_out)
            med = universe_median_return(d, d_out)
            if med is None: continue
            for sym, r in s0.items():
                if _is_excluded(r) or sym not in s1: continue
                bp, p0, p1 = _fnum(r.get("bull_prob_7d")), _fnum(r.get("price")), _fnum(s1[sym].get("price"))
                if bp is None or not p0 or not p1 or p0 <= 0: continue
                ret = (p1 / p0 - 1) * 100
                obs.append((bp, ret, ret - med, d))
        if not obs:
            continue
        buckets = []
        for lo, hi in CALIB_BUCKETS:
            b = [o for o in obs if lo <= o[0] < hi]
            if not b: continue
            buckets.append({
                "range": f"{lo}-{hi - 1}",
                "predicted_mean": round(sum(o[0] for o in b) / len(b), 1),
                "n": len(b),
                "hit_rate": round(sum(o[1] > 0 for o in b) / len(b), 3),
                "beat_market_rate": round(sum(o[2] > 0 for o in b) / len(b), 3),
                "median_return": round(_median([o[1] for o in b]), 2),
            })
        result["horizons"][str(h)] = {
            "n_obs": len(obs),
            "n_days": len({o[3] for o in obs}),
            "base_hit_rate": round(sum(o[1] > 0 for o in obs) / len(obs), 3),
            "spearman_excess": round(_spearman([o[0] for o in obs], [o[2] for o in obs]), 4),
            "buckets": buckets,
        }
    save_json(LEARNING / "calibration.json", result)
    return result


# ─────────────────────── 3. Journal quotidien ─────────────────────────────

def update_journal(weights: dict, today_scores: list[dict]) -> list[dict]:
    """Ajoute une entrée par jour dans journal.json — conserve les MAX_JOURNAL_DAYS derniers."""
    journal_path = LEARNING / "journal.json"
    journal: list[dict] = load_json(journal_path, [])

    # évite les doublons
    if journal and journal[-1]["date"] == TODAY:
        return journal

    btc_row  = next((r for r in today_scores if r.get("symbol") == "BTCUSDT"), None)
    btc_prob = float(btc_row.get("bull_prob_7d", 50)) if btc_row else 50

    top = sorted(
        [r for r in today_scores if float(r.get("score") or 0) >= SCORE_THRESHOLD],
        key=lambda r: -float(r.get("score") or 0)
    )[:5]
    top_names = [r["symbol"].replace("USDT", "") for r in top]

    # meilleur signal haussier du jour
    best_bull = max(
        [(p, weights[p]["hit_rate_14d"]) for p in BULL_PATS
         if p in weights and weights[p].get("hit_rate_14d")],
        key=lambda x: x[1], default=("—", 0.0)
    )

    bear_ok = [p for p in BEAR_PATS
               if p in weights and (weights[p].get("hit_rate_14d") or 0) > 0.50]

    journal.append({
        "date":           TODAY,
        "btc_prob":       round(btc_prob, 1),
        "regime":         "Haussier" if btc_prob >= 55 else ("Baissier" if btc_prob <= 45 else "Neutre"),
        "top_tokens":     top_names,
        "n_top":          len(top),
        "best_bull_pat":  best_bull[0],
        "best_bull_rate": round(best_bull[1], 3),
        "bear_signals_ok": len(bear_ok),
    })

    journal = journal[-MAX_JOURNAL_DAYS:]
    save_json(journal_path, journal)
    return journal


# ─────────────────────── 4. Section évolution ──────────────────────────────

def generate_evolution_section(pat_history: dict, journal: list[dict]) -> str:
    """Décrit comment le projet a évolué depuis le début."""
    lines = []
    a = lines.append

    a("## Comment j'évolue et comment je m'adapte")
    a("")

    # ── Évolution du régime marché ─────────────────────────────────────────
    if len(journal) >= 2:
        a("### Évolution du régime de marché")
        a("")
        a("| Date | Régime | BTC bull_prob | Top tokens |")
        a("|------|--------|---------------|-----------|")
        for entry in journal:
            emoji = "🟢" if entry["regime"] == "Haussier" else ("🔴" if entry["regime"] == "Baissier" else "🟡")
            tops  = ", ".join(entry.get("top_tokens", [])[:3])
            a(f"| {fmt_date(entry['date'])} | {emoji} {entry['regime']} | {entry['btc_prob']}% | {tops} |")
        a("")

        # tendance régime
        first_prob = journal[0]["btc_prob"]
        last_prob  = journal[-1]["btc_prob"]
        delta = last_prob - first_prob
        if delta > 5:
            a(f"📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob {first_prob}% → {last_prob}%")
        elif delta < -5:
            a(f"📉 **Le marché s'est dégradé** depuis le début du journal : BTC bull_prob {first_prob}% → {last_prob}%")
        else:
            a(f"→ **Régime stable** : BTC bull_prob entre {first_prob}% et {last_prob}%")
        a("")

    # ── Évolution des patterns clés ────────────────────────────────────────
    a("### Évolution des patterns clés")
    a("")
    key_patterns = ["bear_flag", "rsi_bullish_divergence", "downtrend", "squeeze_breakout", "rsi_bearish_divergence"]
    for pat in key_patterns:
        hist = pat_history.get(pat, [])
        if len(hist) < 2:
            continue
        first = hist[0]
        last  = hist[-1]
        delta = last["hit_rate"] - first["hit_rate"]
        direction = "📈" if delta > 0.02 else ("📉" if delta < -0.02 else "→")
        kind = "baissier" if pat in BEAR_PATS else "haussier"
        a(f"**`{pat}`** ({kind}) : {first['hit_rate']:.1%} ({fmt_date(first['date'])}) → "
          f"{last['hit_rate']:.1%} ({fmt_date(last['date'])}) — {delta:+.1%} {direction}")
    a("")

    # ── Interprétation ────────────────────────────────────────────────────
    a("### Ce que ça signifie")
    a("")
    bear_flag_hist = pat_history.get("bear_flag", [])
    bull_div_hist  = pat_history.get("rsi_bullish_divergence", [])

    if len(bear_flag_hist) >= 2:
        bf_delta = bear_flag_hist[-1]["hit_rate"] - bear_flag_hist[0]["hit_rate"]
        if bf_delta < -0.03:
            a("- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.")
        elif bf_delta > 0.03:
            a("- Les signaux baissiers **gagnent en précision** : le régime baissier se renforce.")
        else:
            a("- Les signaux baissiers sont **stables** : régime de marché inchangé.")

    if len(bull_div_hist) >= 2:
        bd_delta = bull_div_hist[-1]["hit_rate"] - bull_div_hist[0]["hit_rate"]
        if bd_delta > 0.03:
            a("- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.")
        elif bd_delta < -0.03:
            a("- Les signaux haussiers **reculent** : dans ce marché, les patterns d'achat ne fonctionnent pas encore.")
        else:
            a("- Les signaux haussiers sont **bloqués** sous 40% : je ne suis pas encore fiable pour détecter les hausses.")

    a("")
    a("---")
    a("")
    return "\n".join(lines)


# ─────────────────────── 5. Génération de la mémoire ───────────────────────

def generate_memory(
    weights:       dict,
    pat_history:   dict,
    pred_log:      list[dict],
    formula:       dict,
    today_scores:  list[dict],
    journal:       list[dict] | None = None,
    calibration:   dict | None = None,
) -> str:
    lines = []
    a = lines.append

    # ── En-tête ──────────────────────────────────────────────────────────
    a(f"# Mémoire du Projet Crypto Screening")
    a(f"*Dernière mise à jour : {fmt_date(TODAY)}*")
    a("")
    a("---")
    a("")

    # ── Qui je suis ───────────────────────────────────────────────────────
    a("## Qui je suis")
    a("")
    a("Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.")
    a("Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.")
    a("Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)")
    a("et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).")
    a("J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.")
    a("")
    a("---")
    a("")

    # ── Régime et auto-évaluation ─────────────────────────────────────────
    a("## Mon auto-évaluation")
    a("")

    btc_row  = next((r for r in today_scores if r.get("symbol") == "BTCUSDT"), None)
    btc_prob = float(btc_row.get("bull_prob_7d", 50)) if btc_row else 50

    if btc_prob >= 55:
        regime_emoji = "🟢"
        regime_label = "Haussier"
    elif btc_prob <= 45:
        regime_emoji = "🔴"
        regime_label = "Baissier"
    else:
        regime_emoji = "🟡"
        regime_label = "Neutre"

    a(f"**Régime de marché (BTC bull_prob) :** {regime_emoji} {regime_label} — {btc_prob:.0f}%")
    a("")

    # Signaux fiables
    bull_ok = [p for p in BULL_PATS
               if p in weights and (weights[p].get("hit_rate_14d") or 0) > 0.50]
    bear_ok = [p for p in BEAR_PATS
               if p in weights and (weights[p].get("hit_rate_14d") or 0) > 0.50]
    best_bull = max(
        [(p, weights[p]["hit_rate_14d"]) for p in BULL_PATS
         if p in weights and weights[p].get("hit_rate_14d")],
        key=lambda x: x[1], default=("—", 0.0)
    )

    if bull_ok:
        a(f"**Signaux haussiers fiables (>50%) :** {', '.join(bull_ok)} ✅")
        ready_for_buy = True
    else:
        a(f"**Signaux haussiers fiables (>50%) :** aucun ❌")
        a(f"  → Meilleur signal haussier actuel : `{best_bull[0]}` à {best_bull[1]:.1%}")
        ready_for_buy = False

    a(f"**Signaux baissiers fiables (>50%) :** {len(bear_ok)} / {len(BEAR_PATS)}")
    a("")

    # Précision sur les prédictions mesurées (horizon principal = 7 j)
    H = MAIN_HORIZON
    measured = [p for p in pred_log if p.get(f"return_{H}d") is not None]
    if measured:
        correct = sum(1 for p in measured if p.get(f"correct_{H}d"))
        accuracy = correct / len(measured) * 100
        bm = [p for p in measured if p.get(f"beat_market_{H}d") is not None]
        beat = sum(1 for p in bm if p[f"beat_market_{H}d"]) / len(bm) * 100 if bm else float("nan")
        a(f"**Mes prédictions ≥ {SCORE_THRESHOLD}% à {H} j :** {len(measured)} mesurées — "
          f"{accuracy:.0f}% ont monté, **{beat:.0f}% ont battu la médiane du marché** (50% = hasard)")
        a("")

    if ready_for_buy:
        a("### ✅ Mes signaux d'ACHAT sont exploitables.")
    else:
        a("### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.")
        a("N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.")
    a("")
    a("---")
    a("")

    # ── Patterns — état actuel et évolution ──────────────────────────────
    a("## Ce que j'ai appris sur les patterns")
    a("")

    a("### Signaux baissiers (>50% = le signal prédit correctement la baisse)")
    a("")
    a("| Pattern | Hit rate | Échantillons | Tendance |")
    a("|---------|----------|--------------|---------|")
    bear_sorted = sorted(
        [(p, weights[p]) for p in BEAR_PATS
         if p in weights and weights[p].get("hit_rate_14d") is not None],
        key=lambda x: -(x[1]["hit_rate_14d"] or 0)
    )
    for pat, data in bear_sorted:
        hr = data["hit_rate_14d"]
        n  = data["samples"]
        arrow = trend_arrow(pat_history.get(pat, []))
        a(f"| `{pat}` | {hr:.1%} | {n} | {arrow} |")

    a("")
    a("### Signaux haussiers (>50% = le signal prédit correctement la hausse)")
    a("")
    a("| Pattern | Hit rate | Échantillons | Tendance |")
    a("|---------|----------|--------------|---------|")
    bull_sorted = sorted(
        [(p, weights[p]) for p in BULL_PATS
         if p in weights and weights[p].get("hit_rate_14d") is not None],
        key=lambda x: -(x[1]["hit_rate_14d"] or 0)
    )
    for pat, data in bull_sorted:
        hr = data["hit_rate_14d"]
        n  = data["samples"]
        arrow = trend_arrow(pat_history.get(pat, []))
        a(f"| `{pat}` | {hr:.1%} | {n} | {arrow} |")

    a("")
    a("---")
    a("")

    # ── Prédictions passées ────────────────────────────────────────────────
    a("## Mes prédictions passées et leurs résultats")
    a("")
    a(f"*Une prédiction = un token noté ≥ {SCORE_THRESHOLD}% un jour donné. Jugée à {H} j (horizon de `bull_prob_7d`) "
      f"et à 14 j. « Bat le marché » = a fait mieux que la médiane de tous les tokens sur la même période.*")
    a("")
    if measured:
        by_month: dict[str, list] = {}
        for p in measured:
            by_month.setdefault(p["date"][:6], []).append(p)
        a("| Mois | Prédictions | Ont monté (7 j) | Ont battu le marché (7 j) | Return médian (7 j) |")
        a("|------|-------------|-----------------|---------------------------|---------------------|")
        for m in sorted(by_month):
            L = by_month[m]
            up = sum(1 for p in L if p.get(f"correct_{H}d")) / len(L)
            bmL = [p for p in L if p.get(f"beat_market_{H}d") is not None]
            bt = (sum(1 for p in bmL if p[f"beat_market_{H}d"]) / len(bmL)) if bmL else float("nan")
            med = _median([p[f"return_{H}d"] for p in L])
            a(f"| {m[:4]}-{m[4:]} | {len(L)} | {up:.0%} | {bt:.0%} | {med:+.1f}% |")
        a("")
        a("**Dernières prédictions mesurées :**")
        a("")
        a("| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |")
        a("|------|-------|-------|-------------|------------|-----------|-------------|")
        for p in sorted(measured, key=lambda x: (x["date"], x["score"]), reverse=True)[:20]:
            r7 = p.get(f"return_{H}d"); ex = p.get(f"excess_{H}d"); r14 = p.get("return_14d")
            emoji = "✅" if p.get(f"beat_market_{H}d") else "❌"
            a(f"| {fmt_date(p['date'])} | **{p['symbol'].replace('USDT','')}** | {p['score']:.0f}% | {p['price_at']:.6g} | "
              f"{r7:+.1f}% | {emoji} {ex:+.1f}pp | {f'{r14:+.1f}%' if r14 is not None else '…'} |")
    else:
        a(f"*Aucune prédiction mesurée pour l'instant ({H} jours de recul nécessaires).*")

    a("")
    pending = [p for p in pred_log if p.get(f"return_{H}d") is None]
    if pending:
        a(f"**{len(pending)} prédictions en attente de résultat (< {H} jours).**")
    a("")
    a("---")
    a("")

    # ── Calibration ────────────────────────────────────────────────────────
    cal = (calibration or {}).get("horizons", {}).get(str(H))
    if cal:
        a("## Mes probabilités sont-elles fiables ? (calibration de `bull_prob_7d`)")
        a("")
        a(f"Mesuré sur **tout l'univers** : {cal['n_obs']} observations (token, jour) sur {cal['n_days']} jours. "
          f"Taux de hausse moyen à {H} j, tous tokens confondus : **{cal['base_hit_rate']:.0%}**.")
        a("")
        a("| bull_prob annoncé | Observations | A monté | A battu le marché | Return médian |")
        a("|-------------------|--------------|---------|-------------------|---------------|")
        for b in cal["buckets"]:
            a(f"| {b['range']}% (moy. {b['predicted_mean']:.0f}%) | {b['n']} | {b['hit_rate']:.0%} | "
              f"{b['beat_market_rate']:.0%} | {b['median_return']:+.1f}% |")
        a("")
        rho = cal["spearman_excess"]
        a(f"**Corrélation de rang (bull_prob vs surperformance) : {rho:+.3f}**")
        if abs(rho) < 0.03:
            a("→ **Verdict : mon score ne distingue pas les gagnants des perdants.** Les tokens bien notés ne font pas mieux que les autres.")
        elif rho > 0:
            a("→ Verdict : un pouvoir prédictif apparaît (les tokens mieux notés font un peu mieux). À confirmer dans la durée.")
        else:
            a("→ **Verdict : corrélation négative — les tokens les mieux notés font MOINS bien que les autres.**")
        a("")
        a("---")
        a("")

    # ── Évolution ─────────────────────────────────────────────────────────
    evolution = generate_evolution_section(pat_history, journal or [])
    lines.extend(evolution.split("\n"))

    # ── Score composite ────────────────────────────────────────────────────
    a("## Le score composite est-il utile ?")
    a("")
    corrs   = formula.get("correlations", {})
    n_pairs = formula.get("n_pairs", 0)
    max_c   = max(corrs.values()) if corrs else 0.0
    a(f"J'ai analysé **{n_pairs} paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.")
    a("")
    if corrs:
        a("| Sous-score | Corrélation avec return 14j |")
        a("|------------|---------------------------|")
        for k, v in corrs.items():
            a(f"| {k} | {v:.4f} |")
        a("")
    if max_c < 0.05:
        a("**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**")
        a("C'est pourquoi j'utilise `bull_prob_7d` comme score principal.")
    else:
        a(f"**Verdict : une corrélation commence à émerger (max {max_c:.3f}). À surveiller.**")
    a("")
    a("---")
    a("")

    # ── Aujourd'hui ────────────────────────────────────────────────────────
    a(f"## Aujourd'hui — {fmt_date(TODAY)}")
    a("")
    a(f"**Régime :** {regime_emoji} {regime_label} (BTC bull_prob = {btc_prob:.0f}%)")
    a("")

    top = sorted(
        [r for r in today_scores if float(r.get("score") or 0) >= SCORE_THRESHOLD],
        key=lambda r: -float(r.get("score") or 0)
    )[:12]

    if top:
        a(f"**Top tokens aujourd'hui (score ≥ {SCORE_THRESHOLD}%) :**")
        a("")
        a("| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |")
        a("|-------|-------|--------------|-----------|-------------|")
        for r in top:
            sym   = r.get("symbol", "").replace("USDT", "")
            sc    = float(r.get("score") or 0)
            alpha = float(r.get("alpha_vs_btc") or 0)
            er    = int(float(r.get("exit_risk") or 0))
            er_s  = f"⚠️ {er}" if er >= 4 else str(er)
            cat   = (r.get("catalyst_flags") or "")[:50]
            a(f"| **{sym}** | {sc:.0f}% | {alpha:+.0f}pp | {er_s} | {cat} |")
    else:
        a("*Aucun token au-dessus du seuil aujourd'hui.*")

    a("")
    return "\n".join(lines)


# ─────────────────────────── entrée principale ─────────────────────────────

def run():
    LEARNING.mkdir(parents=True, exist_ok=True)

    weights      = load_json(LEARNING / "pattern_weights.json", {})
    formula      = load_json(LEARNING / "formula_weights.json", {"correlations": {}, "n_pairs": 0})
    today_scores = load_scores_csv(COMPUTED / "scores.csv")

    if not weights or not today_scores:
        log.warning("Données insuffisantes — mémoire non générée")
        return

    pat_history = update_pattern_history(weights)
    log.info(f"pattern_history : {len(pat_history)} patterns trackés")

    pred_log = update_prediction_log(today_scores)
    log.info(f"prediction_log : {len(pred_log)} entrées")

    journal = update_journal(weights, today_scores)
    log.info(f"journal : {len(journal)} entrées")

    try:
        calibration = compute_calibration()
        c7 = calibration.get("horizons", {}).get(str(MAIN_HORIZON), {})
        log.info(f"calibration : {c7.get('n_obs', 0)} obs, spearman={c7.get('spearman_excess')}")
    except Exception as e:
        log.warning(f"calibration impossible : {e}")
        calibration = None

    memory_md   = generate_memory(weights, pat_history, pred_log, formula, today_scores, journal, calibration)
    memory_path = LEARNING / "project_memory.md"
    memory_path.write_text(memory_md, encoding="utf-8")
    log.info(f"project_memory.md généré ({len(memory_md)} caractères)")


if __name__ == "__main__":
    run()
