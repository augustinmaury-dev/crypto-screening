# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 3 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 56%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 43.5%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Précision sur mes prédictions passées :** 42% (8/19 correctes)

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bearish_divergence` | 68.5% | 581 | → |
| `double_top_90d` | 67.5% | 2829 | → |
| `shooting_star_4h` | 61.3% | 225 | → |
| `downtrend` | 59.9% | 14671 | → |
| `bearish_engulfing_4h` | 59.6% | 675 | → |
| `evening_star_4h` | 57.4% | 625 | → |
| `macd_bearish_cross` | 55.6% | 5531 | → |
| `resistance_test` | 54.9% | 1322 | → |
| `death_cross` | 53.9% | 297 | → |
| `breakdown_30d` | 53.7% | 108 | → |
| `bear_flag` | 49.1% | 562 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 43.5% | 2351 | → |
| `squeeze_breakout` | 41.5% | 195 | 📈 |
| `support_bounce` | 40.5% | 2175 | → |
| `bullish_engulfing_4h` | 38.9% | 881 | → |
| `double_bottom_90d` | 37.8% | 1917 | → |
| `golden_cross` | 35.4% | 367 | → |
| `macd_bullish_cross` | 34.0% | 6683 | → |
| `bull_flag` | 34.0% | 147 | → |
| `uptrend` | 33.5% | 7013 | → |
| `hammer_4h` | 33.3% | 177 | → |
| `morning_star_4h` | 31.7% | 717 | → |
| `breakout_30d` | 18.5% | 227 | → |

---

## Mes prédictions passées et leurs résultats

**19 prédictions mesurées — précision globale : 42%**

| Date | Token | Score | Prix prédit | Prix 14j après | Résultat |
|------|-------|-------|-------------|----------------|---------|
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
| 19 août 2026 | **EURI** | 74% | 1.1601 | 1.1578 | ❌ -0.2% |
| 19 août 2026 | **XUSD** | 70% | 1.0009 | 1.0004 | ❌ -0.1% |
| 18 août 2026 | **ACE** | 77% | 0.1958 | 0.1936 | ❌ -1.1% |
| 18 août 2026 | **RED** | 70% | 0.0994 | 0.1095 | ✅ +10.2% |
| 18 août 2026 | **EURI** | 75% | 1.1581 | 1.1593 | ✅ +0.1% |
| 17 août 2026 | **ACE** | 76% | 0.1526 | 0.1697 | ✅ +11.2% |
| 17 août 2026 | **PLUME** | 75% | 0.01261 | 0.01465 | ✅ +16.2% |

**223 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 3 sep 2026 | **PROM** | 76% | 4.587 |
| 3 sep 2026 | **RED** | 76% | 0.1186 |
| 3 sep 2026 | **COMP** | 76% | 20.16 |
| 3 sep 2026 | **HIVE** | 76% | 0.0454 |
| 3 sep 2026 | **PUNDIX** | 76% | 0.0909 |
| 3 sep 2026 | **GLM** | 75% | 0.1064 |
| 3 sep 2026 | **ENSO** | 74% | 0.858 |
| 3 sep 2026 | **T** | 73% | 0.00447 |
| 3 sep 2026 | **CVC** | 73% | 0.02019 |
| 3 sep 2026 | **CGPT** | 73% | 0.01979 |
| 3 sep 2026 | **ZKC** | 72% | 0.0483 |
| 3 sep 2026 | **WAXP** | 72% | 0.00432 |
| 3 sep 2026 | **ARK** | 72% | 0.1135 |
| 3 sep 2026 | **HEMI** | 71% | 0.01591 |
| 3 sep 2026 | **ANKR** | 71% | 0.00421 |

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

→ **Régime stable** : BTC bull_prob entre 57.0% et 56.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.1% (3 sep 2026) — -36.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.5% (3 sep 2026) — +6.9% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 59.9% (3 sep 2026) — -9.4% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 41.5% (3 sep 2026) — +17.7% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 68.5% (3 sep 2026) — -6.9% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **32097 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0074 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 3 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 56%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **PROM** | 76% | +20pp | 0 | ⚡ Volume ×6.3 vs médiane |
| **RED** | 76% | +20pp | 2 | ⚡ Volume ×4.3 vs médiane |
| **COMP** | 76% | +20pp | 2 |  |
| **HIVE** | 76% | +20pp | 2 | ⚡ Volume ×17.6 vs médiane |
| **PUNDIX** | 76% | +20pp | 0 | ⚡ Volume ×4.4 vs médiane |
| **BFUSD** | 76% | +20pp | 3 |  |
| **GLM** | 75% | +19pp | 3 | ⚡ Volume ×4.7 vs médiane |
| **ENSO** | 74% | +18pp | 0 | ⚡ Volume ×5.8 vs médiane |
| **T** | 73% | +17pp | 0 | ⚡ Volume ×10.8 vs médiane |
| **CVC** | 73% | +17pp | 2 | ⚡ Volume ×4.9 vs médiane |
| **CGPT** | 73% | +17pp | 1 |  |
| **ZKC** | 72% | +16pp | 0 | ⚡ Volume ×4.7 vs médiane |
