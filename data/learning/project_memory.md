# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 6 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟡 Neutre — 54%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 43.6%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Précision sur mes prédictions passées :** 57% (17/30 correctes)

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bearish_divergence` | 67.6% | 617 | → |
| `double_top_90d` | 67.1% | 2903 | → |
| `shooting_star_4h` | 61.5% | 226 | → |
| `downtrend` | 59.1% | 15093 | → |
| `bearish_engulfing_4h` | 58.8% | 747 | → |
| `evening_star_4h` | 57.3% | 647 | → |
| `macd_bearish_cross` | 55.5% | 5612 | → |
| `resistance_test` | 54.6% | 1399 | → |
| `breakdown_30d` | 53.7% | 108 | → |
| `death_cross` | 53.4% | 311 | → |
| `bear_flag` | 49.1% | 562 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 43.6% | 2358 | → |
| `squeeze_breakout` | 43.4% | 226 | → |
| `support_bounce` | 40.8% | 2237 | → |
| `bullish_engulfing_4h` | 39.5% | 912 | → |
| `double_bottom_90d` | 39.0% | 2018 | → |
| `golden_cross` | 38.8% | 397 | → |
| `hammer_4h` | 38.7% | 204 | 📈 |
| `macd_bullish_cross` | 36.1% | 7145 | → |
| `uptrend` | 34.4% | 7288 | → |
| `bull_flag` | 34.2% | 149 | → |
| `morning_star_4h` | 31.6% | 725 | → |
| `breakout_30d` | 26.4% | 307 | → |

---

## Mes prédictions passées et leurs résultats

**30 prédictions mesurées — précision globale : 57%**

| Date | Token | Score | Prix prédit | Prix 14j après | Résultat |
|------|-------|-------|-------------|----------------|---------|
| 23 août 2026 | **EUL** | 73% | 1.247 | 1.294 | ✅ +3.8% |
| 23 août 2026 | **TUT** | 72% | 0.06405 | 0.02601 | ❌ -59.4% |
| 23 août 2026 | **COTI** | 71% | 0.01233 | 0.01759 | ✅ +42.7% |
| 23 août 2026 | **POWR** | 70% | 0.0431 | 0.0493 | ✅ +14.4% |
| 23 août 2026 | **USDP** | 72% | 0.9997 | 1 | ✅ +0.0% |
| 22 août 2026 | **PEOPLE** | 75% | 0.01042 | 0.00822 | ❌ -21.1% |
| 22 août 2026 | **HIVE** | 73% | 0.0455 | 0.0465 | ✅ +2.2% |
| 22 août 2026 | **UNI** | 72% | 4.2 | 6.257 | ✅ +49.0% |
| 22 août 2026 | **ME** | 71% | 0.06818 | 0.06374 | ❌ -6.5% |
| 22 août 2026 | **XAI** | 71% | 0.00782 | 0.00757 | ❌ -3.2% |
| 22 août 2026 | **DOLO** | 71% | 0.02582 | 0.02737 | ✅ +6.0% |
| 22 août 2026 | **SHELL** | 71% | 0.0229 | 0.0226 | ❌ -1.3% |
| 22 août 2026 | **ASTER** | 70% | 0.678 | 0.769 | ✅ +13.4% |
| 22 août 2026 | **MORPHO** | 70% | 2.253 | 2.54 | ✅ +12.7% |
| 22 août 2026 | **PYTH** | 70% | 0.05067 | 0.05424 | ✅ +7.0% |
| 22 août 2026 | **BROCCOLI714** | 70% | 0.01917 | 0.02152 | ✅ +12.3% |
| 21 août 2026 | **PROM** | 72% | 2.425 | 5.008 | ✅ +106.5% |
| 21 août 2026 | **XPL** | 70% | 0.09535 | 0.10204 | ✅ +7.0% |
| 20 août 2026 | **PLUME** | 75% | 0.01261 | 0.01423 | ✅ +12.8% |
| 20 août 2026 | **TRUMP** | 74% | 1.642 | 2.412 | ✅ +46.9% |
| 20 août 2026 | **XEC** | 73% | 6.95e-06 | 7.01e-06 | ✅ +0.9% |
| 20 août 2026 | **MET** | 70% | 0.219 | 0.1981 | ❌ -9.5% |
| 20 août 2026 | **ACE** | 70% | 0.1884 | 0.1805 | ❌ -4.2% |
| 20 août 2026 | **EURI** | 70% | 1.1693 | 1.1615 | ❌ -0.7% |
| 19 août 2026 | **GPS** | 70% | 0.01236 | 0.01009 | ❌ -18.4% |

**270 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 6 sep 2026 | **XVS** | 80% | 3.27 |
| 6 sep 2026 | **WOO** | 79% | 0.01236 |
| 6 sep 2026 | **T** | 76% | 0.00459 |
| 6 sep 2026 | **MET** | 76% | 0.2098 |
| 6 sep 2026 | **GMX** | 76% | 8.25 |
| 6 sep 2026 | **NOM** | 76% | 0.00183 |
| 6 sep 2026 | **BOME** | 75% | 0.0009261 |
| 6 sep 2026 | **NMR** | 74% | 9.46 |
| 6 sep 2026 | **SAHARA** | 74% | 0.00942 |
| 6 sep 2026 | **1000CAT** | 74% | 0.002233 |
| 6 sep 2026 | **OG** | 74% | 2.884 |
| 6 sep 2026 | **FORM** | 73% | 0.2709 |
| 6 sep 2026 | **GRT** | 73% | 0.01989 |
| 6 sep 2026 | **SOPH** | 73% | 0.00417 |
| 6 sep 2026 | **SUSHI** | 72% | 0.2447 |

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

→ **Régime stable** : BTC bull_prob entre 57.0% et 54.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.1% (6 sep 2026) — -36.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.6% (6 sep 2026) — +7.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 59.1% (6 sep 2026) — -10.2% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 43.4% (6 sep 2026) — +19.6% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 67.6% (6 sep 2026) — -7.8% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **33188 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0086 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 6 sep 2026

**Régime :** 🟡 Neutre (BTC bull_prob = 54%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **XVS** | 80% | +26pp | 2 |  |
| **WOO** | 79% | +25pp | 0 | ⚡ Volume ×26.3 vs médiane |
| **T** | 76% | +22pp | 0 | ⚡ Volume ×6.0 vs médiane |
| **MET** | 76% | +22pp | 1 |  |
| **GMX** | 76% | +22pp | 2 |  |
| **NOM** | 76% | +22pp | 0 | ⚡ Volume ×5.2 vs médiane |
| **BOME** | 75% | +21pp | 1 | ⚡ Volume ×4.8 vs médiane |
| **NMR** | 74% | +20pp | 2 |  |
| **SAHARA** | 74% | +20pp | 0 | ⚡ Volume ×40.4 vs médiane |
| **1000CAT** | 74% | +20pp | 0 | ⚡ Volume ×4.7 vs médiane |
| **OG** | 74% | +20pp | 3 |  |
| **FORM** | 73% | +19pp | 2 |  |
