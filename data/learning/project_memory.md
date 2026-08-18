# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 18 août 2026*

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
| `bear_flag` | 84.8% | 303 | → |
| `double_top_90d` | 75.2% | 2450 | → |
| `rsi_bearish_divergence` | 75.1% | 485 | → |
| `shooting_star_4h` | 74.3% | 171 | → |
| `downtrend` | 69.2% | 11983 | → |
| `bearish_engulfing_4h` | 67.2% | 555 | → |
| `evening_star_4h` | 64.0% | 531 | → |
| `macd_bearish_cross` | 61.8% | 4717 | → |
| `breakdown_30d` | 60.9% | 87 | → |
| `death_cross` | 60.1% | 263 | → |
| `resistance_test` | 55.0% | 1110 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 36.4% | 2018 | → |
| `bullish_engulfing_4h` | 32.1% | 739 | → |
| `support_bounce` | 31.3% | 1720 | → |
| `golden_cross` | 29.7% | 316 | → |
| `hammer_4h` | 29.6% | 162 | → |
| `bull_flag` | 29.4% | 109 | → |
| `double_bottom_90d` | 28.1% | 1608 | → |
| `uptrend` | 26.4% | 6034 | → |
| `morning_star_4h` | 25.8% | 620 | → |
| `squeeze_breakout` | 24.2% | 124 | → |
| `macd_bullish_cross` | 22.3% | 5298 | → |
| `breakout_30d` | 15.9% | 195 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**5 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
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

## Aujourd'hui — 18 août 2026

**Régime :** 🟡 Neutre (BTC bull_prob = 54%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ACE** | 77% | +23pp | 0 | 🔥 Trending #3 sur CoinGecko|⚡ Volume ×9.0 vs média |
| **EURI** | 75% | +21pp | 2 | ⚡ Volume ×6.3 vs médiane |
| **RED** | 70% | +16pp | 0 | ⚡ Volume ×10.1 vs médiane |
