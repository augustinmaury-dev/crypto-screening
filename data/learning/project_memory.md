# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 28 sep 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.).
Depuis le 26/09/2026, mon `score` est la **probabilité qu'un token fasse mieux que la médiane du marché sur 7 jours**,
calculée par un modèle réentraîné chaque jour sur toutes mes prédictions passées déjà mesurées (`06b_ml_score.py`).
Je surveille aussi le **régime de marché** (altseason ou saison Bitcoin), car ce qui marche change selon le régime.

---

## Mon auto-évaluation

### Régime de marché : 🌱 Altseason en formation

- **Indice altseason** : 82.0 sur 30 j, 59.2 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 6.7 % sur 30 j · **Tokens au-dessus de leur MA50** : 81.5 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 10).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 56162 observations (134 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **53%** du temps (règle simple « grosses caps peu volatiles » : 48% ; hasard : 50 %)
- Confiance (calibration) : k = 0.20 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `macd_n` (−), `bear_signals` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 9 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2620 prédictions mesurées — 47% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 61.4% | 3559 | 📉 |
| `downtrend` | 57.2% | 16307 | → |
| `bearish_engulfing_4h` | 54.4% | 913 | 📉 |
| `breakdown_30d` | 53.5% | 127 | 📉 |
| `shooting_star_4h` | 53.2% | 301 | 📉 |
| `evening_star_4h` | 52.3% | 797 | 📉 |
| `rsi_bearish_divergence` | 51.9% | 1116 | 📉 |
| `death_cross` | 50.8% | 362 | → |
| `resistance_test` | 50.1% | 1821 | → |
| `macd_bearish_cross` | 49.3% | 7645 | 📉 |
| `bear_flag` | 48.0% | 598 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 54.2% | 391 | 📈 |
| `golden_cross` | 47.2% | 633 | 📈 |
| `uptrend` | 46.5% | 10854 | 📈 |
| `hammer_4h` | 45.9% | 296 | 📈 |
| `rsi_bullish_divergence` | 44.1% | 2469 | → |
| `bull_flag` | 44.0% | 293 | → |
| `bullish_engulfing_4h` | 43.8% | 1095 | 📈 |
| `support_bounce` | 42.9% | 2538 | → |
| `double_bottom_90d` | 42.8% | 2388 | → |
| `macd_bullish_cross` | 39.6% | 8167 | → |
| `morning_star_4h` | 36.4% | 867 | → |
| `breakout_30d` | 34.6% | 416 | 📈 |

---

## Mes prédictions passées et leurs résultats

*Une prédiction = un des 20 tokens les mieux classés un jour donné. Jugée à 7 j et à 14 j. « Bat le marché » = a fait mieux que la médiane de tous les tokens sur la même période.*

| Mois | Modèle | Prédictions | Ont monté (7 j) | Ont battu le marché (7 j) | Return médian (7 j) |
|------|--------|-------------|-----------------|---------------------------|---------------------|
| 2026-05 | Ancienne formule | 480 | 32% | 61% | -4.4% |
| 2026-06 | Ancienne formule | 480 | 47% | 46% | -0.6% |
| 2026-07 | Ancienne formule | 620 | 43% | 54% | -1.0% |
| 2026-08 | Ancienne formule | 620 | 52% | 42% | +0.4% |
| 2026-09 | Ancienne formule | 420 | 62% | 45% | +3.2% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 21 sep 2026 | **ASTER** | 80% | 0.754 | -8.2% | ❌ -7.7pp | … |
| 21 sep 2026 | **FLOW** | 80% | 0.03223 | -7.5% | ❌ -7.0pp | … |
| 21 sep 2026 | **NMR** | 80% | 9.39 | +21.6% | ✅ +22.1pp | … |
| 21 sep 2026 | **WBETH** | 80% | 3024.99 | -2.6% | ❌ -2.1pp | … |
| 21 sep 2026 | **EGLD** | 77% | 4.306 | +2.0% | ✅ +2.5pp | … |
| 21 sep 2026 | **FORM** | 77% | 0.2664 | +7.5% | ✅ +8.0pp | … |
| 21 sep 2026 | **MASK** | 77% | 0.486 | -7.4% | ❌ -6.9pp | … |
| 21 sep 2026 | **XVG** | 77% | 0.003113 | +0.0% | ✅ +0.5pp | … |
| 21 sep 2026 | **AI** | 76% | 0.0185 | +0.0% | ✅ +0.5pp | … |
| 21 sep 2026 | **BNT** | 76% | 0.3355 | +2.3% | ✅ +2.8pp | … |
| 21 sep 2026 | **CAKE** | 76% | 2.531 | +2.7% | ✅ +3.2pp | … |
| 21 sep 2026 | **TRB** | 76% | 19.06 | -2.0% | ❌ -1.5pp | … |
| 21 sep 2026 | **CETUS** | 75% | 0.02757 | +0.8% | ✅ +1.3pp | … |
| 21 sep 2026 | **ENSO** | 75% | 1.021 | -5.1% | ❌ -4.6pp | … |
| 21 sep 2026 | **KERNEL** | 75% | 0.0475 | +6.5% | ✅ +7.0pp | … |
| 21 sep 2026 | **LQTY** | 75% | 0.2291 | +1.1% | ✅ +1.6pp | … |
| 21 sep 2026 | **LSK** | 75% | 0.3921 | -20.6% | ❌ -20.1pp | … |
| 21 sep 2026 | **VTHO** | 75% | 0.000667 | +4.2% | ✅ +4.7pp | … |
| 21 sep 2026 | **XLM** | 75% | 0.2071 | +4.1% | ✅ +4.6pp | … |
| 21 sep 2026 | **XRP** | 74% | 1.4815 | -0.1% | ✅ +0.4pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 131 | -0.002 | 50% | 50% | 51% | 50% | 50% | 49% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
| 30 août 2026 | 🟢 Haussier | — | (bull_prob 55.0%) | ZK, BAND, DOLO |
| 31 août 2026 | 🟢 Haussier | — | (bull_prob 62.0%) | ZK, ENSO, BMT |
| 1 sep 2026 | 🟢 Haussier | — | (bull_prob 56.0%) | STRAX, NOT, SOMI |
| 2 sep 2026 | 🟢 Haussier | — | (bull_prob 67.0%) | ANKR, SOPH, TUSD |
| 3 sep 2026 | 🟢 Haussier | — | (bull_prob 56.0%) | PROM, RED, COMP |
| 4 sep 2026 | 🟡 Neutre | — | (bull_prob 51.0%) | HIVE, PROM, ZKP |
| 5 sep 2026 | 🟢 Haussier | — | (bull_prob 58.0%) | AIXBT, 1000CAT, ZKP |
| 6 sep 2026 | 🟡 Neutre | — | (bull_prob 54.0%) | XVS, WOO, T |
| 7 sep 2026 | 🟢 Haussier | — | (bull_prob 64.0%) | YGG, USTC, ILV |
| 8 sep 2026 | 🟢 Haussier | — | (bull_prob 69.0%) | ORCA, 1000CAT, UMA |
| 9 sep 2026 | 🟢 Haussier | — | (bull_prob 69.0%) | HOLO, ORCA, GLM |
| 10 sep 2026 | 🟢 Haussier | — | (bull_prob 69.0%) | BFUSD, GLM, NEWT |
| 11 sep 2026 | 🟢 Haussier | — | (bull_prob 69.0%) | MET, ORCA, THETA |
| 12 sep 2026 | 🟢 Haussier | — | (bull_prob 66.0%) | MET, THE, ORCA |
| 13 sep 2026 | 🟢 Haussier | — | (bull_prob 67.0%) | ILV, MET, GLM |
| 14 sep 2026 | 🟢 Haussier | — | (bull_prob 73.0%) | GLM, API3, THE |
| 15 sep 2026 | 🟢 Haussier | — | (bull_prob 76.0%) | AXL, AWE, GLM |
| 16 sep 2026 | 🟢 Haussier | — | (bull_prob 67.0%) | ASTR, POL, HIVE |
| 17 sep 2026 | 🟢 Haussier | — | (bull_prob 67.0%) | A, ASTR, BNSOL |
| 18 sep 2026 | 🟢 Haussier | — | (bull_prob 70.0%) | ROSE, ENSO, LSK |
| 19 sep 2026 | 🟢 Haussier | — | (bull_prob 60.0%) | ESP, SLP, C98 |
| 20 sep 2026 | 🟢 Haussier | — | (bull_prob 66.0%) | KMNO, HOT, JOE |
| 21 sep 2026 | 🟢 Haussier | — | (bull_prob 67.0%) | ASTER, FLOW, NMR |
| 22 sep 2026 | 🟢 Haussier | — | (bull_prob 64.0%) | ASTER, PENGU, FORM |
| 23 sep 2026 | 🟢 Haussier | — | (bull_prob 65.0%) | PENGU, BROCCOLI714, WIN |
| 24 sep 2026 | 🟢 Haussier | — | (bull_prob 67.0%) | ONDO, COMP, AI |
| 25 sep 2026 | 🟢 Haussier | — | (bull_prob 65.0%) | IQ, ONDO, EIGEN |
| 26 sep 2026 | 🌱 Altseason en formation | 83 | +4.7% | RENDER, ENS, LINK |
| 27 sep 2026 | 🌱 Altseason en formation | 87 | +9.4% | LINK, SOL, TAO |
| 28 sep 2026 | 🌱 Altseason en formation | 82 | +6.7% | SOL, LINK, TAO |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.0% (28 sep 2026) — -37.1% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.1% (28 sep 2026) — +7.5% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 57.2% (28 sep 2026) — -12.1% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 54.2% (28 sep 2026) — +30.4% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 51.9% (28 sep 2026) — -23.5% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **40679 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0127 |
| momentum | 0.0280 |
| risk | 0.0137 |
| antiscam | 0.0000 |
| signal | 0.0053 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 28 sep 2026

**Régime :** 🌱 Altseason en formation (indice altseason 30 j : 82.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **SOL** | Etabli | 54.5% | +1.9pp | 2 |  |
| **LINK** | Etabli | 53.9% | +1.3pp | ⚠️ 4 | 🔥 Trending #6 sur CoinGecko |
| **TAO** | Etabli | 53.9% | +1.3pp | 0 |  |
| **XLM** | Etabli | 53.7% | +1.1pp | ⚠️ 4 |  |
| **ADA** | Etabli | 53.5% | +0.9pp | 0 |  |
| **KAIA** | Mid | 53.3% | +0.7pp | 0 |  |
| **ETH** | Etabli | 53.2% | +0.6pp | ⚠️ 5 |  |
| **BNSOL** | Speculative | 53.2% | +0.6pp | ⚠️ 4 |  |
| **XRP** | Etabli | 53.1% | +0.5pp | 0 |  |
| **VET** | Etabli | 53.1% | +0.5pp | 3 |  |
| **ENS** | Mid | 53.0% | +0.4pp | 0 |  |
| **ENJ** | Mid | 52.9% | +0.3pp | 0 |  |
