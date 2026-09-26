# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 26 sep 2026*

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

- **Indice altseason** : 83.0 sur 30 j, 64.3 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 4.7 % sur 30 j · **Tokens au-dessus de leur MA50** : 91.4 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 8).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 55234 observations (132 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **50%** du temps (règle simple « grosses caps peu volatiles » : 49% ; hasard : 50 %)
- Confiance (calibration) : k = 0.20 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `bear_signals` (−), `vol_30d_ann` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 10 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2580 prédictions mesurées — 46% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 62.2% | 3511 | 📉 |
| `downtrend` | 57.5% | 16213 | → |
| `bearish_engulfing_4h` | 54.7% | 905 | → |
| `breakdown_30d` | 54.4% | 125 | → |
| `shooting_star_4h` | 53.4% | 298 | 📉 |
| `rsi_bearish_divergence` | 53.1% | 1075 | 📉 |
| `evening_star_4h` | 53.0% | 787 | 📉 |
| `death_cross` | 51.4% | 356 | → |
| `macd_bearish_cross` | 51.3% | 7316 | 📉 |
| `resistance_test` | 50.3% | 1781 | 📉 |
| `bear_flag` | 48.0% | 598 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 51.0% | 363 | 📈 |
| `golden_cross` | 46.6% | 612 | 📈 |
| `uptrend` | 45.1% | 10519 | 📈 |
| `hammer_4h` | 44.6% | 285 | 📈 |
| `bull_flag` | 44.0% | 293 | → |
| `rsi_bullish_divergence` | 43.9% | 2455 | → |
| `bullish_engulfing_4h` | 42.7% | 1072 | → |
| `support_bounce` | 42.5% | 2500 | → |
| `double_bottom_90d` | 42.3% | 2364 | → |
| `macd_bullish_cross` | 39.4% | 8130 | 📈 |
| `morning_star_4h` | 35.7% | 854 | 📈 |
| `breakout_30d` | 33.3% | 399 | 📈 |

---

## Mes prédictions passées et leurs résultats

*Une prédiction = un des 20 tokens les mieux classés un jour donné. Jugée à 7 j et à 14 j. « Bat le marché » = a fait mieux que la médiane de tous les tokens sur la même période.*

| Mois | Modèle | Prédictions | Ont monté (7 j) | Ont battu le marché (7 j) | Return médian (7 j) |
|------|--------|-------------|-----------------|---------------------------|---------------------|
| 2026-05 | Ancienne formule | 480 | 32% | 61% | -4.4% |
| 2026-06 | Ancienne formule | 480 | 47% | 46% | -0.6% |
| 2026-07 | Ancienne formule | 620 | 43% | 54% | -1.0% |
| 2026-08 | Ancienne formule | 620 | 52% | 42% | +0.4% |
| 2026-09 | Ancienne formule | 380 | 61% | 44% | +3.1% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 19 sep 2026 | **ESP** | 80% | 0.09691 | +4.4% | ❌ -5.6pp | … |
| 19 sep 2026 | **SLP** | 80% | 0.000667 | +7.2% | ❌ -2.8pp | … |
| 19 sep 2026 | **C98** | 78% | 0.01612 | +0.2% | ❌ -9.8pp | … |
| 19 sep 2026 | **ASTER** | 76% | 0.768 | -4.8% | ❌ -14.8pp | … |
| 19 sep 2026 | **A** | 76% | 0.0898 | +13.7% | ✅ +3.7pp | … |
| 19 sep 2026 | **SSV** | 76% | 3.206 | +0.4% | ❌ -9.6pp | … |
| 19 sep 2026 | **LSK** | 75% | 0.4424 | -23.3% | ❌ -33.3pp | … |
| 19 sep 2026 | **LUNA** | 75% | 0.048 | +12.7% | ✅ +2.7pp | … |
| 19 sep 2026 | **CVC** | 74% | 0.02732 | +14.5% | ✅ +4.5pp | … |
| 19 sep 2026 | **MTL** | 74% | 0.295 | +19.4% | ✅ +9.4pp | … |
| 19 sep 2026 | **PROVE** | 74% | 0.2162 | +13.0% | ✅ +3.0pp | … |
| 19 sep 2026 | **STEEM** | 74% | 0.05652 | +20.0% | ✅ +10.0pp | … |
| 19 sep 2026 | **USUAL** | 74% | 0.01276 | +14.7% | ✅ +4.6pp | … |
| 19 sep 2026 | **ASTR** | 73% | 0.006763 | +11.9% | ✅ +1.9pp | … |
| 19 sep 2026 | **AVAX** | 73% | 9.313 | +17.6% | ✅ +7.6pp | … |
| 19 sep 2026 | **BANANA** | 73% | 4.059 | +5.8% | ❌ -4.2pp | … |
| 19 sep 2026 | **IMX** | 73% | 0.14 | +18.6% | ✅ +8.5pp | … |
| 19 sep 2026 | **ORCA** | 73% | 1.457 | +13.2% | ✅ +3.2pp | … |
| 19 sep 2026 | **SKY** | 73% | 0.06958 | +12.4% | ✅ +2.4pp | … |
| 19 sep 2026 | **TRUMP** | 72% | 2.051 | +4.9% | ❌ -5.1pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 129 | -0.002 | 50% | 50% | 51% | 50% | 50% | 49% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
| 28 août 2026 | 🟢 Haussier | — | (bull_prob 70.0%) | SOL, MORPHO, GMX |
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

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.0% (26 sep 2026) — -37.1% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.9% (26 sep 2026) — +7.3% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 57.5% (26 sep 2026) — -11.8% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 51.0% (26 sep 2026) — +27.2% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 53.1% (26 sep 2026) — -22.3% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **39956 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0107 |
| momentum | 0.0202 |
| risk | 0.0126 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 26 sep 2026

**Régime :** 🌱 Altseason en formation (indice altseason 30 j : 83.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **RENDER** | Etabli | 57.0% | +4.7pp | ⚠️ 6 |  |
| **ENS** | Mid | 55.9% | +3.6pp | ⚠️ 4 |  |
| **LINK** | Etabli | 55.8% | +3.5pp | 2 |  |
| **WIF** | Mid | 55.6% | +3.3pp | ⚠️ 4 |  |
| **SOL** | Etabli | 55.4% | +3.1pp | ⚠️ 4 |  |
| **BNSOL** | Speculative | 55.2% | +2.9pp | ⚠️ 4 |  |
| **KAIA** | Mid | 55.2% | +2.9pp | ⚠️ 4 |  |
| **AXL** | Mid | 55.1% | +2.8pp | 2 |  |
| **ETC** | Etabli | 54.9% | +2.6pp | ⚠️ 4 |  |
| **PEPE** | Etabli | 54.6% | +2.3pp | 2 |  |
| **HBAR** | Etabli | 54.5% | +2.2pp | 2 |  |
| **WOO** | Speculative | 54.0% | +1.7pp | ⚠️ 4 |  |
