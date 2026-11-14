# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 14 nov 2026*

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

- **Indice altseason** : 27.3 sur 30 j, 48.0 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC)
- **BTC** : -17.5 % sur 30 j · **Tokens au-dessus de leur MA50** : 3.3 %
- *Échelle : indice 90 j ≥ 75 → 🚀 Altseason ; indice 30 j ≥ 75 → 🌱 Altseason en formation ; indice 30 j ≥ 60 → 🌤️ Altseason modérée ; ≤ 25 → saison Bitcoin.*
- **Le « mode altseason » du classement est abandonné depuis le 11/11/2026.** Il ajoutait du momentum quand l'indice dépassait 60 : en réel, 51 % de réussite quand il était actif contre 68 % sinon. Sur 2,6 ans de cours, un indice élevé a été suivi des PIRES mois pour les altcoins : l'indice sert maintenant de thermomètre, plus à modifier le classement.
- **Thermomètre (941 jours de cours) : Contexte un peu moins défavorable aux altcoins que d'habitude.** Indice altseason à 19 % (tranche 0–25 %). Les 340 jours passés dans cette tranche ont été suivis, sur 30 j, d'une altcoin médiane à -2.3 % (BTC +2.7 %) ; 36 % des altcoins ont battu BTC (moyenne toutes périodes : 30 %).
- **Taux de base à garder en tête :** sur 30 j, l'altcoin médiane fait -6.6 % et BTC +1.5 % ; seules 30 % des altcoins battent BTC (38 % sur 7 j). L'adversaire à battre, c'est BTC, pas « la médiane du marché ».

### Ma méthode aujourd'hui : mélange modèle + règle (`ml_blend`)

- Modèle entraîné sur 71491 observations (181 jours), horizon 7 j ; depuis le 11/11/2026 le classement est le **mélange** du modèle et de la règle simple « grosse cap peu volatile » (plus régulier mois après mois que l'un ou l'autre seul).

**Analyse des erreurs — 126 jours rejoués** (chaque semaine prédite uniquement avec des données antérieures) ; top 20 jugé à 7 j contre trois adversaires :

| Méthode | Bat la médiane du marché | Bat BTC | A monté | Les 20 derniers battent la médiane |
|---|---|---|---|---|
| **Mélange (utilisé)** | 64% | 40% | 42% | 36% |
| Modèle appris seul | 62% | 42% | 44% | 34% |
| Règle simple seule | 66% | 41% | 44% | 42% |
| *Un token pris au hasard* | *50%* | *38%* | *41%* | *50%* |

*Lecture honnête : le classement sait écarter les mauvais tokens (les 20 derniers font nettement moins bien que le hasard), mais son top 20 ne bat pas BTC plus d'une fois sur deux. Il sert à choisir PARMI les altcoins, pas à décider d'en détenir.*

- 96 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `catalyst_score` (−), `rsi_14` (+), `vol_30d_ann` (−), `p_ma50` (−), `pat_double_bottom_90d` (+), `pat_bear_flag` (−)

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 45.3%
**Signaux baissiers fiables (>50%) :** 11 / 11

**Mon top 20 quotidien, jugé à 7 j — toutes méthodes confondues depuis mai (ancienne formule incluse) :** 3663 prédictions mesurées — 40% ont monté, 52% ont battu la médiane du marché (50% = hasard)

**Modèle appris (depuis le 26/09/2026 ; mélangé à la règle simple depuis le 11/11/2026) :** 903 prédictions mesurées sur 43 jours — 19% ont monté, **57% ont battu la médiane du marché**

### ✅ En conditions réelles, mon classement bat le marché (57% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `breakdown_30d` | 67.3% | 263 | 📈 |
| `double_top_90d` | 65.2% | 4745 | → |
| `evening_star_4h` | 63.5% | 1248 | → |
| `bearish_engulfing_4h` | 61.7% | 1383 | 📈 |
| `downtrend` | 60.3% | 20706 | → |
| `shooting_star_4h` | 56.9% | 397 | 📈 |
| `macd_bearish_cross` | 56.6% | 10679 | → |
| `rsi_bearish_divergence` | 56.6% | 2041 | → |
| `death_cross` | 56.1% | 501 | → |
| `bear_flag` | 53.3% | 674 | 📈 |
| `resistance_test` | 52.9% | 2799 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 45.3% | 644 | 📉 |
| `double_bottom_90d` | 42.6% | 2919 | → |
| `macd_bullish_cross` | 41.3% | 10853 | → |
| `hammer_4h` | 40.7% | 413 | → |
| `support_bounce` | 40.1% | 3146 | → |
| `uptrend` | 40.1% | 17873 | → |
| `bullish_engulfing_4h` | 38.6% | 1581 | 📉 |
| `rsi_bullish_divergence` | 36.8% | 3246 | 📉 |
| `morning_star_4h` | 36.2% | 1090 | → |
| `bull_flag` | 35.2% | 418 | → |
| `breakout_30d` | 34.3% | 645 | → |
| `golden_cross` | 31.5% | 1529 | → |

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
| 2026-11 | Modèle appris | 140 | 6% | 53% | -8.2% |

**Modèle appris selon le régime de marché** (indice altseason 30 j le jour de la prédiction ; mode altseason actif à partir de 60) :

| Régime le jour de la prédiction | Jours | Prédictions | Ont battu le marché (7 j) | Return médian (7 j) |
|---|---|---|---|---|
| Mode altseason actif (indice ≥ 60) | 22 | 475 | 51% | -4.5% |
| Mode altseason inactif (indice < 60) | 21 | 428 | 64% | -5.0% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 7 nov 2026 | **XRP** | 62% | 1.1661 | -14.6% | ❌ -3.1pp | … |
| 7 nov 2026 | **DOGE** | 61% | 0.07198 | -13.1% | ❌ -1.6pp | … |
| 7 nov 2026 | **SOL** | 61% | 90.04 | -16.0% | ❌ -4.5pp | … |
| 7 nov 2026 | **XLM** | 59% | 0.1525 | -6.8% | ✅ +4.7pp | … |
| 7 nov 2026 | **SHIB** | 59% | 4.51e-06 | -8.4% | ✅ +3.1pp | … |
| 7 nov 2026 | **ADA** | 59% | 0.1831 | -12.0% | ❌ -0.5pp | … |
| 7 nov 2026 | **BTC** | 57% | 75929.8 | -12.0% | ❌ -0.5pp | … |
| 7 nov 2026 | **ENS** | 57% | 4.59 | -10.7% | ✅ +0.8pp | … |
| 7 nov 2026 | **ETC** | 57% | 6.96 | -9.8% | ✅ +1.7pp | … |
| 7 nov 2026 | **PEPE** | 57% | 4.96e-06 | -14.1% | ❌ -2.6pp | … |
| 7 nov 2026 | **WIF** | 57% | 0.161 | -11.5% | ❌ +0.0pp | … |
| 7 nov 2026 | **ETH** | 56% | 2243.82 | -15.7% | ❌ -4.2pp | … |
| 7 nov 2026 | **WLD** | 56% | 0.3406 | -18.6% | ❌ -7.1pp | … |
| 7 nov 2026 | **ONDO** | 56% | 0.3669 | -11.6% | ❌ -0.1pp | … |
| 7 nov 2026 | **NEXO** | 56% | 0.735 | -7.1% | ✅ +4.4pp | … |
| 7 nov 2026 | **JST** | 56% | 0.14296 | +2.0% | ✅ +13.4pp | … |
| 7 nov 2026 | **ORDI** | 56% | 3.246 | -8.1% | ✅ +3.4pp | … |
| 7 nov 2026 | **HBAR** | 56% | 0.06772 | -10.8% | ✅ +0.7pp | … |
| 7 nov 2026 | **FLOKI** | 56% | 2.151e-05 | -11.1% | ✅ +0.4pp | … |
| 7 nov 2026 | **WIN** | 56% | 6.435e-05 | -12.1% | ❌ -0.6pp | … |

**142 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. Le backtest initial (juin→sept. 2026) annonçait 67 % de réussite en altseason ; le suivi réel ci-dessous ne le confirme pas : jugez sur la ligne « En direct ».*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1207 | 48% | 24% (hasard : 10 %) | +4.7 pts | -1.1 pts |
| Altseason (indice 30 j ≥ 60) | 398 | 45% | 20% (hasard : 10 %) | +3.5 pts | -2.3 pts |
| Hors altseason | 799 | 50% | 27% (hasard : 10 %) | +5.5 pts | -0.0 pts |
| Régime inconnu (indice pas encore calculable) | 10 | 30% | 10% (hasard : 10 %) | -5.7 pts | -9.3 pts |
| **En direct** (depuis le 29/09/2026) | 257 | 50% | 30% (hasard : 10 %) | +5.3 pts | +0.0 pts |
| Reconstitués (avant le 29/09/2026) | 950 | 48% | 23% (hasard : 10 %) | +4.6 pts | -1.2 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **JST** | Etabli | +9% | 58.9% | ⚠️ 4 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : DODO, NIGHT. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée découle du **rang** du token : c'est le taux de réussite **réellement observé** pour ce niveau de classement (courbe lissée rang → réussite, ajustée sur les 120 jours de test). Deux tokens voisins dans le classement ont donc des probabilités voisines (≈ 0,1 pt d'écart par rang) : c'est voulu, ce n'est pas une sortie brute du modèle.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-06-18 au 2026-10-15 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 69% | +0.225 |
| Règle simple | 70% | +0.192 |
| Mélange ✅ | 70% | +0.226 |

⚠️ Sur cette période, le token médian a fait **-0.9 %** en 30 j et seuls **46%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `vtrend` (−), `dd90` (−), `runup180` (−), `r90` (+)

**Suivi réel (jugé à 30 j)** : 82 prédictions — **82% ont battu le marché**, 6% ont monté, return médian -19.8 %.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **TRX** | Etabli | 71 % | 58.8 % | -6 % |
| 2 | **SOL** | Etabli | 71 % | 59.0 % | -26 % |
| 3 | **BTC** | Etabli | 71 % | 59.0 % | -18 % |
| 4 | **BNB** | Etabli | 70 % | 59.1 % | -16 % |
| 5 | **JST** | Etabli | 70 % | 58.9 % | +9 % |
| 6 | **ETH** | Etabli | 70 % | 58.7 % | -20 % |
| 7 | **SUN** | Mid | 70 % | 58.1 % | -8 % |
| 8 | **WLFI** | Etabli | 70 % | 52.7 % | -16 % |
| 9 | **ASTER** | Etabli | 70 % | 57.7 % | -8 % |
| 10 | **DOGE** | Etabli | 70 % | 58.9 % | -22 % |
| 11 | **XRP** | Etabli | 70 % | 58.5 % | -24 % |
| 12 | **NEXO** | Etabli | 69 % | 58.0 % | -16 % |

---

## 📑 Annonces d'ETF crypto (SEC EDGAR)

*Tout ETF crypto américain dépose ses documents à la SEC avant son lancement : dossier S-1/S-3 et ses amendements, puis enregistrement en bourse (8-A12B) quelques jours avant la cotation. ZEC et NEAR ont fortement monté autour de leurs ETF. Étude du 29/09/2026 : après un dépôt de dossier, 75 % des tokens ont battu le marché à 7 et 14 j ; avant un 8-A12B, la hausse était souvent déjà faite (+33 pts sur les 14 j précédents). Petit échantillon : suivi réel ci-dessous.*

*« En direct » = dépôts publiés depuis le début du suivi (29/09/2026) ; « reconstitué » = dépôts antérieurs retrouvés après coup dans l'historique de la SEC. Seuls les cas en direct comptent pour juger l'idée.*

*Les pourcentages indiquent entre parenthèses le nombre de cas réellement mesurés à cet horizon (un dépôt récent n'est pas encore mesurable à 14 j).*

| Type de dépôt | Suivi | Événements | Battent le marché à 7 j | Excès médian 7 j | Battent le marché à 14 j | Excès médian 14 j |
|---|---|---|---|---|---|---|
| Dossier / amendement (S-1, S-3) | **En direct** | 4 | 25% (1/4) | -0.9 pts | 67% (2/3) | +2.6 pts |
| Dossier / amendement (S-1, S-3) | Reconstitué | 34 | 76% (26/34) | +3.7 pts | 81% (26/32) | +5.3 pts |
| Enregistrement en bourse (8-A12B) | **En direct** | 2 | 100% (2/2) | +8.7 pts | 0% (0/1) | -1.5 pts |
| Enregistrement en bourse (8-A12B) | Reconstitué | 9 | 56% (5/9) | +2.2 pts | 67% (6/9) | +2.7 pts |

**Dépôts des 30 derniers jours :**

| Date | Token | Dépôt | Fonds | Depuis le dépôt (vs marché) |
|---|---|---|---|---|
| 2026-11-03 | **INJ** | 8-A12B | Canary Staked INJ ETF | +5% (+20 pts) |
| 2026-11-02 | **INJ** | S-1/A | Canary Staked INJ ETF | +10% (+25 pts) |
| 2026-10-28 | **SEI** | 8-A12B | SEI Exchange Traded Funds | -23% (-2 pts) |
| 2026-10-23 | **TAO** | S-1/A | Grayscale Bittensor Trust (TAO)  (GTAO) | -21% (+3 pts) |
| 2026-10-23 | **INJ** | S-1/A | Canary Staked INJ ETF | -3% (+21 pts) |

**Tokens avec un ETF en préparation ou en lancement :** INJ (🟢 8-A12B le 2026-11-03), SEI (🟢 8-A12B le 2026-10-28), TAO (📝 S-1/A le 2026-10-23), PEPE (📝 S-1/A le 2026-10-02), NEAR (🟢 8-A12B le 2026-09-24)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 43 | +0.078 | 56% | 54% | 49% | 52% | 51% | 43% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 53.3% (14 nov 2026) — -31.8% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 36.8% (14 nov 2026) — +0.2% →
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 60.3% (14 nov 2026) — -9.0% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 45.3% (14 nov 2026) — +21.5% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 56.6% (14 nov 2026) — -18.8% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers sont **bloqués** sous 40% : je ne suis pas encore fiable pour détecter les hausses.

---

## Le score composite est-il utile ?

J'ai analysé **57455 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0280 |
| momentum | 0.0116 |
| risk | 0.0148 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 14 nov 2026

**Régime :** 🟡 Neutre (indice altseason 30 j : 27.3)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **BNB** | Etabli | 59.1% | +0.1pp | 1 |  |
| **SOL** | Etabli | 59.0% | +0.0pp | 1 | 🔥 Trending #3 sur CoinGecko |
| **BTC** | Etabli | 59.0% | +0.0pp | 3 | 🔥 Trending #2 sur CoinGecko |
| **JST** | Etabli | 58.9% | -0.1pp | ⚠️ 4 |  |
| **DOGE** | Etabli | 58.9% | -0.1pp | 3 |  |
| **HBAR** | Etabli | 58.8% | -0.2pp | 1 |  |
| **TRX** | Etabli | 58.8% | -0.2pp | ⚠️ 5 |  |
| **BCH** | Etabli | 58.7% | -0.3pp | 3 |  |
| **ETH** | Etabli | 58.7% | -0.3pp | 1 | 🔥 Trending #5 sur CoinGecko |
| **LTC** | Etabli | 58.6% | -0.4pp | 3 |  |
| **ADA** | Etabli | 58.6% | -0.4pp | 3 |  |
| **XRP** | Etabli | 58.5% | -0.5pp | 1 |  |
