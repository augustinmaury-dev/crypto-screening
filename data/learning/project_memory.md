# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 19 août 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟡 Neutre — 54%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 36.4%
**Signaux baissiers fiables (>50%) :** 11 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `bear_flag` | 84.9% | 304 | → |
| `double_top_90d` | 75.1% | 2471 | → |
| `rsi_bearish_divergence` | 75.0% | 488 | → |
| `shooting_star_4h` | 73.7% | 175 | → |
| `downtrend` | 69.2% | 12150 | → |
| `bearish_engulfing_4h` | 66.6% | 569 | → |
| `evening_star_4h` | 64.0% | 545 | → |
| `macd_bearish_cross` | 61.7% | 4739 | → |
| `breakdown_30d` | 60.9% | 87 | → |
| `death_cross` | 59.8% | 264 | → |
| `resistance_test` | 54.9% | 1123 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 36.4% | 2024 | → |
| `bullish_engulfing_4h` | 32.0% | 740 | → |
| `support_bounce` | 31.5% | 1750 | → |
| `golden_cross` | 29.8% | 319 | → |
| `hammer_4h` | 29.6% | 162 | → |
| `bull_flag` | 29.4% | 109 | → |
| `double_bottom_90d` | 28.3% | 1620 | → |
| `uptrend` | 26.7% | 6102 | → |
| `morning_star_4h` | 25.8% | 623 | → |
| `squeeze_breakout` | 24.6% | 126 | → |
| `macd_bullish_cross` | 22.8% | 5410 | → |
| `breakout_30d` | 16.2% | 198 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**13 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 19 août 2026 | **GNO** | 74% | 114.45 |
| 19 août 2026 | **ACE** | 71% | 0.2266 |
| 19 août 2026 | **GPS** | 70% | 0.01236 |
| 19 août 2026 | **ALPINE** | 70% | 0.337 |
| 19 août 2026 | **ACM** | 70% | 0.288 |
| 19 août 2026 | **USDE** | 76% | 1.0005 |
| 19 août 2026 | **EURI** | 74% | 1.1601 |
| 19 août 2026 | **XUSD** | 70% | 1.0009 |
| 18 août 2026 | **ACE** | 77% | 0.1958 |
| 18 août 2026 | **RED** | 70% | 0.0994 |
| 18 août 2026 | **EURI** | 75% | 1.1581 |
| 17 août 2026 | **ACE** | 76% | 0.1526 |
| 17 août 2026 | **PLUME** | 75% | 0.01261 |

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

## Aujourd'hui — 19 août 2026

**Régime :** 🟡 Neutre (BTC bull_prob = 54%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **USDE** | 76% | +22pp | 3 | ⚡ Volume ×4.4 vs médiane |
| **GNO** | 74% | +20pp | 2 | ⚡ Volume ×6.7 vs médiane |
| **EURI** | 74% | +20pp | 2 | ⚡ Volume ×4.9 vs médiane |
| **ACE** | 71% | +17pp | 0 | ⚡ Volume ×9.4 vs médiane |
| **GPS** | 70% | +16pp | 0 | ⚡ Volume ×13.5 vs médiane |
| **ALPINE** | 70% | +16pp | 0 | ⚡ Volume ×6.7 vs médiane |
| **ACM** | 70% | +16pp | 2 | ⚡ Volume ×3.1 vs médiane |
| **XUSD** | 70% | +16pp | 2 |  |
