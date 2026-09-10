# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 10 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 69%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 43.7%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 66.4% | 3000 | → |
| `rsi_bearish_divergence` | 66.0% | 723 | → |
| `downtrend` | 58.4% | 15542 | → |
| `shooting_star_4h` | 57.7% | 253 | → |
| `evening_star_4h` | 57.3% | 660 | → |
| `bearish_engulfing_4h` | 56.9% | 796 | → |
| `macd_bearish_cross` | 55.3% | 5700 | → |
| `resistance_test` | 53.8% | 1499 | → |
| `breakdown_30d` | 53.7% | 108 | → |
| `death_cross` | 52.7% | 317 | → |
| `bear_flag` | 49.1% | 562 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 43.7% | 2378 | → |
| `squeeze_breakout` | 42.6% | 237 | → |
| `golden_cross` | 41.8% | 445 | → |
| `support_bounce` | 41.0% | 2284 | → |
| `double_bottom_90d` | 40.2% | 2155 | → |
| `bullish_engulfing_4h` | 39.9% | 923 | → |
| `hammer_4h` | 38.5% | 205 | → |
| `macd_bullish_cross` | 36.5% | 7289 | → |
| `uptrend` | 35.6% | 7746 | → |
| `bull_flag` | 34.0% | 150 | → |
| `morning_star_4h` | 32.2% | 746 | → |
| `breakout_30d` | 27.7% | 328 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 10 sep 2026 | **GLM** | 79% | 0.1075 |
| 10 sep 2026 | **NEWT** | 79% | 0.04498 |
| 10 sep 2026 | **ARK** | 78% | 0.116 |
| 10 sep 2026 | **LSK** | 78% | 0.1084 |
| 10 sep 2026 | **CVC** | 78% | 0.02169 |
| 10 sep 2026 | **ORCA** | 77% | 1.401 |
| 10 sep 2026 | **XEC** | 76% | 7.3e-06 |
| 10 sep 2026 | **ARPA** | 76% | 0.00915 |
| 10 sep 2026 | **XTZ** | 75% | 0.2523 |
| 10 sep 2026 | **SAHARA** | 75% | 0.00984 |
| 10 sep 2026 | **ANIME** | 74% | 0.00312 |
| 10 sep 2026 | **STRAX** | 74% | 0.00971 |
| 10 sep 2026 | **PORTO** | 74% | 0.451 |
| 10 sep 2026 | **DASH** | 73% | 57.16 |
| 10 sep 2026 | **RSR** | 73% | 0.001395 |

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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 69.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.1% (10 sep 2026) — -36.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.7% (10 sep 2026) — +7.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.4% (10 sep 2026) — -10.9% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 42.6% (10 sep 2026) — +18.8% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 66.0% (10 sep 2026) — -9.4% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **34456 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0085 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 10 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 69%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **BFUSD** | 80% | +11pp | 3 |  |
| **GLM** | 79% | +10pp | 1 |  |
| **NEWT** | 79% | +10pp | 0 | ⚡ Volume ×9.7 vs médiane |
| **ARK** | 78% | +9pp | 0 | ⚡ Volume ×33.2 vs médiane |
| **LSK** | 78% | +9pp | 0 | ⚡ Volume ×8.6 vs médiane |
| **CVC** | 78% | +9pp | 0 | ⚡ Volume ×8.4 vs médiane |
| **ORCA** | 77% | +8pp | 0 |  |
| **XEC** | 76% | +7pp | 0 |  |
| **ARPA** | 76% | +7pp | 1 |  |
| **XTZ** | 75% | +6pp | 2 |  |
| **SAHARA** | 75% | +6pp | 0 | ⚡ Volume ×18.3 vs médiane |
| **ANIME** | 74% | +5pp | 2 | ⚡ Volume ×24.1 vs médiane |
