# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 12 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 66%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 43.6%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 66.2% | 3060 | → |
| `rsi_bearish_divergence` | 65.8% | 746 | → |
| `downtrend` | 58.4% | 15653 | → |
| `shooting_star_4h` | 57.9% | 254 | → |
| `evening_star_4h` | 57.1% | 672 | → |
| `bearish_engulfing_4h` | 56.7% | 806 | → |
| `macd_bearish_cross` | 55.2% | 5814 | → |
| `breakdown_30d` | 54.1% | 111 | → |
| `resistance_test` | 53.6% | 1527 | → |
| `death_cross` | 52.9% | 323 | → |
| `bear_flag` | 49.3% | 564 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 43.6% | 2388 | → |
| `squeeze_breakout` | 42.7% | 248 | → |
| `golden_cross` | 42.1% | 463 | → |
| `support_bounce` | 41.1% | 2298 | → |
| `hammer_4h` | 41.1% | 248 | → |
| `double_bottom_90d` | 40.4% | 2184 | → |
| `bullish_engulfing_4h` | 40.0% | 943 | → |
| `macd_bullish_cross` | 36.5% | 7319 | → |
| `uptrend` | 36.1% | 7999 | → |
| `bull_flag` | 34.0% | 150 | → |
| `morning_star_4h` | 32.3% | 758 | → |
| `breakout_30d` | 28.0% | 329 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 12 sep 2026 | **MET** | 79% | 0.237 |
| 12 sep 2026 | **THE** | 77% | 0.0669 |
| 12 sep 2026 | **ORCA** | 76% | 1.444 |
| 12 sep 2026 | **PUNDIX** | 76% | 0.0993 |
| 12 sep 2026 | **ARK** | 75% | 0.1171 |
| 12 sep 2026 | **ANIME** | 75% | 0.00296 |
| 12 sep 2026 | **BLUR** | 74% | 0.01748 |
| 12 sep 2026 | **CVC** | 74% | 0.02182 |
| 12 sep 2026 | **NEAR** | 73% | 2.37 |
| 12 sep 2026 | **THETA** | 73% | 0.1899 |
| 12 sep 2026 | **SC** | 73% | 0.000946 |
| 12 sep 2026 | **ZRX** | 73% | 0.1059 |
| 12 sep 2026 | **XVS** | 73% | 3.1 |
| 12 sep 2026 | **TREE** | 73% | 0.0431 |
| 12 sep 2026 | **MTL** | 73% | 0.269 |

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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 66.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.3% (12 sep 2026) — -35.8% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.6% (12 sep 2026) — +7.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.4% (12 sep 2026) — -10.9% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 42.7% (12 sep 2026) — +18.9% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 65.8% (12 sep 2026) — -9.6% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **35022 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0095 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 12 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 66%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **MET** | 79% | +13pp | 2 |  |
| **THE** | 77% | +11pp | 1 | ⚡ Volume ×15.7 vs médiane |
| **ORCA** | 76% | +10pp | 0 |  |
| **PUNDIX** | 76% | +10pp | ⚠️ 5 | ⚡ Volume ×9.8 vs médiane |
| **ARK** | 75% | +9pp | 3 | ⚡ Volume ×13.1 vs médiane |
| **ANIME** | 75% | +9pp | 2 |  |
| **BLUR** | 74% | +8pp | 0 |  |
| **CVC** | 74% | +8pp | 2 | ⚡ Volume ×4.3 vs médiane |
| **NEAR** | 73% | +7pp | 2 | 🔥 Trending #5 sur CoinGecko |
| **THETA** | 73% | +7pp | ⚠️ 5 |  |
| **SC** | 73% | +7pp | 2 | ⚡ Volume ×6.6 vs médiane |
| **ZRX** | 73% | +7pp | ⚠️ 5 |  |
