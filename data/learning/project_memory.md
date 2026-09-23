# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 23 sep 2026*

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
  → Meilleur signal haussier actuel : `squeeze_breakout` à 49.0%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 63.8% | 3425 | → |
| `downtrend` | 57.8% | 16100 | → |
| `bearish_engulfing_4h` | 56.1% | 880 | → |
| `breakdown_30d` | 55.8% | 120 | → |
| `evening_star_4h` | 55.2% | 753 | → |
| `shooting_star_4h` | 55.0% | 289 | → |
| `macd_bearish_cross` | 54.7% | 6829 | → |
| `rsi_bearish_divergence` | 54.3% | 1048 | → |
| `death_cross` | 52.3% | 350 | → |
| `resistance_test` | 50.7% | 1734 | → |
| `bear_flag` | 48.3% | 594 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 49.0% | 341 | → |
| `golden_cross` | 44.4% | 576 | → |
| `bull_flag` | 44.0% | 293 | → |
| `rsi_bullish_divergence` | 43.7% | 2444 | → |
| `hammer_4h` | 42.9% | 273 | → |
| `uptrend` | 42.1% | 9931 | → |
| `support_bounce` | 42.1% | 2462 | → |
| `bullish_engulfing_4h` | 41.7% | 1051 | → |
| `double_bottom_90d` | 41.6% | 2338 | → |
| `macd_bullish_cross` | 39.2% | 8058 | → |
| `morning_star_4h` | 35.3% | 845 | → |
| `breakout_30d` | 32.4% | 392 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 23 sep 2026 | **PENGU** | 80% | 0.010131 |
| 23 sep 2026 | **BROCCOLI714** | 80% | 0.02316 |
| 23 sep 2026 | **WIN** | 80% | 3.973e-05 |
| 23 sep 2026 | **ASTER** | 78% | 0.7123 |
| 23 sep 2026 | **XVS** | 77% | 3.366 |
| 23 sep 2026 | **XRP** | 76% | 1.5665 |
| 23 sep 2026 | **UNI** | 76% | 9.744 |
| 23 sep 2026 | **ZEN** | 76% | 8.126 |
| 23 sep 2026 | **SUSHI** | 76% | 0.2747 |
| 23 sep 2026 | **NOT** | 76% | 0.0005 |
| 23 sep 2026 | **API3** | 76% | 0.2767 |
| 23 sep 2026 | **WLD** | 75% | 0.455 |
| 23 sep 2026 | **CAKE** | 75% | 2.61 |
| 23 sep 2026 | **XNO** | 75% | 0.377 |
| 23 sep 2026 | **ORCA** | 75% | 1.566 |

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | BTC bull_prob | Top tokens |
|------|--------|---------------|-----------|
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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 51.0% → 65.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.3% (23 sep 2026) — -36.8% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.7% (23 sep 2026) — +7.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 57.8% (23 sep 2026) — -11.5% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 49.0% (23 sep 2026) — +25.2% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 54.3% (23 sep 2026) — -21.1% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **38900 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0101 |
| momentum | 0.0070 |
| risk | 0.0095 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 23 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 65%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **PENGU** | 80% | +15pp | 2 | 🔥 Trending #2 sur CoinGecko |
| **BROCCOLI714** | 80% | +15pp | 0 |  |
| **WIN** | 80% | +15pp | ⚠️ 5 |  |
| **BFUSD** | 80% | +15pp | 3 |  |
| **ASTER** | 78% | +13pp | 1 |  |
| **XVS** | 77% | +12pp | 2 |  |
| **XRP** | 76% | +11pp | 2 |  |
| **UNI** | 76% | +11pp | ⚠️ 4 | 🔥 Trending #5 sur CoinGecko |
| **ZEN** | 76% | +11pp | 2 |  |
| **SUSHI** | 76% | +11pp | ⚠️ 4 |  |
| **NOT** | 76% | +11pp | 2 |  |
| **API3** | 76% | +11pp | 2 | ⚡ Volume ×6.1 vs médiane |
