# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 1 oct 2026*

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

- **Indice altseason** : 83.0 sur 30 j, 59.2 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 7.2 % sur 30 j · **Tokens au-dessus de leur MA50** : 89.3 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 13).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 54533 observations (137 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **52%** du temps (règle simple « grosses caps peu volatiles » : 46% ; hasard : 50 %)
- Confiance (calibration) : k = 0.40 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 71 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `log_rank` (−), `macd_n` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 9 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2701 prédictions mesurées — 47% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 59.8% | 3653 | 📉 |
| `downtrend` | 56.7% | 16493 | → |
| `bearish_engulfing_4h` | 52.9% | 940 | 📉 |
| `breakdown_30d` | 52.7% | 129 | 📉 |
| `shooting_star_4h` | 52.6% | 308 | → |
| `evening_star_4h` | 51.8% | 805 | 📉 |
| `rsi_bearish_divergence` | 51.2% | 1147 | 📉 |
| `death_cross` | 50.5% | 372 | → |
| `resistance_test` | 50.1% | 1860 | → |
| `bear_flag` | 47.9% | 599 | → |
| `macd_bearish_cross` | 47.9% | 7909 | 📉 |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 54.5% | 398 | 📈 |
| `uptrend` | 48.6% | 11348 | 📈 |
| `golden_cross` | 48.0% | 663 | 📈 |
| `hammer_4h` | 46.3% | 298 | 📈 |
| `bullish_engulfing_4h` | 44.8% | 1115 | 📈 |
| `rsi_bullish_divergence` | 44.6% | 2493 | → |
| `bull_flag` | 44.0% | 293 | → |
| `support_bounce` | 43.3% | 2584 | → |
| `double_bottom_90d` | 43.1% | 2402 | → |
| `macd_bullish_cross` | 40.0% | 8236 | → |
| `morning_star_4h` | 38.5% | 897 | 📈 |
| `breakout_30d` | 34.8% | 422 | 📈 |

---

## Mes prédictions passées et leurs résultats

*Une prédiction = un des 20 tokens les mieux classés un jour donné. Jugée à 7 j et à 14 j. « Bat le marché » = a fait mieux que la médiane de tous les tokens sur la même période.*

| Mois | Modèle | Prédictions | Ont monté (7 j) | Ont battu le marché (7 j) | Return médian (7 j) |
|------|--------|-------------|-----------------|---------------------------|---------------------|
| 2026-05 | Ancienne formule | 481 | 32% | 61% | -4.3% |
| 2026-06 | Ancienne formule | 480 | 47% | 46% | -0.6% |
| 2026-07 | Ancienne formule | 621 | 43% | 54% | -1.0% |
| 2026-08 | Ancienne formule | 630 | 53% | 42% | +0.4% |
| 2026-09 | Ancienne formule | 489 | 62% | 47% | +3.0% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 24 sep 2026 | **COMP** | 80% | 23.03 | +3.6% | ✅ +1.7pp | … |
| 24 sep 2026 | **ONDO** | 80% | 0.4551 | +8.8% | ✅ +6.9pp | … |
| 24 sep 2026 | **AI** | 79% | 0.0196 | -4.1% | ❌ -6.0pp | … |
| 24 sep 2026 | **BTTC** | 78% | 3.7e-07 | +2.7% | ✅ +0.8pp | … |
| 24 sep 2026 | **AUCTION** | 76% | 3.716 | -1.8% | ❌ -3.7pp | … |
| 24 sep 2026 | **BOME** | 76% | 0.0010523 | -7.9% | ❌ -9.8pp | … |
| 24 sep 2026 | **ICP** | 76% | 2.977 | +10.1% | ✅ +8.2pp | … |
| 24 sep 2026 | **QTUM** | 76% | 0.958 | +1.8% | ❌ -0.1pp | … |
| 24 sep 2026 | **ZEC** | 76% | 1482.5 | -6.0% | ❌ -7.9pp | … |
| 24 sep 2026 | **NMR** | 75% | 9.31 | +21.4% | ✅ +19.5pp | … |
| 24 sep 2026 | **ORCA** | 75% | 1.54 | +5.7% | ✅ +3.7pp | … |
| 24 sep 2026 | **TST** | 75% | 0.01971 | -11.2% | ❌ -13.1pp | … |
| 24 sep 2026 | **XRP** | 75% | 1.4724 | +0.7% | ❌ -1.2pp | … |
| 24 sep 2026 | **XVS** | 75% | 3.231 | +8.8% | ✅ +6.9pp | … |
| 24 sep 2026 | **MTL** | 74% | 0.3231 | -2.6% | ❌ -4.5pp | … |
| 24 sep 2026 | **1000CAT** | 73% | 0.002269 | -1.8% | ❌ -3.7pp | … |
| 24 sep 2026 | **CVC** | 73% | 0.03134 | -2.4% | ❌ -4.3pp | … |
| 24 sep 2026 | **LSK** | 73% | 0.3987 | -30.5% | ❌ -32.4pp | … |
| 24 sep 2026 | **MUBARAK** | 73% | 0.04729 | +29.0% | ✅ +27.1pp | … |
| 24 sep 2026 | **NVDAB** | 73% | 223.37 | +3.1% | ✅ +1.2pp | … |

**171 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 796 | 49% | 25% (hasard : 10 %) | +5.8 pts | -0.2 pts |
| Altseason (indice 30 j ≥ 60) | 41 | 66% | 24% (hasard : 10 %) | +22.5 pts | +4.8 pts |
| Hors altseason | 745 | 49% | 25% (hasard : 10 %) | +5.0 pts | -0.8 pts |

**Leaders aujourd'hui — 🚀 Leader (altseason)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **MOVR** | Speculative | +218% | 46.1% | ⚠️ 8 |
| 2 | **NIGHT** | Mid | +103% | 46.7% | ⚠️ 6 |
| 3 | **SUPER** | Mid | +85% | 49.7% | ⚠️ 4 |
| 4 | **INIT** | Speculative | +72% | 49.2% | 2 |
| 5 | **NOM** | Speculative | +69% | 45.6% | ⚠️ 6 |
| 6 | **RED** | Mid | +65% | 48.8% | ⚠️ 4 |
| 7 | **ZRO** | Mid | +64% | 47.0% | 2 |
| 8 | **RUNE** | Mid | +64% | 48.7% | ⚠️ 4 |
| 9 | **HUMA** | Mid | +61% | 47.1% | ⚠️ 4 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : WIN. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 📑 Annonces d'ETF crypto (SEC EDGAR)

*Tout ETF crypto américain dépose ses documents à la SEC avant son lancement : dossier S-1/S-3 et ses amendements, puis enregistrement en bourse (8-A12B) quelques jours avant la cotation. ZEC et NEAR ont fortement monté autour de leurs ETF. Étude du 29/09/2026 : après un dépôt de dossier, 75 % des tokens ont battu le marché à 7 et 14 j ; avant un 8-A12B, la hausse était souvent déjà faite (+33 pts sur les 14 j précédents). Petit échantillon : suivi réel ci-dessous.*

| Type de dépôt | Événements | Battent le marché à 7 j | Excès médian 7 j | Battent le marché à 14 j | Excès médian 14 j |
|---|---|---|---|---|---|
| Dossier / amendement (S-1, S-3) | 34 | 76% | +3.7 pts | 87% | +6.5 pts |
| Enregistrement en bourse (8-A12B) | 9 | 56% | +2.2 pts | 62% | +1.9 pts |

**Dépôts des 30 derniers jours :**

| Date | Token | Dépôt | Fonds | Depuis le dépôt (vs marché) |
|---|---|---|---|---|
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | -7% (-9 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +12% (+11 pts) |
| 2026-09-18 | **INJ** | S-1/A | 21Shares Injective ETF | +11% (+0 pts) |
| 2026-09-16 | **NEAR** | S-1/A | Bitwise NEAR ETF | +101% (+82 pts) |
| 2026-09-15 | **SEI** | S-1/A | Canary Staked SEI ETF | +67% (+52 pts) |
| 2026-09-11 | **LTC** | S-3/A | Grayscale Litecoin Trust (LTC)  (LTCN) | +28% (+9 pts) |
| 2026-09-11 | **BCH** | S-3/A | Grayscale Bitcoin Cash Trust (BCH)  (BCHG) | +36% (+17 pts) |
| 2026-09-08 | **TRX** | 8-A12B | Canary Staked TRX ETF  (TRXS) | -2% (-12 pts) |

**Tokens avec un ETF en préparation ou en lancement :** INJ (📝 S-1/A le 2026-09-24), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), BCH (📝 S-3/A le 2026-09-11), LTC (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24), ETH (📝 S-3/A le 2026-08-19)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 134 | +0.003 | 50% | 50% | 51% | 51% | 50% | 48% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 30 sep 2026 | 🌱 Altseason en formation | 88 | +8.8% | RENDER, ENS, SOL |
| 1 oct 2026 | 🌱 Altseason en formation | 83 | +7.2% | RENDER, TAO, WIF |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 47.9% (1 oct 2026) — -37.2% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.6% (1 oct 2026) — +8.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.7% (1 oct 2026) — -12.6% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 54.5% (1 oct 2026) — +30.7% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 51.2% (1 oct 2026) — -24.2% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **41655 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0155 |
| momentum | 0.0359 |
| risk | 0.0153 |
| antiscam | 0.0000 |
| signal | 0.0145 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 1 oct 2026

**Régime :** 🌱 Altseason en formation (indice altseason 30 j : 83.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **RENDER** | Etabli | 57.0% | +2.5pp | 0 |  |
| **TAO** | Etabli | 56.8% | +2.3pp | 2 |  |
| **WIF** | Mid | 56.2% | +1.7pp | ⚠️ 4 |  |
| **XLM** | Etabli | 56.0% | +1.5pp | 0 |  |
| **LPT** | Mid | 56.0% | +1.5pp | 2 |  |
| **ADA** | Etabli | 55.9% | +1.4pp | 2 |  |
| **WOO** | Speculative | 55.8% | +1.3pp | 0 |  |
| **PEPE** | Etabli | 55.8% | +1.3pp | 3 |  |
| **ETH** | Etabli | 55.6% | +1.1pp | ⚠️ 5 |  |
| **ENS** | Mid | 55.6% | +1.1pp | ⚠️ 4 |  |
| **SOL** | Etabli | 55.6% | +1.1pp | ⚠️ 5 | 🔥 Trending #11 sur CoinGecko |
| **BNT** | Speculative | 55.5% | +1.0pp | ⚠️ 4 |  |
