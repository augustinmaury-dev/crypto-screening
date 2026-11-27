# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 27 nov 2026*

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

- **Indice altseason** : 36.0 sur 30 j, 59.6 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC)
- **BTC** : -25.8 % sur 30 j · **Tokens au-dessus de leur MA50** : 4.9 %
- *Échelle : indice 90 j ≥ 75 → 🚀 Altseason ; indice 30 j ≥ 75 → 🌱 Altseason en formation ; indice 30 j ≥ 60 → 🌤️ Altseason modérée ; ≤ 25 → saison Bitcoin.*
- **Le « mode altseason » du classement est abandonné depuis le 11/11/2026.** Il ajoutait du momentum quand l'indice dépassait 60 : en réel, 51 % de réussite quand il était actif contre 68 % sinon. Sur 2,6 ans de cours, un indice élevé a été suivi des PIRES mois pour les altcoins : l'indice sert maintenant de thermomètre, plus à modifier le classement.
- **Thermomètre (941 jours de cours) : Contexte habituel : BTC reste difficile à battre.** Indice altseason à 32 % (tranche 25–45 %). Les 308 jours passés dans cette tranche ont été suivis, sur 30 j, d'une altcoin médiane à -6.1 % (BTC +2.6 %) ; 29 % des altcoins ont battu BTC (moyenne toutes périodes : 30 %).
- **Taux de base à garder en tête :** sur 30 j, l'altcoin médiane fait -7.1 % et BTC +1.1 % ; seules 30 % des altcoins battent BTC (38 % sur 7 j). L'adversaire à battre, c'est BTC, pas « la médiane du marché ».

### Ma méthode aujourd'hui : mélange modèle + règle (`ml_blend`)

- Modèle entraîné sur 76574 observations (194 jours), horizon 7 j ; depuis le 11/11/2026 le classement est le **mélange** du modèle et de la règle simple « grosse cap peu volatile » (plus régulier mois après mois que l'un ou l'autre seul).

**Analyse des erreurs — 126 jours rejoués** (chaque semaine prédite uniquement avec des données antérieures) ; top 20 jugé à 7 j contre trois adversaires :

| Méthode | Bat la médiane du marché | Bat BTC | A monté | Les 20 derniers battent la médiane |
|---|---|---|---|---|
| **Mélange (utilisé)** | 62% | 43% | 38% | 36% |
| Modèle appris seul | 59% | 44% | 40% | 36% |
| Règle simple seule | 64% | 44% | 40% | 43% |
| *Un token pris au hasard* | *50%* | *41%* | *39%* | *50%* |

*Lecture honnête : le classement sait écarter les mauvais tokens (les 20 derniers font nettement moins bien que le hasard), mais son top 20 ne bat pas BTC plus d'une fois sur deux. Il sert à choisir PARMI les altcoins, pas à décider d'en détenir.*

- 105 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `catalyst_score` (−), `vol_30d_ann` (−), `rsi_14` (+), `pat_double_bottom_90d` (+), `p_ma50` (−), `pat_bear_flag` (−)

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 43.8%
**Signaux baissiers fiables (>50%) :** 11 / 11

**Mon top 20 quotidien, jugé à 7 j — toutes méthodes confondues depuis mai (ancienne formule incluse) :** 3925 prédictions mesurées — 38% ont monté, 51% ont battu la médiane du marché (50% = hasard)

**Modèle appris (depuis le 26/09/2026 ; mélangé à la règle simple depuis le 11/11/2026) :** 1165 prédictions mesurées sur 56 jours — 17% ont monté, **55% ont battu la médiane du marché**

### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché (55% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `breakdown_30d` | 69.7% | 327 | 📈 |
| `double_top_90d` | 67.7% | 5228 | → |
| `evening_star_4h` | 65.2% | 1355 | → |
| `bearish_engulfing_4h` | 64.8% | 1593 | 📈 |
| `downtrend` | 64.6% | 23808 | 📈 |
| `death_cross` | 62.6% | 613 | 📈 |
| `shooting_star_4h` | 60.0% | 433 | 📈 |
| `macd_bearish_cross` | 58.1% | 11332 | → |
| `rsi_bearish_divergence` | 56.9% | 2067 | → |
| `bear_flag` | 53.7% | 693 | → |
| `resistance_test` | 52.8% | 2931 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 43.8% | 691 | → |
| `double_bottom_90d` | 42.1% | 2958 | → |
| `uptrend` | 39.4% | 18378 | → |
| `macd_bullish_cross` | 39.1% | 11672 | → |
| `hammer_4h` | 38.7% | 437 | → |
| `support_bounce` | 37.6% | 3438 | → |
| `bullish_engulfing_4h` | 35.3% | 1773 | → |
| `bull_flag` | 35.1% | 419 | → |
| `breakout_30d` | 34.2% | 653 | → |
| `morning_star_4h` | 33.9% | 1180 | → |
| `golden_cross` | 30.7% | 1577 | → |
| `rsi_bullish_divergence` | 30.6% | 4048 | 📉 |

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
| 2026-10 | Modèle appris | 633 | 16% | 59% | -4.7% |
| 2026-11 | Modèle appris | 402 | 9% | 50% | -8.5% |

**Modèle appris selon le régime de marché** (indice altseason 30 j le jour de la prédiction ; mode altseason actif à partir de 60) :

| Régime le jour de la prédiction | Jours | Prédictions | Ont battu le marché (7 j) | Return médian (7 j) |
|---|---|---|---|---|
| Mode altseason actif (indice ≥ 60) | 22 | 475 | 51% | -4.5% |
| Mode altseason inactif (indice < 60) | 34 | 690 | 58% | -6.1% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 20 nov 2026 | **JST** | 58% | 0.1445 | +1.6% | ❌ -2.4pp | … |
| 20 nov 2026 | **TRX** | 58% | 0.3033 | -0.8% | ❌ -4.8pp | … |
| 20 nov 2026 | **HBAR** | 58% | 0.0513 | +4.6% | ✅ +0.6pp | … |
| 20 nov 2026 | **SUN** | 58% | 0.01467 | -1.8% | ❌ -5.8pp | … |
| 20 nov 2026 | **GNO** | 58% | 94.03 | -8.2% | ❌ -12.2pp | … |
| 20 nov 2026 | **WLFI** | 58% | 0.0446 | -15.2% | ❌ -19.3pp | … |
| 20 nov 2026 | **ETC** | 58% | 5.39 | +8.9% | ✅ +4.9pp | … |
| 20 nov 2026 | **IOTA** | 58% | 0.0298 | +8.4% | ✅ +4.4pp | … |
| 20 nov 2026 | **LTC** | 58% | 39.96 | +9.1% | ✅ +5.1pp | … |
| 20 nov 2026 | **FF** | 58% | 0.10219 | -3.7% | ❌ -7.7pp | … |
| 20 nov 2026 | **币安人生** | 58% | 0.4286 | +5.7% | ✅ +1.6pp | … |
| 20 nov 2026 | **EGLD** | 57% | 2.254 | +1.9% | ❌ -2.1pp | … |
| 20 nov 2026 | **ENS** | 57% | 3.52 | -1.4% | ❌ -5.4pp | … |
| 20 nov 2026 | **FLOKI** | 57% | 1.618e-05 | +1.6% | ❌ -2.4pp | … |
| 20 nov 2026 | **DCR** | 57% | 9.99 | +4.4% | ✅ +0.4pp | … |
| 20 nov 2026 | **GAS** | 57% | 0.905 | +6.2% | ✅ +2.2pp | … |
| 20 nov 2026 | **BCH** | 57% | 191.4 | +7.0% | ✅ +3.0pp | … |
| 20 nov 2026 | **MORPHO** | 57% | 1.492 | +9.1% | ✅ +5.0pp | … |
| 20 nov 2026 | **SUPER** | 57% | 0.1136 | +4.5% | ✅ +0.5pp | … |
| 20 nov 2026 | **BTTC** | 57% | 3.1e-07 | +0.0% | ❌ -4.0pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. Le backtest initial (juin→sept. 2026) annonçait 67 % de réussite en altseason ; le suivi réel ci-dessous ne le confirme pas : jugez sur la ligne « En direct ».*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1239 | 49% | 25% (hasard : 10 %) | +4.8 pts | -0.7 pts |
| Altseason (indice 30 j ≥ 60) | 398 | 45% | 20% (hasard : 10 %) | +3.5 pts | -2.3 pts |
| Hors altseason | 831 | 51% | 28% (hasard : 10 %) | +5.6 pts | +0.3 pts |
| Régime inconnu (indice pas encore calculable) | 10 | 30% | 10% (hasard : 10 %) | -5.7 pts | -9.3 pts |
| **En direct** (depuis le 29/09/2026) | 289 | 52% | 33% (hasard : 10 %) | +5.7 pts | +1.1 pts |
| Reconstitués (avant le 29/09/2026) | 950 | 48% | 23% (hasard : 10 %) | +4.6 pts | -1.2 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **OPG** | Mid | +41% | 51.3% | 2 |
| 2 | **JST** | Etabli | +4% | 56.8% | 3 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : NIGHT, PORTAL. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée découle du **rang** du token : c'est le taux de réussite **réellement observé** pour ce niveau de classement (courbe lissée rang → réussite, ajustée sur les 120 jours de test). Deux tokens voisins dans le classement ont donc des probabilités voisines (≈ 0,1 pt d'écart par rang) : c'est voulu, ce n'est pas une sortie brute du modèle.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-07-01 au 2026-10-28 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 71% | +0.225 |
| Règle simple | 72% | +0.185 |
| Mélange ✅ | 72% | +0.223 |

⚠️ Sur cette période, le token médian a fait **-3.1 %** en 30 j et seuls **42%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `vtrend` (−), `dd90` (−), `size` (+), `r90` (+)

**Suivi réel (jugé à 30 j)** : 345 prédictions — **77% ont battu le marché**, 5% ont monté, return médian -24.9 %.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **TRX** | Etabli | 72 % | 56.7 % | -9 % |
| 2 | **ETH** | Etabli | 72 % | 56.7 % | -29 % |
| 3 | **SOL** | Etabli | 72 % | 56.7 % | -29 % |
| 4 | **BTC** | Etabli | 71 % | 56.8 % | -26 % |
| 5 | **BNB** | Etabli | 71 % | 56.7 % | -26 % |
| 6 | **XRP** | Etabli | 71 % | 56.6 % | -28 % |
| 7 | **WLFI** | Etabli | 71 % | 56.4 % | -27 % |
| 8 | **ACM** | Speculative | 71 % | 54.4 % | -17 % |
| 9 | **JST** | Etabli | 71 % | 56.8 % | +4 % |
| 10 | **SUN** | Mid | 70 % | 56.5 % | -11 % |
| 11 | **DOGE** | Etabli | 70 % | 56.5 % | -27 % |
| 12 | **NEXO** | Etabli | 70 % | 56.6 % | -23 % |

---

## 📑 Annonces d'ETF crypto (SEC EDGAR)

*Tout ETF crypto américain dépose ses documents à la SEC avant son lancement : dossier S-1/S-3 et ses amendements, puis enregistrement en bourse (8-A12B) quelques jours avant la cotation. ZEC et NEAR ont fortement monté autour de leurs ETF. Étude du 29/09/2026 : après un dépôt de dossier, 75 % des tokens ont battu le marché à 7 et 14 j ; avant un 8-A12B, la hausse était souvent déjà faite (+33 pts sur les 14 j précédents). Petit échantillon : suivi réel ci-dessous.*

*« En direct » = dépôts publiés depuis le début du suivi (29/09/2026) ; « reconstitué » = dépôts antérieurs retrouvés après coup dans l'historique de la SEC. Seuls les cas en direct comptent pour juger l'idée.*

*Les pourcentages indiquent entre parenthèses le nombre de cas réellement mesurés à cet horizon (un dépôt récent n'est pas encore mesurable à 14 j).*

| Type de dépôt | Suivi | Événements | Battent le marché à 7 j | Excès médian 7 j | Battent le marché à 14 j | Excès médian 14 j |
|---|---|---|---|---|---|---|
| Dossier / amendement (S-1, S-3) | **En direct** | 4 | 25% (1/4) | -0.9 pts | 75% (3/4) | +8.6 pts |
| Dossier / amendement (S-1, S-3) | Reconstitué | 34 | 76% (26/34) | +3.7 pts | 81% (26/32) | +5.3 pts |
| Enregistrement en bourse (8-A12B) | **En direct** | 2 | 100% (2/2) | +8.7 pts | 50% (1/2) | +8.0 pts |
| Enregistrement en bourse (8-A12B) | Reconstitué | 9 | 56% (5/9) | +2.2 pts | 67% (6/9) | +2.7 pts |

**Dépôts des 30 derniers jours :**

| Date | Token | Dépôt | Fonds | Depuis le dépôt (vs marché) |
|---|---|---|---|---|
| 2026-11-03 | **INJ** | 8-A12B | Canary Staked INJ ETF | -14% (+8 pts) |
| 2026-11-02 | **INJ** | S-1/A | Canary Staked INJ ETF | -10% (+12 pts) |
| 2026-10-28 | **SEI** | 8-A12B | SEI Exchange Traded Funds | -28% (-1 pts) |

**Tokens avec un ETF en préparation ou en lancement :** INJ (🟢 8-A12B le 2026-11-03), SEI (🟢 8-A12B le 2026-10-28), TAO (📝 S-1/A le 2026-10-23), PEPE (📝 S-1/A le 2026-10-02)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 56 | +0.053 | 55% | 53% | 49% | 52% | 51% | 45% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
| 29 oct 2026 | 🟠 Bitcoin domine (court terme) | 18 | -3.9% | BTC, NEXO, ASTER |
| 30 oct 2026 | 🟠 Bitcoin domine (court terme) | 14 | -8.4% | ETH, SOL, XRP |
| 31 oct 2026 | 🟠 Bitcoin domine (court terme) | 18 | -7.4% | XRP, SOL, ADA |
| 1 nov 2026 | 🟠 Bitcoin domine (court terme) | 15 | -10.1% | ETH, DOGE, ALGO |
| 2 nov 2026 | 🟠 Bitcoin domine (court terme) | 13 | -8.4% | SOL, WIN, DOGE |
| 3 nov 2026 | 🟠 Bitcoin domine (court terme) | 12 | -9.2% | SOL, ETH, DOGE |
| 4 nov 2026 | 🟠 Bitcoin domine (court terme) | 13 | -7.3% | ETH, ADA, TAO |
| 5 nov 2026 | 🟠 Bitcoin domine (court terme) | 11 | -10.3% | TAO, SOL, ADA |
| 6 nov 2026 | 🟠 Bitcoin domine (court terme) | 17 | -9.0% | XLM, SHIB, SOL |
| 7 nov 2026 | 🟠 Bitcoin domine (court terme) | 11 | -8.0% | XRP, DOGE, SOL |
| 8 nov 2026 | 🟠 Bitcoin domine (court terme) | 14 | -8.1% | SOL, DOGE, XRP |
| 9 nov 2026 | 🟠 Bitcoin domine (court terme) | 15 | -9.4% | DOGE, XRP, SOL |
| 10 nov 2026 | 🟠 Bitcoin domine (court terme) | 13 | -10.3% | SOL, DOGE, XRP |
| 11 nov 2026 | 🟠 Bitcoin domine (court terme) | 13 | -10.7% | SOL, BTC, ETH |
| 12 nov 2026 | 🟠 Bitcoin domine (court terme) | 15 | -14.7% | BTC, SOL, BNB |
| 13 nov 2026 | 🟡 Neutre | 25 | -16.8% | DOGE, SOL, TRX |
| 14 nov 2026 | 🟡 Neutre | 27 | -17.5% | BNB, SOL, BTC |
| 15 nov 2026 | 🟠 Bitcoin domine (court terme) | 14 | -21.2% | JST, ETH, DOGE |
| 16 nov 2026 | 🟠 Bitcoin domine (court terme) | 18 | -20.8% | JST, HBAR, XLM |
| 17 nov 2026 | 🟠 Bitcoin domine (court terme) | 24 | -22.2% | JST, BNB, ETH |
| 18 nov 2026 | 🟡 Neutre | 29 | -23.3% | JST, BNB, NEXO |
| 19 nov 2026 | 🟠 Bitcoin domine (court terme) | 24 | -23.5% | JST, TRX, BNB |
| 20 nov 2026 | 🟠 Bitcoin domine (court terme) | 18 | -28.7% | JST, TRX, SUN |
| 21 nov 2026 | 🟠 Bitcoin domine (court terme) | 17 | -26.2% | JST, TRX, WLFI |
| 22 nov 2026 | 🟠 Bitcoin domine (court terme) | 22 | -25.3% | JST, GPS, WLFI |
| 23 nov 2026 | 🟡 Neutre | 32 | -23.9% | JST, SUN, NEXO |
| 24 nov 2026 | 🟡 Neutre | 32 | -25.3% | JST, GPS, SUN |
| 25 nov 2026 | 🟡 Neutre | 27 | -25.0% | JST, TRX, SUN |
| 26 nov 2026 | 🟡 Neutre | 32 | -24.8% | JST, TRX, BTC |
| 27 nov 2026 | 🟡 Neutre | 36 | -25.8% | JST, BTC, TRX |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 53.7% (27 nov 2026) — -31.4% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 30.6% (27 nov 2026) — -6.0% 📉
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 64.6% (27 nov 2026) — -4.7% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 43.8% (27 nov 2026) — +20.0% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 56.9% (27 nov 2026) — -18.5% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **reculent** : dans ce marché, les patterns d'achat ne fonctionnent pas encore.

---

## Le score composite est-il utile ?

J'ai analysé **62375 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0281 |
| momentum | 0.0333 |
| risk | 0.0344 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 27 nov 2026

**Régime :** 🟡 Neutre (indice altseason 30 j : 36.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **JST** | Etabli | 56.8% | +0.0pp | 3 |  |
| **BTC** | Etabli | 56.8% | +0.0pp | 0 | 🔥 Trending #4 sur CoinGecko |
| **TRX** | Etabli | 56.7% | -0.1pp | 0 |  |
| **ETH** | Etabli | 56.7% | -0.1pp | 0 |  |
| **SOL** | Etabli | 56.7% | -0.1pp | 0 | 🔥 Trending #13 sur CoinGecko |
| **BNB** | Etabli | 56.7% | -0.1pp | 1 |  |
| **NEXO** | Etabli | 56.6% | -0.2pp | 1 |  |
| **XRP** | Etabli | 56.6% | -0.2pp | 0 | 🔥 Trending #7 sur CoinGecko |
| **SHIB** | Etabli | 56.6% | -0.2pp | 2 |  |
| **SUN** | Mid | 56.5% | -0.3pp | 2 |  |
| **XLM** | Etabli | 56.5% | -0.3pp | 0 |  |
| **DOGE** | Etabli | 56.5% | -0.3pp | 0 |  |
