# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 31 août 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 62%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 42.0%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Précision sur mes prédictions passées :** 100% (2/2 correctes)

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bearish_divergence` | 69.4% | 571 | → |
| `double_top_90d` | 69.2% | 2739 | → |
| `shooting_star_4h` | 62.0% | 221 | 📉 |
| `downtrend` | 61.3% | 14238 | → |
| `bearish_engulfing_4h` | 60.9% | 650 | → |
| `evening_star_4h` | 59.7% | 600 | → |
| `death_cross` | 57.2% | 276 | → |
| `macd_bearish_cross` | 57.1% | 5291 | → |
| `breakdown_30d` | 56.9% | 102 | → |
| `resistance_test` | 54.9% | 1280 | → |
| `bear_flag` | 49.5% | 558 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 42.0% | 2277 | → |
| `support_bounce` | 38.9% | 2095 | → |
| `bullish_engulfing_4h` | 36.9% | 833 | → |
| `double_bottom_90d` | 36.2% | 1857 | → |
| `squeeze_breakout` | 35.6% | 174 | → |
| `golden_cross` | 34.1% | 358 | → |
| `macd_bullish_cross` | 32.5% | 6503 | → |
| `uptrend` | 32.4% | 6802 | → |
| `hammer_4h` | 31.6% | 171 | → |
| `morning_star_4h` | 31.3% | 697 | → |
| `bull_flag` | 30.8% | 133 | → |
| `breakout_30d` | 18.4% | 223 | → |

---

## Mes prédictions passées et leurs résultats

**2 prédictions mesurées — précision globale : 100%**

| Date | Token | Score | Prix prédit | Prix 14j après | Résultat |
|------|-------|-------|-------------|----------------|---------|
| 17 août 2026 | **ACE** | 76% | 0.1526 | 0.1697 | ✅ +11.2% |
| 17 août 2026 | **PLUME** | 75% | 0.01261 | 0.01465 | ✅ +16.2% |

**167 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 31 août 2026 | **ZK** | 77% | 0.00898 |
| 31 août 2026 | **ENSO** | 76% | 0.908 |
| 31 août 2026 | **BMT** | 75% | 0.02049 |
| 31 août 2026 | **AUCTION** | 75% | 3.528 |
| 31 août 2026 | **JASMY** | 73% | 0.00474 |
| 31 août 2026 | **GMX** | 73% | 7.53 |
| 31 août 2026 | **TNSR** | 73% | 0.0368 |
| 31 août 2026 | **API3** | 73% | 0.2188 |
| 31 août 2026 | **VELODROME** | 73% | 0.02216 |
| 31 août 2026 | **TRX** | 72% | 0.3335 |
| 31 août 2026 | **F** | 72% | 0.003207 |
| 31 août 2026 | **UMA** | 72% | 0.367 |
| 31 août 2026 | **PROM** | 71% | 5.766 |
| 31 août 2026 | **RUNE** | 71% | 0.474 |
| 31 août 2026 | **XVS** | 71% | 3.11 |

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

→ **Régime stable** : BTC bull_prob entre 57.0% et 62.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.5% (31 août 2026) — -35.6% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 42.0% (31 août 2026) — +5.4% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 61.3% (31 août 2026) — -8.0% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 35.6% (31 août 2026) — +11.8% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 69.4% (31 août 2026) — -6.0% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **31066 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0046 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 31 août 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 62%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ZK** | 77% | +18pp | 0 | ⚡ Volume ×6.3 vs médiane |
| **ENSO** | 76% | +17pp | 0 | ⚡ Volume ×11.3 vs médiane |
| **BMT** | 75% | +16pp | 0 | ⚡ Volume ×293.9 vs médiane |
| **AUCTION** | 75% | +16pp | 0 | ⚡ Volume ×11.2 vs médiane |
| **JASMY** | 73% | +14pp | 0 |  |
| **GMX** | 73% | +14pp | 0 |  |
| **TNSR** | 73% | +14pp | 0 |  |
| **API3** | 73% | +14pp | 0 |  |
| **VELODROME** | 73% | +14pp | 0 |  |
| **BFUSD** | 73% | +14pp | 3 |  |
| **TRX** | 72% | +13pp | 3 |  |
| **F** | 72% | +13pp | 2 | ⚡ Volume ×6.4 vs médiane |
