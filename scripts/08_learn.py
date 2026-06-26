"""Apprentissage adaptatif — mesure la précision de chaque pattern et met à jour les poids.

Processus quotidien (après 06_score) :
  1. Lit le CSV de scores d'aujourd'hui (prix actuels)
  2. Pour chaque snapshot historique à 7/14/30 jours :
     - Récupère les patterns détectés ce jour-là et les prix
     - Calcule le return réel entre date_detection et aujourd'hui
     - Enregistre dans outcomes.csv
  3. Calcule le hit_rate par pattern sur 14 jours
  4. Met à jour pattern_weights.json

Les poids sont lus par 06_score.py à chaque run pour pondérer score_signal.
"""
from __future__ import annotations
from common import ROOT, TODAY, COMPUTED, HISTORY, setup_logger
import csv, json, math
from datetime import datetime, timedelta, timezone
from pathlib import Path

log = setup_logger("08_learn")

LEARNING = ROOT / "data" / "learning"

BULLISH_PATS = {
    "breakout_30d", "rsi_bullish_divergence", "golden_cross",
    "macd_bullish_cross", "double_bottom_90d", "bull_flag",
    "uptrend", "support_bounce", "hammer_4h", "bullish_engulfing_4h",
    "morning_star_4h", "squeeze_breakout",
}
BEARISH_PATS = {
    "breakdown_30d", "rsi_bearish_divergence", "death_cross",
    "macd_bearish_cross", "double_top_90d", "bear_flag",
    "downtrend", "resistance_test", "shooting_star_4h",
    "bearish_engulfing_4h", "evening_star_4h",
}
ALL_PATS = BULLISH_PATS | BEARISH_PATS

HORIZONS = [7, 14, 30]   # jours mesurés
MIN_SAMPLES = 5           # observations minimales avant d'ajuster le poids
MAX_WEIGHT = 2.5
MIN_WEIGHT = 0.1
# Horizon de référence pour le calcul des poids (meilleur compromis signal/bruit)
WEIGHT_HORIZON = 14


# ─────────────────────────── I/O helpers ───────────────────────────────────

def date_n_ago(n: int) -> str:
    return (datetime.now(timezone.utc) - timedelta(days=n)).strftime("%Y%m%d")

def load_snapshot(date_str: str) -> dict | None:
    """Charge un snapshot CSV par date YYYYMMDD depuis history/."""
    path = HISTORY / f"scores_{date_str}.csv"
    if not path.exists():
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return {r["symbol"]: r for r in csv.DictReader(f)}
    except Exception as e:
        log.warning(f"Impossible de lire {path}: {e}")
        return None

def load_today_prices() -> dict:
    """Prix actuels depuis le CSV du jour."""
    path = COMPUTED / "scores.csv"
    if not path.exists():
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return {r["symbol"]: float(r["price"])
                    for r in csv.DictReader(f) if r.get("price")}
    except Exception as e:
        log.warning(f"Impossible de lire CSV du jour: {e}")
        return {}

def load_existing_keys() -> set:
    """Charge les clés déjà enregistrées pour éviter les doublons."""
    outcomes_path = LEARNING / "outcomes.csv"
    if not outcomes_path.exists():
        return set()
    keys = set()
    try:
        with open(outcomes_path, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                keys.add((r["date_detected"], r["date_measured"],
                          r["horizon_days"], r["symbol"], r["pattern"]))
    except Exception:
        pass
    return keys

def append_outcomes(rows: list):
    """Ajoute de nouvelles observations à outcomes.csv."""
    outcomes_path = LEARNING / "outcomes.csv"
    is_new = not outcomes_path.exists()
    fieldnames = [
        "date_detected", "date_measured", "horizon_days",
        "symbol", "pattern", "direction",
        "price_at_detection", "price_now", "return_pct", "correct",
    ]
    with open(outcomes_path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        if is_new:
            w.writeheader()
        w.writerows(rows)


# ─────────────────────────── calcul des poids ──────────────────────────────

def compute_weights() -> dict:
    """Lit outcomes.csv, calcule le hit_rate 14j par pattern, retourne les poids."""
    outcomes_path = LEARNING / "outcomes.csv"
    if not outcomes_path.exists():
        return {}

    stats: dict[str, dict] = {}
    try:
        with open(outcomes_path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if int(row["horizon_days"]) != WEIGHT_HORIZON:
                    continue
                pat = row["pattern"]
                correct = (row["correct"] == "1")
                if pat not in stats:
                    stats[pat] = {"correct": 0, "total": 0}
                stats[pat]["total"] += 1
                if correct:
                    stats[pat]["correct"] += 1
    except Exception as e:
        log.warning(f"Erreur lecture outcomes: {e}")
        return {}

    # Charge poids précédents
    weights_path = LEARNING / "pattern_weights.json"
    previous = {}
    if weights_path.exists():
        try:
            previous = json.loads(weights_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    updated: dict[str, dict] = {}

    for pat in ALL_PATS:
        s = stats.get(pat, {"correct": 0, "total": 0})
        n = s["total"]
        hit_rate = (s["correct"] / n) if n > 0 else 0.5

        if n < MIN_SAMPLES:
            # Pas encore assez de données : garde le poids précédent
            prev = previous.get(pat, {})
            w = prev.get("weight", 1.0) if isinstance(prev, dict) else 1.0
        else:
            # Poids linéaire : hit_rate=0.5 → 1.0, 0.75 → 2.0, 0.25 → 0.0
            raw = 1.0 + (hit_rate - 0.5) * 4.0
            w = max(MIN_WEIGHT, min(MAX_WEIGHT, raw))

        updated[pat] = {
            "weight":       round(w, 3),
            "hit_rate_14d": round(hit_rate, 3) if n >= MIN_SAMPLES else None,
            "samples":      n,
        }

    return updated


def save_weights(weights: dict):
    weights_path = LEARNING / "pattern_weights.json"
    weights_path.write_text(
        json.dumps(weights, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    ranked = sorted(
        [(p, v["weight"], v.get("hit_rate_14d"), v.get("samples", 0))
         for p, v in weights.items() if v.get("samples", 0) >= MIN_SAMPLES],
        key=lambda x: -x[1]
    )
    if ranked:
        log.info(f"Poids adaptatifs mis a jour ({len(ranked)} patterns avec >= {MIN_SAMPLES} obs.) :")
        for p, w, hr, n in ranked[:5]:
            log.info(f"  {p:<30s}  poids={w:.2f}  hit_rate={hr:.0%}  n={n}")
    else:
        log.info("Pas encore assez d'observations pour ajuster les poids")


# ─────────────────── Poids formule composite ───────────────────────────────
# Axes : solidity, momentum, risk, antiscam, signal
# Défauts v1.2 : 0.20 / 0.30 / 0.15 / 0.20 / 0.15
DEFAULT_FORMULA = {
    "solidity":  0.20,
    "momentum":  0.30,
    "risk":      0.15,
    "antiscam":  0.20,
    "signal":    0.15,
}

def _pearson(xs: list, ys: list) -> float:
    """Corrélation de Pearson entre deux listes de même longueur."""
    n = len(xs)
    if n < 5: return 0.0
    mx, my = sum(xs)/n, sum(ys)/n
    num  = sum((x-mx)*(y-my) for x,y in zip(xs,ys))
    dsx  = math.sqrt(sum((x-mx)**2 for x in xs))
    dsy  = math.sqrt(sum((y-my)**2 for y in ys))
    return (num / (dsx * dsy)) if dsx and dsy else 0.0

def compute_formula_weights() -> dict | None:
    """Corrèle chaque sous-score avec le return 14j réel, produit formula_weights.json.

    Méthode :
      Pour chaque ligne d'outcomes.csv (horizon=14) :
        - Récupère le return_pct réel
        - Charge les sous-scores du snapshot historique correspondant
        - Stocke (return, score_sol, score_mom, score_risk, score_anti, score_sig)
      Calcule la corrélation de Pearson de chaque axe avec le return.
      Convertit en poids normalisés, blendés avec les défauts selon la quantité de données.
    """
    outcomes_path = LEARNING / "outcomes.csv"
    if not outcomes_path.exists():
        return None

    # ── agrège les returns par (date_detected, symbol) ────────────────────
    returns_by_key: dict[tuple, list] = {}
    try:
        with open(outcomes_path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if int(row["horizon_days"]) != WEIGHT_HORIZON: continue
                key = (row["date_detected"], row["symbol"])
                ret = float(row["return_pct"])
                returns_by_key.setdefault(key, []).append(ret)
    except Exception as e:
        log.warning(f"compute_formula_weights: lecture outcomes: {e}")
        return None

    if len(returns_by_key) < 20:
        log.info(f"Pas assez de paires (date,symbol) pour calibrer la formule ({len(returns_by_key)}<20)")
        return None

    # ── joint avec les sous-scores historiques ────────────────────────────
    axes = ["score_solidity", "score_momentum", "score_risk", "score_antiscam", "score_signal"]
    data: dict[str, list] = {a: [] for a in axes}
    data["return"] = []

    dates_needed = set(k[0] for k in returns_by_key)
    for date_str in dates_needed:
        snap_path = HISTORY / f"scores_{date_str}.csv"
        if not snap_path.exists(): continue
        try:
            with open(snap_path, encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    key = (date_str, row["symbol"])
                    if key not in returns_by_key: continue
                    ret = sum(returns_by_key[key]) / len(returns_by_key[key])
                    ok = True
                    vals = {}
                    for a in axes:
                        v = row.get(a)
                        if v is None or v == "":
                            ok = False; break
                        vals[a] = float(v)
                    if not ok: continue
                    data["return"].append(ret)
                    for a in axes:
                        data[a].append(vals[a])
        except Exception as e:
            log.warning(f"compute_formula_weights: lecture {snap_path.name}: {e}")

    n_pairs = len(data["return"])
    if n_pairs < 20:
        log.info(f"Paires valides insuffisantes pour calibrer la formule ({n_pairs}<20)")
        return None

    # ── corrélations de Pearson ───────────────────────────────────────────
    corrs = {}
    for a in axes:
        c = _pearson(data[a], data["return"])
        corrs[a] = max(0.0, c)   # ne retient que les corrélations positives

    total_corr = sum(corrs.values())
    if total_corr < 1e-6:
        log.info("Corrélations nulles — données trop peu variées pour ajuster la formule")
        return None

    # ── poids appris (normalisés, somme = 1) ─────────────────────────────
    learned = {a: corrs[a] / total_corr for a in axes}

    # ── blend : plus on a de données, plus on fait confiance au modèle ───
    # blend_factor ∈ [0, 0.6] — plafond à 60% pour ne jamais totalement ignorer les défauts
    blend = min(0.60, n_pairs / 500)

    name_map = {
        "score_solidity": "solidity",
        "score_momentum": "momentum",
        "score_risk":     "risk",
        "score_antiscam": "antiscam",
        "score_signal":   "signal",
    }
    blended = {}
    for a in axes:
        key = name_map[a]
        w = DEFAULT_FORMULA[key] * (1 - blend) + learned[a] * blend
        blended[key] = round(w, 4)

    # Renormalise pour que la somme fasse exactement 1.0
    s = sum(blended.values())
    blended = {k: round(v/s, 4) for k, v in blended.items()}

    result = {
        "weights":    blended,
        "n_pairs":    n_pairs,
        "blend_factor": round(blend, 3),
        "correlations": {name_map[a]: round(corrs[a], 4) for a in axes},
        "generated_date": TODAY,
    }

    fw_path = LEARNING / "formula_weights.json"
    fw_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    log.info(f"formula_weights mis a jour (n={n_pairs}, blend={blend:.0%}) :")
    for k, w in blended.items():
        c = result["correlations"].get(k, 0)
        log.info(f"  {k:<12s}  poids={w:.3f}  corr={c:.3f}")
    return result


# ─────────────────────────── entrée principale ─────────────────────────────

def run():
    LEARNING.mkdir(parents=True, exist_ok=True)

    today_prices = load_today_prices()
    if not today_prices:
        log.warning("Pas de prix d'aujourd'hui — apprentissage ignore")
        return

    existing_keys = load_existing_keys()
    total_new = 0

    for horizon in HORIZONS:
        date_ago = date_n_ago(horizon)
        snapshot = load_snapshot(date_ago)
        if not snapshot:
            log.info(f"Pas de snapshot J-{horizon} ({date_ago}) — ignore")
            continue

        new_rows = []
        for sym, row in snapshot.items():
            price_then = float(row.get("price") or 0)
            if price_then <= 0 or sym not in today_prices:
                continue

            price_now = today_prices[sym]
            ret = (price_now - price_then) / price_then

            patterns = [p for p in (row.get("patterns") or "").split("|") if p]
            for pat in patterns:
                if pat not in ALL_PATS:
                    continue
                key = (date_ago, TODAY, str(horizon), sym, pat)
                if key in existing_keys:
                    continue  # déjà enregistré

                direction = "bull" if pat in BULLISH_PATS else "bear"
                correct   = 1 if (direction == "bull" and ret > 0) or \
                                  (direction == "bear" and ret < 0) else 0

                new_rows.append({
                    "date_detected":      date_ago,
                    "date_measured":      TODAY,
                    "horizon_days":       horizon,
                    "symbol":             sym,
                    "pattern":            pat,
                    "direction":          direction,
                    "price_at_detection": round(price_then, 8),
                    "price_now":          round(price_now, 8),
                    "return_pct":         round(ret * 100, 3),
                    "correct":            correct,
                })
                existing_keys.add(key)

        if new_rows:
            append_outcomes(new_rows)
            total_new += len(new_rows)
            log.info(f"J-{horizon} ({date_ago}): {len(new_rows)} nouvelles observations")
        else:
            log.info(f"J-{horizon} ({date_ago}): deja traite")

    log.info(f"Total nouvelles observations : {total_new}")

    # ── Poids patterns ────────────────────────────────────────────────────
    weights = compute_weights()
    if weights:
        save_weights(weights)
    else:
        log.info("Pas encore d'outcomes — poids patterns non modifies")

    # ── Poids formule composite ───────────────────────────────────────────
    fw = compute_formula_weights()
    if not fw:
        log.info("Pas encore assez de donnees pour calibrer la formule — defaults conserves")


if __name__ == "__main__":
    run()
