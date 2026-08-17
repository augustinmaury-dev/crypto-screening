# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 17 août 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟡 Neutre — 50%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 36.6%
**Signaux baissiers fiables (>50%) :** 11 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `bear_flag` | 85.1% | 302 | → |
| `double_top_90d` | 75.4% | 2430 | → |
| `rsi_bearish_divergence` | 75.4% | 483 | → |
| `shooting_star_4h` | 74.3% | 171 | → |
| `downtrend` | 69.3% | 11822 | → |
| `bearish_engulfing_4h` | 67.8% | 543 | → |
| `evening_star_4h` | 64.4% | 517 | → |
| `macd_bearish_cross` | 61.9% | 4690 | → |
| `breakdown_30d` | 61.6% | 86 | → |
| `death_cross` | 60.3% | 262 | → |
| `resistance_test` | 55.2% | 1096 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 36.6% | 1986 | → |
| `bullish_engulfing_4h` | 31.9% | 734 | → |
| `support_bounce` | 31.2% | 1693 | → |
| `golden_cross` | 29.7% | 313 | → |
| `hammer_4h` | 29.6% | 159 | → |
| `bull_flag` | 29.4% | 109 | → |
| `double_bottom_90d` | 27.9% | 1601 | → |
| `uptrend` | 26.1% | 5966 | → |
| `morning_star_4h` | 25.8% | 616 | → |
| `squeeze_breakout` | 23.8% | 122 | → |
| `macd_bullish_cross` | 21.7% | 5199 | → |
| `breakout_30d` | 15.5% | 194 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**2 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
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

## Aujourd'hui — 17 août 2026

**Régime :** 🟡 Neutre (BTC bull_prob = 50%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ACE** | 76% | +29pp | 0 | 🔥 Trending #4 sur CoinGecko|⚡ Volume ×9.6 vs média |
| **PLUME** | 75% | +28pp | 0 | ⚡ Volume ×16.3 vs médiane |
