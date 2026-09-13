# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 13 sep 2026*

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
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 43.5%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 66.0% | 3093 | → |
| `rsi_bearish_divergence` | 65.0% | 766 | → |
| `downtrend` | 58.3% | 15701 | → |
| `evening_star_4h` | 57.0% | 679 | → |
| `bearish_engulfing_4h` | 56.6% | 811 | → |
| `shooting_star_4h` | 55.6% | 266 | 📉 |
| `macd_bearish_cross` | 55.1% | 5888 | → |
| `breakdown_30d` | 54.1% | 111 | → |
| `death_cross` | 53.4% | 328 | → |
| `resistance_test` | 53.4% | 1538 | → |
| `bear_flag` | 49.4% | 565 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 43.5% | 2392 | → |
| `squeeze_breakout` | 43.1% | 253 | → |
| `golden_cross` | 42.1% | 475 | → |
| `support_bounce` | 41.3% | 2317 | → |
| `hammer_4h` | 41.1% | 248 | → |
| `double_bottom_90d` | 40.5% | 2201 | → |
| `bullish_engulfing_4h` | 40.0% | 947 | → |
| `macd_bullish_cross` | 36.5% | 7339 | → |
| `uptrend` | 36.4% | 8131 | → |
| `bull_flag` | 34.9% | 152 | → |
| `morning_star_4h` | 32.3% | 771 | → |
| `breakout_30d` | 28.1% | 334 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 13 sep 2026 | **ILV** | 80% | 3.55 |
| 13 sep 2026 | **MET** | 79% | 0.2335 |
| 13 sep 2026 | **GLM** | 78% | 0.1224 |
| 13 sep 2026 | **GAS** | 77% | 1.331 |
| 13 sep 2026 | **THE** | 77% | 0.0679 |
| 13 sep 2026 | **ORCA** | 75% | 1.374 |
| 13 sep 2026 | **NEWT** | 75% | 0.04504 |
| 13 sep 2026 | **POLYX** | 74% | 0.0454 |
| 13 sep 2026 | **ASTR** | 74% | 0.006402 |
| 13 sep 2026 | **GMT** | 74% | 0.00782 |
| 13 sep 2026 | **NEO** | 73% | 2.281 |
| 13 sep 2026 | **SOPH** | 73% | 0.00442 |
| 13 sep 2026 | **BERA** | 72% | 0.1949 |
| 13 sep 2026 | **THETA** | 72% | 0.2086 |
| 13 sep 2026 | **ZIL** | 72% | 0.003021 |

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | BTC bull_prob | Top tokens |
|------|--------|---------------|-----------|
| 21 août 2026 | 🟢 Haussier | 57.0% | PROM, XPL |
| 22 août 2026 | 🟡 Neutre | 50.0% | PEOPLE, HIVE, UNI |
| 23 août 2026 | 🟡 Neutre | 46.0% | EUL, TUT, USDP |
| 24 août 2026 | 🔴 Baissier | 44.0% | TUT, COTI, EUL |
| 25 août 2026 | 🟡 Neutre | 51.0% | PEOPLE, EURI, TUT |
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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 67.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.4% (13 sep 2026) — -35.7% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.5% (13 sep 2026) — +6.9% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.3% (13 sep 2026) — -11.0% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 43.1% (13 sep 2026) — +19.3% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 65.0% (13 sep 2026) — -10.4% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **35325 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0089 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 13 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 67%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ILV** | 80% | +13pp | 0 | ⚡ Volume ×18.7 vs médiane |
| **MET** | 79% | +12pp | 2 | 🔥 Trending #7 sur CoinGecko |
| **GLM** | 78% | +11pp | 2 | ⚡ Volume ×12.8 vs médiane |
| **GAS** | 77% | +10pp | 1 |  |
| **THE** | 77% | +10pp | 1 | ⚡ Volume ×11.2 vs médiane |
| **ORCA** | 75% | +8pp | 0 |  |
| **NEWT** | 75% | +8pp | 0 |  |
| **POLYX** | 74% | +7pp | ⚠️ 4 | ⚡ Volume ×23.9 vs médiane |
| **ASTR** | 74% | +7pp | 2 |  |
| **GMT** | 74% | +7pp | 0 |  |
| **NEO** | 73% | +6pp | 2 |  |
| **SOPH** | 73% | +6pp | 0 | ⚡ Volume ×12.3 vs médiane |
