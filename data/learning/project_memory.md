# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 21 août 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 57%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 36.7%
**Signaux baissiers fiables (>50%) :** 11 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `bear_flag` | 79.0% | 338 | 📉 |
| `double_top_90d` | 74.2% | 2513 | → |
| `rsi_bearish_divergence` | 74.1% | 498 | → |
| `shooting_star_4h` | 71.7% | 184 | 📉 |
| `downtrend` | 68.1% | 12505 | → |
| `bearish_engulfing_4h` | 65.4% | 584 | → |
| `evening_star_4h` | 63.2% | 555 | → |
| `macd_bearish_cross` | 61.7% | 4775 | → |
| `breakdown_30d` | 60.7% | 89 | → |
| `death_cross` | 59.6% | 265 | → |
| `resistance_test` | 54.7% | 1149 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 36.7% | 2051 | → |
| `support_bounce` | 32.9% | 1821 | → |
| `bullish_engulfing_4h` | 32.2% | 754 | → |
| `golden_cross` | 30.0% | 323 | → |
| `hammer_4h` | 29.4% | 163 | → |
| `double_bottom_90d` | 29.3% | 1653 | → |
| `bull_flag` | 29.1% | 110 | → |
| `uptrend` | 27.9% | 6240 | → |
| `squeeze_breakout` | 27.2% | 136 | → |
| `morning_star_4h` | 26.6% | 629 | → |
| `macd_bullish_cross` | 25.6% | 5723 | → |
| `breakout_30d` | 15.8% | 203 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**21 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 21 août 2026 | **PROM** | 72% | 2.425 |
| 21 août 2026 | **XPL** | 70% | 0.09535 |
| 20 août 2026 | **PLUME** | 75% | 0.01261 |
| 20 août 2026 | **TRUMP** | 74% | 1.642 |
| 20 août 2026 | **XEC** | 73% | 6.95e-06 |
| 20 août 2026 | **MET** | 70% | 0.219 |
| 20 août 2026 | **ACE** | 70% | 0.1884 |
| 20 août 2026 | **EURI** | 70% | 1.1693 |
| 19 août 2026 | **GNO** | 74% | 114.45 |
| 19 août 2026 | **ACE** | 71% | 0.2266 |
| 19 août 2026 | **GPS** | 70% | 0.01236 |
| 19 août 2026 | **ALPINE** | 70% | 0.337 |
| 19 août 2026 | **ACM** | 70% | 0.288 |
| 19 août 2026 | **USDE** | 76% | 1.0005 |
| 19 août 2026 | **EURI** | 74% | 1.1601 |

---

## Comment j'évolue et comment je m'adapte

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 79.0% (21 août 2026) — -6.1% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 36.7% (21 août 2026) — +0.1% →
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 68.1% (21 août 2026) — -1.2% →
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 27.2% (21 août 2026) — +3.4% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 74.1% (21 août 2026) — -1.3% →

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers sont **bloqués** sous 40% : je ne suis pas encore fiable pour détecter les hausses.

---

## Le score composite est-il utile ?

J'ai analysé **24093 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0002 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 21 août 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 57%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **PROM** | 72% | +25pp | 1 |  |
| **XPL** | 70% | +23pp | 0 | ⚡ Volume ×15.1 vs médiane |
