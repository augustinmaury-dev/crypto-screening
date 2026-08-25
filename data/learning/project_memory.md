# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 25 août 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟡 Neutre — 51%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 37.9%
**Signaux baissiers fiables (>50%) :** 11 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 72.4% | 2597 | → |
| `rsi_bearish_divergence` | 71.0% | 535 | → |
| `shooting_star_4h` | 67.5% | 200 | → |
| `downtrend` | 65.1% | 13232 | → |
| `bearish_engulfing_4h` | 63.6% | 607 | → |
| `evening_star_4h` | 62.1% | 570 | → |
| `macd_bearish_cross` | 61.3% | 4819 | → |
| `breakdown_30d` | 60.0% | 90 | → |
| `death_cross` | 59.6% | 265 | → |
| `resistance_test` | 54.6% | 1206 | → |
| `bear_flag` | 52.8% | 519 | 📉 |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 37.9% | 2111 | → |
| `support_bounce` | 36.4% | 1952 | → |
| `bullish_engulfing_4h` | 33.1% | 771 | → |
| `double_bottom_90d` | 32.7% | 1747 | → |
| `golden_cross` | 32.5% | 338 | → |
| `squeeze_breakout` | 31.8% | 154 | → |
| `macd_bullish_cross` | 31.1% | 6289 | → |
| `hammer_4h` | 30.4% | 168 | → |
| `uptrend` | 30.0% | 6488 | → |
| `morning_star_4h` | 28.7% | 654 | → |
| `bull_flag` | 28.6% | 112 | → |
| `breakout_30d` | 16.4% | 213 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**45 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
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
| 23 août 2026 | **COTI** | 71% | 0.01233 |
| 23 août 2026 | **POWR** | 70% | 0.0431 |
| 23 août 2026 | **USDP** | 72% | 0.9997 |
| 22 août 2026 | **PEOPLE** | 75% | 0.01042 |
| 22 août 2026 | **HIVE** | 73% | 0.0455 |

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

📉 **Le marché s'est dégradé** depuis le début du journal : BTC bull_prob 57.0% → 51.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 52.8% (25 août 2026) — -32.3% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 37.9% (25 août 2026) — +1.3% →
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 65.1% (25 août 2026) — -4.2% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 31.8% (25 août 2026) — +8.0% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 71.0% (25 août 2026) — -4.4% 📉

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

## Aujourd'hui — 25 août 2026

**Régime :** 🟡 Neutre (BTC bull_prob = 51%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **PEOPLE** | 74% | +32pp | 0 |  |
| **EURI** | 74% | +32pp | 2 | ⚡ Volume ×4.5 vs médiane |
| **TUT** | 71% | +29pp | 1 | ⚡ Volume ×5.0 vs médiane |
