# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 24 août 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🔴 Baissier — 44%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 37.2%
**Signaux baissiers fiables (>50%) :** 11 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 72.8% | 2576 | → |
| `rsi_bearish_divergence` | 71.6% | 528 | → |
| `shooting_star_4h` | 68.2% | 198 | → |
| `downtrend` | 65.8% | 13056 | → |
| `bearish_engulfing_4h` | 63.7% | 606 | → |
| `evening_star_4h` | 62.1% | 568 | → |
| `macd_bearish_cross` | 61.5% | 4803 | → |
| `breakdown_30d` | 60.7% | 89 | → |
| `death_cross` | 59.6% | 265 | → |
| `bear_flag` | 56.3% | 483 | 📉 |
| `resistance_test` | 54.6% | 1193 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 37.2% | 2077 | → |
| `support_bounce` | 36.1% | 1935 | → |
| `bullish_engulfing_4h` | 33.0% | 770 | → |
| `squeeze_breakout` | 32.2% | 152 | → |
| `golden_cross` | 32.0% | 334 | → |
| `double_bottom_90d` | 31.9% | 1723 | → |
| `macd_bullish_cross` | 30.3% | 6200 | → |
| `hammer_4h` | 29.9% | 167 | → |
| `uptrend` | 29.5% | 6428 | → |
| `bull_flag` | 28.8% | 111 | → |
| `morning_star_4h` | 28.6% | 651 | → |
| `breakout_30d` | 16.5% | 212 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**42 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
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
| 22 août 2026 | **UNI** | 72% | 4.2 |
| 22 août 2026 | **ME** | 71% | 0.06818 |
| 22 août 2026 | **XAI** | 71% | 0.00782 |

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | BTC bull_prob | Top tokens |
|------|--------|---------------|-----------|
| 21 août 2026 | 🟢 Haussier | 57.0% | PROM, XPL |
| 22 août 2026 | 🟡 Neutre | 50.0% | PEOPLE, HIVE, UNI |
| 23 août 2026 | 🟡 Neutre | 46.0% | EUL, TUT, USDP |
| 24 août 2026 | 🔴 Baissier | 44.0% | TUT, COTI, EUL |

📉 **Le marché s'est dégradé** depuis le début du journal : BTC bull_prob 57.0% → 44.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 56.3% (24 août 2026) — -28.8% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 37.2% (24 août 2026) — +0.6% →
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 65.8% (24 août 2026) — -3.5% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 32.2% (24 août 2026) — +8.4% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 71.6% (24 août 2026) — -3.8% 📉

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

## Aujourd'hui — 24 août 2026

**Régime :** 🔴 Baissier (BTC bull_prob = 44%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **TUT** | 73% | +29pp | 0 | ⚡ Volume ×5.9 vs médiane |
| **COTI** | 71% | +27pp | 0 | ⚡ Volume ×3.8 vs médiane |
| **EUL** | 71% | +27pp | 0 |  |
| **ONG** | 70% | +26pp | 0 | ⚡ Volume ×6.0 vs médiane |
| **EURI** | 70% | +26pp | ⚠️ 4 | ⚡ Volume ×4.0 vs médiane |
