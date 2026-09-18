# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 18 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 70%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 46.1%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 65.5% | 3283 | → |
| `rsi_bearish_divergence` | 62.3% | 844 | → |
| `downtrend` | 58.2% | 15909 | → |
| `bearish_engulfing_4h` | 56.6% | 868 | → |
| `evening_star_4h` | 56.3% | 726 | → |
| `breakdown_30d` | 56.3% | 119 | → |
| `shooting_star_4h` | 55.5% | 274 | → |
| `macd_bearish_cross` | 55.2% | 6670 | → |
| `resistance_test` | 52.8% | 1611 | → |
| `death_cross` | 52.7% | 347 | → |
| `bear_flag` | 49.0% | 575 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 46.1% | 282 | → |
| `rsi_bullish_divergence` | 43.6% | 2428 | → |
| `golden_cross` | 43.1% | 527 | → |
| `hammer_4h` | 42.2% | 263 | → |
| `support_bounce` | 41.6% | 2396 | → |
| `bull_flag` | 40.6% | 239 | → |
| `double_bottom_90d` | 40.5% | 2259 | → |
| `bullish_engulfing_4h` | 40.4% | 986 | → |
| `uptrend` | 37.8% | 8872 | → |
| `macd_bullish_cross` | 36.8% | 7445 | → |
| `morning_star_4h` | 32.8% | 798 | → |
| `breakout_30d` | 29.5% | 353 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 18 sep 2026 | **ROSE** | 80% | 0.0072 |
| 18 sep 2026 | **ENSO** | 80% | 0.943 |
| 18 sep 2026 | **LSK** | 78% | 0.4501 |
| 18 sep 2026 | **AXS** | 78% | 0.999 |
| 18 sep 2026 | **LPT** | 77% | 1.523 |
| 18 sep 2026 | **ASTR** | 77% | 0.006536 |
| 18 sep 2026 | **STEEM** | 77% | 0.05559 |
| 18 sep 2026 | **ARB** | 76% | 0.2047 |
| 18 sep 2026 | **MET** | 76% | 0.2489 |
| 18 sep 2026 | **ORCA** | 76% | 1.432 |
| 18 sep 2026 | **1INCH** | 76% | 0.0949 |
| 18 sep 2026 | **CVC** | 76% | 0.02654 |
| 18 sep 2026 | **APT** | 75% | 0.683 |
| 18 sep 2026 | **SKY** | 75% | 0.06646 |
| 18 sep 2026 | **REZ** | 75% | 0.003929 |

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
| 18 sep 2026 | 🟢 Haussier | 70.0% | ROSE, ENSO, LSK |

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 70.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.0% (18 sep 2026) — -36.1% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.6% (18 sep 2026) — +7.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.2% (18 sep 2026) — -11.1% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 46.1% (18 sep 2026) — +22.3% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 62.3% (18 sep 2026) — -13.1% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **37052 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0083 |
| momentum | 0.0000 |
| risk | 0.0034 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 18 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 70%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ROSE** | 80% | +10pp | 2 |  |
| **ENSO** | 80% | +10pp | 0 |  |
| **LSK** | 78% | +8pp | 0 | ⚡ Volume ×16.5 vs médiane |
| **AXS** | 78% | +8pp | 0 |  |
| **LPT** | 77% | +7pp | 0 |  |
| **ASTR** | 77% | +7pp | 2 |  |
| **STEEM** | 77% | +7pp | 0 | ⚡ Volume ×4.5 vs médiane |
| **ARB** | 76% | +6pp | ⚠️ 6 | 🔥 Trending #3 sur CoinGecko|⚡ Volume ×5.1 vs média |
| **MET** | 76% | +6pp | 2 |  |
| **ORCA** | 76% | +6pp | 1 |  |
| **1INCH** | 76% | +6pp | 3 |  |
| **CVC** | 76% | +6pp | 0 | ⚡ Volume ×4.1 vs médiane |
