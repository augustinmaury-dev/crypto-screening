# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 22 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 64%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 47.8%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 64.2% | 3399 | → |
| `downtrend` | 57.9% | 16062 | → |
| `bearish_engulfing_4h` | 56.3% | 877 | → |
| `breakdown_30d` | 55.8% | 120 | → |
| `rsi_bearish_divergence` | 55.5% | 1019 | → |
| `evening_star_4h` | 55.4% | 751 | → |
| `shooting_star_4h` | 55.0% | 289 | → |
| `macd_bearish_cross` | 54.8% | 6809 | → |
| `death_cross` | 52.3% | 350 | → |
| `resistance_test` | 51.2% | 1712 | → |
| `bear_flag` | 49.1% | 579 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 47.8% | 324 | → |
| `golden_cross` | 44.0% | 564 | → |
| `bull_flag` | 44.0% | 293 | → |
| `rsi_bullish_divergence` | 43.7% | 2441 | → |
| `hammer_4h` | 42.4% | 269 | → |
| `support_bounce` | 42.1% | 2450 | → |
| `bullish_engulfing_4h` | 41.7% | 1049 | → |
| `double_bottom_90d` | 41.3% | 2323 | → |
| `uptrend` | 41.0% | 9715 | → |
| `macd_bullish_cross` | 38.6% | 7947 | → |
| `morning_star_4h` | 35.3% | 845 | → |
| `breakout_30d` | 32.1% | 386 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 22 sep 2026 | **ASTER** | 80% | 0.719 |
| 22 sep 2026 | **PENGU** | 80% | 0.008946 |
| 22 sep 2026 | **FORM** | 80% | 0.3268 |
| 22 sep 2026 | **ICP** | 78% | 2.915 |
| 22 sep 2026 | **MTL** | 78% | 0.306 |
| 22 sep 2026 | **XRP** | 77% | 1.5307 |
| 22 sep 2026 | **TST** | 77% | 0.01906 |
| 22 sep 2026 | **ZEN** | 76% | 7.695 |
| 22 sep 2026 | **ORCA** | 76% | 1.476 |
| 22 sep 2026 | **COOKIE** | 76% | 0.0127 |
| 22 sep 2026 | **CVC** | 76% | 0.02773 |
| 22 sep 2026 | **SHIB** | 75% | 5.91e-06 |
| 22 sep 2026 | **VTHO** | 75% | 0.000699 |
| 22 sep 2026 | **XEC** | 75% | 8.67e-06 |
| 22 sep 2026 | **AVNT** | 75% | 0.1152 |

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | BTC bull_prob | Top tokens |
|------|--------|---------------|-----------|
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
| 14 sep 2026 | 🟢 Haussier | 73.0% | GLM, API3, THE |
| 15 sep 2026 | 🟢 Haussier | 76.0% | AXL, AWE, GLM |
| 16 sep 2026 | 🟢 Haussier | 67.0% | ASTR, POL, HIVE |
| 17 sep 2026 | 🟢 Haussier | 67.0% | A, ASTR, BNSOL |
| 18 sep 2026 | 🟢 Haussier | 70.0% | ROSE, ENSO, LSK |
| 19 sep 2026 | 🟢 Haussier | 60.0% | ESP, SLP, C98 |
| 20 sep 2026 | 🟢 Haussier | 66.0% | KMNO, HOT, JOE |
| 21 sep 2026 | 🟢 Haussier | 67.0% | ASTER, FLOW, NMR |
| 22 sep 2026 | 🟢 Haussier | 64.0% | ASTER, PENGU, FORM |

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 44.0% → 64.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.1% (22 sep 2026) — -36.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.7% (22 sep 2026) — +7.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 57.9% (22 sep 2026) — -11.4% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 47.8% (22 sep 2026) — +24.0% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 55.5% (22 sep 2026) — -19.9% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **38551 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0095 |
| momentum | 0.0023 |
| risk | 0.0076 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 22 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 64%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ASTER** | 80% | +16pp | 1 |  |
| **PENGU** | 80% | +16pp | 0 | 🔥 Trending #3 sur CoinGecko |
| **FORM** | 80% | +16pp | 0 | ⚡ Volume ×7.8 vs médiane |
| **ICP** | 78% | +14pp | 2 |  |
| **MTL** | 78% | +14pp | 0 | ⚡ Volume ×5.4 vs médiane |
| **XRP** | 77% | +13pp | 2 |  |
| **TST** | 77% | +13pp | 0 |  |
| **ZEN** | 76% | +12pp | 0 |  |
| **ORCA** | 76% | +12pp | 2 |  |
| **COOKIE** | 76% | +12pp | 0 | ⚡ Volume ×8.6 vs médiane |
| **CVC** | 76% | +12pp | 0 | ⚡ Volume ×5.0 vs médiane |
| **SHIB** | 75% | +11pp | 2 |  |
