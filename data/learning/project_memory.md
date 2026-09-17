# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 17 sep 2026*

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
  → Meilleur signal haussier actuel : `squeeze_breakout` à 45.4%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 65.8% | 3244 | → |
| `rsi_bearish_divergence` | 63.3% | 812 | → |
| `downtrend` | 58.3% | 15866 | → |
| `evening_star_4h` | 56.4% | 723 | → |
| `bearish_engulfing_4h` | 56.4% | 860 | → |
| `breakdown_30d` | 56.3% | 119 | → |
| `shooting_star_4h` | 55.9% | 270 | → |
| `macd_bearish_cross` | 55.2% | 6575 | → |
| `death_cross` | 53.0% | 345 | → |
| `resistance_test` | 53.0% | 1588 | → |
| `bear_flag` | 49.1% | 574 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 45.4% | 273 | → |
| `rsi_bullish_divergence` | 43.6% | 2427 | → |
| `golden_cross` | 42.7% | 517 | → |
| `hammer_4h` | 42.1% | 261 | → |
| `support_bounce` | 41.5% | 2384 | → |
| `double_bottom_90d` | 40.4% | 2246 | → |
| `bullish_engulfing_4h` | 40.3% | 978 | → |
| `bull_flag` | 39.5% | 220 | → |
| `uptrend` | 37.3% | 8678 | → |
| `macd_bullish_cross` | 36.6% | 7393 | → |
| `morning_star_4h` | 32.6% | 788 | → |
| `breakout_30d` | 28.9% | 349 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 17 sep 2026 | **A** | 80% | 0.0768 |
| 17 sep 2026 | **ASTR** | 80% | 0.006311 |
| 17 sep 2026 | **BNSOL** | 79% | 114.1 |
| 17 sep 2026 | **LSK** | 78% | 0.4832 |
| 17 sep 2026 | **DASH** | 76% | 58.49 |
| 17 sep 2026 | **THE** | 76% | 0.07 |
| 17 sep 2026 | **REZ** | 75% | 0.003849 |
| 17 sep 2026 | **ARK** | 75% | 0.1414 |
| 17 sep 2026 | **MTL** | 75% | 0.279 |
| 17 sep 2026 | **RAY** | 74% | 1.4422 |
| 17 sep 2026 | **0G** | 74% | 0.2025 |
| 17 sep 2026 | **AWE** | 74% | 0.06404 |
| 17 sep 2026 | **IO** | 73% | 0.1301 |
| 17 sep 2026 | **SOLV** | 73% | 0.00438 |
| 17 sep 2026 | **WBTC** | 73% | 76862.9 |

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
| 14 sep 2026 | 🟢 Haussier | 73.0% | GLM, API3, THE |
| 15 sep 2026 | 🟢 Haussier | 76.0% | AXL, AWE, GLM |
| 16 sep 2026 | 🟢 Haussier | 67.0% | ASTR, POL, HIVE |
| 17 sep 2026 | 🟢 Haussier | 67.0% | A, ASTR, BNSOL |

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 67.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.1% (17 sep 2026) — -36.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.6% (17 sep 2026) — +7.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.3% (17 sep 2026) — -11.0% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 45.4% (17 sep 2026) — +21.6% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 63.3% (17 sep 2026) — -12.1% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **36704 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0083 |
| momentum | 0.0000 |
| risk | 0.0019 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 17 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 67%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **A** | 80% | +13pp | 1 | ⚡ Volume ×7.0 vs médiane |
| **ASTR** | 80% | +13pp | 0 | ⚡ Volume ×6.2 vs médiane |
| **BNSOL** | 79% | +12pp | 1 |  |
| **LSK** | 78% | +11pp | 0 | ⚡ Volume ×26.8 vs médiane |
| **DASH** | 76% | +9pp | 1 |  |
| **THE** | 76% | +9pp | 1 | ⚡ Volume ×115.0 vs médiane |
| **REZ** | 75% | +8pp | 0 | ⚡ Volume ×13.3 vs médiane |
| **ARK** | 75% | +8pp | 0 | ⚡ Volume ×6.6 vs médiane |
| **MTL** | 75% | +8pp | 0 | ⚡ Volume ×8.1 vs médiane |
| **RAY** | 74% | +7pp | 0 |  |
| **0G** | 74% | +7pp | 3 | ⚡ Volume ×4.4 vs médiane |
| **AWE** | 74% | +7pp | 0 |  |
