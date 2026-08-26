# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 26 août 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🔴 Baissier — 39%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 38.8%
**Signaux baissiers fiables (>50%) :** 11 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 71.9% | 2618 | → |
| `rsi_bearish_divergence` | 70.6% | 541 | → |
| `shooting_star_4h` | 67.5% | 200 | → |
| `downtrend` | 64.4% | 13404 | → |
| `bearish_engulfing_4h` | 63.4% | 612 | → |
| `macd_bearish_cross` | 61.1% | 4848 | → |
| `evening_star_4h` | 61.0% | 580 | → |
| `death_cross` | 59.6% | 265 | → |
| `breakdown_30d` | 59.6% | 94 | → |
| `resistance_test` | 54.5% | 1217 | → |
| `bear_flag` | 52.1% | 526 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 38.8% | 2141 | → |
| `support_bounce` | 36.6% | 1968 | → |
| `double_bottom_90d` | 33.6% | 1773 | → |
| `bullish_engulfing_4h` | 33.3% | 775 | → |
| `golden_cross` | 32.7% | 342 | → |
| `squeeze_breakout` | 32.1% | 156 | → |
| `macd_bullish_cross` | 31.7% | 6352 | → |
| `hammer_4h` | 30.4% | 168 | → |
| `uptrend` | 30.4% | 6546 | → |
| `bull_flag` | 28.9% | 114 | → |
| `morning_star_4h` | 28.7% | 654 | → |
| `breakout_30d` | 16.8% | 214 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**50 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 26 août 2026 | **EUL** | 75% | 1.398 |
| 26 août 2026 | **EDEN** | 74% | 0.06057 |
| 26 août 2026 | **BMT** | 71% | 0.02333 |
| 26 août 2026 | **USDP** | 77% | 1.0005 |
| 26 août 2026 | **EURI** | 74% | 1.1674 |
| 25 août 2026 | **PEOPLE** | 74% | 0.00915 |
| 25 août 2026 | **TUT** | 71% | 0.04777 |
| 25 août 2026 | **EURI** | 74% | 1.1662 |
| 24 août 2026 | **TUT** | 73% | 0.08001 |
| 24 août 2026 | **COTI** | 71% | 0.0123 |
| 24 août 2026 | **EUL** | 71% | 1.334 |
| 24 août 2026 | **ONG** | 70% | 0.07388 |
| 24 août 2026 | **EURI** | 70% | 1.1674 |
| 23 août 2026 | **EUL** | 73% | 1.247 |
| 23 août 2026 | **TUT** | 72% | 0.06405 |

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

📉 **Le marché s'est dégradé** depuis le début du journal : BTC bull_prob 57.0% → 39.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 52.1% (26 août 2026) — -33.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 38.8% (26 août 2026) — +2.2% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 64.4% (26 août 2026) — -4.9% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 32.1% (26 août 2026) — +8.3% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 70.6% (26 août 2026) — -4.8% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers sont **bloqués** sous 40% : je ne suis pas encore fiable pour détecter les hausses.

---

## Le score composite est-il utile ?

J'ai analysé **24093 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0002 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 26 août 2026

**Régime :** 🔴 Baissier (BTC bull_prob = 39%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **USDP** | 77% | +38pp | 2 | ⚡ Volume ×3.7 vs médiane |
| **EUL** | 75% | +36pp | 0 | ⚡ Volume ×3.3 vs médiane |
| **EDEN** | 74% | +35pp | 0 | ⚡ Volume ×3.1 vs médiane |
| **EURI** | 74% | +35pp | 2 | ⚡ Volume ×4.1 vs médiane |
| **BMT** | 71% | +32pp | 0 | ⚡ Volume ×30.1 vs médiane |
