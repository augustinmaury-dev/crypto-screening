# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 2 sep 2026*

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
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 43.4%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Précision sur mes prédictions passées :** 38% (5/13 correctes)

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bearish_divergence` | 69.2% | 574 | → |
| `double_top_90d` | 68.0% | 2800 | → |
| `shooting_star_4h` | 61.4% | 223 | → |
| `downtrend` | 60.4% | 14533 | → |
| `bearish_engulfing_4h` | 59.7% | 670 | → |
| `evening_star_4h` | 58.5% | 614 | → |
| `macd_bearish_cross` | 55.6% | 5492 | → |
| `death_cross` | 55.2% | 290 | → |
| `resistance_test` | 55.0% | 1308 | → |
| `breakdown_30d` | 54.2% | 107 | → |
| `bear_flag` | 49.2% | 561 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 43.4% | 2347 | → |
| `support_bounce` | 39.5% | 2129 | → |
| `squeeze_breakout` | 37.7% | 183 | → |
| `bullish_engulfing_4h` | 37.6% | 859 | → |
| `double_bottom_90d` | 37.1% | 1887 | → |
| `golden_cross` | 35.0% | 363 | → |
| `bull_flag` | 33.6% | 143 | → |
| `uptrend` | 33.2% | 6941 | → |
| `hammer_4h` | 33.0% | 176 | → |
| `macd_bullish_cross` | 33.0% | 6578 | → |
| `morning_star_4h` | 31.6% | 716 | → |
| `breakout_30d` | 18.4% | 223 | → |

---

## Mes prédictions passées et leurs résultats

**13 prédictions mesurées — précision globale : 38%**

| Date | Token | Score | Prix prédit | Prix 14j après | Résultat |
|------|-------|-------|-------------|----------------|---------|
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

**205 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 2 sep 2026 | **ANKR** | 80% | 0.00405 |
| 2 sep 2026 | **SOPH** | 79% | 0.00432 |
| 2 sep 2026 | **SUSHI** | 75% | 0.2005 |
| 2 sep 2026 | **LA** | 75% | 0.0685 |
| 2 sep 2026 | **IQ** | 75% | 0.00072 |
| 2 sep 2026 | **CVC** | 74% | 0.01991 |
| 2 sep 2026 | **WIN** | 74% | 3.044e-05 |
| 2 sep 2026 | **HIVE** | 73% | 0.0439 |
| 2 sep 2026 | **CAKE** | 72% | 1.79 |
| 2 sep 2026 | **PROM** | 72% | 4.591 |
| 2 sep 2026 | **ACE** | 72% | 0.1918 |
| 2 sep 2026 | **ENSO** | 72% | 0.875 |
| 2 sep 2026 | **0G** | 72% | 0.1819 |
| 2 sep 2026 | **ZKC** | 72% | 0.0478 |
| 2 sep 2026 | **JST** | 71% | 0.10646 |

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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 67.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.2% (2 sep 2026) — -35.9% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.4% (2 sep 2026) — +6.8% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 60.4% (2 sep 2026) — -8.9% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 37.7% (2 sep 2026) — +13.9% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 69.2% (2 sep 2026) — -6.2% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **31755 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0065 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 2 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 67%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ANKR** | 80% | +21pp | 2 | ⚡ Volume ×5.6 vs médiane |
| **SOPH** | 79% | +20pp | 0 | ⚡ Volume ×12.9 vs médiane |
| **TUSD** | 79% | +20pp | 3 | ⚡ Volume ×10.0 vs médiane |
| **SUSHI** | 75% | +16pp | 2 |  |
| **LA** | 75% | +16pp | 0 | ⚡ Volume ×5.5 vs médiane |
| **IQ** | 75% | +16pp | 0 | ⚡ Volume ×7.5 vs médiane |
| **CVC** | 74% | +15pp | 0 | ⚡ Volume ×4.7 vs médiane |
| **WIN** | 74% | +15pp | 1 |  |
| **HIVE** | 73% | +14pp | 0 |  |
| **CAKE** | 72% | +13pp | 2 |  |
| **PROM** | 72% | +13pp | 0 |  |
| **ACE** | 72% | +13pp | 1 |  |
