# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 16 sep 2026*

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
  → Meilleur signal haussier actuel : `squeeze_breakout` à 43.9%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 65.9% | 3204 | → |
| `rsi_bearish_divergence` | 63.9% | 797 | → |
| `downtrend` | 58.3% | 15825 | → |
| `evening_star_4h` | 56.7% | 712 | → |
| `bearish_engulfing_4h` | 56.7% | 850 | → |
| `breakdown_30d` | 55.9% | 118 | → |
| `shooting_star_4h` | 55.6% | 266 | → |
| `macd_bearish_cross` | 55.1% | 6394 | → |
| `death_cross` | 53.1% | 341 | → |
| `resistance_test` | 53.0% | 1574 | → |
| `bear_flag` | 49.4% | 571 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 43.9% | 264 | → |
| `rsi_bullish_divergence` | 43.5% | 2423 | → |
| `golden_cross` | 42.4% | 505 | → |
| `hammer_4h` | 42.1% | 261 | → |
| `support_bounce` | 41.6% | 2371 | → |
| `bullish_engulfing_4h` | 40.4% | 968 | → |
| `double_bottom_90d` | 40.4% | 2236 | → |
| `bull_flag` | 38.0% | 200 | → |
| `uptrend` | 37.1% | 8535 | → |
| `macd_bullish_cross` | 36.5% | 7376 | → |
| `morning_star_4h` | 32.6% | 779 | → |
| `breakout_30d` | 28.5% | 344 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 16 sep 2026 | **ASTR** | 80% | 0.006332 |
| 16 sep 2026 | **POL** | 76% | 0.09379 |
| 16 sep 2026 | **HIVE** | 76% | 0.0507 |
| 16 sep 2026 | **ARB** | 75% | 0.1657 |
| 16 sep 2026 | **POLYX** | 75% | 0.0379 |
| 16 sep 2026 | **AWE** | 75% | 0.06342 |
| 16 sep 2026 | **GLM** | 75% | 0.1091 |
| 16 sep 2026 | **REZ** | 75% | 0.003528 |
| 16 sep 2026 | **STEEM** | 75% | 0.05682 |
| 16 sep 2026 | **MTL** | 75% | 0.289 |
| 16 sep 2026 | **KNC** | 75% | 0.1308 |
| 16 sep 2026 | **RAY** | 74% | 1.3459 |
| 16 sep 2026 | **THE** | 74% | 0.0653 |
| 16 sep 2026 | **G** | 74% | 0.00418 |
| 16 sep 2026 | **LSK** | 73% | 0.6387 |

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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 67.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.4% (16 sep 2026) — -35.7% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.5% (16 sep 2026) — +6.9% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.3% (16 sep 2026) — -11.0% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 43.9% (16 sep 2026) — +20.1% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 63.9% (16 sep 2026) — -11.5% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **36345 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0087 |
| momentum | 0.0000 |
| risk | 0.0012 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 16 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 67%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ASTR** | 80% | +13pp | 0 | ⚡ Volume ×6.4 vs médiane |
| **POL** | 76% | +9pp | 1 |  |
| **HIVE** | 76% | +9pp | 0 | ⚡ Volume ×4.0 vs médiane |
| **ARB** | 75% | +8pp | 3 | 🔥 Trending #5 sur CoinGecko|⚡ Volume ×3.7 vs média |
| **POLYX** | 75% | +8pp | 2 |  |
| **AWE** | 75% | +8pp | 0 |  |
| **GLM** | 75% | +8pp | 1 |  |
| **REZ** | 75% | +8pp | 0 | ⚡ Volume ×6.5 vs médiane |
| **STEEM** | 75% | +8pp | 0 | ⚡ Volume ×9.8 vs médiane |
| **MTL** | 75% | +8pp | 0 | ⚡ Volume ×12.4 vs médiane |
| **KNC** | 75% | +8pp | 0 |  |
| **RAY** | 74% | +7pp | 0 |  |
