# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 13 oct 2026*

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

- **Indice altseason** : 67.0 sur 30 j, 66.3 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 8.9 % sur 30 j · **Tokens au-dessus de leur MA50** : 57.8 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 25).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 58956 observations (149 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **46%** du temps (règle simple « grosses caps peu volatiles » : 52% ; hasard : 50 %)
- Confiance (calibration) : k = 0.24 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 79 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `vol_30d_ann` (−), `bear_signals` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 9 / 11

**Mon top 20 quotidien, jugé à 7 j :** 3010 prédictions mesurées — 46% ont monté, **49% ont battu la médiane du marché** (50% = hasard)

### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché (42% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 58.7% | 3835 | → |
| `downtrend` | 56.0% | 17720 | → |
| `breakdown_30d` | 53.3% | 137 | → |
| `bearish_engulfing_4h` | 53.0% | 1029 | → |
| `evening_star_4h` | 52.7% | 861 | → |
| `rsi_bearish_divergence` | 51.7% | 1672 | 📈 |
| `shooting_star_4h` | 51.6% | 335 | → |
| `death_cross` | 50.1% | 405 | → |
| `resistance_test` | 50.1% | 2246 | → |
| `macd_bearish_cross` | 48.2% | 8251 | → |
| `bear_flag` | 48.0% | 600 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 55.9% | 476 | → |
| `uptrend` | 49.1% | 13272 | → |
| `hammer_4h` | 47.4% | 342 | → |
| `bullish_engulfing_4h` | 46.2% | 1216 | → |
| `golden_cross` | 46.1% | 909 | 📉 |
| `bull_flag` | 44.7% | 300 | → |
| `rsi_bullish_divergence` | 44.5% | 2524 | → |
| `double_bottom_90d` | 44.0% | 2637 | → |
| `macd_bullish_cross` | 44.0% | 9821 | → |
| `support_bounce` | 43.7% | 2699 | → |
| `morning_star_4h` | 39.4% | 935 | → |
| `breakout_30d` | 36.6% | 558 | → |

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
| 2026-10 | Modèle appris | 120 | 18% | 32% | -6.8% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 6 oct 2026 | **ADA** | 58% | 0.276 | -13.7% | ❌ -5.8pp | … |
| 6 oct 2026 | **ENJ** | 58% | 0.03315 | -7.5% | ✅ +0.4pp | … |
| 6 oct 2026 | **WIF** | 57% | 0.2513 | -16.6% | ❌ -8.7pp | … |
| 6 oct 2026 | **KAIA** | 57% | 0.04 | +16.8% | ✅ +24.6pp | … |
| 6 oct 2026 | **SOL** | 57% | 121.08 | -10.8% | ❌ -2.9pp | … |
| 6 oct 2026 | **FLOKI** | 57% | 2.91e-05 | -11.1% | ❌ -3.2pp | … |
| 6 oct 2026 | **APT** | 56% | 0.8267 | +0.3% | ✅ +8.2pp | … |
| 6 oct 2026 | **HOT** | 56% | 0.000457 | -12.7% | ❌ -4.8pp | … |
| 6 oct 2026 | **BCH** | 56% | 316.5 | -13.6% | ❌ -5.7pp | … |
| 6 oct 2026 | **BONK** | 56% | 3.77e-06 | -13.8% | ❌ -5.9pp | … |
| 6 oct 2026 | **SEI** | 56% | 0.07392 | -14.5% | ❌ -6.7pp | … |
| 6 oct 2026 | **AXL** | 56% | 0.0546 | +2.4% | ✅ +10.3pp | … |
| 6 oct 2026 | **PEPE** | 55% | 4.36e-06 | -3.0% | ✅ +4.9pp | … |
| 6 oct 2026 | **GMT** | 55% | 0.00887 | -8.3% | ❌ -0.5pp | … |
| 6 oct 2026 | **ETH** | 55% | 2719.66 | -7.2% | ✅ +0.7pp | … |
| 6 oct 2026 | **BNB** | 55% | 786.13 | -5.1% | ✅ +2.8pp | … |
| 6 oct 2026 | **SHIB** | 55% | 5.89e-06 | -11.2% | ❌ -3.3pp | … |
| 6 oct 2026 | **TAO** | 55% | 303.3 | -7.2% | ✅ +0.6pp | … |
| 6 oct 2026 | **DOGE** | 55% | 0.09613 | -11.7% | ❌ -3.8pp | … |
| 6 oct 2026 | **SUI** | 55% | 1.2027 | -12.2% | ❌ -4.3pp | … |

**145 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 955 | 48% | 23% (hasard : 10 %) | +4.5 pts | -1.2 pts |
| Altseason (indice 30 j ≥ 60) | 198 | 44% | 15% (hasard : 10 %) | +3.1 pts | -3.1 pts |
| Hors altseason | 708 | 49% | 25% (hasard : 10 %) | +5.6 pts | -0.4 pts |

**Leaders aujourd'hui — 🚀 Leader (altseason)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **S** | Mid | +163% | 48.2% | ⚠️ 6 |
| 2 | **BAT** | Mid | +130% | 48.4% | ⚠️ 8 |
| 3 | **INIT** | Speculative | +77% | 50.0% | ⚠️ 7 |
| 4 | **ZK** | Mid | +75% | 48.6% | ⚠️ 4 |
| 5 | **BEAMX** | Speculative | +68% | 50.7% | ⚠️ 4 |
| 6 | **TIA** | Mid | +67% | 48.5% | 2 |
| 7 | **AERO** | Etabli | +61% | 50.2% | ⚠️ 5 |
| 8 | **AVA** | Speculative | +53% | 49.3% | ⚠️ 5 |
| 9 | **PYTH** | Etabli | +52% | 49.1% | ⚠️ 5 |
| 10 | **OP** | Mid | +51% | 49.7% | ⚠️ 5 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : STX, VELODROME. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée est le taux de réussite **réellement observé** pour la tranche de classement du token.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-05-17 au 2026-09-13 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 69% | +0.187 |
| Règle simple | 70% | +0.166 |
| Mélange ✅ | 70% | +0.191 |

⚠️ Sur cette période, le token médian a fait **-2.1 %** en 30 j et seuls **46%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `runup180` (−), `vtrend` (−), `r90` (+), `dd90` (−)

**Suivi réel** : 42 prédictions en attente — premiers résultats à partir du 11 nov 2026.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **BTC** | Etabli | 70 % | 52.8 % | +9 % |
| 2 | **BNB** | Etabli | 70 % | 51.4 % | +4 % |
| 3 | **TRX** | Etabli | 70 % | 47.1 % | -4 % |
| 4 | **SOL** | Etabli | 70 % | 52.1 % | +8 % |
| 5 | **ASTER** | Etabli | 70 % | 52.0 % | -0 % |
| 6 | **ETH** | Etabli | 70 % | 52.5 % | +2 % |
| 7 | **WLFI** | Etabli | 70 % | 49.7 % | -2 % |
| 8 | **JST** | Etabli | 70 % | 50.6 % | +23 % |
| 9 | **XRP** | Etabli | 70 % | 52.2 % | +3 % |
| 10 | **LTC** | Etabli | 70 % | 52.1 % | +14 % |
| 11 | **DOGE** | Etabli | 70 % | 52.0 % | +2 % |
| 12 | **ADX** | Speculative | 70 % | 51.2 % | +15 % |

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
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | -5% (+3 pts) |
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | -2% (+0 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +16% (+18 pts) |
| 2026-09-18 | **INJ** | S-1/A | 21Shares Injective ETF | +17% (+11 pts) |
| 2026-09-16 | **NEAR** | S-1/A | Bitwise NEAR ETF | +107% (+93 pts) |
| 2026-09-15 | **SEI** | S-1/A | Canary Staked SEI ETF | +45% (+35 pts) |

**Tokens avec un ETF en préparation ou en lancement :** PEPE (📝 S-1/A le 2026-10-02), INJ (📝 S-1/A le 2026-09-24), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), LTC (📝 S-3/A le 2026-09-11), BCH (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24), ETH (📝 S-3/A le 2026-08-19)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 11 | +0.007 | 43% | 48% | 50% | 51% | 50% | 49% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 10 oct 2026 | 🟡 Neutre | 71 | +6.4% | PARTI, JUV, ENJ |
| 11 oct 2026 | 🌱 Altseason en formation | 76 | +7.9% | PARTI, ADA, RENDER |
| 12 oct 2026 | 🟡 Neutre | 69 | +7.3% | PARTI, LAZIO, APT |
| 13 oct 2026 | 🟡 Neutre | 67 | +8.9% | RONIN, PEPE, SUI |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.0% (13 oct 2026) — -37.1% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.5% (13 oct 2026) — +7.9% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.0% (13 oct 2026) — -13.3% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 55.9% (13 oct 2026) — +32.1% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 51.7% (13 oct 2026) — -23.7% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **46257 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0177 |
| momentum | 0.0427 |
| risk | 0.0250 |
| antiscam | 0.0000 |
| signal | 0.0213 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 13 oct 2026

**Régime :** 🟡 Neutre (indice altseason 30 j : 67.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **RONIN** | Speculative | 53.9% | +1.1pp | 1 |  |
| **PEPE** | Etabli | 53.6% | +0.8pp | 1 |  |
| **SUI** | Etabli | 53.0% | +0.2pp | 1 |  |
| **PARTI** | Speculative | 52.9% | +0.1pp | ⚠️ 6 |  |
| **BTC** | Etabli | 52.8% | +0.0pp | 3 | 🔥 Trending #10 sur CoinGecko |
| **TAO** | Etabli | 52.8% | +0.0pp | 1 |  |
| **NEXO** | Etabli | 52.8% | +0.0pp | 3 |  |
| **APT** | Etabli | 52.7% | -0.1pp | 1 |  |
| **DOT** | Etabli | 52.5% | -0.3pp | 3 |  |
| **ADA** | Etabli | 52.5% | -0.3pp | 1 |  |
| **ETH** | Etabli | 52.5% | -0.3pp | 1 |  |
| **ETC** | Etabli | 52.5% | -0.3pp | 1 |  |
