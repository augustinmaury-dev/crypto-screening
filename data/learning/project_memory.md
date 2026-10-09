# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 9 oct 2026*

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

- **Indice altseason** : 58.0 sur 30 j, 57.1 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 4.2 % sur 30 j · **Tokens au-dessus de leur MA50** : 57.6 %

### Mon modèle aujourd'hui : `ml_gb`

- Entraîné sur 57681 observations (145 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **52%** du temps (règle simple « grosses caps peu volatiles » : 48% ; hasard : 50 %)
- Confiance (calibration) : k = 0.33 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 75 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `bear_signals` (−), `log_rank` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 6 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2892 prédictions mesurées — 47% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 58.4% | 3788 | → |
| `downtrend` | 55.9% | 17288 | → |
| `breakdown_30d` | 53.4% | 133 | → |
| `bearish_engulfing_4h` | 52.4% | 971 | → |
| `evening_star_4h` | 52.0% | 830 | → |
| `shooting_star_4h` | 51.1% | 325 | → |
| `death_cross` | 50.0% | 394 | → |
| `resistance_test` | 49.8% | 2122 | → |
| `rsi_bearish_divergence` | 49.1% | 1473 | → |
| `bear_flag` | 47.9% | 599 | → |
| `macd_bearish_cross` | 47.7% | 8068 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 56.9% | 466 | → |
| `uptrend` | 49.9% | 12633 | → |
| `golden_cross` | 48.1% | 809 | → |
| `hammer_4h` | 47.7% | 331 | → |
| `bullish_engulfing_4h` | 46.5% | 1199 | → |
| `bull_flag` | 44.8% | 297 | → |
| `rsi_bullish_divergence` | 44.6% | 2511 | → |
| `double_bottom_90d` | 44.3% | 2540 | → |
| `macd_bullish_cross` | 44.1% | 9748 | 📈 |
| `support_bounce` | 43.7% | 2670 | → |
| `morning_star_4h` | 39.3% | 929 | → |
| `breakout_30d` | 37.1% | 517 | 📈 |

---

## Mes prédictions passées et leurs résultats

*Une prédiction = un des 20 tokens les mieux classés un jour donné. Jugée à 7 j et à 14 j. « Bat le marché » = a fait mieux que la médiane de tous les tokens sur la même période.*

| Mois | Modèle | Prédictions | Ont monté (7 j) | Ont battu le marché (7 j) | Return médian (7 j) |
|------|--------|-------------|-----------------|---------------------------|---------------------|
| 2026-05 | Ancienne formule | 481 | 32% | 61% | -4.3% |
| 2026-06 | Ancienne formule | 480 | 47% | 46% | -0.6% |
| 2026-07 | Ancienne formule | 621 | 43% | 54% | -1.0% |
| 2026-08 | Ancienne formule | 630 | 53% | 42% | +0.4% |
| 2026-09 | Ancienne formule | 510 | 62% | 47% | +2.8% |
| 2026-09 | Modèle appris | 130 | 48% | 52% | -0.1% |
| 2026-10 | Modèle appris | 40 | 10% | 30% | -6.5% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 2 oct 2026 | **RENDER** | 58% | 1.985 | -6.0% | ✅ +2.7pp | … |
| 2 oct 2026 | **KAIA** | 58% | 0.0371 | +46.4% | ✅ +55.0pp | … |
| 2 oct 2026 | **LPT** | 57% | 1.766 | -3.5% | ✅ +5.2pp | … |
| 2 oct 2026 | **WIF** | 57% | 0.2533 | -17.1% | ❌ -8.4pp | … |
| 2 oct 2026 | **IOTA** | 57% | 0.0555 | -9.9% | ❌ -1.2pp | … |
| 2 oct 2026 | **WOO** | 57% | 0.01395 | -12.9% | ❌ -4.2pp | … |
| 2 oct 2026 | **TAO** | 57% | 312.2 | -12.7% | ❌ -4.0pp | … |
| 2 oct 2026 | **ENS** | 57% | 7.22 | -15.1% | ❌ -6.4pp | … |
| 2 oct 2026 | **ADA** | 57% | 0.2561 | -7.8% | ✅ +0.9pp | … |
| 2 oct 2026 | **BONK** | 57% | 3.88e-06 | -14.9% | ❌ -6.3pp | … |
| 2 oct 2026 | **SOL** | 56% | 122.37 | -10.5% | ❌ -1.8pp | … |
| 2 oct 2026 | **BNT** | 56% | 0.3589 | -12.1% | ❌ -3.5pp | … |
| 2 oct 2026 | **ICP** | 56% | 3.327 | -10.8% | ❌ -2.1pp | … |
| 2 oct 2026 | **XLM** | 56% | 0.2254 | -14.8% | ❌ -6.1pp | … |
| 2 oct 2026 | **1INCH** | 56% | 0.1057 | -9.4% | ❌ -0.7pp | … |
| 2 oct 2026 | **COMP** | 56% | 24.7 | -3.9% | ✅ +4.7pp | … |
| 2 oct 2026 | **ETH** | 56% | 2751.57 | -9.7% | ❌ -1.1pp | … |
| 2 oct 2026 | **BTC** | 56% | 86656 | -4.6% | ✅ +4.0pp | … |
| 2 oct 2026 | **AXL** | 55% | 0.0534 | -4.7% | ✅ +4.0pp | … |
| 2 oct 2026 | **LINK** | 55% | 14.343 | -11.2% | ❌ -2.5pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 916 | 48% | 23% (hasard : 10 %) | +4.7 pts | -1.2 pts |
| Altseason (indice 30 j ≥ 60) | 149 | 44% | 15% (hasard : 10 %) | +3.5 pts | -3.6 pts |
| Hors altseason | 728 | 49% | 26% (hasard : 10 %) | +5.6 pts | -0.3 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **RLC** | Mid | +247% | 40.8% | ⚠️ 8 |
| 2 | **STRK** | Mid | +123% | 42.6% | ⚠️ 6 |
| 3 | **KAIA** | Mid | +76% | 43.2% | ⚠️ 6 |
| 4 | **W** | Mid | +71% | 43.8% | ⚠️ 6 |
| 5 | **MAGIC** | Speculative | +69% | 44.1% | ⚠️ 6 |
| 6 | **BEAMX** | Speculative | +66% | 47.0% | ⚠️ 4 |
| 7 | **PYTH** | Etabli | +56% | 46.6% | ⚠️ 7 |
| 8 | **C** | Speculative | +56% | 47.7% | ⚠️ 5 |
| 9 | **S** | Mid | +48% | 47.2% | ⚠️ 5 |
| 10 | **BAT** | Mid | +46% | 46.4% | ⚠️ 6 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : MET, RAY. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 📑 Annonces d'ETF crypto (SEC EDGAR)

*Tout ETF crypto américain dépose ses documents à la SEC avant son lancement : dossier S-1/S-3 et ses amendements, puis enregistrement en bourse (8-A12B) quelques jours avant la cotation. ZEC et NEAR ont fortement monté autour de leurs ETF. Étude du 29/09/2026 : après un dépôt de dossier, 75 % des tokens ont battu le marché à 7 et 14 j ; avant un 8-A12B, la hausse était souvent déjà faite (+33 pts sur les 14 j précédents). Petit échantillon : suivi réel ci-dessous.*

| Type de dépôt | Événements | Battent le marché à 7 j | Excès médian 7 j | Battent le marché à 14 j | Excès médian 14 j |
|---|---|---|---|---|---|
| Dossier / amendement (S-1, S-3) | 35 | 74% | +3.5 pts | 81% | +5.3 pts |
| Enregistrement en bourse (8-A12B) | 9 | 56% | +2.2 pts | 67% | +2.7 pts |

**Dépôts des 30 derniers jours :**

| Date | Token | Dépôt | Fonds | Depuis le dépôt (vs marché) |
|---|---|---|---|---|
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | -13% (-5 pts) |
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | -14% (-11 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +8% (+11 pts) |
| 2026-09-18 | **INJ** | S-1/A | 21Shares Injective ETF | +3% (-2 pts) |
| 2026-09-16 | **NEAR** | S-1/A | Bitwise NEAR ETF | +94% (+80 pts) |
| 2026-09-15 | **SEI** | S-1/A | Canary Staked SEI ETF | +50% (+40 pts) |
| 2026-09-11 | **LTC** | S-3/A | Grayscale Litecoin Trust (LTC)  (LTCN) | +21% (+9 pts) |
| 2026-09-11 | **BCH** | S-3/A | Grayscale Bitcoin Cash Trust (BCH)  (BCHG) | +21% (+9 pts) |

**Tokens avec un ETF en préparation ou en lancement :** PEPE (📝 S-1/A le 2026-10-02), INJ (📝 S-1/A le 2026-09-24), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), BCH (📝 S-3/A le 2026-09-11), LTC (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24), ETH (📝 S-3/A le 2026-08-19)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.003 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 7 | +0.040 | 49% | 51% | 50% | 52% | 48% | 48% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 2 oct 2026 | 🌱 Altseason en formation | 82 | +13.0% | RENDER, KAIA, LPT |
| 3 oct 2026 | 🌱 Altseason en formation | 81 | +8.7% | BTC, RENDER, SOL |
| 4 oct 2026 | 🌱 Altseason en formation | 81 | +4.7% | KAIA, RENDER, SUI |
| 5 oct 2026 | 🌱 Altseason en formation | 77 | +7.4% | RENDER, EIGEN, CHZ |
| 6 oct 2026 | 🌱 Altseason en formation | 76 | +8.1% | ADA, ENJ, WIF |
| 7 oct 2026 | 🟡 Neutre | 64 | +4.6% | KAIA, IOTA, JASMY |
| 8 oct 2026 | 🟡 Neutre | 60 | +5.3% | IOTA, ENJ, SUI |
| 9 oct 2026 | 🟡 Neutre | 58 | +4.2% | SUI, ENJ, DOGE |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 47.9% (9 oct 2026) — -37.2% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.6% (9 oct 2026) — +8.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 55.9% (9 oct 2026) — -13.4% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 56.9% (9 oct 2026) — +33.1% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 49.1% (9 oct 2026) — -26.3% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **44778 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0176 |
| momentum | 0.0469 |
| risk | 0.0240 |
| antiscam | 0.0000 |
| signal | 0.0248 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 9 oct 2026

**Régime :** 🟡 Neutre (indice altseason 30 j : 58.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **SUI** | Etabli | 55.7% | +3.1pp | ⚠️ 7 |  |
| **ENJ** | Mid | 55.4% | +2.8pp | 3 |  |
| **DOGE** | Etabli | 55.3% | +2.7pp | 3 |  |
| **WIF** | Mid | 55.3% | +2.7pp | ⚠️ 5 |  |
| **SHIB** | Etabli | 54.7% | +2.1pp | ⚠️ 5 |  |
| **XLM** | Etabli | 54.3% | +1.7pp | 3 |  |
| **FLOKI** | Mid | 54.2% | +1.6pp | 3 |  |
| **IOTA** | Mid | 54.2% | +1.6pp | 3 |  |
| **ETC** | Etabli | 54.1% | +1.5pp | 1 |  |
| **TAO** | Etabli | 54.0% | +1.4pp | ⚠️ 5 |  |
| **PEPE** | Etabli | 54.0% | +1.4pp | 3 |  |
| **ADA** | Etabli | 53.9% | +1.3pp | 3 |  |
