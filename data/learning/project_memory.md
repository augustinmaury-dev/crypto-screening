# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 29 sep 2026*

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

### Régime de marché : 🟡 Neutre

- **Indice altseason** : None sur 30 j, None sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 7.0 % sur 30 j · **Tokens au-dessus de leur MA50** : 87.1 %

### Mon modèle aujourd'hui : `ml_gb`

- Entraîné sur 56626 observations (135 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **48%** du temps (règle simple « grosses caps peu volatiles » : 47% ; hasard : 50 %)
- Confiance (calibration) : k = 0.20 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `macd_n` (−), `vol_30d_ann` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 8 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2640 prédictions mesurées — 47% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 60.9% | 3588 | 📉 |
| `downtrend` | 57.1% | 16365 | → |
| `bearish_engulfing_4h` | 54.3% | 915 | → |
| `breakdown_30d` | 53.1% | 128 | 📉 |
| `shooting_star_4h` | 52.8% | 305 | 📉 |
| `evening_star_4h` | 52.3% | 797 | 📉 |
| `rsi_bearish_divergence` | 51.5% | 1127 | 📉 |
| `death_cross` | 50.8% | 364 | → |
| `resistance_test` | 50.0% | 1834 | → |
| `macd_bearish_cross` | 48.8% | 7738 | 📉 |
| `bear_flag` | 47.9% | 599 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 54.5% | 396 | 📈 |
| `golden_cross` | 47.7% | 644 | 📈 |
| `uptrend` | 47.1% | 11017 | 📈 |
| `hammer_4h` | 46.1% | 297 | 📈 |
| `rsi_bullish_divergence` | 44.3% | 2477 | → |
| `bullish_engulfing_4h` | 44.2% | 1102 | 📈 |
| `bull_flag` | 44.0% | 293 | → |
| `support_bounce` | 43.0% | 2545 | → |
| `double_bottom_90d` | 43.0% | 2396 | → |
| `macd_bullish_cross` | 39.8% | 8198 | → |
| `morning_star_4h` | 38.0% | 888 | 📈 |
| `breakout_30d` | 34.9% | 418 | 📈 |

---

## Mes prédictions passées et leurs résultats

*Une prédiction = un des 20 tokens les mieux classés un jour donné. Jugée à 7 j et à 14 j. « Bat le marché » = a fait mieux que la médiane de tous les tokens sur la même période.*

| Mois | Modèle | Prédictions | Ont monté (7 j) | Ont battu le marché (7 j) | Return médian (7 j) |
|------|--------|-------------|-----------------|---------------------------|---------------------|
| 2026-05 | Ancienne formule | 480 | 32% | 61% | -4.4% |
| 2026-06 | Ancienne formule | 480 | 47% | 46% | -0.6% |
| 2026-07 | Ancienne formule | 620 | 43% | 54% | -1.0% |
| 2026-08 | Ancienne formule | 620 | 52% | 42% | +0.4% |
| 2026-09 | Ancienne formule | 440 | 62% | 45% | +3.1% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 22 sep 2026 | **ASTER** | 80% | 0.719 | +1.1% | ❌ -1.7pp | … |
| 22 sep 2026 | **FORM** | 80% | 0.3268 | -10.0% | ❌ -12.8pp | … |
| 22 sep 2026 | **PENGU** | 80% | 0.008946 | +11.0% | ✅ +8.1pp | … |
| 22 sep 2026 | **ICP** | 78% | 2.915 | +16.9% | ✅ +14.1pp | … |
| 22 sep 2026 | **MTL** | 78% | 0.306 | +7.7% | ✅ +4.8pp | … |
| 22 sep 2026 | **TST** | 77% | 0.01906 | -6.5% | ❌ -9.4pp | … |
| 22 sep 2026 | **XRP** | 77% | 1.5307 | +1.0% | ❌ -1.8pp | … |
| 22 sep 2026 | **COOKIE** | 76% | 0.0127 | -4.7% | ❌ -7.5pp | … |
| 22 sep 2026 | **CVC** | 76% | 0.02773 | +8.0% | ✅ +5.2pp | … |
| 22 sep 2026 | **ORCA** | 76% | 1.476 | +12.7% | ✅ +9.8pp | … |
| 22 sep 2026 | **ZEN** | 76% | 7.695 | -8.4% | ❌ -11.2pp | … |
| 22 sep 2026 | **AT** | 75% | 0.1576 | -5.5% | ❌ -8.3pp | … |
| 22 sep 2026 | **AVNT** | 75% | 0.1152 | +9.5% | ✅ +6.6pp | … |
| 22 sep 2026 | **PLTRB** | 75% | 184.35 | +1.5% | ❌ -1.4pp | … |
| 22 sep 2026 | **SHIB** | 75% | 5.91e-06 | -1.0% | ❌ -3.9pp | … |
| 22 sep 2026 | **VTHO** | 75% | 0.000699 | -0.3% | ❌ -3.1pp | … |
| 22 sep 2026 | **XEC** | 75% | 8.67e-06 | -1.5% | ❌ -4.4pp | … |
| 22 sep 2026 | **SUSHI** | 74% | 0.2487 | +6.8% | ✅ +3.9pp | … |
| 22 sep 2026 | **WIN** | 74% | 3.962e-05 | +19.8% | ✅ +17.0pp | … |
| 22 sep 2026 | **XVS** | 74% | 3.27 | +3.3% | ✅ +0.4pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 132 | -0.001 | 50% | 50% | 51% | 50% | 50% | 48% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 29 sep 2026 | 🟡 Neutre | — | +7.0% | MSTRB, NEXO, BNB |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 47.9% (29 sep 2026) — -37.2% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.3% (29 sep 2026) — +7.7% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 57.1% (29 sep 2026) — -12.2% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 54.5% (29 sep 2026) — +30.7% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 51.5% (29 sep 2026) — -23.9% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **41004 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0135 |
| momentum | 0.0312 |
| risk | 0.0143 |
| antiscam | 0.0000 |
| signal | 0.0089 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 29 sep 2026

**Régime :** 🟡 Neutre (indice altseason 30 j : None)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **MSTRB** | Speculative | 54.3% | +0.6pp | ⚠️ 5 |  |
| **NEXO** | Speculative | 54.0% | +0.3pp | ⚠️ 5 |  |
| **BNB** | Speculative | 53.9% | +0.2pp | ⚠️ 5 |  |
| **ETH** | Speculative | 53.9% | +0.2pp | ⚠️ 5 | 🔥 Trending #14 sur CoinGecko |
| **WBTC** | Speculative | 53.8% | +0.1pp | ⚠️ 4 |  |
| **BTC** | Speculative | 53.7% | +0.0pp | ⚠️ 7 | 🔥 Trending #8 sur CoinGecko |
| **LUNC** | Speculative | 53.5% | -0.2pp | 0 |  |
| **BNSOL** | Speculative | 53.4% | -0.3pp | ⚠️ 4 |  |
| **LPT** | Speculative | 53.2% | -0.5pp | 2 |  |
| **PEPE** | Speculative | 53.1% | -0.6pp | 0 |  |
| **TAO** | Speculative | 53.1% | -0.6pp | 2 |  |
| **FLOKI** | Speculative | 53.1% | -0.6pp | 0 |  |
