# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 30 août 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 55%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 41.8%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 69.8% | 2711 | → |
| `rsi_bearish_divergence` | 69.4% | 563 | → |
| `shooting_star_4h` | 65.7% | 207 | → |
| `downtrend` | 61.9% | 14080 | → |
| `bearish_engulfing_4h` | 61.7% | 639 | → |
| `evening_star_4h` | 59.5% | 598 | → |
| `death_cross` | 58.5% | 270 | → |
| `macd_bearish_cross` | 57.8% | 5211 | → |
| `breakdown_30d` | 56.9% | 102 | → |
| `resistance_test` | 54.7% | 1270 | → |
| `bear_flag` | 49.6% | 556 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 41.8% | 2263 | → |
| `support_bounce` | 38.4% | 2075 | → |
| `bullish_engulfing_4h` | 36.8% | 832 | → |
| `double_bottom_90d` | 35.8% | 1841 | → |
| `squeeze_breakout` | 35.5% | 172 | → |
| `golden_cross` | 33.7% | 356 | → |
| `macd_bullish_cross` | 32.2% | 6464 | → |
| `uptrend` | 32.0% | 6744 | → |
| `hammer_4h` | 31.6% | 171 | → |
| `morning_star_4h` | 30.8% | 689 | → |
| `bull_flag` | 30.4% | 125 | → |
| `breakout_30d` | 17.8% | 219 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**141 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 30 août 2026 | **ZK** | 77% | 0.00908 |
| 30 août 2026 | **BAND** | 76% | 0.1784 |
| 30 août 2026 | **DOLO** | 76% | 0.02635 |
| 30 août 2026 | **ENSO** | 75% | 0.885 |
| 30 août 2026 | **BMT** | 75% | 0.02187 |
| 30 août 2026 | **WCT** | 74% | 0.03901 |
| 30 août 2026 | **MAGIC** | 72% | 0.0494 |
| 30 août 2026 | **GMX** | 70% | 7.83 |
| 30 août 2026 | **AUCTION** | 70% | 3.711 |
| 30 août 2026 | **LISTA** | 70% | 0.0722 |
| 30 août 2026 | **INIT** | 70% | 0.05833 |
| 30 août 2026 | **EURI** | 74% | 1.1579 |
| 29 août 2026 | **MASK** | 79% | 0.433 |
| 29 août 2026 | **ARPA** | 78% | 0.00949 |
| 29 août 2026 | **GNO** | 76% | 117.09 |

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

→ **Régime stable** : BTC bull_prob entre 57.0% et 55.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.6% (30 août 2026) — -35.5% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 41.8% (30 août 2026) — +5.2% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 61.9% (30 août 2026) — -7.4% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 35.5% (30 août 2026) — +11.7% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 69.4% (30 août 2026) — -6.0% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **30740 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0039 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 30 août 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 55%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ZK** | 77% | +22pp | 0 | ⚡ Volume ×7.4 vs médiane |
| **BAND** | 76% | +21pp | 0 | ⚡ Volume ×5.8 vs médiane |
| **DOLO** | 76% | +21pp | 0 | ⚡ Volume ×4.0 vs médiane |
| **ENSO** | 75% | +20pp | 0 | ⚡ Volume ×69.7 vs médiane |
| **BMT** | 75% | +20pp | 0 | ⚡ Volume ×18.3 vs médiane |
| **WCT** | 74% | +19pp | 0 |  |
| **EURI** | 74% | +19pp | ⚠️ 5 | ⚡ Volume ×4.3 vs médiane |
| **MAGIC** | 72% | +17pp | 0 | ⚡ Volume ×11.2 vs médiane |
| **GMX** | 70% | +15pp | 2 |  |
| **AUCTION** | 70% | +15pp | 2 | ⚡ Volume ×21.7 vs médiane |
| **LISTA** | 70% | +15pp | ⚠️ 5 | ⚡ Volume ×4.8 vs médiane |
| **INIT** | 70% | +15pp | 2 |  |
