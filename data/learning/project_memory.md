# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 25 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 65%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 49.4%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 62.8% | 3481 | → |
| `downtrend` | 57.6% | 16169 | → |
| `bearish_engulfing_4h` | 55.8% | 886 | → |
| `evening_star_4h` | 54.4% | 767 | → |
| `breakdown_30d` | 54.4% | 125 | → |
| `shooting_star_4h` | 54.3% | 293 | → |
| `rsi_bearish_divergence` | 53.9% | 1058 | → |
| `macd_bearish_cross` | 52.6% | 7125 | → |
| `death_cross` | 51.7% | 354 | → |
| `resistance_test` | 50.6% | 1762 | → |
| `bear_flag` | 48.2% | 596 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 49.4% | 350 | → |
| `golden_cross` | 45.8% | 600 | → |
| `uptrend` | 44.2% | 10343 | → |
| `hammer_4h` | 44.1% | 281 | → |
| `bull_flag` | 44.0% | 293 | → |
| `rsi_bullish_divergence` | 43.9% | 2454 | → |
| `double_bottom_90d` | 42.0% | 2352 | → |
| `support_bounce` | 42.0% | 2477 | → |
| `bullish_engulfing_4h` | 41.9% | 1055 | → |
| `macd_bullish_cross` | 39.4% | 8115 | → |
| `morning_star_4h` | 35.4% | 848 | → |
| `breakout_30d` | 33.2% | 398 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 25 sep 2026 | **IQ** | 78% | 0.000976 |
| 25 sep 2026 | **ONDO** | 77% | 0.5452 |
| 25 sep 2026 | **EIGEN** | 75% | 0.2458 |
| 25 sep 2026 | **QTUM** | 75% | 1.034 |
| 25 sep 2026 | **AT** | 75% | 0.1514 |
| 25 sep 2026 | **LINK** | 74% | 13.959 |
| 25 sep 2026 | **XRP** | 73% | 1.6138 |
| 25 sep 2026 | **NEAR** | 73% | 5.042 |
| 25 sep 2026 | **NMR** | 73% | 9.72 |
| 25 sep 2026 | **MUBARAK** | 73% | 0.04543 |
| 25 sep 2026 | **NVDAB** | 73% | 225.99 |
| 25 sep 2026 | **LSK** | 72% | 0.3477 |
| 25 sep 2026 | **AI** | 72% | 0.0197 |
| 25 sep 2026 | **FLOW** | 72% | 0.03209 |
| 25 sep 2026 | **SUSHI** | 72% | 0.2602 |

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | BTC bull_prob | Top tokens |
|------|--------|---------------|-----------|
| 27 août 2026 | 🔴 Baissier | 42.0% | WAXP, TRX, ALT |
| 28 août 2026 | 🟢 Haussier | 70.0% | SOL, MORPHO, GMX |
| 29 août 2026 | 🟢 Haussier | 55.0% | MASK, ARPA, GNO |
| 30 août 2026 | 🟢 Haussier | 55.0% | ZK, BAND, DOLO |
| 31 août 2026 | 🟢 Haussier | 62.0% | ZK, ENSO, BMT |
| 1 sep 2026 | 🟢 Haussier | 56.0% | STRAX, NOT, SOMI |
| 2 sep 2026 | 🟢 Haussier | 67.0% | ANKR, SOPH, TUSD |
| 3 sep 2026 | 🟢 Haussier | 56.0% | PROM, RED, COMP |
| 4 sep 2026 | 🟡 Neutre | 51.0% | HIVE, PROM, ZKP |
| 5 sep 2026 | 🟢 Haussier | 58.0% | AIXBT, 1000CAT, ZKP |
| 6 sep 2026 | 🟡 Neutre | 54.0% | XVS, WOO, T |
| 7 sep 2026 | 🟢 Haussier | 64.0% | YGG, USTC, ILV |
| 8 sep 2026 | 🟢 Haussier | 69.0% | ORCA, 1000CAT, UMA |
| 9 sep 2026 | 🟢 Haussier | 69.0% | HOLO, ORCA, GLM |
| 10 sep 2026 | 🟢 Haussier | 69.0% | BFUSD, GLM, NEWT |
| 11 sep 2026 | 🟢 Haussier | 69.0% | MET, ORCA, THETA |
| 12 sep 2026 | 🟢 Haussier | 66.0% | MET, THE, ORCA |
| 13 sep 2026 | 🟢 Haussier | 67.0% | ILV, MET, GLM |
| 14 sep 2026 | 🟢 Haussier | 73.0% | GLM, API3, THE |
| 15 sep 2026 | 🟢 Haussier | 76.0% | AXL, AWE, GLM |
| 16 sep 2026 | 🟢 Haussier | 67.0% | ASTR, POL, HIVE |
| 17 sep 2026 | 🟢 Haussier | 67.0% | A, ASTR, BNSOL |
| 18 sep 2026 | 🟢 Haussier | 70.0% | ROSE, ENSO, LSK |
| 19 sep 2026 | 🟢 Haussier | 60.0% | ESP, SLP, C98 |
| 20 sep 2026 | 🟢 Haussier | 66.0% | KMNO, HOT, JOE |
| 21 sep 2026 | 🟢 Haussier | 67.0% | ASTER, FLOW, NMR |
| 22 sep 2026 | 🟢 Haussier | 64.0% | ASTER, PENGU, FORM |
| 23 sep 2026 | 🟢 Haussier | 65.0% | PENGU, BROCCOLI714, WIN |
| 24 sep 2026 | 🟢 Haussier | 67.0% | ONDO, COMP, AI |
| 25 sep 2026 | 🟢 Haussier | 65.0% | IQ, ONDO, EIGEN |

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 42.0% → 65.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.2% (25 sep 2026) — -36.9% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.9% (25 sep 2026) — +7.3% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 57.6% (25 sep 2026) — -11.7% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 49.4% (25 sep 2026) — +25.6% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 53.9% (25 sep 2026) — -21.5% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **39590 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0105 |
| momentum | 0.0153 |
| risk | 0.0112 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 25 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 65%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **IQ** | 78% | +13pp | 0 | ⚡ Volume ×5.8 vs médiane |
| **ONDO** | 77% | +12pp | ⚠️ 4 | 🔥 Trending #2 sur CoinGecko |
| **EIGEN** | 75% | +10pp | 2 |  |
| **QTUM** | 75% | +10pp | ⚠️ 4 |  |
| **AT** | 75% | +10pp | 2 |  |
| **LINK** | 74% | +9pp | 2 | 🔥 Trending #5 sur CoinGecko |
| **XRP** | 73% | +8pp | ⚠️ 4 |  |
| **NEAR** | 73% | +8pp | ⚠️ 6 | 🔥 Trending #1 sur CoinGecko |
| **NMR** | 73% | +8pp | 0 |  |
| **MUBARAK** | 73% | +8pp | 0 |  |
| **NVDAB** | 73% | +8pp | 2 |  |
| **LSK** | 72% | +7pp | 3 | ⚡ Volume ×18.3 vs médiane |
