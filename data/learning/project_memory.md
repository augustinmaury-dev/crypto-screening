# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 14 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 73%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 43.6%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 65.8% | 3130 | → |
| `rsi_bearish_divergence` | 64.4% | 779 | → |
| `downtrend` | 58.3% | 15744 | → |
| `evening_star_4h` | 56.7% | 697 | → |
| `bearish_engulfing_4h` | 56.6% | 821 | → |
| `shooting_star_4h` | 55.6% | 266 | → |
| `macd_bearish_cross` | 54.8% | 6034 | → |
| `breakdown_30d` | 54.8% | 115 | → |
| `death_cross` | 53.0% | 332 | → |
| `resistance_test` | 53.0% | 1550 | → |
| `bear_flag` | 49.5% | 568 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 43.6% | 257 | → |
| `rsi_bullish_divergence` | 43.5% | 2398 | → |
| `golden_cross` | 42.4% | 486 | → |
| `support_bounce` | 41.6% | 2330 | → |
| `hammer_4h` | 41.4% | 251 | → |
| `double_bottom_90d` | 40.5% | 2215 | → |
| `bullish_engulfing_4h` | 40.2% | 960 | → |
| `uptrend` | 36.8% | 8265 | → |
| `macd_bullish_cross` | 36.5% | 7350 | → |
| `bull_flag` | 36.2% | 160 | → |
| `morning_star_4h` | 32.6% | 774 | → |
| `breakout_30d` | 28.1% | 338 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 14 sep 2026 | **GLM** | 80% | 0.1171 |
| 14 sep 2026 | **API3** | 80% | 0.2447 |
| 14 sep 2026 | **THE** | 77% | 0.066 |
| 14 sep 2026 | **MINA** | 76% | 0.0813 |
| 14 sep 2026 | **IOTA** | 74% | 0.0451 |
| 14 sep 2026 | **STEEM** | 74% | 0.05641 |
| 14 sep 2026 | **IQ** | 74% | 0.000888 |
| 14 sep 2026 | **BTC** | 73% | 78106 |
| 14 sep 2026 | **INJ** | 73% | 6.137 |
| 14 sep 2026 | **1INCH** | 73% | 0.0928 |
| 14 sep 2026 | **ZRX** | 73% | 0.1095 |
| 14 sep 2026 | **WBETH** | 73% | 2777.2 |
| 14 sep 2026 | **VANA** | 73% | 0.963 |
| 14 sep 2026 | **ILV** | 73% | 3.47 |
| 14 sep 2026 | **ZIL** | 72% | 0.002997 |

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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 73.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.5% (14 sep 2026) — -35.6% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.5% (14 sep 2026) — +6.9% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.3% (14 sep 2026) — -11.0% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 43.6% (14 sep 2026) — +19.8% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 64.4% (14 sep 2026) — -11.0% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **35652 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0090 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 14 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 73%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **GLM** | 80% | +10pp | 2 | ⚡ Volume ×12.0 vs médiane |
| **API3** | 80% | +10pp | 0 | ⚡ Volume ×9.5 vs médiane |
| **THE** | 77% | +7pp | 1 | ⚡ Volume ×21.6 vs médiane |
| **MINA** | 76% | +6pp | 0 |  |
| **IOTA** | 74% | +4pp | 2 |  |
| **STEEM** | 74% | +4pp | 0 | ⚡ Volume ×17.7 vs médiane |
| **IQ** | 74% | +4pp | 0 | ⚡ Volume ×12.8 vs médiane |
| **BTC** | 73% | +3pp | ⚠️ 5 | 🔥 Trending #6 sur CoinGecko |
| **INJ** | 73% | +3pp | 2 |  |
| **1INCH** | 73% | +3pp | 1 |  |
| **ZRX** | 73% | +3pp | 2 |  |
| **WBETH** | 73% | +3pp | 3 |  |
