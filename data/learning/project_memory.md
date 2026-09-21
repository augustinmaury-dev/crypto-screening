# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 21 sep 2026*

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
  → Meilleur signal haussier actuel : `squeeze_breakout` à 47.1%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 64.5% | 3373 | → |
| `downtrend` | 58.0% | 16025 | → |
| `rsi_bearish_divergence` | 56.9% | 992 | → |
| `bearish_engulfing_4h` | 56.5% | 874 | → |
| `evening_star_4h` | 56.4% | 738 | → |
| `breakdown_30d` | 55.8% | 120 | → |
| `shooting_star_4h` | 55.4% | 287 | → |
| `macd_bearish_cross` | 55.0% | 6785 | → |
| `death_cross` | 52.3% | 350 | → |
| `resistance_test` | 51.5% | 1687 | → |
| `bear_flag` | 49.0% | 577 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 47.1% | 314 | → |
| `golden_cross` | 43.7% | 554 | → |
| `rsi_bullish_divergence` | 43.7% | 2437 | → |
| `bull_flag` | 43.3% | 289 | → |
| `hammer_4h` | 42.3% | 267 | → |
| `support_bounce` | 42.1% | 2434 | → |
| `bullish_engulfing_4h` | 41.4% | 1038 | → |
| `double_bottom_90d` | 41.1% | 2308 | → |
| `uptrend` | 40.0% | 9500 | → |
| `macd_bullish_cross` | 38.0% | 7807 | → |
| `morning_star_4h` | 35.1% | 841 | → |
| `breakout_30d` | 31.7% | 379 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 21 sep 2026 | **ASTER** | 80% | 0.754 |
| 21 sep 2026 | **FLOW** | 80% | 0.03223 |
| 21 sep 2026 | **NMR** | 80% | 9.39 |
| 21 sep 2026 | **WBETH** | 80% | 3024.99 |
| 21 sep 2026 | **EGLD** | 77% | 4.306 |
| 21 sep 2026 | **MASK** | 77% | 0.486 |
| 21 sep 2026 | **FORM** | 77% | 0.2664 |
| 21 sep 2026 | **XVG** | 77% | 0.003113 |
| 21 sep 2026 | **CAKE** | 76% | 2.531 |
| 21 sep 2026 | **TRB** | 76% | 19.06 |
| 21 sep 2026 | **AI** | 76% | 0.0185 |
| 21 sep 2026 | **BNT** | 76% | 0.3355 |
| 21 sep 2026 | **XLM** | 75% | 0.2071 |
| 21 sep 2026 | **LSK** | 75% | 0.3921 |
| 21 sep 2026 | **VTHO** | 75% | 0.000667 |

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | BTC bull_prob | Top tokens |
|------|--------|---------------|-----------|
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
| 21 sep 2026 | 🟢 Haussier | 67.0% | ASTER, FLOW, NMR |

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 46.0% → 67.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.0% (21 sep 2026) — -36.1% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.7% (21 sep 2026) — +7.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.0% (21 sep 2026) — -11.3% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 47.1% (21 sep 2026) — +23.3% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 56.9% (21 sep 2026) — -18.5% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **38187 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0091 |
| momentum | 0.0000 |
| risk | 0.0071 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 21 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 67%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ASTER** | 80% | +13pp | 2 |  |
| **FLOW** | 80% | +13pp | 2 |  |
| **NMR** | 80% | +13pp | 0 |  |
| **WBETH** | 80% | +13pp | 2 |  |
| **EGLD** | 77% | +10pp | 1 |  |
| **MASK** | 77% | +10pp | ⚠️ 4 | ⚡ Volume ×7.5 vs médiane |
| **FORM** | 77% | +10pp | 1 |  |
| **XVG** | 77% | +10pp | 2 |  |
| **CAKE** | 76% | +9pp | 2 |  |
| **TRB** | 76% | +9pp | 2 |  |
| **AI** | 76% | +9pp | 0 |  |
| **BNT** | 76% | +9pp | 2 |  |
