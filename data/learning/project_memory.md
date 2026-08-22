# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 22 août 2026*

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
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 37.0%
**Signaux baissiers fiables (>50%) :** 11 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 73.6% | 2534 | → |
| `rsi_bearish_divergence` | 73.4% | 504 | → |
| `shooting_star_4h` | 70.2% | 188 | → |
| `bear_flag` | 68.8% | 388 | 📉 |
| `downtrend` | 67.2% | 12690 | → |
| `bearish_engulfing_4h` | 64.3% | 597 | → |
| `evening_star_4h` | 62.6% | 562 | → |
| `macd_bearish_cross` | 61.6% | 4788 | → |
| `breakdown_30d` | 60.7% | 89 | → |
| `death_cross` | 59.6% | 265 | → |
| `resistance_test` | 54.6% | 1165 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 37.0% | 2063 | → |
| `support_bounce` | 33.9% | 1853 | → |
| `bullish_engulfing_4h` | 32.2% | 758 | → |
| `golden_cross` | 30.7% | 326 | → |
| `double_bottom_90d` | 30.1% | 1672 | → |
| `hammer_4h` | 29.9% | 164 | → |
| `bull_flag` | 29.1% | 110 | → |
| `uptrend` | 28.6% | 6306 | → |
| `squeeze_breakout` | 27.7% | 137 | → |
| `morning_star_4h` | 27.6% | 638 | → |
| `macd_bullish_cross` | 27.5% | 5891 | → |
| `breakout_30d` | 15.7% | 204 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**32 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 22 août 2026 | **PEOPLE** | 75% | 0.01042 |
| 22 août 2026 | **HIVE** | 73% | 0.0455 |
| 22 août 2026 | **UNI** | 72% | 4.2 |
| 22 août 2026 | **ME** | 71% | 0.06818 |
| 22 août 2026 | **XAI** | 71% | 0.00782 |
| 22 août 2026 | **DOLO** | 71% | 0.02582 |
| 22 août 2026 | **SHELL** | 71% | 0.0229 |
| 22 août 2026 | **ASTER** | 70% | 0.678 |
| 22 août 2026 | **MORPHO** | 70% | 2.253 |
| 22 août 2026 | **PYTH** | 70% | 0.05067 |
| 22 août 2026 | **BROCCOLI714** | 70% | 0.01917 |
| 21 août 2026 | **PROM** | 72% | 2.425 |
| 21 août 2026 | **XPL** | 70% | 0.09535 |
| 20 août 2026 | **PLUME** | 75% | 0.01261 |
| 20 août 2026 | **TRUMP** | 74% | 1.642 |

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | BTC bull_prob | Top tokens |
|------|--------|---------------|-----------|
| 21 août 2026 | 🟢 Haussier | 57.0% | PROM, XPL |
| 22 août 2026 | 🟡 Neutre | 50.0% | PEOPLE, HIVE, UNI |

📉 **Le marché s'est dégradé** depuis le début du journal : BTC bull_prob 57.0% → 50.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 68.8% (22 août 2026) — -16.3% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 37.0% (22 août 2026) — +0.4% →
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 67.2% (22 août 2026) — -2.1% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 27.7% (22 août 2026) — +3.9% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 73.4% (22 août 2026) — -2.0% 📉

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

## Aujourd'hui — 22 août 2026

**Régime :** 🟡 Neutre (BTC bull_prob = 50%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **PEOPLE** | 75% | +32pp | 0 | ⚡ Volume ×5.2 vs médiane |
| **HIVE** | 73% | +30pp | 0 |  |
| **UNI** | 72% | +29pp | 0 |  |
| **ME** | 71% | +28pp | 0 |  |
| **XAI** | 71% | +28pp | 0 |  |
| **DOLO** | 71% | +28pp | 0 |  |
| **SHELL** | 71% | +28pp | 0 |  |
| **ASTER** | 70% | +27pp | 0 |  |
| **MORPHO** | 70% | +27pp | ⚠️ 4 |  |
| **PYTH** | 70% | +27pp | ⚠️ 4 | ⚡ Volume ×46.7 vs médiane |
| **BROCCOLI714** | 70% | +27pp | 2 |  |
