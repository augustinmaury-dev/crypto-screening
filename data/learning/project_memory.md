# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 8 sep 2026*

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
| `double_top_90d` | 66.6% | 2950 | → |
| `rsi_bearish_divergence` | 66.0% | 656 | → |
| `shooting_star_4h` | 59.6% | 235 | → |
| `downtrend` | 58.6% | 15357 | → |
| `bearish_engulfing_4h` | 57.6% | 780 | → |
| `evening_star_4h` | 57.3% | 654 | → |
| `macd_bearish_cross` | 55.3% | 5646 | → |
| `resistance_test` | 54.5% | 1451 | → |
| `breakdown_30d` | 53.7% | 108 | → |
| `death_cross` | 52.9% | 314 | → |
| `bear_flag` | 49.1% | 562 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 43.6% | 2370 | → |
| `squeeze_breakout` | 43.4% | 226 | → |
| `golden_cross` | 40.9% | 423 | → |
| `support_bounce` | 40.9% | 2254 | → |
| `double_bottom_90d` | 39.9% | 2088 | → |
| `bullish_engulfing_4h` | 39.8% | 917 | → |
| `hammer_4h` | 38.7% | 204 | → |
| `macd_bullish_cross` | 36.5% | 7261 | → |
| `uptrend` | 35.2% | 7513 | → |
| `bull_flag` | 34.0% | 150 | → |
| `morning_star_4h` | 31.8% | 738 | → |
| `breakout_30d` | 27.2% | 313 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 8 sep 2026 | **ORCA** | 80% | 1.4 |
| 8 sep 2026 | **1000CAT** | 80% | 0.00213 |
| 8 sep 2026 | **UMA** | 77% | 0.385 |
| 8 sep 2026 | **RAY** | 76% | 1.0778 |
| 8 sep 2026 | **SAHARA** | 75% | 0.00952 |
| 8 sep 2026 | **HEMI** | 75% | 0.00894 |
| 8 sep 2026 | **HAEDAL** | 75% | 0.01975 |
| 8 sep 2026 | **INJ** | 74% | 6.254 |
| 8 sep 2026 | **NMR** | 74% | 9.45 |
| 8 sep 2026 | **USTC** | 74% | 0.00556 |
| 8 sep 2026 | **DASH** | 72% | 63.14 |
| 8 sep 2026 | **COTI** | 72% | 0.01767 |
| 8 sep 2026 | **SFP** | 72% | 0.2815 |
| 8 sep 2026 | **XVS** | 72% | 3.3 |
| 8 sep 2026 | **ZKC** | 72% | 0.0488 |

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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 69.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.1% (8 sep 2026) — -36.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.6% (8 sep 2026) — +7.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.6% (8 sep 2026) — -10.7% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 43.4% (8 sep 2026) — +19.6% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 66.0% (8 sep 2026) — -9.4% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **33849 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

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

## Aujourd'hui — 8 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 69%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ORCA** | 80% | +11pp | 0 | ⚡ Volume ×5.0 vs médiane |
| **1000CAT** | 80% | +11pp | 0 | ⚡ Volume ×7.5 vs médiane |
| **UMA** | 77% | +8pp | 0 | ⚡ Volume ×4.7 vs médiane |
| **RAY** | 76% | +7pp | 0 | ⚡ Volume ×6.7 vs médiane |
| **SAHARA** | 75% | +6pp | 0 | ⚡ Volume ×8.3 vs médiane |
| **HEMI** | 75% | +6pp | 3 | ⚡ Volume ×4.1 vs médiane |
| **HAEDAL** | 75% | +6pp | ⚠️ 5 | ⚡ Volume ×14.9 vs médiane |
| **INJ** | 74% | +5pp | 2 |  |
| **NMR** | 74% | +5pp | 0 |  |
| **USTC** | 74% | +5pp | 0 |  |
| **DASH** | 72% | +3pp | 0 |  |
| **COTI** | 72% | +3pp | ⚠️ 4 |  |
