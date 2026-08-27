# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 27 août 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🔴 Baissier — 42%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 39.2%
**Signaux baissiers fiables (>50%) :** 11 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 71.4% | 2640 | → |
| `rsi_bearish_divergence` | 70.3% | 545 | → |
| `shooting_star_4h` | 66.5% | 203 | → |
| `downtrend` | 63.7% | 13574 | → |
| `bearish_engulfing_4h` | 63.5% | 613 | → |
| `evening_star_4h` | 60.8% | 584 | → |
| `macd_bearish_cross` | 60.5% | 4909 | → |
| `death_cross` | 59.6% | 265 | → |
| `breakdown_30d` | 57.4% | 101 | 📉 |
| `resistance_test` | 54.4% | 1229 | → |
| `bear_flag` | 51.4% | 533 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 39.2% | 2160 | → |
| `support_bounce` | 36.9% | 1984 | → |
| `double_bottom_90d` | 34.4% | 1795 | → |
| `bullish_engulfing_4h` | 33.5% | 780 | → |
| `golden_cross` | 32.9% | 346 | → |
| `squeeze_breakout` | 32.5% | 160 | → |
| `macd_bullish_cross` | 31.9% | 6381 | → |
| `uptrend` | 30.9% | 6601 | → |
| `hammer_4h` | 30.8% | 169 | → |
| `bull_flag` | 29.6% | 115 | → |
| `morning_star_4h` | 28.9% | 658 | → |
| `breakout_30d` | 16.8% | 214 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**76 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 27 août 2026 | **WAXP** | 75% | 0.00426 |
| 27 août 2026 | **TRX** | 74% | 0.3379 |
| 27 août 2026 | **ALT** | 74% | 0.00656 |
| 27 août 2026 | **RARE** | 74% | 0.01326 |
| 27 août 2026 | **MORPHO** | 73% | 2.586 |
| 27 août 2026 | **GMX** | 73% | 7.76 |
| 27 août 2026 | **HEMI** | 73% | 0.00881 |
| 27 août 2026 | **OGN** | 73% | 0.01873 |
| 27 août 2026 | **EUL** | 72% | 1.438 |
| 27 août 2026 | **LSK** | 72% | 0.0973 |
| 27 août 2026 | **XVS** | 71% | 3.19 |
| 27 août 2026 | **EDEN** | 71% | 0.0599 |
| 27 août 2026 | **VELODROME** | 71% | 0.02269 |
| 27 août 2026 | **HAEDAL** | 71% | 0.01939 |
| 27 août 2026 | **SUI** | 70% | 0.7806 |

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

📉 **Le marché s'est dégradé** depuis le début du journal : BTC bull_prob 57.0% → 42.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 51.4% (27 août 2026) — -33.7% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 39.2% (27 août 2026) — +2.6% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 63.7% (27 août 2026) — -5.6% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 32.5% (27 août 2026) — +8.7% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 70.3% (27 août 2026) — -5.1% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers sont **bloqués** sous 40% : je ne suis pas encore fiable pour détecter les hausses.

---

## Le score composite est-il utile ?

J'ai analysé **29737 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0006 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 27 août 2026

**Régime :** 🔴 Baissier (BTC bull_prob = 42%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **WAXP** | 75% | +33pp | 0 | ⚡ Volume ×5.6 vs médiane |
| **TRX** | 74% | +32pp | 2 |  |
| **ALT** | 74% | +32pp | 0 |  |
| **RARE** | 74% | +32pp | 0 |  |
| **BFUSD** | 74% | +32pp | 2 |  |
| **MORPHO** | 73% | +31pp | 0 |  |
| **GMX** | 73% | +31pp | 2 |  |
| **HEMI** | 73% | +31pp | 0 | ⚡ Volume ×5.9 vs médiane |
| **OGN** | 73% | +31pp | 0 |  |
| **EUL** | 72% | +30pp | 0 |  |
| **LSK** | 72% | +30pp | 0 |  |
| **FRAX** | 72% | +30pp | 0 |  |
