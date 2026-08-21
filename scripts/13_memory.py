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
OUTCOME_HORIZON  = 14   # jours après lesquels on mesure si la prédiction était correcte
MAX_JOURNAL_DAYS = 30   # jours de journal conservés

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

def trend_arrow(history: list[dict]) -> str:
    """Flèche de tendance basée sur les 2 derniers snapshots."""
    if len(history) < 2:
        return "→"
    delta = history[-1]["hit_rate"] - history[-2]["hit_rate"]
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

def update_prediction_log(today_scores: list[dict]) -> list[dict]:
    """
    1. Enregistre les nouvelles prédictions (tokens score >= SCORE_THRESHOLD).
    2. Mesure les outcomes des prédictions faites il y a OUTCOME_HORIZON jours.
    """
    log_path = LEARNING / "prediction_log.json"
    pred_log: list[dict] = load_json(log_path, [])
    existing_keys = {(p["date"], p["symbol"]) for p in pred_log}

    # Prix actuels pour calculer les outcomes
    current_prices = {
        r["symbol"]: float(r["price"])
        for r in today_scores
        if r.get("price") and float(r.get("price") or 0) > 0
    }

    # ── Enregistre prédictions d'aujourd'hui ──────────────────────────────
    new_count = 0
    for row in today_scores:
        sym   = row.get("symbol", "")
        score = float(row.get("score") or 0)
        if score < SCORE_THRESHOLD:
            continue
        if (TODAY, sym) in existing_keys:
            continue
        pred_log.append({
            "date":           TODAY,
            "symbol":         sym,
            "score":          score,
            "bull_prob":      float(row.get("bull_prob_7d") or score),
            "alpha_vs_btc":   float(row.get("alpha_vs_btc") or 0),
            "vs_btc_label":   row.get("vs_btc_label", ""),
            "price_at":       float(row.get("price") or 0),
            "patterns":       row.get("patterns", ""),
            "catalyst_flags": row.get("catalyst_flags", ""),
            "exit_risk":      int(float(row.get("exit_risk") or 0)),
            "price_outcome":  None,
            "return_pct":     None,
            "correct":        None,
            "measured_date":  None,
        })
        new_count += 1

    log.info(f"Nouvelles prédictions enregistrées : {new_count}")

    # ── Met à jour les outcomes ────────────────────────────────────────────
    target_date = date_n_ago(OUTCOME_HORIZON)
    updated = 0
    for p in pred_log:
        if p.get("measured_date") is not None:
            continue  # déjà mesuré
        if p["date"] > target_date:
            continue  # trop récent
        sym = p["symbol"]
        price_then = p.get("price_at", 0)
        if sym not in current_prices or price_then <= 0:
            continue
        price_now = current_prices[sym]
        ret = (price_now - price_then) / price_then * 100
        p["price_outcome"]  = round(price_now, 8)
        p["return_pct"]     = round(ret, 2)
        p["correct"]        = ret > 0
        p["measured_date"]  = TODAY
        updated += 1

    log.info(f"Outcomes mis à jour : {updated} prédictions")

    # Garde les 300 dernières entrées
    pred_log = pred_log[-300:]
    save_json(log_path, pred_log)
    return pred_log


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

    # Précision sur les prédictions mesurées
    measured = [p for p in pred_log if p.get("measured_date") is not None]
    if measured:
        correct = sum(1 for p in measured if p.get("correct"))
        accuracy = correct / len(measured) * 100
        a(f"**Précision sur mes prédictions passées :** {accuracy:.0f}% ({correct}/{len(measured)} correctes)")
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

    if measured:
        a(f"**{len(measured)} prédictions mesurées — précision globale : {accuracy:.0f}%**")
        a("")
        a("| Date | Token | Score | Prix prédit | Prix 14j après | Résultat |")
        a("|------|-------|-------|-------------|----------------|---------|")
        for p in sorted(measured, key=lambda x: x["date"], reverse=True)[:25]:
            emoji  = "✅" if p.get("correct") else "❌"
            ret    = p.get("return_pct")
            ret_s  = f"{ret:+.1f}%" if ret is not None else "?"
            p_out  = p.get("price_outcome")
            p_out_s = f"{p_out:.6g}" if p_out else "?"
            a(f"| {fmt_date(p['date'])} | **{p['symbol'].replace('USDT','')}** | {p['score']:.0f}% | {p['price_at']:.6g} | {p_out_s} | {emoji} {ret_s} |")
    else:
        a("*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*")

    a("")
    pending = [p for p in pred_log if p.get("measured_date") is None]
    if pending:
        a(f"**{len(pending)} prédictions en attente de résultat (< 14 jours) :**")
        a("")
        a("| Date | Token | Score | Prix |")
        a("|------|-------|-------|------|")
        for p in sorted(pending, key=lambda x: x["date"], reverse=True)[:15]:
            a(f"| {fmt_date(p['date'])} | **{p['symbol'].replace('USDT','')}** | {p['score']:.0f}% | {p['price_at']:.6g} |")

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

    memory_md   = generate_memory(weights, pat_history, pred_log, formula, today_scores, journal)
    memory_path = LEARNING / "project_memory.md"
    memory_path.write_text(memory_md, encoding="utf-8")
    log.info(f"project_memory.md généré ({len(memory_md)} caractères)")


if __name__ == "__main__":
    run()
