# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 9 sep 2026*

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
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 43.6%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 66.4% | 2975 | → |
| `rsi_bearish_divergence` | 65.8% | 675 | → |
| `shooting_star_4h` | 58.5% | 241 | → |
| `downtrend` | 58.4% | 15480 | → |
| `evening_star_4h` | 57.2% | 656 | → |
| `bearish_engulfing_4h` | 56.9% | 792 | → |
| `macd_bearish_cross` | 55.2% | 5675 | → |
| `resistance_test` | 53.9% | 1480 | → |
| `breakdown_30d` | 53.7% | 108 | → |
| `death_cross` | 52.5% | 316 | → |
| `bear_flag` | 49.1% | 562 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 43.6% | 2372 | → |
| `squeeze_breakout` | 43.0% | 228 | → |
| `golden_cross` | 41.9% | 434 | → |
| `support_bounce` | 41.0% | 2261 | → |
| `double_bottom_90d` | 40.5% | 2122 | → |
| `bullish_engulfing_4h` | 40.0% | 920 | → |
| `hammer_4h` | 38.7% | 204 | → |
| `macd_bullish_cross` | 36.6% | 7277 | → |
| `uptrend` | 35.6% | 7627 | → |
| `bull_flag` | 34.0% | 150 | → |
| `morning_star_4h` | 32.2% | 743 | → |
| `breakout_30d` | 27.1% | 314 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 9 sep 2026 | **HOLO** | 80% | 0.0675 |
| 9 sep 2026 | **ORCA** | 80% | 1.446 |
| 9 sep 2026 | **GLM** | 80% | 0.1082 |
| 9 sep 2026 | **G** | 80% | 0.00399 |
| 9 sep 2026 | **OSMO** | 78% | 0.0377 |
| 9 sep 2026 | **DASH** | 77% | 65.61 |
| 9 sep 2026 | **ETC** | 77% | 8.32 |
| 9 sep 2026 | **FORM** | 76% | 0.2987 |
| 9 sep 2026 | **HAEDAL** | 76% | 0.02002 |
| 9 sep 2026 | **XTZ** | 75% | 0.2625 |
| 9 sep 2026 | **ZRX** | 74% | 0.108 |
| 9 sep 2026 | **CELO** | 74% | 0.07891 |
| 9 sep 2026 | **MIRA** | 74% | 0.04971 |
| 9 sep 2026 | **ZKP** | 74% | 0.0481 |
| 9 sep 2026 | **NEWT** | 73% | 0.04446 |

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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 69.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.1% (9 sep 2026) — -36.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.6% (9 sep 2026) — +7.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.4% (9 sep 2026) — -10.9% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 43.0% (9 sep 2026) — +19.2% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 65.8% (9 sep 2026) — -9.6% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **34157 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0084 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 9 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 69%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **HOLO** | 80% | +11pp | 0 | ⚡ Volume ×6.2 vs médiane |
| **ORCA** | 80% | +11pp | 0 | ⚡ Volume ×6.8 vs médiane |
| **GLM** | 80% | +11pp | 1 | ⚡ Volume ×6.6 vs médiane |
| **G** | 80% | +11pp | 0 |  |
| **OSMO** | 78% | +9pp | 0 | ⚡ Volume ×3.9 vs médiane |
| **DASH** | 77% | +8pp | 2 |  |
| **ETC** | 77% | +8pp | 2 |  |
| **FORM** | 76% | +7pp | 0 | ⚡ Volume ×10.0 vs médiane |
| **HAEDAL** | 76% | +7pp | ⚠️ 4 | ⚡ Volume ×4.0 vs médiane |
| **XTZ** | 75% | +6pp | 2 | ⚡ Volume ×6.2 vs médiane |
| **ZRX** | 74% | +5pp | ⚠️ 4 | ⚡ Volume ×5.1 vs médiane |
| **CELO** | 74% | +5pp | 2 |  |
