# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 1 nov 2026*

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

- **Indice altseason** : 15.2 sur 30 j, 52.6 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC)
- **BTC** : -10.1 % sur 30 j · **Tokens au-dessus de leur MA50** : 7.7 %
- *Échelle unique (depuis le 26/10/2026) : indice 90 j ≥ 75 → 🚀 Altseason ; indice 30 j ≥ 75 → 🌱 Altseason en formation ; indice 30 j ≥ 60 → 🌤️ Altseason modérée ; ≤ 25 → saison Bitcoin. Le **mode altseason** du classement et le groupe « Altseason » des leaders utilisent le même seuil (indice 30 j ≥ 60) : 🌱 et 🌤️ = mode altseason actif ; seule l'étiquette 🚀 (fondée sur 90 j) peut coexister avec un mode inactif si le court terme s'essouffle.* Aujourd'hui : mode altseason **inactif** (indice 30 j = 15.2).
- **Modèle dédié à l'altseason : prêt** (36 jours d'altseason mesurés, seuil 30). Il est utilisé seulement les jours où le mode altseason est actif — aujourd'hui : **non utilisé** (`ml_gb`).

### Mon modèle aujourd'hui : `ml_gb`

- Entraîné sur 66408 observations (168 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **62%** du temps (règle simple « grosses caps peu volatiles » : 71% ; hasard : 50 %)
- Confiance (calibration) : k = 0.59 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 85 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `vol_30d_ann` (−), `pat_bear_flag` (−), `log_rank` (−)

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 48.2%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Mon top 20 quotidien, jugé à 7 j :** 3400 prédictions mesurées — 43% ont monté, **51% ont battu la médiane du marché** (50% = hasard)

### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché (53% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 62.5% | 4334 | → |
| `evening_star_4h` | 61.3% | 1157 | → |
| `breakdown_30d` | 59.5% | 190 | 📈 |
| `bearish_engulfing_4h` | 58.3% | 1235 | → |
| `downtrend` | 57.4% | 18878 | → |
| `rsi_bearish_divergence` | 56.5% | 1993 | → |
| `macd_bearish_cross` | 56.0% | 10363 | → |
| `shooting_star_4h` | 53.7% | 363 | → |
| `death_cross` | 52.2% | 460 | → |
| `resistance_test` | 52.2% | 2656 | → |
| `bear_flag` | 48.4% | 609 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 48.2% | 597 | → |
| `hammer_4h` | 44.4% | 374 | → |
| `macd_bullish_cross` | 43.2% | 10203 | → |
| `support_bounce` | 43.1% | 2862 | → |
| `rsi_bullish_divergence` | 42.7% | 2732 | → |
| `double_bottom_90d` | 42.7% | 2880 | → |
| `bullish_engulfing_4h` | 42.4% | 1416 | → |
| `uptrend` | 42.2% | 16661 | 📉 |
| `morning_star_4h` | 37.5% | 1022 | → |
| `bull_flag` | 35.2% | 418 | → |
| `breakout_30d` | 34.6% | 633 | → |
| `golden_cross` | 34.1% | 1401 | 📉 |

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
| 2026-10 | Modèle appris | 510 | 16% | 54% | -5.2% |

**Modèle appris selon le régime de marché** (indice altseason 30 j le jour de la prédiction ; mode altseason actif à partir de 60) :

| Régime le jour de la prédiction | Jours | Prédictions | Ont battu le marché (7 j) | Return médian (7 j) |
|---|---|---|---|---|
| Mode altseason actif (indice ≥ 60) | 22 | 475 | 51% | -4.5% |
| Mode altseason inactif (indice < 60) | 8 | 165 | 62% | -4.3% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 25 oct 2026 | **DOGE** | 60% | 0.07657 | -1.2% | ✅ +2.4pp | … |
| 25 oct 2026 | **ETH** | 60% | 2334.04 | -2.9% | ✅ +0.7pp | … |
| 25 oct 2026 | **ADA** | 60% | 0.2043 | -5.3% | ❌ -1.8pp | … |
| 25 oct 2026 | **WIN** | 60% | 6.304e-05 | +6.2% | ✅ +9.7pp | … |
| 25 oct 2026 | **SHIB** | 60% | 4.87e-06 | -3.7% | ❌ -0.2pp | … |
| 25 oct 2026 | **ETC** | 59% | 7.52 | -4.8% | ❌ -1.3pp | … |
| 25 oct 2026 | **TAO** | 59% | 248.5 | -5.1% | ❌ -1.5pp | … |
| 25 oct 2026 | **1INCH** | 58% | 0.0884 | -4.3% | ❌ -0.8pp | … |
| 25 oct 2026 | **XLM** | 58% | 0.1692 | -0.7% | ✅ +2.8pp | … |
| 25 oct 2026 | **WIF** | 58% | 0.1776 | +0.7% | ✅ +4.3pp | … |
| 25 oct 2026 | **XRP** | 58% | 1.2966 | -3.4% | ✅ +0.1pp | … |
| 25 oct 2026 | **BTC** | 58% | 80466.4 | -3.1% | ✅ +0.4pp | … |
| 25 oct 2026 | **AAVE** | 58% | 136.16 | +1.7% | ✅ +5.3pp | … |
| 25 oct 2026 | **FLOKI** | 57% | 2.299e-05 | +1.1% | ✅ +4.6pp | … |
| 25 oct 2026 | **ONDO** | 57% | 0.4025 | +1.3% | ✅ +4.8pp | … |
| 25 oct 2026 | **ARB** | 57% | 0.1654 | -1.2% | ✅ +2.3pp | … |
| 25 oct 2026 | **IOTA** | 57% | 0.0429 | -7.5% | ❌ -3.9pp | … |
| 25 oct 2026 | **SUI** | 57% | 0.917 | -1.8% | ✅ +1.7pp | … |
| 25 oct 2026 | **WLFI** | 57% | 0.0531 | -4.9% | ❌ -1.4pp | … |
| 25 oct 2026 | **YFI** | 56% | 2096 | -3.3% | ✅ +0.2pp | … |

**143 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. Le backtest initial (juin→sept. 2026) annonçait 67 % de réussite en altseason ; le suivi réel ci-dessous ne le confirme pas : jugez sur la ligne « En direct ».*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1145 | 47% | 23% (hasard : 10 %) | +4.5 pts | -1.4 pts |
| Altseason (indice 30 j ≥ 60) | 398 | 45% | 20% (hasard : 10 %) | +3.5 pts | -2.3 pts |
| Hors altseason | 737 | 49% | 25% (hasard : 10 %) | +5.1 pts | -1.0 pts |
| Régime inconnu (indice pas encore calculable) | 10 | 30% | 10% (hasard : 10 %) | -5.7 pts | -9.3 pts |
| **En direct** (depuis le 29/09/2026) | 195 | 45% | 25% (hasard : 10 %) | +3.9 pts | -2.1 pts |
| Reconstitués (avant le 29/09/2026) | 950 | 48% | 23% (hasard : 10 %) | +4.6 pts | -1.2 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **BEAMX** | Speculative | +129% | 39.5% | ⚠️ 4 |
| 2 | **JST** | Etabli | +8% | 52.1% | ⚠️ 5 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : PEPE, SOLV, WIN. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée découle du **rang** du token : c'est le taux de réussite **réellement observé** pour ce niveau de classement (courbe lissée rang → réussite, ajustée sur les 120 jours de test). Deux tokens voisins dans le classement ont donc des probabilités voisines (≈ 0,1 pt d'écart par rang) : c'est voulu, ce n'est pas une sortie brute du modèle.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-06-05 au 2026-10-02 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 68% | +0.211 |
| Règle simple | 68% | +0.184 |
| Mélange ✅ | 69% | +0.215 |

⚠️ Sur cette période, le token médian a fait **+1.7 %** en 30 j et seuls **50%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `runup180` (−), `vtrend` (−), `dd90` (−), `r90` (+)

**Suivi réel** : 426 prédictions en attente — premiers résultats à partir du 11 nov 2026.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **TRX** | Etabli | 69 % | 49.2 % | -7 % |
| 2 | **WLFI** | Etabli | 69 % | 55.0 % | -10 % |
| 3 | **BNB** | Etabli | 69 % | 52.3 % | -8 % |
| 4 | **SOL** | Etabli | 68 % | 58.6 % | -22 % |
| 5 | **BTC** | Etabli | 68 % | 60.1 % | -10 % |
| 6 | **ASTER** | Etabli | 68 % | 49.8 % | -6 % |
| 7 | **ETH** | Etabli | 68 % | 64.1 % | -18 % |
| 8 | **JST** | Etabli | 68 % | 52.1 % | +8 % |
| 9 | **SUN** | Mid | 68 % | 49.5 % | -10 % |
| 10 | **DOGE** | Etabli | 68 % | 63.6 % | -22 % |
| 11 | **GRAM** | Etabli | 68 % | 55.1 % | -21 % |
| 12 | **NEXO** | Etabli | 68 % | 56.2 % | -10 % |

---

## 📑 Annonces d'ETF crypto (SEC EDGAR)

*Tout ETF crypto américain dépose ses documents à la SEC avant son lancement : dossier S-1/S-3 et ses amendements, puis enregistrement en bourse (8-A12B) quelques jours avant la cotation. ZEC et NEAR ont fortement monté autour de leurs ETF. Étude du 29/09/2026 : après un dépôt de dossier, 75 % des tokens ont battu le marché à 7 et 14 j ; avant un 8-A12B, la hausse était souvent déjà faite (+33 pts sur les 14 j précédents). Petit échantillon : suivi réel ci-dessous.*

*« En direct » = dépôts publiés depuis le début du suivi (29/09/2026) ; « reconstitué » = dépôts antérieurs retrouvés après coup dans l'historique de la SEC. Seuls les cas en direct comptent pour juger l'idée.*

| Type de dépôt | Suivi | Événements | Battent le marché à 7 j | Excès médian 7 j | Battent le marché à 14 j | Excès médian 14 j |
|---|---|---|---|---|---|---|
| Dossier / amendement (S-1, S-3) | **En direct** | 3 | 0% | -0.9 pts | 100% | +2.6 pts |
| Dossier / amendement (S-1, S-3) | Reconstitué | 34 | 76% | +3.7 pts | 81% | +5.3 pts |
| Enregistrement en bourse (8-A12B) | Reconstitué | 9 | 56% | +2.2 pts | 67% | +2.7 pts |

**Dépôts des 30 derniers jours :**

| Date | Token | Dépôt | Fonds | Depuis le dépôt (vs marché) |
|---|---|---|---|---|
| 2026-10-28 | **SEI** | 8-A12B | SEI Exchange Traded Funds | -9% (-4 pts) |
| 2026-10-23 | **TAO** | S-1/A | Grayscale Bittensor Trust (TAO)  (GTAO) | -10% (-1 pts) |
| 2026-10-23 | **INJ** | S-1/A | Canary Staked INJ ETF | -10% (-1 pts) |
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | +10% (+31 pts) |

**Tokens avec un ETF en préparation ou en lancement :** SEI (🟢 8-A12B le 2026-10-28), TAO (📝 S-1/A le 2026-10-23), INJ (📝 S-1/A le 2026-10-23), PEPE (📝 S-1/A le 2026-10-02), NEAR (🟢 8-A12B le 2026-09-24), LTC (📝 S-3/A le 2026-09-11), BCH (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 30 | +0.071 | 53% | 52% | 50% | 53% | 51% | 44% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 29 oct 2026 | 🟠 Bitcoin domine (court terme) | 18 | -3.9% | BTC, NEXO, ASTER |
| 30 oct 2026 | 🟠 Bitcoin domine (court terme) | 14 | -8.4% | ETH, SOL, XRP |
| 31 oct 2026 | 🟠 Bitcoin domine (court terme) | 18 | -7.4% | XRP, SOL, ADA |
| 1 nov 2026 | 🟠 Bitcoin domine (court terme) | 15 | -10.1% | ETH, DOGE, ALGO |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.4% (1 nov 2026) — -36.7% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 42.7% (1 nov 2026) — +6.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 57.4% (1 nov 2026) — -11.9% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 48.2% (1 nov 2026) — +24.4% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 56.5% (1 nov 2026) — -18.9% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **53068 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0232 |
| momentum | 0.0041 |
| risk | 0.0121 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 1 nov 2026

**Régime :** 🟠 Bitcoin domine (court terme) (indice altseason 30 j : 15.2)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **ETH** | Etabli | 64.1% | +4.0pp | ⚠️ 5 | 🔥 Trending #15 sur CoinGecko |
| **DOGE** | Etabli | 63.6% | +3.5pp | 3 |  |
| **ALGO** | Etabli | 62.1% | +2.0pp | 3 |  |
| **XRP** | Etabli | 62.0% | +1.9pp | ⚠️ 5 |  |
| **SHIB** | Etabli | 61.5% | +1.4pp | ⚠️ 5 |  |
| **WIN** | Mid | 61.4% | +1.3pp | 2 |  |
| **ADA** | Etabli | 60.7% | +0.6pp | 3 |  |
| **TAO** | Etabli | 60.6% | +0.5pp | 3 | 🔥 Trending #11 sur CoinGecko |
| **BTC** | Etabli | 60.1% | +0.0pp | 3 | 🔥 Trending #3 sur CoinGecko |
| **ETC** | Etabli | 59.7% | -0.4pp | 3 |  |
| **SOL** | Etabli | 58.6% | -1.5pp | 3 | 🔥 Trending #6 sur CoinGecko |
| **WLD** | Etabli | 58.4% | -1.7pp | 3 |  |
