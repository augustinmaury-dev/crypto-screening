# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 1 sep 2026*

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
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 43.0%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Précision sur mes prédictions passées :** 80% (4/5 correctes)

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bearish_divergence` | 69.4% | 571 | → |
| `double_top_90d` | 68.6% | 2770 | → |
| `shooting_star_4h` | 62.0% | 221 | → |
| `downtrend` | 60.8% | 14391 | → |
| `bearish_engulfing_4h` | 60.4% | 659 | → |
| `evening_star_4h` | 59.4% | 603 | → |
| `macd_bearish_cross` | 56.3% | 5391 | → |
| `death_cross` | 56.2% | 283 | → |
| `resistance_test` | 54.9% | 1293 | → |
| `breakdown_30d` | 54.7% | 106 | 📉 |
| `bear_flag` | 49.4% | 559 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 43.0% | 2321 | → |
| `support_bounce` | 39.2% | 2111 | → |
| `bullish_engulfing_4h` | 37.1% | 843 | → |
| `squeeze_breakout` | 37.1% | 178 | → |
| `double_bottom_90d` | 36.7% | 1871 | → |
| `golden_cross` | 34.4% | 360 | → |
| `uptrend` | 32.8% | 6868 | → |
| `macd_bullish_cross` | 32.7% | 6540 | → |
| `bull_flag` | 31.9% | 138 | → |
| `morning_star_4h` | 31.7% | 704 | → |
| `hammer_4h` | 31.4% | 172 | → |
| `breakout_30d` | 18.4% | 223 | → |

---

## Mes prédictions passées et leurs résultats

**5 prédictions mesurées — précision globale : 80%**

| Date | Token | Score | Prix prédit | Prix 14j après | Résultat |
|------|-------|-------|-------------|----------------|---------|
| 18 août 2026 | **ACE** | 77% | 0.1958 | 0.1936 | ❌ -1.1% |
| 18 août 2026 | **RED** | 70% | 0.0994 | 0.1095 | ✅ +10.2% |
| 18 août 2026 | **EURI** | 75% | 1.1581 | 1.1593 | ✅ +0.1% |
| 17 août 2026 | **ACE** | 76% | 0.1526 | 0.1697 | ✅ +11.2% |
| 17 août 2026 | **PLUME** | 75% | 0.01261 | 0.01465 | ✅ +16.2% |

**186 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 1 sep 2026 | **STRAX** | 78% | 0.00958 |
| 1 sep 2026 | **NOT** | 76% | 0.000466 |
| 1 sep 2026 | **SOMI** | 76% | 0.1152 |
| 1 sep 2026 | **ONT** | 74% | 0.05552 |
| 1 sep 2026 | **ENSO** | 74% | 0.864 |
| 1 sep 2026 | **0G** | 73% | 0.2079 |
| 1 sep 2026 | **AR** | 73% | 2.206 |
| 1 sep 2026 | **ZK** | 73% | 0.00929 |
| 1 sep 2026 | **SUSHI** | 73% | 0.2 |
| 1 sep 2026 | **DOGS** | 72% | 4.106e-05 |
| 1 sep 2026 | **ZKC** | 72% | 0.0504 |
| 1 sep 2026 | **AXL** | 71% | 0.0423 |
| 1 sep 2026 | **RUNE** | 71% | 0.482 |
| 1 sep 2026 | **BMT** | 71% | 0.02026 |
| 1 sep 2026 | **ANIME** | 71% | 0.00278 |

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

→ **Régime stable** : BTC bull_prob entre 57.0% et 56.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.4% (1 sep 2026) — -35.7% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.0% (1 sep 2026) — +6.4% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 60.8% (1 sep 2026) — -8.5% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 37.1% (1 sep 2026) — +13.3% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 69.4% (1 sep 2026) — -6.0% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **31406 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0057 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 1 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 56%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **STRAX** | 78% | +22pp | 0 | ⚡ Volume ×5.1 vs médiane |
| **NOT** | 76% | +20pp | 2 | ⚡ Volume ×5.2 vs médiane |
| **SOMI** | 76% | +20pp | 0 | ⚡ Volume ×5.1 vs médiane |
| **ONT** | 74% | +18pp | 0 | ⚡ Volume ×5.7 vs médiane |
| **ENSO** | 74% | +18pp | 0 | ⚡ Volume ×58.4 vs médiane |
| **0G** | 73% | +17pp | 0 | ⚡ Volume ×11.7 vs médiane |
| **AR** | 73% | +17pp | 0 |  |
| **ZK** | 73% | +17pp | 0 |  |
| **SUSHI** | 73% | +17pp | 2 |  |
| **DOGS** | 72% | +16pp | 0 |  |
| **ZKC** | 72% | +16pp | 0 | ⚡ Volume ×7.2 vs médiane |
| **AXL** | 71% | +15pp | 0 |  |
