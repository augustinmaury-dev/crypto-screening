# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 23 août 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟡 Neutre — 46%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 37.1%
**Signaux baissiers fiables (>50%) :** 11 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 73.2% | 2555 | → |
| `rsi_bearish_divergence` | 72.8% | 515 | → |
| `shooting_star_4h` | 69.8% | 192 | → |
| `downtrend` | 66.5% | 12873 | → |
| `bearish_engulfing_4h` | 64.0% | 602 | → |
| `evening_star_4h` | 62.1% | 567 | → |
| `macd_bearish_cross` | 61.5% | 4793 | → |
| `bear_flag` | 61.5% | 439 | 📉 |
| `breakdown_30d` | 60.7% | 89 | → |
| `death_cross` | 59.6% | 265 | → |
| `resistance_test` | 54.5% | 1179 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 37.1% | 2072 | → |
| `support_bounce` | 35.3% | 1903 | → |
| `bullish_engulfing_4h` | 32.9% | 768 | → |
| `golden_cross` | 31.3% | 329 | → |
| `double_bottom_90d` | 31.0% | 1695 | → |
| `squeeze_breakout` | 30.6% | 147 | 📈 |
| `hammer_4h` | 29.7% | 165 | → |
| `bull_flag` | 29.1% | 110 | → |
| `uptrend` | 29.0% | 6368 | → |
| `macd_bullish_cross` | 29.0% | 6056 | → |
| `morning_star_4h` | 28.3% | 647 | → |
| `breakout_30d` | 16.6% | 211 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**37 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 23 août 2026 | **EUL** | 73% | 1.247 |
| 23 août 2026 | **TUT** | 72% | 0.06405 |
| 23 août 2026 | **COTI** | 71% | 0.01233 |
| 23 août 2026 | **POWR** | 70% | 0.0431 |
| 23 août 2026 | **USDP** | 72% | 0.9997 |
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

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | BTC bull_prob | Top tokens |
|------|--------|---------------|-----------|
| 21 août 2026 | 🟢 Haussier | 57.0% | PROM, XPL |
| 22 août 2026 | 🟡 Neutre | 50.0% | PEOPLE, HIVE, UNI |
| 23 août 2026 | 🟡 Neutre | 46.0% | EUL, TUT, USDP |

📉 **Le marché s'est dégradé** depuis le début du journal : BTC bull_prob 57.0% → 46.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 61.5% (23 août 2026) — -23.6% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 37.1% (23 août 2026) — +0.5% →
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 66.5% (23 août 2026) — -2.8% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 30.6% (23 août 2026) — +6.8% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 72.8% (23 août 2026) — -2.6% 📉

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

## Aujourd'hui — 23 août 2026

**Régime :** 🟡 Neutre (BTC bull_prob = 46%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **EUL** | 73% | +29pp | 0 | ⚡ Volume ×4.2 vs médiane |
| **TUT** | 72% | +28pp | 1 | ⚡ Volume ×6.8 vs médiane |
| **USDP** | 72% | +28pp | ⚠️ 5 | ⚡ Volume ×21.0 vs médiane |
| **COTI** | 71% | +27pp | 1 | ⚡ Volume ×8.6 vs médiane |
| **POWR** | 70% | +26pp | 0 |  |
