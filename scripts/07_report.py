"""Génère report.md avec top par tier, suspects, setups, diff vs veille."""
from __future__ import annotations
from common import COMPUTED, HISTORY, ROOT, TODAY, setup_logger
import csv, glob, json, os
from datetime import datetime
log = setup_logger("07_report")

DISCLAIMER = (
"# ⚠️ AVERTISSEMENT\n"
"**Ce document n'est pas un conseil financier.** Le scoring reflète des indicateurs passés et publics, "
"pas une prédiction. La crypto peut faire perdre la totalité du capital investi. "
"Aucune action d'achat ou de vente n'est suggérée ici — seulement un classement à examiner.\n\n"
)

def load_csv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def fmt(v, kind="num"):
    if v is None or v == "" or v == "None": return "—"
    try:
        x = float(v)
        if kind == "pct": return f"{x*100:.1f}%"
        if kind == "pct_raw": return f"{x:.1f}%"
        if kind == "money":
            if x > 1e9: return f"{x/1e9:.2f}B$"
            if x > 1e6: return f"{x/1e6:.2f}M$"
            if x > 1e3: return f"{x/1e3:.1f}k$"
            return f"{x:.2f}$"
        if kind == "px":
            if x < 0.01: return f"{x:.6f}"
            if x < 1: return f"{x:.4f}"
            return f"{x:.2f}"
        return f"{x:.1f}"
    except: return str(v)

def previous_snapshot():
    files = sorted(glob.glob(str(HISTORY / "scores_*.csv")))
    if len(files) < 2: return None
    return files[-2]

def diff_vs_previous(today_rows, prev_path):
    prev = {r["symbol"]: r for r in load_csv(prev_path)}
    deltas = []
    for r in today_rows:
        p = prev.get(r["symbol"])
        if not p: continue
        try:
            d = float(r["score"]) - float(p["score"])
            deltas.append((r["symbol"], d, r))
        except: pass
    deltas.sort(key=lambda x: x[1], reverse=True)
    return deltas

def section_top_by_tier(rows, tier_name, n=20):
    sub = [r for r in rows if r["tier"] == tier_name
           and r["suspect"] != "True"
           and r.get("stablecoin") != "True"]
    sub.sort(key=lambda r: -float(r["score"]))
    sub = sub[:n]
    if not sub: return f"### {tier_name}\nAucun token.\n\n"
    out = [f"### Top {len(sub)} — Tier **{tier_name}**\n"]
    out.append("| # | Symbol | Score | Sol. | Mom. | Sig. | Risq. | Anti | Prix | Vol 24h | Δ24h | RSI | DD90 | Patterns |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(sub, 1):
        out.append(f"| {i} | **{r['symbol']}** | {fmt(r['score'])} | "
                   f"{fmt(r['score_solidity'])} | {fmt(r['score_momentum'])} | "
                   f"{fmt(r.get('score_signal','—'))} | {fmt(r['score_risk'])} | {fmt(r['score_antiscam'])} | "
                   f"{fmt(r['price'],'px')} | {fmt(r['vol_24h_usd'],'money')} | "
                   f"{fmt(r['change_24h_pct'],'pct_raw')} | {fmt(r['rsi_14'])} | "
                   f"{fmt(r['drawdown_90d'],'pct')} | {r['patterns'] or '—'} |")
    out.append("")
    return "\n".join(out) + "\n"

def section_suspects(rows):
    sus = [r for r in rows if r["suspect"] == "True"]
    if not sus: return "## Suspects\nAucun token flaggé SUSPECT lors de ce run.\n\n"
    sus.sort(key=lambda r: -float(r["vol_24h_usd"] or 0))
    out = [f"## Suspects flaggés ({len(sus)})\n",
           "Tokens automatiquement exclus du classement principal pour ≥ 2 red flags.\n",
           "| Symbol | Vol 24h | Tier | Red flags | Âge (j) | Catégories |",
           "|---|---|---|---|---|---|"]
    for r in sus[:40]:
        out.append(f"| {r['symbol']} | {fmt(r['vol_24h_usd'],'money')} | {r['tier']} | "
                   f"{r['n_red_flags']} | {r['age_days']} | {r['categories'][:60]} |")
    if len(sus) > 40: out.append(f"\n_…et {len(sus)-40} autres dans le CSV._\n")
    return "\n".join(out) + "\n"

BULLISH_PATS = {
    "breakout_30d", "rsi_bullish_divergence", "golden_cross", "macd_bullish_cross",
    "double_bottom_90d", "bull_flag", "uptrend", "support_bounce",
    "hammer_4h", "bullish_engulfing_4h", "morning_star_4h",
}
BEARISH_PATS = {
    "breakdown_30d", "rsi_bearish_divergence", "death_cross", "macd_bearish_cross",
    "double_top_90d", "bear_flag", "downtrend", "resistance_test",
    "shooting_star_4h", "bearish_engulfing_4h", "evening_star_4h",
}
PAT_LABEL = {
    "breakout_30d": "Breakout 30j", "breakdown_30d": "Breakdown 30j",
    "rsi_bullish_divergence": "Divergence RSI haussiere", "rsi_bearish_divergence": "Divergence RSI baissiere",
    "golden_cross": "Golden Cross MA50/200", "death_cross": "Death Cross MA50/200",
    "macd_bullish_cross": "Croisement MACD haussier", "macd_bearish_cross": "Croisement MACD baissier",
    "double_bottom_90d": "Double fond 90j", "double_top_90d": "Double sommet 90j",
    "bull_flag": "Bull flag", "bear_flag": "Bear flag",
    "uptrend": "Structure haussiere (HH+HL)", "downtrend": "Structure baissiere (LH+LL)",
    "support_bounce": "Rebond sur support", "resistance_test": "Test de resistance",
    "hammer_4h": "Marteau 4h", "shooting_star_4h": "Etoile filante 4h",
    "bullish_engulfing_4h": "Engulfing haussier 4h", "bearish_engulfing_4h": "Engulfing baissier 4h",
    "morning_star_4h": "Morning star 4h", "evening_star_4h": "Evening star 4h",
    "doji_4h": "Doji 4h",
}

def section_patterns(rows):
    """Analyse complète des patterns : biais directionnel + setups notables."""
    active = [r for r in rows if r.get("suspect") != "True" and r.get("stablecoin") != "True"]

    # Biais global
    bull_count = sum(int(r.get("bull_signals") or 0) for r in active)
    bear_count = sum(int(r.get("bear_signals") or 0) for r in active)
    bias_tokens = {"haussier": 0, "baissier": 0, "neutre": 0, "mixte": 0}
    for r in active:
        bias_tokens[r.get("bias", "neutre")] = bias_tokens.get(r.get("bias", "neutre"), 0) + 1

    out = ["## Analyse de patterns — signaux techniques\n",
           "> Indicateurs passés uniquement. Aucun signal n'est une recommandation.\n\n",
           "### Vue d'ensemble\n",
           f"| Metrique | Valeur |",
           f"|---|---|",
           f"| Tokens avec biais haussier | **{bias_tokens['haussier']}** |",
           f"| Tokens avec biais baissier | **{bias_tokens['baissier']}** |",
           f"| Tokens mixtes / neutres | {bias_tokens['mixte'] + bias_tokens['neutre']} |",
           f"| Total signaux haussiers detectes | {bull_count} |",
           f"| Total signaux baissiers detectes | {bear_count} |",
           ""]

    # Top tokens par biais haussier
    bull_tokens = sorted([r for r in active if r.get("bias") == "haussier"],
                         key=lambda r: (-int(r.get("bull_signals") or 0), -float(r.get("score") or 0)))
    if bull_tokens:
        out.append("### Setups haussiers les plus confluents\n")
        out.append("| Symbol | Tier | Score | Signaux haussiers | Signaux baissiers | Patterns detectes | Support 90j | Prix actuel |")
        out.append("|---|---|---|---|---|---|---|---|")
        for r in bull_tokens[:10]:
            pats = [PAT_LABEL.get(p, p) for p in (r.get("patterns") or "").split("|") if p and p in BULLISH_PATS]
            out.append(f"| **{r['symbol']}** | {r['tier']} | {fmt(r['score'])} | "
                       f"+{r.get('bull_signals','0')} | -{r.get('bear_signals','0')} | "
                       f"{', '.join(pats) or '—'} | {fmt(r.get('support_90d'),'px')} | {fmt(r['price'],'px')} |")
        out.append("")

    # Top tokens par biais baissier
    bear_tokens = sorted([r for r in active if r.get("bias") == "baissier"],
                         key=lambda r: (-int(r.get("bear_signals") or 0), -float(r.get("score") or 0)))
    if bear_tokens:
        out.append("### Setups baissiers les plus confluents\n")
        out.append("| Symbol | Tier | Score | Signaux baissiers | Signaux haussiers | Patterns detectes | Resistance 90j | Prix actuel |")
        out.append("|---|---|---|---|---|---|---|---|")
        for r in bear_tokens[:10]:
            pats = [PAT_LABEL.get(p, p) for p in (r.get("patterns") or "").split("|") if p and p in BEARISH_PATS]
            out.append(f"| **{r['symbol']}** | {r['tier']} | {fmt(r['score'])} | "
                       f"-{r.get('bear_signals','0')} | +{r.get('bull_signals','0')} | "
                       f"{', '.join(pats) or '—'} | {fmt(r.get('resistance_90d'),'px')} | {fmt(r['price'],'px')} |")
        out.append("")

    # Tokens mixtes (signaux contradictoires — à surveiller)
    mixed = [r for r in active if r.get("bias") == "mixte"]
    if mixed:
        out.append("### Signaux contradictoires (mixtes) — a surveiller\n")
        out.append("| Symbol | Tier | Bull | Bear | Patterns |")
        out.append("|---|---|---|---|---|")
        for r in sorted(mixed, key=lambda r: -float(r.get("score") or 0))[:8]:
            pats = (r.get("patterns") or "").split("|")
            labels = [PAT_LABEL.get(p, p) for p in pats if p]
            out.append(f"| **{r['symbol']}** | {r['tier']} | +{r.get('bull_signals','0')} | "
                       f"-{r.get('bear_signals','0')} | {', '.join(labels) or '—'} |")
        out.append("")

    # Détail setups notables (top 8 tous biais confondus, le plus de signaux)
    all_with_pats = [(r, int(r.get("bull_signals") or 0) + int(r.get("bear_signals") or 0))
                     for r in active if (r.get("patterns") or "")]
    all_with_pats.sort(key=lambda x: (-x[1], -float(x[0].get("score") or 0)))

    out.append("### Detail des 8 setups les plus confluents\n")
    if not all_with_pats:
        out.append("_Aucun pattern detecte._\n")
    else:
        for r, n_sig in all_with_pats[:8]:
            pats = [p for p in (r.get("patterns") or "").split("|") if p]
            bull_p = [PAT_LABEL.get(p, p) for p in pats if p in BULLISH_PATS]
            bear_p = [PAT_LABEL.get(p, p) for p in pats if p in BEARISH_PATS]
            neut_p = [PAT_LABEL.get(p, p) for p in pats if p not in BULLISH_PATS and p not in BEARISH_PATS]
            rsi_v = fmt(r.get("rsi_14"))
            out.append(f"**{r['symbol']}** ({r['tier']}) — Score {fmt(r['score'])} — "
                       f"RSI {rsi_v} — Prix {fmt(r['price'],'px')} — Vol 24h {fmt(r.get('vol_24h_usd'),'money')}")
            if bull_p: out.append(f"  - Haussiers : {', '.join(bull_p)}")
            if bear_p: out.append(f"  - Baissiers : {', '.join(bear_p)}")
            if neut_p: out.append(f"  - Neutres : {', '.join(neut_p)}")
            if r.get("support_90d"):  out.append(f"  - Support 90j : {fmt(r['support_90d'],'px')}")
            if r.get("resistance_90d"): out.append(f"  - Resistance 90j : {fmt(r['resistance_90d'],'px')}")
            out.append("")

    return "\n".join(out) + "\n"

def section_diff(today_rows, prev_path):
    if not prev_path:
        return "## Mouvements vs analyse précédente\n_Aucun snapshot antérieur disponible — premier run._\n\n"
    deltas = diff_vs_previous(today_rows, prev_path)
    prev_date = os.path.basename(prev_path).replace("scores_", "").replace(".csv", "")
    out = [f"## Mouvements vs snapshot {prev_date}\n"]
    if not deltas:
        out.append("_Pas de tokens communs._\n"); return "\n".join(out) + "\n"
    biggest_up = deltas[:5]; biggest_down = deltas[-5:][::-1]
    out.append("**+ Plus fortes hausses de score**\n")
    out.append("| Symbol | Δ score | Score | Patterns |\n|---|---|---|---|")
    for sym, d, r in biggest_up:
        out.append(f"| {sym} | +{d:.1f} | {fmt(r['score'])} | {r['patterns'] or '—'} |")
    out.append("\n**− Plus fortes baisses**\n")
    out.append("| Symbol | Δ score | Score | Patterns |\n|---|---|---|---|")
    for sym, d, r in biggest_down:
        out.append(f"| {sym} | {d:.1f} | {fmt(r['score'])} | {r['patterns'] or '—'} |")
    return "\n".join(out) + "\n\n"

def section_market_signal(rows):
    """Signal macro : vaut-il mieux être en crypto ou en EUR en ce moment ?

    Composantes (score de -10 à +10) :
      1. Position BTC vs MAs          (-2 à +2)
      2. RSI BTC                       (-1 à +1)
      3. Drawdown BTC 90j              (-2 à +1)
      4. Breadth : % tokens haussiers  (-2 à +2)
      5. Proportion downtrend marché   (-2 à +1)
      6. Volume global vs médiane       (-1 à +1)

    Seuils :
      score ≥ +4  → Crypto favorable
      +1 à +3     → Mixte / prudence
      -1 à 0      → Signal neutre
      ≤ -2        → Conditions défavorables, EUR potentiellement préférable
    """
    active = [r for r in rows if r.get("suspect") != "True" and r.get("stablecoin") != "True"]
    btc = next((r for r in rows if r["symbol"] == "BTCUSDT"), None)

    score = 0
    details = []

    # ── 1. Position BTC vs MA50/MA200 ─────────────────────────────────────
    if btc:
        try:
            p, ma50, ma200 = float(btc["price"]), float(btc["ma_50"]), float(btc["ma_200"])
            if p > ma50 > ma200:
                score += 2; details.append(("BTC vs MAs", "+2", "Prix > MA50 > MA200 — tendance haussière"))
            elif p > ma50:
                score += 1; details.append(("BTC vs MAs", "+1", "Prix > MA50 mais < MA200 — récupération partielle"))
            elif p < ma50 < ma200:
                score -= 2; details.append(("BTC vs MAs", "-2", "Prix < MA50 < MA200 — tendance baissière confirmée"))
            else:
                score -= 1; details.append(("BTC vs MAs", "-1", "Configuration MAs dégradée"))
        except Exception:
            details.append(("BTC vs MAs", "n/a", "Données insuffisantes"))

    # ── 2. RSI BTC ────────────────────────────────────────────────────────
    if btc:
        try:
            rsi = float(btc["rsi_14"])
            if 45 <= rsi <= 65:
                score += 1; details.append(("RSI BTC", "+1", f"RSI {rsi:.1f} — zone saine"))
            elif rsi < 30:
                score -= 1; details.append(("RSI BTC", "-1", f"RSI {rsi:.1f} — survente (rebond possible mais incertain)"))
            elif rsi > 75:
                score -= 1; details.append(("RSI BTC", "-1", f"RSI {rsi:.1f} — surachat"))
            else:
                details.append(("RSI BTC", "0", f"RSI {rsi:.1f} — neutre"))
        except Exception:
            details.append(("RSI BTC", "n/a", "Données insuffisantes"))

    # ── 3. Drawdown BTC 90j ───────────────────────────────────────────────
    if btc:
        try:
            dd = float(btc["drawdown_90d"])
            if dd < 0.15:
                score += 1; details.append(("Drawdown BTC 90j", "+1", f"{dd*100:.1f}% — faible drawdown"))
            elif dd < 0.30:
                details.append(("Drawdown BTC 90j", "0", f"{dd*100:.1f}% — drawdown modéré"))
            elif dd < 0.50:
                score -= 1; details.append(("Drawdown BTC 90j", "-1", f"{dd*100:.1f}% — drawdown significatif"))
            else:
                score -= 2; details.append(("Drawdown BTC 90j", "-2", f"{dd*100:.1f}% — drawdown majeur"))
        except Exception:
            details.append(("Drawdown BTC 90j", "n/a", "Données insuffisantes"))

    # ── 4. Breadth : % tokens avec biais haussier ─────────────────────────
    if active:
        n_bull = sum(1 for r in active if r.get("bias") == "haussier")
        n_bear = sum(1 for r in active if r.get("bias") == "baissier")
        pct_bull = n_bull / len(active) if active else 0
        if pct_bull >= 0.50:
            score += 2; details.append(("Breadth marché", "+2", f"{pct_bull*100:.0f}% tokens haussiers — marché large en hausse"))
        elif pct_bull >= 0.35:
            score += 1; details.append(("Breadth marché", "+1", f"{pct_bull*100:.0f}% tokens haussiers — légère dominance haussière"))
        elif pct_bull <= 0.20:
            score -= 2; details.append(("Breadth marché", "-2", f"{pct_bull*100:.0f}% tokens haussiers — marché largement baissier"))
        elif pct_bull <= 0.30:
            score -= 1; details.append(("Breadth marché", "-1", f"{pct_bull*100:.0f}% tokens haussiers — dominance baissière"))
        else:
            details.append(("Breadth marché", "0", f"{pct_bull*100:.0f}% tokens haussiers — équilibre"))

    # ── 5. Proportion de tokens en downtrend ──────────────────────────────
    if active:
        n_down = sum(1 for r in active if "downtrend" in (r.get("patterns") or ""))
        n_up   = sum(1 for r in active if "uptrend"   in (r.get("patterns") or ""))
        pct_down = n_down / len(active)
        pct_up   = n_up   / len(active)
        if pct_down >= 0.35:
            score -= 2; details.append(("Structures tendance", "-2", f"{pct_down*100:.0f}% tokens en downtrend — tendance de fond baissière"))
        elif pct_down >= 0.20:
            score -= 1; details.append(("Structures tendance", "-1", f"{pct_down*100:.0f}% downtrends vs {pct_up*100:.0f}% uptrends"))
        elif pct_up >= 0.30:
            score += 1; details.append(("Structures tendance", "+1", f"{pct_up*100:.0f}% tokens en uptrend — structure haussière générale"))
        else:
            details.append(("Structures tendance", "0", f"{pct_down*100:.0f}% downtrends / {pct_up*100:.0f}% uptrends — mixte"))

    # ── 6. Volume BTC vs médiane ──────────────────────────────────────────
    if btc:
        try:
            vr = float(btc["vol_ratio_vs_med90"])
            if vr > 1.5:
                score += 1; details.append(("Volume BTC", "+1", f"{vr:.2f}× médiane — volume élevé (intérêt fort)"))
            elif vr < 0.5:
                score -= 1; details.append(("Volume BTC", "-1", f"{vr:.2f}× médiane — volume faible (désintérêt)"))
            else:
                details.append(("Volume BTC", "0", f"{vr:.2f}× médiane — volume normal"))
        except Exception:
            details.append(("Volume BTC", "n/a", "Données insuffisantes"))

    # ── Verdict ───────────────────────────────────────────────────────────
    if score >= 4:
        verdict = "🟢 CRYPTO FAVORABLE"
        interpretation = (
            "Les indicateurs macro convergent positivement. "
            "BTC en tendance haussière, breadth large, structures solides."
        )
        eur_note = "Rester en crypto semble justifié par les conditions actuelles."
    elif score >= 1:
        verdict = "🟡 CONDITIONS MIXTES — Prudence"
        interpretation = (
            "Le marché envoie des signaux contradictoires. "
            "Certains indicateurs sont positifs, d'autres préoccupants."
        )
        eur_note = "Diversifier partiellement vers EUR ou réduire l'exposition peut être raisonnable."
    elif score >= -1:
        verdict = "🟠 SIGNAL NEUTRE — Surveillance accrue"
        interpretation = (
            "Pas de tendance claire. Le marché est dans une zone d'indécision. "
            "La prudence s'impose avant de prendre des positions importantes."
        )
        eur_note = "Conserver une part significative en EUR/stablecoins est prudent dans ce contexte."
    else:
        verdict = "🔴 CONDITIONS DÉFAVORABLES — EUR potentiellement préférable"
        interpretation = (
            "Les indicateurs macro sont majoritairement baissiers : "
            "downtrends généralisés, breadth faible, BTC sous ses moyennes mobiles."
        )
        eur_note = "Les conditions suggèrent qu'une exposition réduite au crypto et une position EUR plus forte méritent d'être envisagées."

    out = [
        "## 🌐 Signal Marché Global — Crypto vs EUR\n",
        f"> ⚠️ Indicateur macro basé sur des données passées uniquement. Pas un conseil de gestion.\n\n",
        f"### {verdict}  (score composite : {score:+d} / 10)\n",
        f"_{interpretation}_\n\n",
        f"**Note EUR :** {eur_note}\n\n",
        "### Détail des composantes\n",
        "| Composante | Signal | Interprétation |",
        "|---|---|---|",
    ]
    for label, sig, interp in details:
        color = "🟢" if sig.startswith("+") and sig != "+0" else ("🔴" if sig.startswith("-") else "⚪")
        out.append(f"| {label} | {color} {sig} | {interp} |")

    # Historique du signal (si snapshots disponibles)
    import glob as _glob
    hist_files = sorted(_glob.glob(str(HISTORY / "scores_*.csv")))
    if len(hist_files) >= 3:
        out.append("\n### Évolution du signal (7 derniers jours disponibles)\n")
        out.append("| Date | Score | Verdict |")
        out.append("|---|---|---|")
        for hf in hist_files[-7:]:
            try:
                hrows = load_csv(hf)
                hdate = hf.replace("\\", "/").split("/")[-1].replace("scores_", "").replace(".csv", "")
                hdate_fmt = f"{hdate[:4]}-{hdate[4:6]}-{hdate[6:]}"
                hactive = [r for r in hrows if r.get("suspect") != "True" and r.get("stablecoin") != "True"]
                hbtc = next((r for r in hrows if r["symbol"] == "BTCUSDT"), None)
                # Score simplifié pour l'historique
                hs = 0
                if hbtc:
                    try:
                        hp, hma50, hma200 = float(hbtc["price"]), float(hbtc["ma_50"]), float(hbtc["ma_200"])
                        if hp > hma50 > hma200: hs += 2
                        elif hp < hma50 < hma200: hs -= 2
                        else: hs -= 1
                    except: pass
                if hactive:
                    hn_bull = sum(1 for r in hactive if r.get("bias") == "haussier")
                    hpct = hn_bull / len(hactive)
                    if hpct >= 0.45: hs += 2
                    elif hpct <= 0.25: hs -= 2
                    elif hpct <= 0.35: hs -= 1
                hv = "🟢 Favorable" if hs >= 4 else ("🟡 Mixte" if hs >= 1 else ("🟠 Neutre" if hs >= -1 else "🔴 Défavorable"))
                out.append(f"| {hdate_fmt} | {hs:+d} | {hv} |")
            except: pass

    out.append("")
    return "\n".join(out) + "\n"


def section_explosion(rows):
    """Section candidats explosion : tokens dont le profil actuel ressemble aux pré-explosions historiques."""
    active = [r for r in rows
              if r.get("suspect") != "True" and r.get("stablecoin") != "True"
              and r.get("explosion_score")]

    forts    = [r for r in active if int(r.get("explosion_score", 0) or 0) >= 9]
    moderes  = [r for r in active if 6 <= int(r.get("explosion_score", 0) or 0) < 9]
    surveill = [r for r in active if 4 <= int(r.get("explosion_score", 0) or 0) < 6]

    forts.sort(   key=lambda r: -int(r.get("explosion_score", 0) or 0))
    moderes.sort(  key=lambda r: -int(r.get("explosion_score", 0) or 0))
    surveill.sort( key=lambda r: -int(r.get("explosion_score", 0) or 0))

    out = [
        "## 🔥 Candidats à une explosion de prix\n",
        "> Basé sur la ressemblance avec le profil technique des tokens ayant explosé dans l'historique.\n"
        "> Indicateurs passés uniquement. Aucune garantie de performance future.\n\n",
    ]

    if not forts and not moderes and not surveill:
        out.append("_Aucun candidat détecté sur ce run._\n\n")
        return "\n".join(out)

    def tbl(title, items, n=10):
        if not items: return []
        t = [f"### {title} ({len(items)} tokens)\n",
             "| Symbol | Tier | Score global | Score explosion | RSI | DD90 | Vol ratio | Patterns | Raisons |",
             "|---|---|---|---|---|---|---|---|---|"]
        for r in items[:n]:
            pats = (r.get("patterns") or "").replace("|", " · ")[:60]
            reasons = (r.get("explosion_label") or "") + " " + (r.get("reasons") or "")
            t.append(
                f"| **{r['symbol']}** | {r['tier']} | {fmt(r['score_global'])} | "
                f"**{r.get('explosion_score', 0)}** | {fmt(r.get('rsi_14'))} | "
                f"{fmt(r.get('drawdown_90d'), 'pct')} | {fmt(r.get('vol_ratio_vs_med90'))} | "
                f"{pats or '—'} | {reasons[:80]} |"
            )
        t.append("")
        return t

    out += tbl("🔥 Profil fort — très similaire aux explosions passées", forts)
    out += tbl("⚡ Profil modéré — ressemblance notable", moderes)
    out += tbl("👀 À surveiller — signaux précoces", surveill, n=8)

    # Profil utilisé
    prof_path = ROOT / "data" / "learning" / "explosion_profile.json"
    if prof_path.exists():
        try:
            prof = json.loads(prof_path.read_text(encoding="utf-8"))
            n_obs = prof.get("forte", {}).get("n_observations", 0)
            n_tok = prof.get("n_tokens_analyzed", 0)
            rsi_med = prof.get("forte", {}).get("rsi_median", "—")
            out.append(f"_Profil construit sur **{n_obs} observations pré-explosion** "
                       f"({n_tok} tokens analysés). RSI médian avant explosion : {rsi_med}._\n\n")
        except Exception:
            pass

    return "\n".join(out) + "\n"


def main():
    today_csv = COMPUTED / "scores.csv"
    if not today_csv.exists():
        log.error(f"Pas de CSV : {today_csv}"); return
    rows = load_csv(today_csv)
    prev = previous_snapshot()
    # Date réelle du fichier scores.csv
    import os as _os
    from datetime import datetime as _dt, timezone as _tz
    csv_mtime = _os.path.getmtime(today_csv)
    csv_date = _dt.fromtimestamp(csv_mtime, tz=_tz.utc)
    date_str = csv_date.strftime("%Y-%m-%d %H:%M UTC")
    age_days = (_dt.now(_tz.utc) - csv_date).days
    staleness = ""
    if age_days >= 2:
        staleness = (f"\n\n> ⚠️ **Le pipeline n'a pas tourné récemment — données potentiellement obsolètes.**"
                     f" Le rapport date du {csv_date.strftime('%d %B %Y')}, soit {age_days} jours."
                     f" Les données ci-dessous reflètent la situation à cette date.\n")
    parts = [DISCLAIMER,
             f"# Crypto USDT screening — {TODAY[:4]}-{TODAY[4:6]}-{TODAY[6:]}\n",
             staleness,
             f"_Univers : {len(rows)} tokens scorés. "
             f"Etabli : {sum(1 for r in rows if r['tier']=='Etabli')}, "
             f"Mid : {sum(1 for r in rows if r['tier']=='Mid')}, "
             f"Speculative : {sum(1 for r in rows if r['tier']=='Speculative')}. "
             f"Suspects : {sum(1 for r in rows if r['suspect']=='True')}. "
             f"Stablecoins exclus : {sum(1 for r in rows if r.get('stablecoin')=='True')}._\n\n",
             section_market_signal(rows),
             section_explosion(rows),
             section_diff(rows, prev),
             "## Top par tier\n",
             section_top_by_tier(rows, "Etabli", 20),
             section_top_by_tier(rows, "Mid", 20),
             section_top_by_tier(rows, "Speculative", 20),
             section_patterns(rows),
             section_suspects(rows),
             "---\n_Méthodologie complète : voir `methodology.md`. CSV brut : "
             f"`data/computed/scores.csv` (généré le {date_str})._\n"]
    (ROOT / "report.md").write_text("\n".join(parts), encoding="utf-8")
    log.info(f"Report g\u00e9n\u00e9r\u00e9 : {ROOT / 'report.md'}")

if __name__ == "__main__":
    main()
