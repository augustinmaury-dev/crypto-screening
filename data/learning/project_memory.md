# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 27 sep 2026*

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

- **Indice altseason** : 87.0 sur 30 j, 62.2 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 9.4 % sur 30 j · **Tokens au-dessus de leur MA50** : 91.6 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 9).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 55698 observations (133 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **53%** du temps (règle simple « grosses caps peu volatiles » : 49% ; hasard : 50 %)
- Confiance (calibration) : k = 0.20 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `macd_n` (−), `bear_signals` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 10 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2600 prédictions mesurées — 47% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 61.8% | 3536 | 📉 |
| `downtrend` | 57.4% | 16255 | → |
| `bearish_engulfing_4h` | 54.6% | 906 | → |
| `breakdown_30d` | 54.4% | 125 | → |
| `shooting_star_4h` | 53.0% | 300 | 📉 |
| `evening_star_4h` | 52.9% | 788 | 📉 |
| `rsi_bearish_divergence` | 52.4% | 1096 | 📉 |
| `death_cross` | 51.1% | 358 | → |
| `macd_bearish_cross` | 50.2% | 7488 | 📉 |
| `resistance_test` | 50.1% | 1802 | 📉 |
| `bear_flag` | 48.0% | 598 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 53.3% | 381 | 📈 |
| `golden_cross` | 47.0% | 623 | 📈 |
| `uptrend` | 45.8% | 10691 | 📈 |
| `hammer_4h` | 44.8% | 288 | 📈 |
| `bull_flag` | 44.0% | 293 | → |
| `rsi_bullish_divergence` | 43.9% | 2460 | → |
| `bullish_engulfing_4h` | 43.4% | 1085 | 📈 |
| `support_bounce` | 42.8% | 2524 | → |
| `double_bottom_90d` | 42.6% | 2377 | → |
| `macd_bullish_cross` | 39.5% | 8148 | 📈 |
| `morning_star_4h` | 36.2% | 862 | 📈 |
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
| 2026-09 | Ancienne formule | 400 | 62% | 44% | +3.5% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 20 sep 2026 | **BAR** | 80% | 0.281 | +1.1% | ❌ -12.0pp | … |
| 20 sep 2026 | **HOT** | 80% | 0.000396 | +17.9% | ✅ +4.8pp | … |
| 20 sep 2026 | **JOE** | 80% | 0.0326 | +24.9% | ✅ +11.8pp | … |
| 20 sep 2026 | **KMNO** | 80% | 0.0276 | +68.3% | ✅ +55.2pp | … |
| 20 sep 2026 | **MAGIC** | 80% | 0.0467 | +12.0% | ❌ -1.1pp | … |
| 20 sep 2026 | **RLC** | 80% | 0.3042 | +18.6% | ✅ +5.6pp | … |
| 20 sep 2026 | **ASTER** | 78% | 0.736 | +0.1% | ❌ -13.0pp | … |
| 20 sep 2026 | **GAS** | 78% | 1.323 | +14.1% | ✅ +1.1pp | … |
| 20 sep 2026 | **IOTX** | 78% | 0.003281 | +10.2% | ❌ -2.9pp | … |
| 20 sep 2026 | **USUAL** | 77% | 0.01272 | +18.6% | ✅ +5.5pp | … |
| 20 sep 2026 | **ARK** | 76% | 0.1503 | +68.8% | ✅ +55.7pp | … |
| 20 sep 2026 | **PROVE** | 76% | 0.2262 | +5.7% | ❌ -7.4pp | … |
| 20 sep 2026 | **SUSHI** | 76% | 0.2409 | +12.4% | ❌ -0.7pp | … |
| 20 sep 2026 | **BNT** | 75% | 0.3169 | +11.6% | ❌ -1.5pp | … |
| 20 sep 2026 | **F** | 75% | 0.003636 | +4.7% | ❌ -8.4pp | … |
| 20 sep 2026 | **G** | 75% | 0.00722 | -23.1% | ❌ -36.2pp | … |
| 20 sep 2026 | **LSK** | 75% | 0.3761 | -10.9% | ❌ -24.0pp | … |
| 20 sep 2026 | **AGLD** | 74% | 0.1952 | +12.6% | ❌ -0.5pp | … |
| 20 sep 2026 | **MTL** | 74% | 0.3 | +13.6% | ✅ +0.6pp | … |
| 20 sep 2026 | **ZEC** | 74% | 1445.05 | +15.3% | ✅ +2.2pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 130 | -0.002 | 50% | 50% | 51% | 50% | 50% | 49% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
| 29 août 2026 | 🟢 Haussier | — | (bull_prob 55.0%) | MASK, ARPA, GNO |
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

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.0% (27 sep 2026) — -37.1% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.9% (27 sep 2026) — +7.3% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 57.4% (27 sep 2026) — -11.9% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 53.3% (27 sep 2026) — +29.5% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 52.4% (27 sep 2026) — -23.0% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **40316 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0118 |
| momentum | 0.0252 |
| risk | 0.0134 |
| antiscam | 0.0000 |
| signal | 0.0030 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 27 sep 2026

**Régime :** 🌱 Altseason en formation (indice altseason 30 j : 87.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **LINK** | Etabli | 56.6% | +4.4pp | ⚠️ 4 |  |
| **SOL** | Etabli | 56.1% | +3.9pp | 2 |  |
| **TAO** | Etabli | 55.7% | +3.5pp | ⚠️ 4 | 🔥 Trending #12 sur CoinGecko |
| **BNSOL** | Speculative | 55.2% | +3.0pp | 2 |  |
| **WIF** | Mid | 55.1% | +2.9pp | ⚠️ 4 |  |
| **ENS** | Mid | 55.1% | +2.9pp | ⚠️ 4 |  |
| **AAVE** | Etabli | 55.0% | +2.8pp | ⚠️ 4 |  |
| **KAIA** | Mid | 54.6% | +2.4pp | ⚠️ 4 |  |
| **WOO** | Speculative | 54.5% | +2.3pp | 2 |  |
| **ETC** | Etabli | 54.4% | +2.2pp | ⚠️ 4 |  |
| **NEO** | Mid | 53.8% | +1.6pp | 2 |  |
| **ADA** | Etabli | 53.8% | +1.6pp | ⚠️ 4 |  |
