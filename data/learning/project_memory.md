# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 15 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 76%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 44.2%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 65.7% | 3166 | → |
| `rsi_bearish_divergence` | 64.1% | 790 | → |
| `downtrend` | 58.3% | 15786 | → |
| `evening_star_4h` | 56.8% | 704 | → |
| `bearish_engulfing_4h` | 56.4% | 826 | → |
| `breakdown_30d` | 55.6% | 117 | → |
| `shooting_star_4h` | 55.6% | 266 | → |
| `macd_bearish_cross` | 54.7% | 6203 | → |
| `resistance_test` | 53.1% | 1563 | → |
| `death_cross` | 52.8% | 337 | → |
| `bear_flag` | 49.5% | 570 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 44.2% | 260 | → |
| `rsi_bullish_divergence` | 43.5% | 2410 | → |
| `golden_cross` | 42.2% | 495 | → |
| `hammer_4h` | 41.9% | 258 | → |
| `support_bounce` | 41.7% | 2357 | → |
| `double_bottom_90d` | 40.4% | 2227 | → |
| `bullish_engulfing_4h` | 40.3% | 963 | → |
| `bull_flag` | 37.3% | 177 | → |
| `uptrend` | 37.0% | 8397 | → |
| `macd_bullish_cross` | 36.5% | 7362 | → |
| `morning_star_4h` | 32.6% | 775 | → |
| `breakout_30d` | 28.4% | 341 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 15 sep 2026 | **AXL** | 80% | 0.0455 |
| 15 sep 2026 | **AWE** | 80% | 0.0635 |
| 15 sep 2026 | **GLM** | 79% | 0.1168 |
| 15 sep 2026 | **LSK** | 77% | 0.3766 |
| 15 sep 2026 | **FF** | 77% | 0.14512 |
| 15 sep 2026 | **THE** | 77% | 0.0666 |
| 15 sep 2026 | **QKC** | 77% | 0.00248 |
| 15 sep 2026 | **BTC** | 76% | 76934 |
| 15 sep 2026 | **ZIL** | 76% | 0.002867 |
| 15 sep 2026 | **GAS** | 75% | 1.264 |
| 15 sep 2026 | **REZ** | 75% | 0.003657 |
| 15 sep 2026 | **STEEM** | 75% | 0.05733 |
| 15 sep 2026 | **HIVE** | 74% | 0.0525 |
| 15 sep 2026 | **MTL** | 74% | 0.293 |
| 15 sep 2026 | **DOGS** | 74% | 4.829e-05 |

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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 76.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.5% (15 sep 2026) — -35.6% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.5% (15 sep 2026) — +6.9% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.3% (15 sep 2026) — -11.0% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 44.2% (15 sep 2026) — +20.4% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 64.1% (15 sep 2026) — -11.3% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **35991 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0090 |
| momentum | 0.0000 |
| risk | 0.0005 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 15 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 76%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **AXL** | 80% | +13pp | 2 | ⚡ Volume ×10.7 vs médiane |
| **AWE** | 80% | +13pp | 0 |  |
| **GLM** | 79% | +12pp | 2 |  |
| **LSK** | 77% | +10pp | 0 | ⚡ Volume ×37.5 vs médiane |
| **FF** | 77% | +10pp | 0 |  |
| **THE** | 77% | +10pp | 1 | ⚡ Volume ×20.7 vs médiane |
| **QKC** | 77% | +10pp | 0 | ⚡ Volume ×6.6 vs médiane |
| **BTC** | 76% | +9pp | 3 | 🔥 Trending #2 sur CoinGecko |
| **ZIL** | 76% | +9pp | 0 | ⚡ Volume ×8.8 vs médiane |
| **GAS** | 75% | +8pp | 1 |  |
| **REZ** | 75% | +8pp | 0 | ⚡ Volume ×80.8 vs médiane |
| **STEEM** | 75% | +8pp | 2 | ⚡ Volume ×12.6 vs médiane |
