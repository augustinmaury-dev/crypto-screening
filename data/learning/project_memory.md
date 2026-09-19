# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 19 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 60%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 45.7%
**Signaux baissiers fiables (>50%) :** 10 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 65.0% | 3319 | → |
| `rsi_bearish_divergence` | 60.2% | 896 | 📉 |
| `downtrend` | 58.1% | 15953 | → |
| `bearish_engulfing_4h` | 56.6% | 870 | → |
| `evening_star_4h` | 56.4% | 732 | → |
| `breakdown_30d` | 56.3% | 119 | → |
| `shooting_star_4h` | 55.4% | 280 | → |
| `macd_bearish_cross` | 55.0% | 6741 | → |
| `resistance_test` | 52.5% | 1629 | → |
| `death_cross` | 52.4% | 349 | → |
| `bear_flag` | 49.0% | 575 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 45.7% | 291 | → |
| `rsi_bullish_divergence` | 43.6% | 2431 | → |
| `golden_cross` | 43.4% | 535 | → |
| `bull_flag` | 42.3% | 260 | → |
| `hammer_4h` | 42.2% | 263 | → |
| `support_bounce` | 41.7% | 2406 | → |
| `bullish_engulfing_4h` | 40.9% | 1000 | → |
| `double_bottom_90d` | 40.6% | 2272 | → |
| `uptrend` | 38.5% | 9066 | → |
| `macd_bullish_cross` | 37.0% | 7522 | → |
| `morning_star_4h` | 33.1% | 807 | → |
| `breakout_30d` | 30.1% | 359 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**300 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 19 sep 2026 | **ESP** | 80% | 0.09691 |
| 19 sep 2026 | **SLP** | 80% | 0.000667 |
| 19 sep 2026 | **C98** | 78% | 0.01612 |
| 19 sep 2026 | **ASTER** | 76% | 0.768 |
| 19 sep 2026 | **A** | 76% | 0.0898 |
| 19 sep 2026 | **SSV** | 76% | 3.206 |
| 19 sep 2026 | **LSK** | 75% | 0.4424 |
| 19 sep 2026 | **LUNA** | 75% | 0.048 |
| 19 sep 2026 | **PROVE** | 74% | 0.2162 |
| 19 sep 2026 | **STEEM** | 74% | 0.05652 |
| 19 sep 2026 | **USUAL** | 74% | 0.01276 |
| 19 sep 2026 | **CVC** | 74% | 0.02732 |
| 19 sep 2026 | **MTL** | 74% | 0.295 |
| 19 sep 2026 | **AVAX** | 73% | 9.313 |
| 19 sep 2026 | **SKY** | 73% | 0.06958 |

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
| 16 sep 2026 | 🟢 Haussier | 67.0% | ASTR, POL, HIVE |
| 17 sep 2026 | 🟢 Haussier | 67.0% | A, ASTR, BNSOL |
| 18 sep 2026 | 🟢 Haussier | 70.0% | ROSE, ENSO, LSK |
| 19 sep 2026 | 🟢 Haussier | 60.0% | ESP, SLP, C98 |

→ **Régime stable** : BTC bull_prob entre 57.0% et 60.0%

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 49.0% (19 sep 2026) — -36.1% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.6% (19 sep 2026) — +7.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.1% (19 sep 2026) — -11.2% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 45.7% (19 sep 2026) — +21.9% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 60.2% (19 sep 2026) — -15.2% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **37426 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0087 |
| momentum | 0.0000 |
| risk | 0.0051 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 19 sep 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 60%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **ESP** | 80% | +20pp | 3 | ⚡ Volume ×6.5 vs médiane |
| **SLP** | 80% | +20pp | 3 |  |
| **C98** | 78% | +18pp | 2 |  |
| **ASTER** | 76% | +16pp | 2 |  |
| **A** | 76% | +16pp | 2 | ⚡ Volume ×11.5 vs médiane |
| **SSV** | 76% | +16pp | 2 |  |
| **LSK** | 75% | +15pp | 0 | ⚡ Volume ×9.2 vs médiane |
| **LUNA** | 75% | +15pp | 0 |  |
| **PROVE** | 74% | +14pp | 2 | ⚡ Volume ×104.0 vs médiane |
| **STEEM** | 74% | +14pp | 0 |  |
| **USUAL** | 74% | +14pp | 2 |  |
| **CVC** | 74% | +14pp | 0 |  |
