# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 24 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 67%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 49.1%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 63.3% | 3454 | → |
| `downtrend` | 57.7% | 16134 | → |
| `bearish_engulfing_4h` | 56.0% | 882 | → |
| `breakdown_30d` | 55.3% | 123 | → |
| `evening_star_4h` | 55.2% | 753 | → |
| `shooting_star_4h` | 54.5% | 292 | → |
| `macd_bearish_cross` | 54.1% | 6927 | → |
| `rsi_bearish_divergence` | 54.1% | 1052 | → |
| `death_cross` | 52.0% | 352 | → |
| `resistance_test` | 50.7% | 1749 | → |
| `bear_flag` | 48.2% | 596 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 49.1% | 344 | → |
| `golden_cross` | 45.1% | 588 | → |
| `bull_flag` | 44.0% | 293 | → |
| `rsi_bullish_divergence` | 43.8% | 2449 | → |
| `hammer_4h` | 43.5% | 276 | → |
| `uptrend` | 43.2% | 10144 | → |
| `support_bounce` | 42.0% | 2471 | → |
| `bullish_engulfing_4h` | 41.9% | 1055 | → |
| `double_bottom_90d` | 41.8% | 2345 | → |
| `macd_bullish_cross` | 39.3% | 8097 | → |
| `morning_star_4h` | 35.4% | 847 | → |
| `breakout_30d` | 32.7% | 394 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 24 sep 2026 | **ONDO** | 80% | 0.4551 |
| 24 sep 2026 | **COMP** | 80% | 23.03 |
| 24 sep 2026 | **AI** | 79% | 0.0196 |
| 24 sep 2026 | **BTTC** | 78% | 3.7e-07 |
| 24 sep 2026 | **ZEC** | 76% | 1482.5 |
| 24 sep 2026 | **ICP** | 76% | 2.977 |
| 24 sep 2026 | **BOME** | 76% | 0.0010523 |
| 24 sep 2026 | **QTUM** | 76% | 0.958 |
| 24 sep 2026 | **AUCTION** | 76% | 3.716 |
| 24 sep 2026 | **XRP** | 75% | 1.4724 |
| 24 sep 2026 | **ORCA** | 75% | 1.54 |
| 24 sep 2026 | **NMR** | 75% | 9.31 |
| 24 sep 2026 | **XVS** | 75% | 3.231 |
| 24 sep 2026 | **TST** | 75% | 0.01971 |
| 24 sep 2026 | **MTL** | 74% | 0.3231 |

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | BTC bull_prob | Top tokens |
|------|--------|---------------|-----------|
| 26 août 2026 | 🔴 Baissier | 39.0% | USDP, EUL, EDEN |
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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 39.0% → 67.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.2% (24 sep 2026) — -36.9% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.8% (24 sep 2026) — +7.2% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 57.7% (24 sep 2026) — -11.6% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 49.1% (24 sep 2026) — +25.3% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 54.1% (24 sep 2026) — -21.3% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **39233 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0103 |
| momentum | 0.0113 |
| risk | 0.0101 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 24 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 67%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ONDO** | 80% | +13pp | 2 | 🔥 Trending #1 sur CoinGecko |
| **COMP** | 80% | +13pp | 2 | ⚡ Volume ×6.8 vs médiane |
| **AI** | 79% | +12pp | 0 | ⚡ Volume ×5.9 vs médiane |
| **BTTC** | 78% | +11pp | 2 |  |
| **ZEC** | 76% | +9pp | 2 | 🔥 Trending #4 sur CoinGecko |
| **ICP** | 76% | +9pp | 2 |  |
| **BOME** | 76% | +9pp | 0 |  |
| **QTUM** | 76% | +9pp | 2 |  |
| **AUCTION** | 76% | +9pp | 2 |  |
| **XRP** | 75% | +8pp | 0 |  |
| **ORCA** | 75% | +8pp | ⚠️ 4 |  |
| **NMR** | 75% | +8pp | 0 |  |
