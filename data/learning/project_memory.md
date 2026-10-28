# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 28 oct 2026*

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

### Régime de marché : 🟠 Bitcoin domine (court terme)

- **Indice altseason** : 17.2 sur 30 j, 60.8 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : -2.4 % sur 30 j · **Tokens au-dessus de leur MA50** : 12.8 %
- *Deux seuils différents : l'**étiquette** du régime suit les seuils classiques (≥ 75 = altseason, ≤ 25 = saison Bitcoin) ; le **mode altseason** du classement s'active dès que l'indice 30 j atteint 60.* Aujourd'hui : mode altseason **inactif** (indice 30 j = 17.2).
- **Modèle dédié à l'altseason : prêt** (36 jours d'altseason mesurés, seuil 30). Il est utilisé seulement les jours où le mode altseason est actif — aujourd'hui : **non utilisé** (`ml_gb`).

### Mon modèle aujourd'hui : `ml_gb`

- Entraîné sur 64844 observations (164 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **59%** du temps (règle simple « grosses caps peu volatiles » : 66% ; hasard : 50 %)
- Confiance (calibration) : k = 0.52 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 85 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `vol_30d_ann` (−), `pat_bear_flag` (−), `log_rank` (−)

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 48.3%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Mon top 20 quotidien, jugé à 7 j :** 3320 prédictions mesurées — 43% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché (51% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 61.7% | 4217 | → |
| `evening_star_4h` | 60.7% | 1111 | 📈 |
| `breakdown_30d` | 59.4% | 170 | 📈 |
| `bearish_engulfing_4h` | 57.7% | 1212 | → |
| `downtrend` | 57.1% | 18558 | → |
| `rsi_bearish_divergence` | 56.3% | 1959 | → |
| `macd_bearish_cross` | 55.4% | 10137 | 📈 |
| `shooting_star_4h` | 53.1% | 358 | → |
| `resistance_test` | 51.9% | 2605 | → |
| `death_cross` | 51.2% | 443 | → |
| `bear_flag` | 48.4% | 607 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 48.3% | 594 | 📉 |
| `hammer_4h` | 44.7% | 367 | → |
| `support_bounce` | 43.7% | 2810 | → |
| `rsi_bullish_divergence` | 43.3% | 2664 | → |
| `macd_bullish_cross` | 43.3% | 10147 | → |
| `uptrend` | 43.2% | 16023 | 📉 |
| `double_bottom_90d` | 42.6% | 2867 | → |
| `bullish_engulfing_4h` | 42.5% | 1395 | 📉 |
| `morning_star_4h` | 37.7% | 1011 | → |
| `golden_cross` | 35.4% | 1348 | 📉 |
| `bull_flag` | 34.9% | 415 | → |
| `breakout_30d` | 34.7% | 631 | → |

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
| 2026-10 | Modèle appris | 430 | 16% | 51% | -5.7% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 21 oct 2026 | **APT** | 56% | 0.8227 | -16.7% | ❌ -9.9pp | … |
| 21 oct 2026 | **ADA** | 56% | 0.2257 | -9.9% | ❌ -3.1pp | … |
| 21 oct 2026 | **ETH** | 56% | 2470.68 | -5.3% | ✅ +1.5pp | … |
| 21 oct 2026 | **SHIB** | 56% | 5.17e-06 | -4.3% | ✅ +2.5pp | … |
| 21 oct 2026 | **IOTA** | 56% | 0.047 | -11.1% | ❌ -4.3pp | … |
| 21 oct 2026 | **NEXO** | 56% | 0.823 | -2.5% | ✅ +4.2pp | … |
| 21 oct 2026 | **1INCH** | 56% | 0.0948 | -7.4% | ❌ -0.6pp | … |
| 21 oct 2026 | **XRP** | 56% | 1.3576 | -2.6% | ✅ +4.1pp | … |
| 21 oct 2026 | **DOGE** | 56% | 0.08209 | -3.5% | ✅ +3.3pp | … |
| 21 oct 2026 | **XLM** | 56% | 0.1845 | -7.8% | ❌ -1.0pp | … |
| 21 oct 2026 | **BNB** | 56% | 746.54 | +0.7% | ✅ +7.5pp | … |
| 21 oct 2026 | **ETC** | 56% | 8.09 | -6.5% | ✅ +0.2pp | … |
| 21 oct 2026 | **SOL** | 56% | 107.06 | -5.1% | ✅ +1.7pp | … |
| 21 oct 2026 | **TAO** | 56% | 273.3 | -7.2% | ❌ -0.4pp | … |
| 21 oct 2026 | **YFI** | 55% | 2239 | -6.7% | ✅ +0.1pp | … |
| 21 oct 2026 | **BTC** | 55% | 83629.3 | -3.4% | ✅ +3.4pp | … |
| 21 oct 2026 | **WIF** | 55% | 0.2089 | -13.5% | ❌ -6.7pp | … |
| 21 oct 2026 | **LAZIO** | 55% | 0.413 | -6.8% | ❌ +0.0pp | … |
| 21 oct 2026 | **ALGO** | 55% | 0.1133 | -10.2% | ❌ -3.4pp | … |
| 21 oct 2026 | **AVAX** | 55% | 9.7 | -8.2% | ❌ -1.4pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1123 | 47% | 23% (hasard : 10 %) | +4.3 pts | -1.4 pts |
| Altseason (indice 30 j ≥ 60) | 342 | 44% | 18% (hasard : 10 %) | +1.1 pts | -2.6 pts |
| Hors altseason | 633 | 48% | 24% (hasard : 10 %) | +5.0 pts | -1.1 pts |
| **En direct** (depuis le 29/09/2026) | 173 | 45% | 23% (hasard : 10 %) | +2.6 pts | -1.9 pts |
| Reconstitués (avant le 29/09/2026) | 950 | 48% | 23% (hasard : 10 %) | +4.6 pts | -1.2 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **BEAMX** | Speculative | +70% | 52.5% | ⚠️ 7 |
| 2 | **HAEDAL** | Speculative | +54% | 41.4% | ⚠️ 6 |
| 3 | **PARTI** | Speculative | +51% | 56.9% | ⚠️ 4 |
| 4 | **MEGA** | Mid | +24% | 45.5% | 2 |
| 5 | **ERA** | Speculative | +23% | 41.6% | 2 |
| 6 | **GMX** | Mid | +14% | 46.3% | 2 |
| 7 | **BABY** | Mid | +11% | 45.6% | 2 |
| 8 | **JST** | Etabli | +7% | 55.5% | ⚠️ 5 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : INIT, PEPE, WIN. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée est le taux de réussite **réellement observé** pour la tranche de classement du token.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-06-01 au 2026-09-28 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 68% | +0.210 |
| Règle simple | 68% | +0.177 |
| Mélange ✅ | 67% | +0.209 |

⚠️ Sur cette période, le token médian a fait **+1.7 %** en 30 j et seuls **50%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `runup180` (−), `vtrend` (−), `dd90` (−), `r90` (+)

**Suivi réel** : 345 prédictions en attente — premiers résultats à partir du 11 nov 2026.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **TRX** | Etabli | 68 % | 56.4 % | -1 % |
| 2 | **BTC** | Etabli | 67 % | 58.1 % | -2 % |
| 3 | **BNB** | Etabli | 67 % | 57.1 % | -1 % |
| 4 | **ASTER** | Etabli | 67 % | 59.3 % | +2 % |
| 5 | **SOL** | Etabli | 67 % | 60.3 % | -14 % |
| 6 | **WLFI** | Etabli | 67 % | 56.8 % | -7 % |
| 7 | **ETH** | Etabli | 67 % | 61.3 % | -12 % |
| 8 | **JST** | Etabli | 67 % | 55.5 % | +7 % |
| 9 | **DOGE** | Etabli | 67 % | 57.2 % | -14 % |
| 10 | **NEXO** | Etabli | 67 % | 60.3 % | -6 % |
| 11 | **SUN** | Mid | 66 % | 57.3 % | -5 % |
| 12 | **LTC** | Etabli | 66 % | 56.7 % | -17 % |

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
| 2026-10-23 | **TAO** | S-1/A | Grayscale Bittensor Trust (TAO)  (GTAO) | -3% (+1 pts) |
| 2026-10-23 | **INJ** | S-1/A | Canary Staked INJ ETF | -1% (+2 pts) |
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | +9% (+27 pts) |

**Tokens avec un ETF en préparation ou en lancement :** TAO (📝 S-1/A le 2026-10-23), INJ (📝 S-1/A le 2026-10-23), PEPE (📝 S-1/A le 2026-10-02), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), LTC (📝 S-3/A le 2026-09-11), BCH (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 26 | +0.080 | 50% | 52% | 50% | 52% | 51% | 43% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 22 oct 2026 | 🟡 Neutre | 53 | -4.8% | DOGE, WIN, BTC |
| 23 oct 2026 | 🟡 Neutre | 40 | -4.5% | BTC, TAO, XRP |
| 24 oct 2026 | 🟡 Neutre | 34 | -3.5% | TAO, XRP, BTC |
| 25 oct 2026 | 🟠 Bitcoin domine (court terme) | 20 | -4.7% | DOGE, ETH, ADA |
| 26 oct 2026 | 🟠 Bitcoin domine (court terme) | 20 | -5.4% | BTC, ETH, SHIB |
| 27 oct 2026 | 🟠 Bitcoin domine (court terme) | 18 | -5.3% | SOL, ETH, BTC |
| 28 oct 2026 | 🟠 Bitcoin domine (court terme) | 17 | -2.4% | ETH, SOL, NEXO |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.4% (28 oct 2026) — -36.7% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.3% (28 oct 2026) — +6.7% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 57.1% (28 oct 2026) — -12.2% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 48.3% (28 oct 2026) — +24.5% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 56.3% (28 oct 2026) — -19.1% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **51790 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0244 |
| momentum | 0.0054 |
| risk | 0.0125 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 28 oct 2026

**Régime :** 🟠 Bitcoin domine (court terme) (indice altseason 30 j : 17.2)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **ETH** | Etabli | 61.3% | +3.2pp | ⚠️ 5 |  |
| **SOL** | Etabli | 60.3% | +2.2pp | 3 |  |
| **NEXO** | Etabli | 60.3% | +2.2pp | 3 |  |
| **ASTER** | Etabli | 59.3% | +1.2pp | 2 |  |
| **ETC** | Etabli | 59.1% | +1.0pp | 3 |  |
| **SHIB** | Etabli | 58.9% | +0.8pp | ⚠️ 5 |  |
| **XRP** | Etabli | 58.8% | +0.7pp | 2 |  |
| **ADA** | Etabli | 58.3% | +0.2pp | 3 |  |
| **XLM** | Etabli | 58.3% | +0.2pp | 3 |  |
| **BTC** | Etabli | 58.1% | +0.0pp | 3 | 🔥 Trending #7 sur CoinGecko |
| **TAO** | Etabli | 57.6% | -0.5pp | 3 |  |
| **GNO** | Mid | 57.6% | -0.5pp | 3 |  |
