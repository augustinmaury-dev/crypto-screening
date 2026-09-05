# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 5 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 58%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 43.5%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Précision sur mes prédictions passées :** 53% (17/32 correctes)

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bearish_divergence` | 67.9% | 611 | → |
| `double_top_90d` | 67.3% | 2878 | → |
| `shooting_star_4h` | 61.3% | 225 | → |
| `downtrend` | 59.6% | 14947 | → |
| `bearish_engulfing_4h` | 59.2% | 740 | → |
| `evening_star_4h` | 57.4% | 646 | → |
| `macd_bearish_cross` | 55.6% | 5590 | → |
| `resistance_test` | 55.0% | 1375 | → |
| `death_cross` | 53.9% | 308 | → |
| `breakdown_30d` | 53.7% | 108 | → |
| `bear_flag` | 49.1% | 562 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 43.5% | 2352 | → |
| `squeeze_breakout` | 42.9% | 224 | → |
| `support_bounce` | 40.8% | 2233 | → |
| `bullish_engulfing_4h` | 39.4% | 901 | → |
| `double_bottom_90d` | 38.4% | 1985 | → |
| `golden_cross` | 37.6% | 386 | → |
| `macd_bullish_cross` | 34.9% | 6979 | → |
| `hammer_4h` | 34.9% | 189 | → |
| `bull_flag` | 34.2% | 149 | → |
| `uptrend` | 33.9% | 7187 | → |
| `morning_star_4h` | 31.8% | 721 | → |
| `breakout_30d` | 26.2% | 305 | 📈 |

---

## Mes prédictions passées et leurs résultats

**32 prédictions mesurées — précision globale : 53%**

| Date | Token | Score | Prix prédit | Prix 14j après | Résultat |
|------|-------|-------|-------------|----------------|---------|
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
| 19 août 2026 | **GNO** | 74% | 114.45 | 114.1 | ❌ -0.3% |
| 19 août 2026 | **ACE** | 71% | 0.2266 | 0.1918 | ❌ -15.4% |
| 19 août 2026 | **GPS** | 70% | 0.01236 | 0.01009 | ❌ -18.4% |
| 19 août 2026 | **ALPINE** | 70% | 0.337 | 0.347 | ✅ +3.0% |
| 19 août 2026 | **ACM** | 70% | 0.288 | 0.28 | ❌ -2.8% |
| 19 août 2026 | **USDE** | 76% | 1.0005 | 0.9999 | ❌ -0.1% |

**248 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 5 sep 2026 | **AIXBT** | 75% | 0.02216 |
| 5 sep 2026 | **1000CAT** | 75% | 0.002312 |
| 5 sep 2026 | **ZKP** | 74% | 0.0497 |
| 5 sep 2026 | **CATI** | 74% | 0.05253 |
| 5 sep 2026 | **DIA** | 74% | 0.1462 |
| 5 sep 2026 | **ENJ** | 73% | 0.0275 |
| 5 sep 2026 | **SAHARA** | 73% | 0.00915 |
| 5 sep 2026 | **SOPH** | 73% | 0.00435 |
| 5 sep 2026 | **COTI** | 72% | 0.01484 |
| 5 sep 2026 | **ZK** | 72% | 0.01003 |
| 5 sep 2026 | **ZKC** | 72% | 0.0492 |
| 5 sep 2026 | **BANANA** | 72% | 4.058 |
| 5 sep 2026 | **PROM** | 71% | 5.288 |
| 5 sep 2026 | **AWE** | 71% | 0.06132 |
| 5 sep 2026 | **NOM** | 71% | 0.00191 |

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

→ **Régime stable** : BTC bull_prob entre 57.0% et 58.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.1% (5 sep 2026) — -36.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.5% (5 sep 2026) — +6.9% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 59.6% (5 sep 2026) — -9.7% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 42.9% (5 sep 2026) — +19.1% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 67.9% (5 sep 2026) — -7.5% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **32840 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0083 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 5 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 58%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **AIXBT** | 75% | +17pp | 2 | ⚡ Volume ×5.1 vs médiane |
| **1000CAT** | 75% | +17pp | ⚠️ 4 | ⚡ Volume ×5.3 vs médiane |
| **ZKP** | 74% | +16pp | 0 | ⚡ Volume ×4.6 vs médiane |
| **CATI** | 74% | +16pp | 0 | ⚡ Volume ×5.5 vs médiane |
| **DIA** | 74% | +16pp | 3 |  |
| **ENJ** | 73% | +15pp | 0 |  |
| **SAHARA** | 73% | +15pp | 0 | ⚡ Volume ×77.2 vs médiane |
| **SOPH** | 73% | +15pp | 0 |  |
| **COTI** | 72% | +14pp | 0 | ⚡ Volume ×4.4 vs médiane |
| **ZK** | 72% | +14pp | 0 | ⚡ Volume ×3.0 vs médiane |
| **ZKC** | 72% | +14pp | 0 | ⚡ Volume ×174.4 vs médiane |
| **BANANA** | 72% | +14pp | ⚠️ 5 |  |
