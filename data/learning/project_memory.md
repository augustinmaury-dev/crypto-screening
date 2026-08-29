# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 29 août 2026*

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
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 41.3%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 70.3% | 2686 | → |
| `rsi_bearish_divergence` | 69.5% | 554 | → |
| `shooting_star_4h` | 65.5% | 206 | → |
| `downtrend` | 62.5% | 13914 | → |
| `bearish_engulfing_4h` | 62.4% | 631 | → |
| `evening_star_4h` | 59.7% | 596 | → |
| `death_cross` | 59.0% | 268 | → |
| `macd_bearish_cross` | 58.6% | 5114 | → |
| `breakdown_30d` | 56.9% | 102 | → |
| `resistance_test` | 54.5% | 1256 | → |
| `bear_flag` | 50.0% | 552 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 41.3% | 2247 | → |
| `support_bounce` | 37.8% | 2041 | → |
| `double_bottom_90d` | 35.3% | 1825 | → |
| `bullish_engulfing_4h` | 35.1% | 804 | → |
| `squeeze_breakout` | 34.7% | 170 | → |
| `golden_cross` | 33.4% | 353 | → |
| `macd_bullish_cross` | 32.1% | 6435 | → |
| `uptrend` | 31.6% | 6698 | → |
| `hammer_4h` | 31.2% | 170 | → |
| `bull_flag` | 30.8% | 120 | → |
| `morning_star_4h` | 29.1% | 670 | → |
| `breakout_30d` | 17.5% | 217 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**129 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 29 août 2026 | **MASK** | 79% | 0.433 |
| 29 août 2026 | **ARPA** | 78% | 0.00949 |
| 29 août 2026 | **GNO** | 76% | 117.09 |
| 29 août 2026 | **BMT** | 76% | 0.02302 |
| 29 août 2026 | **ENSO** | 75% | 0.889 |
| 29 août 2026 | **AI** | 75% | 0.019 |
| 29 août 2026 | **TURBO** | 74% | 0.001024 |
| 29 août 2026 | **ONT** | 74% | 0.05783 |
| 29 août 2026 | **TUT** | 72% | 0.03794 |
| 29 août 2026 | **COTI** | 71% | 0.01342 |
| 29 août 2026 | **AMP** | 70% | 0.00045 |
| 29 août 2026 | **HUMA** | 70% | 0.02037 |
| 29 août 2026 | **EURI** | 74% | 1.1574 |
| 28 août 2026 | **SOL** | 76% | 103.38 |
| 28 août 2026 | **MORPHO** | 76% | 2.426 |

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

→ **Régime stable** : BTC bull_prob entre 57.0% et 55.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 50.0% (29 août 2026) — -35.1% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 41.3% (29 août 2026) — +4.7% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 62.5% (29 août 2026) — -6.8% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 34.7% (29 août 2026) — +10.9% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 69.5% (29 août 2026) — -5.9% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **30406 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0030 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 29 août 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 55%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **MASK** | 79% | +24pp | 2 | ⚡ Volume ×4.8 vs médiane |
| **ARPA** | 78% | +23pp | 0 | ⚡ Volume ×3.2 vs médiane |
| **GNO** | 76% | +21pp | 0 |  |
| **BMT** | 76% | +21pp | 0 | ⚡ Volume ×249.5 vs médiane |
| **ENSO** | 75% | +20pp | 0 | ⚡ Volume ×8.4 vs médiane |
| **AI** | 75% | +20pp | 0 | ⚡ Volume ×4.2 vs médiane |
| **TURBO** | 74% | +19pp | 0 | ⚡ Volume ×3.8 vs médiane |
| **ONT** | 74% | +19pp | 0 | ⚡ Volume ×8.5 vs médiane |
| **EURI** | 74% | +19pp | ⚠️ 5 | ⚡ Volume ×4.9 vs médiane |
| **TUT** | 72% | +17pp | 1 | ⚡ Volume ×5.1 vs médiane |
| **COTI** | 71% | +16pp | 0 | ⚡ Volume ×13.7 vs médiane |
| **AMP** | 70% | +15pp | 0 |  |
