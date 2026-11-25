# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 25 nov 2026*

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

- **Indice altseason** : 27.3 sur 30 j, 48.5 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC)
- **BTC** : -25.0 % sur 30 j · **Tokens au-dessus de leur MA50** : 4.1 %
- *Échelle : indice 90 j ≥ 75 → 🚀 Altseason ; indice 30 j ≥ 75 → 🌱 Altseason en formation ; indice 30 j ≥ 60 → 🌤️ Altseason modérée ; ≤ 25 → saison Bitcoin.*
- **Le « mode altseason » du classement est abandonné depuis le 11/11/2026.** Il ajoutait du momentum quand l'indice dépassait 60 : en réel, 51 % de réussite quand il était actif contre 68 % sinon. Sur 2,6 ans de cours, un indice élevé a été suivi des PIRES mois pour les altcoins : l'indice sert maintenant de thermomètre, plus à modifier le classement.
- **Thermomètre (941 jours de cours) : Contexte habituel : BTC reste difficile à battre.** Indice altseason à 26 % (tranche 25–45 %). Les 308 jours passés dans cette tranche ont été suivis, sur 30 j, d'une altcoin médiane à -6.1 % (BTC +2.6 %) ; 29 % des altcoins ont battu BTC (moyenne toutes périodes : 30 %).
- **Taux de base à garder en tête :** sur 30 j, l'altcoin médiane fait -7.0 % et BTC +1.1 % ; seules 30 % des altcoins battent BTC (38 % sur 7 j). L'adversaire à battre, c'est BTC, pas « la médiane du marché ».

### Ma méthode aujourd'hui : mélange modèle + règle (`ml_blend`)

- Modèle entraîné sur 75792 observations (192 jours), horizon 7 j ; depuis le 11/11/2026 le classement est le **mélange** du modèle et de la règle simple « grosse cap peu volatile » (plus régulier mois après mois que l'un ou l'autre seul).

**Analyse des erreurs — 126 jours rejoués** (chaque semaine prédite uniquement avec des données antérieures) ; top 20 jugé à 7 j contre trois adversaires :

| Méthode | Bat la médiane du marché | Bat BTC | A monté | Les 20 derniers battent la médiane |
|---|---|---|---|---|
| **Mélange (utilisé)** | 62% | 42% | 39% | 37% |
| Modèle appris seul | 60% | 43% | 41% | 35% |
| Règle simple seule | 64% | 43% | 40% | 43% |
| *Un token pris au hasard* | *50%* | *41%* | *39%* | *50%* |

*Lecture honnête : le classement sait écarter les mauvais tokens (les 20 derniers font nettement moins bien que le hasard), mais son top 20 ne bat pas BTC plus d'une fois sur deux. Il sert à choisir PARMI les altcoins, pas à décider d'en détenir.*

- 105 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `catalyst_score` (−), `vol_30d_ann` (−), `rsi_14` (+), `pat_double_bottom_90d` (+), `p_ma50` (−), `pat_bear_flag` (−)

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 44.2%
**Signaux baissiers fiables (>50%) :** 11 / 11

**Mon top 20 quotidien, jugé à 7 j — toutes méthodes confondues depuis mai (ancienne formule incluse) :** 3885 prédictions mesurées — 38% ont monté, 51% ont battu la médiane du marché (50% = hasard)

**Modèle appris (depuis le 26/09/2026 ; mélangé à la règle simple depuis le 11/11/2026) :** 1125 prédictions mesurées sur 54 jours — 16% ont monté, **55% ont battu la médiane du marché**

### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché (55% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `breakdown_30d` | 68.6% | 312 | → |
| `double_top_90d` | 67.4% | 5153 | → |
| `evening_star_4h` | 65.0% | 1333 | → |
| `downtrend` | 64.0% | 23291 | 📈 |
| `bearish_engulfing_4h` | 63.7% | 1522 | → |
| `death_cross` | 60.7% | 570 | 📈 |
| `macd_bearish_cross` | 58.0% | 11257 | → |
| `shooting_star_4h` | 57.6% | 408 | → |
| `rsi_bearish_divergence` | 56.9% | 2066 | → |
| `bear_flag` | 53.5% | 691 | → |
| `resistance_test` | 52.9% | 2909 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 44.2% | 684 | → |
| `double_bottom_90d` | 42.1% | 2957 | → |
| `macd_bullish_cross` | 39.6% | 11446 | → |
| `uptrend` | 39.4% | 18328 | → |
| `hammer_4h` | 39.3% | 430 | → |
| `support_bounce` | 37.6% | 3420 | → |
| `bullish_engulfing_4h` | 35.5% | 1750 | → |
| `bull_flag` | 35.1% | 419 | → |
| `breakout_30d` | 34.3% | 651 | → |
| `morning_star_4h` | 34.1% | 1166 | → |
| `rsi_bullish_divergence` | 31.9% | 3849 | 📉 |
| `golden_cross` | 30.7% | 1573 | → |

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
| 2026-11 | Modèle appris | 362 | 6% | 49% | -9.3% |

**Modèle appris selon le régime de marché** (indice altseason 30 j le jour de la prédiction ; mode altseason actif à partir de 60) :

| Régime le jour de la prédiction | Jours | Prédictions | Ont battu le marché (7 j) | Return médian (7 j) |
|---|---|---|---|---|
| Mode altseason actif (indice ≥ 60) | 22 | 475 | 51% | -4.5% |
| Mode altseason inactif (indice < 60) | 32 | 650 | 58% | -6.3% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 18 nov 2026 | **BNB** | 58% | 581.76 | -5.6% | ✅ +0.9pp | … |
| 18 nov 2026 | **JST** | 58% | 0.14519 | +2.0% | ✅ +8.5pp | … |
| 18 nov 2026 | **NEXO** | 58% | 0.65 | -4.0% | ✅ +2.5pp | … |
| 18 nov 2026 | **BTC** | 58% | 63068.7 | -5.3% | ✅ +1.2pp | … |
| 18 nov 2026 | **BCH** | 58% | 207 | -3.0% | ✅ +3.5pp | … |
| 18 nov 2026 | **HBAR** | 58% | 0.05625 | -9.4% | ❌ -2.9pp | … |
| 18 nov 2026 | **SKY** | 58% | 0.05109 | -21.4% | ❌ -14.9pp | … |
| 18 nov 2026 | **SHIB** | 58% | 3.79e-06 | -6.6% | ❌ -0.1pp | … |
| 18 nov 2026 | **WLFI** | 58% | 0.0454 | -7.0% | ❌ -0.6pp | … |
| 18 nov 2026 | **DOGE** | 58% | 0.05875 | -6.6% | ❌ -0.1pp | … |
| 18 nov 2026 | **LTC** | 58% | 43.74 | -4.2% | ✅ +2.2pp | … |
| 18 nov 2026 | **SUN** | 58% | 0.01492 | -2.6% | ✅ +3.9pp | … |
| 18 nov 2026 | **DOT** | 58% | 0.718 | -8.8% | ❌ -2.3pp | … |
| 18 nov 2026 | **TRX** | 58% | 0.3095 | -1.6% | ✅ +4.9pp | … |
| 18 nov 2026 | **ALGO** | 58% | 0.078 | -0.3% | ✅ +6.2pp | … |
| 18 nov 2026 | **CAKE** | 58% | 1.585 | -2.4% | ✅ +4.1pp | … |
| 18 nov 2026 | **币安人生** | 58% | 0.4827 | -9.6% | ❌ -3.1pp | … |
| 18 nov 2026 | **ENS** | 58% | 3.84 | -11.5% | ❌ -5.0pp | … |
| 18 nov 2026 | **FLOKI** | 58% | 1.752e-05 | -6.6% | ❌ -0.1pp | … |
| 18 nov 2026 | **IMX** | 57% | 0.0952 | -5.9% | ✅ +0.6pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. Le backtest initial (juin→sept. 2026) annonçait 67 % de réussite en altseason ; le suivi réel ci-dessous ne le confirme pas : jugez sur la ligne « En direct ».*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1233 | 49% | 25% (hasard : 10 %) | +4.9 pts | -0.5 pts |
| Altseason (indice 30 j ≥ 60) | 398 | 45% | 20% (hasard : 10 %) | +3.5 pts | -2.3 pts |
| Hors altseason | 825 | 51% | 28% (hasard : 10 %) | +5.7 pts | +0.4 pts |
| Régime inconnu (indice pas encore calculable) | 10 | 30% | 10% (hasard : 10 %) | -5.7 pts | -9.3 pts |
| **En direct** (depuis le 29/09/2026) | 283 | 53% | 33% (hasard : 10 %) | +5.9 pts | +1.5 pts |
| Reconstitués (avant le 29/09/2026) | 950 | 48% | 23% (hasard : 10 %) | +4.6 pts | -1.2 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **OPG** | Mid | +53% | 51.4% | ⚠️ 4 |
| 2 | **JST** | Etabli | +4% | 56.9% | ⚠️ 6 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : DODO, LISTA, MMT. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée découle du **rang** du token : c'est le taux de réussite **réellement observé** pour ce niveau de classement (courbe lissée rang → réussite, ajustée sur les 120 jours de test). Deux tokens voisins dans le classement ont donc des probabilités voisines (≈ 0,1 pt d'écart par rang) : c'est voulu, ce n'est pas une sortie brute du modèle.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-06-29 au 2026-10-26 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 71% | +0.231 |
| Règle simple | 72% | +0.189 |
| Mélange ✅ | 72% | +0.228 |

⚠️ Sur cette période, le token médian a fait **-3.1 %** en 30 j et seuls **42%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `vtrend` (−), `dd90` (−), `r90` (+), `size` (+)

**Suivi réel (jugé à 30 j)** : 305 prédictions — **79% ont battu le marché**, 5% ont monté, return médian -24.6 %.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **TRX** | Etabli | 72 % | 56.9 % | -8 % |
| 2 | **BTC** | Etabli | 72 % | 56.6 % | -25 % |
| 3 | **SOL** | Etabli | 72 % | 56.7 % | -31 % |
| 4 | **WLFI** | Etabli | 71 % | 56.5 % | -20 % |
| 5 | **BNB** | Etabli | 71 % | 56.7 % | -26 % |
| 6 | **XRP** | Etabli | 71 % | 56.7 % | -28 % |
| 7 | **ETH** | Etabli | 71 % | 56.5 % | -27 % |
| 8 | **ACM** | Speculative | 71 % | 54.9 % | -19 % |
| 9 | **JST** | Etabli | 71 % | 56.9 % | +4 % |
| 10 | **DOGE** | Etabli | 70 % | 55.2 % | -28 % |
| 11 | **PSG** | Speculative | 70 % | 55.5 % | -25 % |
| 12 | **LTC** | Etabli | 70 % | 55.0 % | -26 % |

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
| 2026-11-03 | **INJ** | 8-A12B | Canary Staked INJ ETF | -20% (+4 pts) |
| 2026-11-02 | **INJ** | S-1/A | Canary Staked INJ ETF | -16% (+8 pts) |
| 2026-10-28 | **SEI** | 8-A12B | SEI Exchange Traded Funds | -38% (-8 pts) |

**Tokens avec un ETF en préparation ou en lancement :** INJ (🟢 8-A12B le 2026-11-03), SEI (🟢 8-A12B le 2026-10-28), TAO (📝 S-1/A le 2026-10-23), PEPE (📝 S-1/A le 2026-10-02)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 54 | +0.049 | 55% | 53% | 48% | 52% | 51% | 45% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 53.5% (25 nov 2026) — -31.6% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 31.9% (25 nov 2026) — -4.7% 📉
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 64.0% (25 nov 2026) — -5.3% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 44.2% (25 nov 2026) — +20.4% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 56.9% (25 nov 2026) — -18.5% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **reculent** : dans ce marché, les patterns d'achat ne fonctionnent pas encore.

---

## Le score composite est-il utile ?

J'ai analysé **61560 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0282 |
| momentum | 0.0314 |
| risk | 0.0314 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 25 nov 2026

**Régime :** 🟡 Neutre (indice altseason 30 j : 27.3)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **JST** | Etabli | 56.9% | +0.3pp | ⚠️ 6 |  |
| **TRX** | Etabli | 56.9% | +0.3pp | 0 |  |
| **SUN** | Mid | 56.9% | +0.3pp | 0 |  |
| **NEXO** | Etabli | 56.8% | +0.2pp | 1 |  |
| **GPS** | Mid | 56.8% | +0.2pp | ⚠️ 4 |  |
| **SOL** | Etabli | 56.7% | +0.1pp | 0 | 🔥 Trending #13 sur CoinGecko |
| **币安人生** | Mid | 56.7% | +0.1pp | 1 |  |
| **BNB** | Etabli | 56.7% | +0.1pp | 1 |  |
| **SHIB** | Etabli | 56.7% | +0.1pp | 1 |  |
| **XRP** | Etabli | 56.7% | +0.1pp | 0 |  |
| **BTC** | Etabli | 56.6% | +0.0pp | 1 | 🔥 Trending #5 sur CoinGecko |
| **XNO** | Mid | 56.6% | +0.0pp | 0 |  |
