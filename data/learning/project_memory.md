# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 28 août 2026*

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
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 40.7%
**Signaux baissiers fiables (>50%) :** 11 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 70.8% | 2663 | → |
| `rsi_bearish_divergence` | 69.8% | 550 | → |
| `shooting_star_4h` | 66.2% | 204 | → |
| `bearish_engulfing_4h` | 63.5% | 613 | → |
| `downtrend` | 63.1% | 13745 | → |
| `evening_star_4h` | 60.6% | 586 | → |
| `death_cross` | 59.4% | 266 | → |
| `macd_bearish_cross` | 59.4% | 5013 | → |
| `breakdown_30d` | 56.9% | 102 | → |
| `resistance_test` | 54.3% | 1243 | → |
| `bear_flag` | 50.3% | 549 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 40.7% | 2219 | → |
| `support_bounce` | 37.4% | 2007 | → |
| `double_bottom_90d` | 34.8% | 1808 | → |
| `bullish_engulfing_4h` | 33.9% | 787 | → |
| `golden_cross` | 33.1% | 350 | → |
| `squeeze_breakout` | 32.9% | 164 | → |
| `macd_bullish_cross` | 32.0% | 6408 | → |
| `uptrend` | 31.3% | 6652 | → |
| `hammer_4h` | 31.2% | 170 | → |
| `bull_flag` | 30.2% | 116 | → |
| `morning_star_4h` | 29.0% | 663 | → |
| `breakout_30d` | 17.2% | 215 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**116 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 28 août 2026 | **SOL** | 76% | 103.38 |
| 28 août 2026 | **MORPHO** | 76% | 2.426 |
| 28 août 2026 | **GMX** | 75% | 7.56 |
| 28 août 2026 | **ONT** | 74% | 0.05532 |
| 28 août 2026 | **RUNE** | 74% | 0.472 |
| 28 août 2026 | **DGB** | 74% | 0.00481 |
| 28 août 2026 | **LAYER** | 74% | 0.0701 |
| 28 août 2026 | **CAKE** | 73% | 1.704 |
| 28 août 2026 | **COMP** | 73% | 18.05 |
| 28 août 2026 | **TUT** | 73% | 0.04083 |
| 28 août 2026 | **ENSO** | 73% | 0.845 |
| 28 août 2026 | **COTI** | 73% | 0.01215 |
| 28 août 2026 | **ENA** | 72% | 0.1608 |
| 28 août 2026 | **SUPER** | 72% | 0.1112 |
| 28 août 2026 | **EDEN** | 72% | 0.07092 |

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

📈 **Le marché s'est renforcé** depuis le début du journal : BTC bull_prob 57.0% → 70.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 50.3% (28 août 2026) — -34.8% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 40.7% (28 août 2026) — +4.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 63.1% (28 août 2026) — -6.2% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 32.9% (28 août 2026) — +9.1% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 69.8% (28 août 2026) — -5.6% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **30075 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0018 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 28 août 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 70%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **SOL** | 76% | +15pp | 2 | 🔥 Trending #3 sur CoinGecko |
| **MORPHO** | 76% | +15pp | 0 |  |
| **GMX** | 75% | +14pp | 2 |  |
| **EURI** | 75% | +14pp | ⚠️ 5 | ⚡ Volume ×12.2 vs médiane |
| **ONT** | 74% | +13pp | 0 | ⚡ Volume ×7.8 vs médiane |
| **RUNE** | 74% | +13pp | 0 |  |
| **DGB** | 74% | +13pp | 0 |  |
| **LAYER** | 74% | +13pp | 0 |  |
| **CAKE** | 73% | +12pp | 2 |  |
| **COMP** | 73% | +12pp | 0 |  |
| **TUT** | 73% | +12pp | 1 | ⚡ Volume ×8.4 vs médiane |
| **ENSO** | 73% | +12pp | 1 | ⚡ Volume ×8.1 vs médiane |
