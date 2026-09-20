# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 20 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 66%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 45.5%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 64.8% | 3347 | → |
| `rsi_bearish_divergence` | 58.5% | 957 | → |
| `downtrend` | 58.0% | 15991 | → |
| `bearish_engulfing_4h` | 56.6% | 873 | → |
| `evening_star_4h` | 56.4% | 738 | → |
| `breakdown_30d` | 56.3% | 119 | → |
| `shooting_star_4h` | 55.2% | 281 | → |
| `macd_bearish_cross` | 55.0% | 6771 | → |
| `death_cross` | 52.3% | 350 | → |
| `resistance_test` | 52.1% | 1656 | → |
| `bear_flag` | 49.0% | 575 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 45.5% | 299 | → |
| `rsi_bullish_divergence` | 43.7% | 2432 | → |
| `golden_cross` | 43.4% | 544 | → |
| `bull_flag` | 42.7% | 281 | → |
| `hammer_4h` | 42.3% | 265 | → |
| `support_bounce` | 41.9% | 2420 | → |
| `bullish_engulfing_4h` | 41.4% | 1033 | → |
| `double_bottom_90d` | 40.8% | 2289 | → |
| `uptrend` | 38.9% | 9275 | → |
| `macd_bullish_cross` | 37.2% | 7643 | → |
| `morning_star_4h` | 33.4% | 815 | → |
| `breakout_30d` | 31.4% | 369 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 20 sep 2026 | **KMNO** | 80% | 0.0276 |
| 20 sep 2026 | **HOT** | 80% | 0.000396 |
| 20 sep 2026 | **JOE** | 80% | 0.0326 |
| 20 sep 2026 | **MAGIC** | 80% | 0.0467 |
| 20 sep 2026 | **RLC** | 80% | 0.3042 |
| 20 sep 2026 | **BAR** | 80% | 0.281 |
| 20 sep 2026 | **ASTER** | 78% | 0.736 |
| 20 sep 2026 | **GAS** | 78% | 1.323 |
| 20 sep 2026 | **IOTX** | 78% | 0.003281 |
| 20 sep 2026 | **USUAL** | 77% | 0.01272 |
| 20 sep 2026 | **SUSHI** | 76% | 0.2409 |
| 20 sep 2026 | **PROVE** | 76% | 0.2262 |
| 20 sep 2026 | **ARK** | 76% | 0.1503 |
| 20 sep 2026 | **G** | 75% | 0.00722 |
| 20 sep 2026 | **LSK** | 75% | 0.3761 |

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | BTC bull_prob | Top tokens |
|------|--------|---------------|-----------|
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
| 14 sep 2026 | 🟢 Haussier | 73.0% | GLM, API3, THE |
| 15 sep 2026 | 🟢 Haussier | 76.0% | AXL, AWE, GLM |
| 16 sep 2026 | 🟢 Haussier | 67.0% | ASTR, POL, HIVE |
| 17 sep 2026 | 🟢 Haussier | 67.0% | A, ASTR, BNSOL |
| 18 sep 2026 | 🟢 Haussier | 70.0% | ROSE, ENSO, LSK |
| 19 sep 2026 | 🟢 Haussier | 60.0% | ESP, SLP, C98 |
| 20 sep 2026 | 🟢 Haussier | 66.0% | KMNO, HOT, JOE |

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 50.0% → 66.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.0% (20 sep 2026) — -36.1% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.7% (20 sep 2026) — +7.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.0% (20 sep 2026) — -11.3% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 45.5% (20 sep 2026) — +21.7% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 58.5% (20 sep 2026) — -16.9% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **37808 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0087 |
| momentum | 0.0000 |
| risk | 0.0062 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 20 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 66%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **KMNO** | 80% | +14pp | 0 |  |
| **HOT** | 80% | +14pp | 2 |  |
| **JOE** | 80% | +14pp | 2 | ⚡ Volume ×6.8 vs médiane |
| **MAGIC** | 80% | +14pp | 2 |  |
| **RLC** | 80% | +14pp | 0 | ⚡ Volume ×5.9 vs médiane |
| **BAR** | 80% | +14pp | 2 |  |
| **ASTER** | 78% | +12pp | 0 |  |
| **GAS** | 78% | +12pp | 0 |  |
| **IOTX** | 78% | +12pp | 2 |  |
| **USUAL** | 77% | +11pp | 2 |  |
| **SUSHI** | 76% | +10pp | 0 |  |
| **PROVE** | 76% | +10pp | ⚠️ 4 | ⚡ Volume ×8.0 vs médiane |
