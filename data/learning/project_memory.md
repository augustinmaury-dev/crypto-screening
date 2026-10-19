# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 19 oct 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.).
Depuis le 26/09/2026, mon `score` est la **probabilité qu'un token fasse mieux que la médiane du marché sur 7 jours**,
calculée par un modèle réentraîné chaque jour sur toutes mes prédictions passées déjà mesurées (`06b_ml_score.py`).
Je surveille aussi le **régime de marché** (altseason ou saison Bitcoin), car ce qui marche change selon le régime.
Depuis le 12/10/2026, je fais aussi une **prévision à 30 jours** (section 🗓️), jugée à 30 jours, avec le même principe d'apprentissage.

---

## Mon auto-évaluation

### Régime de marché : 🟡 Neutre

- **Indice altseason** : 41.0 sur 30 j, 57.1 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 1.2 % sur 30 j · **Tokens au-dessus de leur MA50** : 25.4 %

### Mon modèle aujourd'hui : `ml_gb`

- Entraîné sur 61309 observations (155 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **55%** du temps (règle simple « grosses caps peu volatiles » : 56% ; hasard : 50 %)
- Confiance (calibration) : k = 0.41 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 82 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `vol_30d_ann` (−), `corr_btc_90d` (+), `log_rank` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 10 / 11

**Mon top 20 quotidien, jugé à 7 j :** 3135 prédictions mesurées — 45% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché (46% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 59.7% | 3967 | → |
| `evening_star_4h` | 57.4% | 997 | 📈 |
| `downtrend` | 56.4% | 18072 | → |
| `bearish_engulfing_4h` | 55.3% | 1122 | 📈 |
| `rsi_bearish_divergence` | 54.5% | 1842 | 📈 |
| `breakdown_30d` | 53.2% | 139 | → |
| `shooting_star_4h` | 52.3% | 346 | → |
| `macd_bearish_cross` | 52.1% | 9252 | 📈 |
| `resistance_test` | 51.7% | 2437 | → |
| `death_cross` | 50.7% | 422 | → |
| `bear_flag` | 48.1% | 603 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 52.9% | 516 | 📉 |
| `uptrend` | 46.8% | 14348 | 📉 |
| `hammer_4h` | 46.7% | 347 | → |
| `bullish_engulfing_4h` | 44.8% | 1280 | → |
| `rsi_bullish_divergence` | 44.3% | 2544 | → |
| `macd_bullish_cross` | 43.8% | 9890 | → |
| `support_bounce` | 43.6% | 2730 | → |
| `double_bottom_90d` | 42.9% | 2779 | → |
| `golden_cross` | 40.5% | 1102 | 📉 |
| `morning_star_4h` | 38.8% | 964 | → |
| `bull_flag` | 36.9% | 382 | 📉 |
| `breakout_30d` | 36.2% | 591 | → |

---

## Mes prédictions passées et leurs résultats

*Une prédiction = un des 20 tokens les mieux classés un jour donné. Jugée à 7 j et à 14 j. « Bat le marché » = a fait mieux que la médiane de tous les tokens sur la même période.*

| Mois | Modèle | Prédictions | Ont monté (7 j) | Ont battu le marché (7 j) | Return médian (7 j) |
|------|--------|-------------|-----------------|---------------------------|---------------------|
| 2026-05 | Ancienne formule | 495 | 32% | 61% | -4.4% |
| 2026-06 | Ancienne formule | 491 | 47% | 46% | -0.5% |
| 2026-07 | Ancienne formule | 626 | 43% | 55% | -1.0% |
| 2026-08 | Ancienne formule | 638 | 53% | 42% | +0.4% |
| 2026-09 | Ancienne formule | 510 | 62% | 47% | +2.8% |
| 2026-09 | Modèle appris | 130 | 48% | 52% | -0.1% |
| 2026-10 | Modèle appris | 245 | 15% | 43% | -7.2% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 12 oct 2026 | **PARTI** | 57% | 0.0345 | -15.4% | ❌ -4.0pp | … |
| 12 oct 2026 | **LAZIO** | 57% | 0.413 | +1.0% | ✅ +12.3pp | … |
| 12 oct 2026 | **APT** | 56% | 0.846 | -9.3% | ✅ +2.1pp | … |
| 12 oct 2026 | **JUV** | 55% | 0.325 | -6.5% | ✅ +4.9pp | … |
| 12 oct 2026 | **SUI** | 55% | 1.0899 | -8.8% | ✅ +2.5pp | … |
| 12 oct 2026 | **ALPINE** | 55% | 0.356 | -9.6% | ✅ +1.8pp | … |
| 12 oct 2026 | **C** | 55% | 0.0979 | -18.6% | ❌ -7.3pp | … |
| 12 oct 2026 | **ADX** | 55% | 0.068 | -12.9% | ❌ -1.6pp | … |
| 12 oct 2026 | **ACM** | 55% | 0.283 | -8.8% | ✅ +2.5pp | … |
| 12 oct 2026 | **TAO** | 55% | 286.6 | -6.1% | ✅ +5.2pp | … |
| 12 oct 2026 | **ADA** | 55% | 0.2445 | -11.0% | ✅ +0.3pp | … |
| 12 oct 2026 | **BAR** | 55% | 0.281 | -5.0% | ✅ +6.3pp | … |
| 12 oct 2026 | **SPELL** | 55% | 9.34e-05 | -9.1% | ✅ +2.2pp | … |
| 12 oct 2026 | **AAVE** | 54% | 163.61 | -9.2% | ✅ +2.1pp | … |
| 12 oct 2026 | **SCR** | 54% | 0.02545 | -22.7% | ❌ -11.4pp | … |
| 12 oct 2026 | **WIN** | 54% | 5.707e-05 | -6.8% | ✅ +4.6pp | … |
| 12 oct 2026 | **GALA** | 54% | 0.002297 | -18.0% | ❌ -6.7pp | … |
| 12 oct 2026 | **AXS** | 54% | 1.215 | -18.2% | ❌ -6.9pp | … |
| 12 oct 2026 | **COMP** | 54% | 23.95 | -10.2% | ✅ +1.1pp | … |
| 12 oct 2026 | **PEPE** | 54% | 4.13e-06 | -0.2% | ✅ +11.1pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1032 | 48% | 22% (hasard : 10 %) | +4.4 pts | -1.1 pts |
| Altseason (indice 30 j ≥ 60) | 261 | 44% | 16% (hasard : 10 %) | +0.6 pts | -1.9 pts |
| Hors altseason | 687 | 48% | 25% (hasard : 10 %) | +4.7 pts | -1.1 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **GTC** | Speculative | +274% | 38.9% | ⚠️ 4 |
| 2 | **AMP** | Mid | +88% | 39.6% | 2 |
| 3 | **IOTX** | Speculative | +25% | 49.2% | 2 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : AVA, OSMO. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée est le taux de réussite **réellement observé** pour la tranche de classement du token.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-05-23 au 2026-09-19 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 68% | +0.197 |
| Règle simple | 68% | +0.165 |
| Mélange ✅ | 68% | +0.195 |

⚠️ Sur cette période, le token médian a fait **+1.6 %** en 30 j et seuls **49%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `runup180` (−), `vtrend` (−), `dd90` (−), `r90` (+)

**Suivi réel** : 162 prédictions en attente — premiers résultats à partir du 11 nov 2026.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **BTC** | Etabli | 68 % | 53.5 % | +1 % |
| 2 | **TRX** | Etabli | 68 % | 49.6 % | -2 % |
| 3 | **BNB** | Etabli | 68 % | 52.2 % | -5 % |
| 4 | **SOL** | Etabli | 68 % | 52.7 % | -7 % |
| 5 | **ASTER** | Etabli | 68 % | 50.6 % | -9 % |
| 6 | **JST** | Etabli | 68 % | 48.8 % | +19 % |
| 7 | **ETH** | Etabli | 68 % | 52.1 % | -9 % |
| 8 | **WLFI** | Etabli | 68 % | 50.7 % | -8 % |
| 9 | **SUN** | Mid | 68 % | 50.6 % | -3 % |
| 10 | **DOGE** | Etabli | 68 % | 53.5 % | -10 % |
| 11 | **NEXO** | Etabli | 68 % | 52.7 % | -5 % |
| 12 | **XRP** | Etabli | 68 % | 52.9 % | -9 % |

---

## 📑 Annonces d'ETF crypto (SEC EDGAR)

*Tout ETF crypto américain dépose ses documents à la SEC avant son lancement : dossier S-1/S-3 et ses amendements, puis enregistrement en bourse (8-A12B) quelques jours avant la cotation. ZEC et NEAR ont fortement monté autour de leurs ETF. Étude du 29/09/2026 : après un dépôt de dossier, 75 % des tokens ont battu le marché à 7 et 14 j ; avant un 8-A12B, la hausse était souvent déjà faite (+33 pts sur les 14 j précédents). Petit échantillon : suivi réel ci-dessous.*

| Type de dépôt | Événements | Battent le marché à 7 j | Excès médian 7 j | Battent le marché à 14 j | Excès médian 14 j |
|---|---|---|---|---|---|
| Dossier / amendement (S-1, S-3) | 35 | 74% | +3.5 pts | 82% | +5.0 pts |
| Enregistrement en bourse (8-A12B) | 9 | 56% | +2.2 pts | 67% | +2.7 pts |

**Dépôts des 30 derniers jours :**

| Date | Token | Dépôt | Fonds | Depuis le dépôt (vs marché) |
|---|---|---|---|---|
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | -8% (+9 pts) |
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | +6% (+17 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +12% (+23 pts) |

**Tokens avec un ETF en préparation ou en lancement :** PEPE (📝 S-1/A le 2026-10-02), NEAR (🟢 8-A12B le 2026-09-24), INJ (📝 S-1/A le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), LTC (📝 S-3/A le 2026-09-11), BCH (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 17 | +0.065 | 46% | 53% | 51% | 50% | 51% | 45% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 10 oct 2026 | 🟡 Neutre | 71 | +6.4% | PARTI, JUV, ENJ |
| 11 oct 2026 | 🌱 Altseason en formation | 76 | +7.9% | PARTI, ADA, RENDER |
| 12 oct 2026 | 🟡 Neutre | 69 | +7.3% | PARTI, LAZIO, APT |
| 13 oct 2026 | 🟡 Neutre | 67 | +8.9% | RONIN, PEPE, SUI |
| 14 oct 2026 | 🟡 Neutre | 65 | +6.0% | PEPE, SUI, BTC |
| 15 oct 2026 | 🟡 Neutre | 61 | +5.3% | PEPE, LAZIO, TAO |
| 16 oct 2026 | 🟡 Neutre | 72 | +8.5% | PEPE, BTC, YFI |
| 17 oct 2026 | 🟡 Neutre | 68 | +6.0% | APT, BTC, PEPE |
| 18 oct 2026 | 🟡 Neutre | 48 | +5.1% | IOTA, PEPE, HOT |
| 19 oct 2026 | 🟡 Neutre | 41 | +1.2% | IOTA, XLM, CHIP |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.1% (19 oct 2026) — -37.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.3% (19 oct 2026) — +7.7% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.4% (19 oct 2026) — -12.9% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 52.9% (19 oct 2026) — +29.1% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 54.5% (19 oct 2026) — -20.9% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **48601 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0208 |
| momentum | 0.0245 |
| risk | 0.0190 |
| antiscam | 0.0000 |
| signal | 0.0045 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 19 oct 2026

**Régime :** 🟡 Neutre (indice altseason 30 j : 41.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **IOTA** | Mid | 54.9% | +1.4pp | 3 |  |
| **XLM** | Etabli | 54.7% | +1.2pp | 3 |  |
| **CHIP** | Mid | 54.4% | +0.9pp | ⚠️ 5 |  |
| **ADA** | Etabli | 54.0% | +0.5pp | 3 |  |
| **ENS** | Mid | 54.0% | +0.5pp | 3 |  |
| **HOT** | Mid | 53.9% | +0.4pp | 3 |  |
| **FLOKI** | Mid | 53.8% | +0.3pp | ⚠️ 5 |  |
| **BERA** | Mid | 53.8% | +0.3pp | 1 |  |
| **VET** | Mid | 53.7% | +0.2pp | 3 |  |
| **FIL** | Etabli | 53.6% | +0.1pp | 1 |  |
| **BTC** | Etabli | 53.5% | +0.0pp | 1 | 🔥 Trending #3 sur CoinGecko |
| **DOGE** | Etabli | 53.5% | +0.0pp | 3 |  |
