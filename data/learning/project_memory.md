# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 7 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 64%

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
| `rsi_bearish_divergence` | 67.3% | 624 | → |
| `double_top_90d` | 66.8% | 2927 | → |
| `shooting_star_4h` | 61.5% | 226 | → |
| `downtrend` | 58.8% | 15230 | → |
| `bearish_engulfing_4h` | 58.7% | 750 | → |
| `evening_star_4h` | 57.3% | 647 | → |
| `macd_bearish_cross` | 55.4% | 5629 | → |
| `resistance_test` | 54.2% | 1425 | → |
| `breakdown_30d` | 53.7% | 108 | → |
| `death_cross` | 53.0% | 313 | → |
| `bear_flag` | 49.1% | 562 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 43.6% | 2367 | → |
| `squeeze_breakout` | 43.4% | 226 | → |
| `support_bounce` | 41.0% | 2245 | → |
| `golden_cross` | 40.2% | 410 | → |
| `double_bottom_90d` | 39.6% | 2052 | → |
| `bullish_engulfing_4h` | 39.5% | 913 | → |
| `hammer_4h` | 38.7% | 204 | → |
| `macd_bullish_cross` | 36.5% | 7230 | → |
| `uptrend` | 34.9% | 7400 | → |
| `bull_flag` | 34.2% | 149 | → |
| `morning_star_4h` | 31.5% | 728 | → |
| `breakout_30d` | 26.6% | 308 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 7 sep 2026 | **YGG** | 80% | 0.0247 |
| 7 sep 2026 | **USTC** | 80% | 0.00567 |
| 7 sep 2026 | **ILV** | 80% | 3.38 |
| 7 sep 2026 | **1000CAT** | 78% | 0.002097 |
| 7 sep 2026 | **FIDA** | 77% | 0.0212 |
| 7 sep 2026 | **LAYER** | 77% | 0.074 |
| 7 sep 2026 | **COTI** | 76% | 0.01691 |
| 7 sep 2026 | **LUNC** | 76% | 5.64e-05 |
| 7 sep 2026 | **HEMI** | 76% | 0.00878 |
| 7 sep 2026 | **FTT** | 76% | 0.2288 |
| 7 sep 2026 | **JOE** | 76% | 0.0335 |
| 7 sep 2026 | **SUI** | 75% | 0.8343 |
| 7 sep 2026 | **GMX** | 75% | 8.39 |
| 7 sep 2026 | **SAHARA** | 75% | 0.00922 |
| 7 sep 2026 | **CATI** | 75% | 0.06358 |

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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 64.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.1% (7 sep 2026) — -36.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.6% (7 sep 2026) — +7.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.8% (7 sep 2026) — -10.5% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 43.4% (7 sep 2026) — +19.6% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 67.3% (7 sep 2026) — -8.1% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **33520 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0086 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 7 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 64%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **YGG** | 80% | +16pp | 0 | ⚡ Volume ×7.5 vs médiane |
| **USTC** | 80% | +16pp | 0 | ⚡ Volume ×3.9 vs médiane |
| **ILV** | 80% | +16pp | 2 |  |
| **1000CAT** | 78% | +14pp | 0 |  |
| **FIDA** | 77% | +13pp | 0 | ⚡ Volume ×5.4 vs médiane |
| **LAYER** | 77% | +13pp | 2 |  |
| **COTI** | 76% | +12pp | 2 | ⚡ Volume ×6.1 vs médiane |
| **LUNC** | 76% | +12pp | 0 | 🔥 Trending #10 sur CoinGecko |
| **HEMI** | 76% | +12pp | 3 | ⚡ Volume ×8.5 vs médiane |
| **FTT** | 76% | +12pp | 1 |  |
| **JOE** | 76% | +12pp | 2 |  |
| **SUI** | 75% | +11pp | 2 |  |
