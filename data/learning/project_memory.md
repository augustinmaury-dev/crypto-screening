# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 4 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟡 Neutre — 51%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 44.0%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Précision sur mes prédictions passées :** 48% (10/21 correctes)

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bearish_divergence` | 68.0% | 603 | → |
| `double_top_90d` | 67.3% | 2854 | → |
| `shooting_star_4h` | 61.3% | 225 | → |
| `bearish_engulfing_4h` | 59.7% | 677 | → |
| `downtrend` | 59.6% | 14808 | → |
| `evening_star_4h` | 57.6% | 627 | → |
| `macd_bearish_cross` | 55.7% | 5561 | → |
| `resistance_test` | 54.8% | 1350 | → |
| `breakdown_30d` | 53.7% | 108 | → |
| `death_cross` | 53.6% | 304 | → |
| `bear_flag` | 49.1% | 562 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 44.0% | 207 | 📈 |
| `rsi_bullish_divergence` | 43.5% | 2352 | → |
| `support_bounce` | 40.9% | 2207 | → |
| `bullish_engulfing_4h` | 39.4% | 901 | → |
| `double_bottom_90d` | 38.3% | 1950 | → |
| `golden_cross` | 36.5% | 375 | → |
| `macd_bullish_cross` | 34.8% | 6823 | → |
| `bull_flag` | 34.5% | 148 | → |
| `uptrend` | 33.8% | 7098 | → |
| `hammer_4h` | 33.3% | 177 | → |
| `morning_star_4h` | 31.8% | 721 | → |
| `breakout_30d` | 23.2% | 250 | 📈 |

---

## Mes prédictions passées et leurs résultats

**21 prédictions mesurées — précision globale : 48%**

| Date | Token | Score | Prix prédit | Prix 14j après | Résultat |
|------|-------|-------|-------------|----------------|---------|
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
| 19 août 2026 | **EURI** | 74% | 1.1601 | 1.1578 | ❌ -0.2% |
| 19 août 2026 | **XUSD** | 70% | 1.0009 | 1.0004 | ❌ -0.1% |
| 18 août 2026 | **ACE** | 77% | 0.1958 | 0.1936 | ❌ -1.1% |
| 18 août 2026 | **RED** | 70% | 0.0994 | 0.1095 | ✅ +10.2% |
| 18 août 2026 | **EURI** | 75% | 1.1581 | 1.1593 | ✅ +0.1% |
| 17 août 2026 | **ACE** | 76% | 0.1526 | 0.1697 | ✅ +11.2% |
| 17 août 2026 | **PLUME** | 75% | 0.01261 | 0.01465 | ✅ +16.2% |

**235 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 4 sep 2026 | **HIVE** | 80% | 0.0462 |
| 4 sep 2026 | **PROM** | 77% | 5.008 |
| 4 sep 2026 | **ZKP** | 75% | 0.0463 |
| 4 sep 2026 | **LISTA** | 75% | 0.0775 |
| 4 sep 2026 | **LPT** | 74% | 1.424 |
| 4 sep 2026 | **T** | 74% | 0.00449 |
| 4 sep 2026 | **ENSO** | 74% | 0.856 |
| 4 sep 2026 | **ARB** | 72% | 0.1344 |
| 4 sep 2026 | **ZKC** | 72% | 0.0484 |
| 4 sep 2026 | **VANA** | 72% | 0.953 |
| 4 sep 2026 | **ANKR** | 72% | 0.00422 |
| 4 sep 2026 | **PYTH** | 70% | 0.05485 |
| 4 sep 2026 | **JASMY** | 70% | 0.00443 |
| 4 sep 2026 | **BFUSD** | 72% | 1 |
| 3 sep 2026 | **PROM** | 76% | 4.587 |

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

📉 **Le marché s'est dégradé** depuis le début du journal : BTC bull_prob 57.0% → 51.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.1% (4 sep 2026) — -36.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.5% (4 sep 2026) — +6.9% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 59.6% (4 sep 2026) — -9.7% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 44.0% (4 sep 2026) — +20.2% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 68.0% (4 sep 2026) — -7.4% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **32457 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0084 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 4 sep 2026

**Régime :** 🟡 Neutre (BTC bull_prob = 51%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **HIVE** | 80% | +29pp | 0 | ⚡ Volume ×5.4 vs médiane |
| **PROM** | 77% | +26pp | 0 | ⚡ Volume ×41.0 vs médiane |
| **ZKP** | 75% | +24pp | 0 | ⚡ Volume ×28.2 vs médiane |
| **LISTA** | 75% | +24pp | 2 |  |
| **LPT** | 74% | +23pp | 0 | ⚡ Volume ×16.6 vs médiane |
| **T** | 74% | +23pp | 0 | ⚡ Volume ×4.9 vs médiane |
| **ENSO** | 74% | +23pp | 0 | ⚡ Volume ×75.2 vs médiane |
| **ARB** | 72% | +21pp | ⚠️ 4 | ⚡ Volume ×3.4 vs médiane |
| **ZKC** | 72% | +21pp | 0 | ⚡ Volume ×161.7 vs médiane |
| **VANA** | 72% | +21pp | 0 | ⚡ Volume ×6.3 vs médiane |
| **ANKR** | 72% | +21pp | 2 | ⚡ Volume ×4.9 vs médiane |
| **BFUSD** | 72% | +21pp | ⚠️ 5 |  |
