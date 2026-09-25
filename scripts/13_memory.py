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
TOP_N_PRED       = 20   # une "prédiction" = un des 20 tokens les mieux classés du jour
# (avant le 25/09/2026 : score >= 70 ; le score appris n'atteint plus ces valeurs, on suit donc le top du classement)
# bull_prob_7d est une prédiction à 7 jours → on la juge à 7 jours.
# 14 jours est mesuré en complément.
OUTCOME_HORIZONS = (7, 14)
MAIN_HORIZON     = 7
SNAPSHOT_TOLERANCE = 2  # si le snapshot J+H manque, on accepte J+H+1 ou J+H+2
MAX_PENDING_AGE  = 30   # une prédiction non mesurable après 30 j (token délisté…) est abandonnée
MAX_JOURNAL_DAYS = 30   # jours de journal conservés
N_QUINTILES = 5

def model_group(row: dict) -> str:
    """Ancienne formule manuelle vs modèle appris (06b_ml_score.py)."""
    m = str(row.get("score_model") or "")
    return "Modèle appris" if m.startswith(("ml_", "naive")) else "Ancienne formule"

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

def make_prediction(date: str, row: dict, rank: int = 0) -> dict:
    score = float(row.get("score") or 0)
    return {
        "date":           date,
        "selection":      f"top{TOP_N_PRED}",
        "rank":           rank,
        "model":          model_group(row),
        "score_model":    row.get("score_model", ""),
        "market_regime":  row.get("market_regime", ""),
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
    1. Backfill : ajoute les prédictions (top TOP_N_PRED du jour) de tous les snapshots
       historiques qui ne sont pas encore dans le log (+ celles d'aujourd'hui).
    2. Mesure les résultats à 7 j et 14 j dès que le snapshot correspondant existe.
    3. Abandonne les prédictions impossibles à mesurer après MAX_PENDING_AGE jours.
    """
    log_path = LEARNING / "prediction_log.json"
    pred_log: list[dict] = load_json(log_path, [])
    # Les entrées de l'ancienne règle (score >= 70) sont reconstruites selon la règle actuelle
    pred_log = [p for p in pred_log if p.get("selection") == f"top{TOP_N_PRED}"]
    existing_keys = {(p["date"], p["symbol"]) for p in pred_log}

    # ── 1. Nouvelles prédictions : snapshots historiques + aujourd'hui ─────
    new_count = 0
    sources = [(d, list((load_snapshot(d) or {}).values())) for d in history_dates()]
    sources.append((TODAY, today_scores))
    for date, rows in sources:
        if not rows or "bull_prob_7d" not in rows[0]:
            continue  # snapshots antérieurs à l'introduction de bull_prob_7d
        eligible = [r for r in rows if not _is_excluded(r) and _fnum(r.get("price"))]
        eligible.sort(key=lambda r: -float(_fnum(r.get("score")) or 0))
        for rank, row in enumerate(eligible[:TOP_N_PRED], 1):
            key = (date, row.get("symbol", ""))
            if key in existing_keys:
                continue
            pred_log.append(make_prediction(date, row, rank))
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
    Juge le score sur TOUT l'univers (pas seulement le top), séparément pour
    l'ancienne formule et le modèle appris :
      - corrélation de rang score ↔ surperformance ;
      - le top 20 du jour bat-il la médiane ? ;
      - quintiles : les 20 % les mieux notés font-ils mieux que les 20 % les moins bien notés ?
    Sauvegardé dans data/learning/calibration.json.
    """
    result = {"generated_date": TODAY, "horizons": {}}
    dates = [d for d in history_dates() if (load_snapshot(d) and "bull_prob_7d" in next(iter(load_snapshot(d).values())))]
    for h in OUTCOME_HORIZONS:
        groups: dict[str, dict] = {}
        for d in dates:
            d_out = find_outcome_snapshot(d, h)
            if not d_out: continue
            s0, s1 = load_snapshot(d), load_snapshot(d_out)
            med = universe_median_return(d, d_out)
            if med is None: continue
            day = []
            for sym, r in s0.items():
                if _is_excluded(r) or sym not in s1: continue
                sc, p0, p1 = _fnum(r.get("score")), _fnum(r.get("price")), _fnum(s1[sym].get("price"))
                if sc is None or not p0 or not p1 or p0 <= 0: continue
                day.append((sc, (p1 / p0 - 1) * 100 - med, (p1 / p0 - 1) * 100))
            if len(day) < 50: continue
            g = groups.setdefault(model_group(next(iter(s0.values()))), {"obs": [], "top_beat": [], "q": [[] for _ in range(N_QUINTILES)], "days": 0})
            g["days"] += 1
            day.sort(key=lambda x: -x[0])
            g["top_beat"].append(sum(1 for x in day[:TOP_N_PRED] if x[1] > 0) / TOP_N_PRED)
            for i, x in enumerate(day):
                g["q"][min(N_QUINTILES - 1, i * N_QUINTILES // len(day))].append(x)
            g["obs"].extend(day)
        out = {}
        for name, g in groups.items():
            obs = g["obs"]
            out[name] = {
                "n_obs": len(obs), "n_days": g["days"],
                "spearman_excess": round(_spearman([o[0] for o in obs], [o[1] for o in obs]), 4),
                "top_beat_rate": round(sum(g["top_beat"]) / len(g["top_beat"]), 3),
                "quintiles": [{"q": i + 1,
                               "beat_market_rate": round(sum(1 for o in q if o[1] > 0) / len(q), 3) if q else None,
                               "median_return": round(_median([o[2] for o in q]), 2) if q else None}
                              for i, q in enumerate(g["q"])],
            }
        result["horizons"][str(h)] = out
    save_json(LEARNING / "calibration.json", result)
    return result


# ─────────────────────── 3. Journal quotidien ─────────────────────────────

def load_market_regime() -> dict:
    """Régime du jour calculé par 06b_ml_score.py (data/computed/market_regime.json)."""
    return (load_json(COMPUTED / "market_regime.json", {}) or {}).get("today", {}) or {}

REGIME_EMOJI = {"Altseason": "🚀", "Altseason en formation": "🌱", "Saison Bitcoin": "🟠",
                "Bitcoin domine (court terme)": "🟠", "Neutre": "🟡",
                "Haussier": "🟢", "Baissier": "🔴"}  # (les deux derniers : anciennes entrées du journal)

def update_journal(weights: dict, today_scores: list[dict]) -> list[dict]:
    """Ajoute une entrée par jour dans journal.json — conserve les MAX_JOURNAL_DAYS derniers."""
    journal_path = LEARNING / "journal.json"
    journal: list[dict] = load_json(journal_path, [])

    # évite les doublons
    if journal and journal[-1]["date"] == TODAY:
        return journal

    reg = load_market_regime()

    top = sorted(
        [r for r in today_scores if not _is_excluded(r)],
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
        "regime":         reg.get("label", "—"),
        "alt_index_30d":  reg.get("alt_index_30d"),
        "alt_index_90d":  reg.get("alt_index_90d"),
        "btc_ret_30d":    reg.get("btc_ret_30d"),
        "score_model":    (today_scores[0].get("score_model") if today_scores else ""),
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
        a("| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |")
        a("|------|--------|-----------------------|----------|-----------|")
        for entry in journal:
            reg = entry.get("regime", "—")
            alt = entry.get("alt_index_30d"); btc = entry.get("btc_ret_30d")
            alt_s = f"{alt:.0f}" if isinstance(alt, (int, float)) else "—"
            btc_s = f"{btc:+.1f}%" if isinstance(btc, (int, float)) else (f"(bull_prob {entry['btc_prob']}%)" if "btc_prob" in entry else "—")
            tops  = ", ".join(entry.get("top_tokens", [])[:3])
            a(f"| {fmt_date(entry['date'])} | {REGIME_EMOJI.get(reg, '')} {reg} | {alt_s} | {btc_s} | {tops} |")
        a("")
        a("*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*")
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
    a("Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.).")
    a("Depuis le 26/09/2026, mon `score` est la **probabilité qu'un token fasse mieux que la médiane du marché sur 7 jours**,")
    a("calculée par un modèle réentraîné chaque jour sur toutes mes prédictions passées déjà mesurées (`06b_ml_score.py`).")
    a("Je surveille aussi le **régime de marché** (altseason ou saison Bitcoin), car ce qui marche change selon le régime.")
    a("")
    a("---")
    a("")

    # ── Régime et auto-évaluation ─────────────────────────────────────────
    a("## Mon auto-évaluation")
    a("")

    reg = load_market_regime()
    regime_label = reg.get("label", "inconnu")
    regime_emoji = REGIME_EMOJI.get(regime_label, "")
    mrep = load_json(LEARNING / "model_report.json", {})

    a(f"### Régime de marché : {regime_emoji} {regime_label}")
    a("")
    if reg:
        a(f"- **Indice altseason** : {reg.get('alt_index_30d', '—')} sur 30 j, {reg.get('alt_index_90d', '—')} sur 90 j "
          f"(= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)")
        a(f"- **BTC** : {reg.get('btc_ret_30d', '—')} % sur 30 j · **Tokens au-dessus de leur MA50** : {reg.get('breadth_ma50', '—')} %")
        if "Altseason" in regime_label or (reg.get("alt_index_30d") or 0) >= 60:
            a("- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) "
              "s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, "
              f"et j'entraînerai un modèle dédié à l'altseason dès que j'aurai {mrep.get('min_alt_days_for_alt_model', 30)} jours "
              f"d'altseason mesurés (actuellement : {mrep.get('alt_days_measured', '?')}).")
    a("")

    if mrep:
        oos = mrep.get("oos_last_5_weeks", {})
        a(f"### Mon modèle aujourd'hui : `{mrep.get('model_used_today', '?')}`")
        a("")
        a(f"- Entraîné sur {mrep.get('train_rows', '?')} observations ({mrep.get('train_days', '?')} jours), horizon {mrep.get('horizon_days', 7)} j")
        if oos.get("model_top20_beat") is not None:
            a(f"- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane "
              f"**{oos['model_top20_beat']:.0%}** du temps (règle simple « grosses caps peu volatiles » : {oos.get('naive_top20_beat', 0):.0%} ; hasard : 50 %)")
        if mrep.get("calibration_k") is not None:
            a(f"- Confiance (calibration) : k = {mrep['calibration_k']:.2f} "
              f"— plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment")
        if mrep.get("top_factors"):
            a("- Ce qui compte le plus en ce moment : " + ", ".join(
                f"`{f['feature']}` ({'+' if f['effect'] > 0 else '−'})" for f in mrep["top_factors"][:6]))
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
        a(f"**Mon top {TOP_N_PRED} quotidien, jugé à {H} j :** {len(measured)} prédictions mesurées — "
          f"{accuracy:.0f}% ont monté, **{beat:.0f}% ont battu la médiane du marché** (50% = hasard)")
        a("")

    ml_live = [p for p in measured if p.get("model") == "Modèle appris" and p.get(f"beat_market_{H}d") is not None]
    if len({p["date"] for p in ml_live}) >= 10:
        live = sum(1 for p in ml_live if p[f"beat_market_{H}d"]) / len(ml_live)
        if live >= 0.55:
            a(f"### ✅ En conditions réelles, mon classement bat le marché ({live:.0%} de mon top {TOP_N_PRED}).")
        else:
            a(f"### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché ({live:.0%} de mon top {TOP_N_PRED}).")
    else:
        a("### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).")
    a("Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.")
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
    a(f"*Une prédiction = un des {TOP_N_PRED} tokens les mieux classés un jour donné. Jugée à {H} j et à 14 j. "
      f"« Bat le marché » = a fait mieux que la médiane de tous les tokens sur la même période.*")
    a("")
    if measured:
        by_month: dict[tuple, list] = {}
        for p in measured:
            by_month.setdefault((p["date"][:6], p.get("model", "Ancienne formule")), []).append(p)
        a("| Mois | Modèle | Prédictions | Ont monté (7 j) | Ont battu le marché (7 j) | Return médian (7 j) |")
        a("|------|--------|-------------|-----------------|---------------------------|---------------------|")
        for (m, model) in sorted(by_month):
            L = by_month[(m, model)]
            up = sum(1 for p in L if p.get(f"correct_{H}d")) / len(L)
            bmL = [p for p in L if p.get(f"beat_market_{H}d") is not None]
            bt = (sum(1 for p in bmL if p[f"beat_market_{H}d"]) / len(bmL)) if bmL else float("nan")
            med = _median([p[f"return_{H}d"] for p in L])
            a(f"| {m[:4]}-{m[4:]} | {model} | {len(L)} | {up:.0%} | {bt:.0%} | {med:+.1f}% |")
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
    cal = (calibration or {}).get("horizons", {}).get(str(H)) or {}
    if cal:
        a("## Mon classement distingue-t-il les gagnants des perdants ?")
        a("")
        a(f"*Mesuré sur **tout l'univers**, à {H} jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. "
          "Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*")
        a("")
        a("| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |")
        a("|--------|-------|---------------------|----------------------|----|----|----|----|----|")
        for name in ("Ancienne formule", "Modèle appris"):
            c = cal.get(name)
            if not c: continue
            qs = " | ".join(f"{q['beat_market_rate']:.0%}" if q["beat_market_rate"] is not None else "—" for q in c["quintiles"])
            a(f"| {name} | {c['n_days']} | {c['spearman_excess']:+.3f} | {c['top_beat_rate']:.0%} | {qs} |")
        a("")
        a("*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*")
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
        a("C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).")
    else:
        a(f"**Verdict : une corrélation commence à émerger (max {max_c:.3f}). À surveiller.**")
    a("")
    a("---")
    a("")

    # ── Aujourd'hui ────────────────────────────────────────────────────────
    a(f"## Aujourd'hui — {fmt_date(TODAY)}")
    a("")
    a(f"**Régime :** {regime_emoji} {regime_label} (indice altseason 30 j : {reg.get('alt_index_30d', '—')})")
    a("")

    top = sorted(
        [r for r in today_scores if not _is_excluded(r)],
        key=lambda r: -float(r.get("score") or 0)
    )[:12]

    if top:
        a(f"**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j "
          f"(modèle : `{top[0].get('score_model') or 'ancienne formule'}`) :")
        a("")
        a("| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |")
        a("|-------|------|-------|--------|-----------|-------------|")
        for r in top:
            sym   = r.get("symbol", "").replace("USDT", "")
            sc    = float(r.get("score") or 0)
            alpha = float(r.get("alpha_vs_btc") or 0)
            er    = int(float(r.get("exit_risk") or 0))
            er_s  = f"⚠️ {er}" if er >= 4 else str(er)
            cat   = (r.get("catalyst_flags") or "")[:50]
            a(f"| **{sym}** | {r.get('tier', '')} | {sc:.1f}% | {alpha:+.1f}pp | {er_s} | {cat} |")
    else:
        a("*Aucun token classé aujourd'hui.*")

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
        for name, c in c7.items():
            log.info(f"calibration [{name}] : {c['n_days']} jours, top{TOP_N_PRED} bat le marché {c['top_beat_rate']:.0%}, spearman={c['spearman_excess']}")
    except Exception as e:
        log.warning(f"calibration impossible : {e}")
        calibration = None

    memory_md   = generate_memory(weights, pat_history, pred_log, formula, today_scores, journal, calibration)
    memory_path = LEARNING / "project_memory.md"
    memory_path.write_text(memory_md, encoding="utf-8")
    log.info(f"project_memory.md généré ({len(memory_md)} caractères)")


if __name__ == "__main__":
    run()
