# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 21 oct 2026*

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

- **Indice altseason** : 47.0 sur 30 j, 64.3 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : -1.6 % sur 30 j · **Tokens au-dessus de leur MA50** : 34.9 %
- *Deux seuils différents : l'**étiquette** du régime suit les seuils classiques (≥ 75 = altseason, ≤ 25 = saison Bitcoin) ; le **mode altseason** du classement s'active dès que l'indice 30 j atteint 60.* Aujourd'hui : mode altseason **inactif** (indice 30 j = 47.0).
- **Modèle dédié à l'altseason : prêt** (33 jours d'altseason mesurés, seuil 30). Il est utilisé seulement les jours où le mode altseason est actif — aujourd'hui : **non utilisé** (`ml_gb`).

### Mon modèle aujourd'hui : `ml_gb`

- Entraîné sur 62095 observations (157 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **57%** du temps (règle simple « grosses caps peu volatiles » : 57% ; hasard : 50 %)
- Confiance (calibration) : k = 0.43 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 82 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `vol_30d_ann` (−), `corr_btc_90d` (+), `log_rank` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 10 / 11

**Mon top 20 quotidien, jugé à 7 j :** 3175 prédictions mesurées — 45% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché (49% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 60.1% | 4021 | → |
| `evening_star_4h` | 58.4% | 1026 | 📈 |
| `downtrend` | 56.5% | 18157 | → |
| `bearish_engulfing_4h` | 55.9% | 1145 | 📈 |
| `rsi_bearish_divergence` | 55.2% | 1876 | 📈 |
| `breakdown_30d` | 53.4% | 146 | → |
| `macd_bearish_cross` | 52.8% | 9461 | 📈 |
| `shooting_star_4h` | 52.4% | 351 | → |
| `resistance_test` | 51.9% | 2488 | → |
| `death_cross` | 50.5% | 428 | → |
| `bear_flag` | 48.1% | 603 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 51.2% | 543 | 📉 |
| `hammer_4h` | 46.6% | 352 | → |
| `uptrend` | 46.0% | 14746 | 📉 |
| `bullish_engulfing_4h` | 44.6% | 1289 | → |
| `rsi_bullish_divergence` | 44.4% | 2556 | → |
| `macd_bullish_cross` | 43.7% | 9942 | → |
| `support_bounce` | 43.7% | 2744 | → |
| `double_bottom_90d` | 42.7% | 2809 | → |
| `golden_cross` | 39.4% | 1173 | 📉 |
| `morning_star_4h` | 38.7% | 967 | → |
| `breakout_30d` | 35.5% | 602 | → |
| `bull_flag` | 34.5% | 411 | 📉 |

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
| 2026-10 | Modèle appris | 285 | 16% | 48% | -6.7% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 14 oct 2026 | **PEPE** | 55% | 4.12e-06 | +10.9% | ✅ +14.4pp | … |
| 14 oct 2026 | **SUI** | 54% | 1.0346 | +0.1% | ✅ +3.5pp | … |
| 14 oct 2026 | **BTC** | 54% | 82798 | +1.0% | ✅ +4.5pp | … |
| 14 oct 2026 | **IOTA** | 54% | 0.0484 | -2.9% | ✅ +0.6pp | … |
| 14 oct 2026 | **JASMY** | 54% | 0.00467 | +2.4% | ✅ +5.8pp | … |
| 14 oct 2026 | **AXS** | 54% | 1.115 | -5.4% | ❌ -1.9pp | … |
| 14 oct 2026 | **TAO** | 54% | 275 | -0.6% | ✅ +2.8pp | … |
| 14 oct 2026 | **RUNE** | 54% | 0.654 | +3.7% | ✅ +7.1pp | … |
| 14 oct 2026 | **NEXO** | 54% | 0.838 | -1.8% | ✅ +1.7pp | … |
| 14 oct 2026 | **NEO** | 54% | 2.349 | -3.2% | ✅ +0.3pp | … |
| 14 oct 2026 | **1INCH** | 53% | 0.0954 | -0.6% | ✅ +2.8pp | … |
| 14 oct 2026 | **IMX** | 53% | 0.169 | -9.0% | ❌ -5.5pp | … |
| 14 oct 2026 | **ARKM** | 53% | 0.1274 | +1.1% | ✅ +4.5pp | … |
| 14 oct 2026 | **EIGEN** | 53% | 0.2375 | -0.6% | ✅ +2.9pp | … |
| 14 oct 2026 | **EDEN** | 53% | 0.05993 | +0.2% | ✅ +3.7pp | … |
| 14 oct 2026 | **FLOKI** | 53% | 2.52e-05 | -1.4% | ✅ +2.0pp | … |
| 14 oct 2026 | **GLM** | 53% | 0.1233 | -4.5% | ❌ -1.1pp | … |
| 14 oct 2026 | **SNX** | 53% | 0.2342 | -3.6% | ❌ -0.2pp | … |
| 14 oct 2026 | **LAZIO** | 53% | 0.406 | +1.7% | ✅ +5.2pp | … |
| 14 oct 2026 | **ZRX** | 53% | 0.1166 | -4.0% | ❌ -0.5pp | … |

**145 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1053 | 48% | 22% (hasard : 10 %) | +4.4 pts | -1.1 pts |
| Altseason (indice 30 j ≥ 60) | 272 | 45% | 16% (hasard : 10 %) | +0.9 pts | -1.7 pts |
| Hors altseason | 681 | 48% | 25% (hasard : 10 %) | +4.8 pts | -1.1 pts |
| **En direct** (depuis le 29/09/2026) | 103 | 50% | 20% (hasard : 10 %) | +3.1 pts | +0.0 pts |
| Reconstitués (avant le 29/09/2026) | 950 | 48% | 23% (hasard : 10 %) | +4.6 pts | -1.2 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **BEAMX** | Speculative | +62% | 49.0% | ⚠️ 4 |
| 2 | **PARTI** | Speculative | +56% | 44.0% | ⚠️ 7 |
| 3 | **ALT** | Mid | +32% | 49.1% | 2 |
| 4 | **JST** | Etabli | +26% | 51.5% | ⚠️ 5 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : CVX, WIN, WLD. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée est le taux de réussite **réellement observé** pour la tranche de classement du token.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-05-25 au 2026-09-21 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 67% | +0.197 |
| Règle simple | 68% | +0.165 |
| Mélange ✅ | 68% | +0.196 |

⚠️ Sur cette période, le token médian a fait **+1.6 %** en 30 j et seuls **49%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `runup180` (−), `vtrend` (−), `dd90` (−), `r90` (+)

**Suivi réel** : 205 prédictions en attente — premiers résultats à partir du 11 nov 2026.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **BTC** | Etabli | 67 % | 55.0 % | -2 % |
| 2 | **TRX** | Etabli | 67 % | 53.9 % | -4 % |
| 3 | **BNB** | Etabli | 67 % | 55.5 % | -5 % |
| 4 | **ASTER** | Etabli | 67 % | 52.0 % | -4 % |
| 5 | **ETH** | Etabli | 66 % | 56.0 % | -10 % |
| 6 | **SOL** | Etabli | 66 % | 55.5 % | -9 % |
| 7 | **WLFI** | Etabli | 66 % | 54.0 % | -3 % |
| 8 | **DOGE** | Etabli | 66 % | 55.7 % | -12 % |
| 9 | **JST** | Etabli | 66 % | 51.5 % | +26 % |
| 10 | **NEXO** | Etabli | 66 % | 55.9 % | -5 % |
| 11 | **XRP** | Etabli | 66 % | 55.8 % | -8 % |
| 12 | **SUN** | Mid | 66 % | 52.6 % | -4 % |

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
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | +2% (+15 pts) |
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | +9% (+15 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +20% (+26 pts) |

**Tokens avec un ETF en préparation ou en lancement :** PEPE (📝 S-1/A le 2026-10-02), INJ (📝 S-1/A le 2026-09-24), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), LTC (📝 S-3/A le 2026-09-11), BCH (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 19 | +0.073 | 50% | 53% | 50% | 50% | 50% | 45% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 20 oct 2026 | 🟡 Neutre | 52 | +1.4% | ENS, ADA, SHIB |
| 21 oct 2026 | 🟡 Neutre | 47 | -1.6% | APT, ADA, ETH |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.1% (21 oct 2026) — -37.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.4% (21 oct 2026) — +7.8% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.5% (21 oct 2026) — -12.8% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 51.2% (21 oct 2026) — +27.4% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 55.2% (21 oct 2026) — -20.2% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **49332 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0221 |
| momentum | 0.0199 |
| risk | 0.0173 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 21 oct 2026

**Régime :** 🟡 Neutre (indice altseason 30 j : 47.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **APT** | Etabli | 56.5% | +1.5pp | 3 |  |
| **ADA** | Etabli | 56.1% | +1.1pp | 3 |  |
| **ETH** | Etabli | 56.0% | +1.0pp | 1 |  |
| **SHIB** | Etabli | 56.0% | +1.0pp | ⚠️ 5 |  |
| **IOTA** | Mid | 55.9% | +0.9pp | 1 |  |
| **NEXO** | Etabli | 55.9% | +0.9pp | 3 |  |
| **1INCH** | Mid | 55.8% | +0.8pp | 3 |  |
| **XRP** | Etabli | 55.8% | +0.8pp | 3 |  |
| **XLM** | Etabli | 55.7% | +0.7pp | 3 |  |
| **DOGE** | Etabli | 55.7% | +0.7pp | 3 |  |
| **TAO** | Etabli | 55.5% | +0.5pp | 3 |  |
| **ETC** | Etabli | 55.5% | +0.5pp | 1 |  |

*Colonne Catalyseurs vide : normal, ce n'est pas une panne — 26 tokens ont un catalyseur aujourd'hui (trending CoinGecko, pic de volume…), mais le modèle a appris que ces tokens font plutôt moins bien ensuite (`catalyst_score` joue contre), ils sont donc rarement dans le top.*
