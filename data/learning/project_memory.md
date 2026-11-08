# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 8 nov 2026*

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

- **Indice altseason** : 14.1 sur 30 j, 39.8 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC)
- **BTC** : -8.1 % sur 30 j · **Tokens au-dessus de leur MA50** : 5.1 %
- *Échelle unique (depuis le 26/10/2026) : indice 90 j ≥ 75 → 🚀 Altseason ; indice 30 j ≥ 75 → 🌱 Altseason en formation ; indice 30 j ≥ 60 → 🌤️ Altseason modérée ; ≤ 25 → saison Bitcoin. Le **mode altseason** du classement et le groupe « Altseason » des leaders utilisent le même seuil (indice 30 j ≥ 60) : 🌱 et 🌤️ = mode altseason actif ; seule l'étiquette 🚀 (fondée sur 90 j) peut coexister avec un mode inactif si le court terme s'essouffle.* Aujourd'hui : mode altseason **inactif** (indice 30 j = 14.1).
- **Modèle dédié à l'altseason : prêt** (36 jours d'altseason mesurés, seuil 30). Il est utilisé seulement les jours où le mode altseason est actif — aujourd'hui : **non utilisé** (`ml_gb`).

### Mon modèle aujourd'hui : `ml_gb`

- Entraîné sur 69145 observations (175 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **59%** du temps (règle simple « grosses caps peu volatiles » : 75% ; hasard : 50 %)
- Confiance (calibration) : k = 0.48 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 92 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `catalyst_score` (−), `rsi_14` (+), `p_ma50` (−), `vol_30d_ann` (−), `pat_double_bottom_90d` (+), `pat_bear_flag` (−)

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 47.7%
**Signaux baissiers fiables (>50%) :** 11 / 11

**Mon top 20 quotidien, jugé à 7 j :** 3543 prédictions mesurées — 42% ont monté, **52% ont battu la médiane du marché** (50% = hasard)

### ✅ En conditions réelles, mon classement bat le marché (58% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 64.0% | 4553 | → |
| `evening_star_4h` | 62.2% | 1200 | → |
| `breakdown_30d` | 60.7% | 201 | → |
| `bearish_engulfing_4h` | 59.7% | 1288 | → |
| `downtrend` | 58.6% | 19643 | → |
| `rsi_bearish_divergence` | 56.4% | 2017 | → |
| `macd_bearish_cross` | 56.3% | 10541 | → |
| `death_cross` | 54.8% | 487 | 📈 |
| `shooting_star_4h` | 54.2% | 369 | → |
| `resistance_test` | 52.4% | 2732 | → |
| `bear_flag` | 51.1% | 644 | 📈 |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 47.7% | 608 | → |
| `double_bottom_90d` | 42.8% | 2898 | → |
| `macd_bullish_cross` | 42.7% | 10393 | → |
| `support_bounce` | 41.9% | 2975 | → |
| `bullish_engulfing_4h` | 41.6% | 1455 | → |
| `hammer_4h` | 41.1% | 409 | 📉 |
| `uptrend` | 40.8% | 17460 | → |
| `rsi_bullish_divergence` | 39.7% | 2963 | 📉 |
| `morning_star_4h` | 37.0% | 1046 | → |
| `bull_flag` | 35.2% | 418 | → |
| `breakout_30d` | 34.5% | 640 | → |
| `golden_cross` | 32.5% | 1483 | → |

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
| 2026-11 | Modèle appris | 20 | 0% | 85% | -6.0% |

**Modèle appris selon le régime de marché** (indice altseason 30 j le jour de la prédiction ; mode altseason actif à partir de 60) :

| Régime le jour de la prédiction | Jours | Prédictions | Ont battu le marché (7 j) | Return médian (7 j) |
|---|---|---|---|---|
| Mode altseason actif (indice ≥ 60) | 22 | 475 | 51% | -4.5% |
| Mode altseason inactif (indice < 60) | 15 | 308 | 70% | -4.2% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 1 nov 2026 | **ETH** | 64% | 2266.9 | -1.4% | ✅ +8.3pp | … |
| 1 nov 2026 | **DOGE** | 64% | 0.07568 | -6.0% | ✅ +3.8pp | … |
| 1 nov 2026 | **ALGO** | 62% | 0.0948 | -0.7% | ✅ +9.0pp | … |
| 1 nov 2026 | **XRP** | 62% | 1.2522 | -7.5% | ✅ +2.2pp | … |
| 1 nov 2026 | **SHIB** | 62% | 4.69e-06 | -4.9% | ✅ +4.8pp | … |
| 1 nov 2026 | **WIN** | 61% | 6.693e-05 | -1.1% | ✅ +8.6pp | … |
| 1 nov 2026 | **ADA** | 61% | 0.1934 | -7.2% | ✅ +2.5pp | … |
| 1 nov 2026 | **TAO** | 61% | 235.9 | -5.0% | ✅ +4.7pp | … |
| 1 nov 2026 | **BTC** | 60% | 77938 | -2.6% | ✅ +7.1pp | … |
| 1 nov 2026 | **ETC** | 60% | 7.16 | -4.6% | ✅ +5.1pp | … |
| 1 nov 2026 | **SOL** | 59% | 94.86 | -6.0% | ✅ +3.7pp | … |
| 1 nov 2026 | **WLD** | 58% | 0.3979 | -18.4% | ❌ -8.7pp | … |
| 1 nov 2026 | **HBAR** | 58% | 0.07166 | -7.0% | ✅ +2.7pp | … |
| 1 nov 2026 | **XLM** | 58% | 0.168 | -10.4% | ❌ -0.7pp | … |
| 1 nov 2026 | **HYPE** | 57% | 87.97 | -11.9% | ❌ -2.2pp | … |
| 1 nov 2026 | **RENDER** | 57% | 1.581 | -1.8% | ✅ +7.9pp | … |
| 1 nov 2026 | **BNT** | 57% | 0.2896 | -6.3% | ✅ +3.3pp | … |
| 1 nov 2026 | **APT** | 57% | 0.6356 | -7.0% | ✅ +2.7pp | … |
| 1 nov 2026 | **DOT** | 57% | 0.95 | -6.0% | ✅ +3.7pp | … |
| 1 nov 2026 | **CAKE** | 56% | 1.946 | -3.1% | ✅ +6.6pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. Le backtest initial (juin→sept. 2026) annonçait 67 % de réussite en altseason ; le suivi réel ci-dessous ne le confirme pas : jugez sur la ligne « En direct ».*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1173 | 47% | 24% (hasard : 10 %) | +4.6 pts | -1.4 pts |
| Altseason (indice 30 j ≥ 60) | 398 | 45% | 20% (hasard : 10 %) | +3.5 pts | -2.3 pts |
| Hors altseason | 765 | 49% | 26% (hasard : 10 %) | +5.2 pts | -0.8 pts |
| Régime inconnu (indice pas encore calculable) | 10 | 30% | 10% (hasard : 10 %) | -5.7 pts | -9.3 pts |
| **En direct** (depuis le 29/09/2026) | 223 | 46% | 27% (hasard : 10 %) | +4.4 pts | -1.9 pts |
| Reconstitués (avant le 29/09/2026) | 950 | 48% | 23% (hasard : 10 %) | +4.6 pts | -1.2 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **MEGA** | Mid | +22% | 50.2% | ⚠️ 8 |
| 2 | **JST** | Etabli | +0% | 56.2% | ⚠️ 5 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : PEPE, WIN. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée découle du **rang** du token : c'est le taux de réussite **réellement observé** pour ce niveau de classement (courbe lissée rang → réussite, ajustée sur les 120 jours de test). Deux tokens voisins dans le classement ont donc des probabilités voisines (≈ 0,1 pt d'écart par rang) : c'est voulu, ce n'est pas une sortie brute du modèle.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-06-12 au 2026-10-09 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 68% | +0.223 |
| Règle simple | 70% | +0.189 |
| Mélange ✅ | 70% | +0.224 |

⚠️ Sur cette période, le token médian a fait **-0.9 %** en 30 j et seuls **47%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `vtrend` (−), `runup180` (−), `dd90` (−), `r90` (+)

**Suivi réel** : 566 prédictions en attente — premiers résultats à partir du 11 nov 2026.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **TRX** | Etabli | 70 % | 54.5 % | -4 % |
| 2 | **BTC** | Etabli | 70 % | 59.4 % | -8 % |
| 3 | **BNB** | Etabli | 70 % | 58.2 % | -6 % |
| 4 | **WLFI** | Etabli | 70 % | 53.6 % | -13 % |
| 5 | **SOL** | Etabli | 70 % | 60.5 % | -19 % |
| 6 | **ASTER** | Etabli | 70 % | 55.1 % | -2 % |
| 7 | **JST** | Etabli | 70 % | 56.2 % | +0 % |
| 8 | **ETH** | Etabli | 70 % | 56.6 % | -10 % |
| 9 | **DOGE** | Etabli | 69 % | 60.2 % | -16 % |
| 10 | **NEXO** | Etabli | 69 % | 55.5 % | -13 % |
| 11 | **SUN** | Mid | 69 % | 52.6 % | -8 % |
| 12 | **ACM** | Speculative | 69 % | 44.1 % | -20 % |

---

## 📑 Annonces d'ETF crypto (SEC EDGAR)

*Tout ETF crypto américain dépose ses documents à la SEC avant son lancement : dossier S-1/S-3 et ses amendements, puis enregistrement en bourse (8-A12B) quelques jours avant la cotation. ZEC et NEAR ont fortement monté autour de leurs ETF. Étude du 29/09/2026 : après un dépôt de dossier, 75 % des tokens ont battu le marché à 7 et 14 j ; avant un 8-A12B, la hausse était souvent déjà faite (+33 pts sur les 14 j précédents). Petit échantillon : suivi réel ci-dessous.*

*« En direct » = dépôts publiés depuis le début du suivi (29/09/2026) ; « reconstitué » = dépôts antérieurs retrouvés après coup dans l'historique de la SEC. Seuls les cas en direct comptent pour juger l'idée.*

| Type de dépôt | Suivi | Événements | Battent le marché à 7 j | Excès médian 7 j | Battent le marché à 14 j | Excès médian 14 j |
|---|---|---|---|---|---|---|
| Dossier / amendement (S-1, S-3) | **En direct** | 3 | 0% | -0.9 pts | 67% | +2.6 pts |
| Dossier / amendement (S-1, S-3) | Reconstitué | 34 | 76% | +3.7 pts | 81% | +5.3 pts |
| Enregistrement en bourse (8-A12B) | **En direct** | 1 | 100% | +0.7 pts | … | … |
| Enregistrement en bourse (8-A12B) | Reconstitué | 9 | 56% | +2.2 pts | 67% | +2.7 pts |

**Dépôts des 30 derniers jours :**

| Date | Token | Dépôt | Fonds | Depuis le dépôt (vs marché) |
|---|---|---|---|---|
| 2026-11-03 | **INJ** | 8-A12B | Canary Staked INJ ETF | +10% (+17 pts) |
| 2026-11-02 | **INJ** | S-1/A | Canary Staked INJ ETF | +15% (+22 pts) |
| 2026-10-28 | **SEI** | 8-A12B | SEI Exchange Traded Funds | -15% (-2 pts) |
| 2026-10-23 | **TAO** | S-1/A | Grayscale Bittensor Trust (TAO)  (GTAO) | -14% (+3 pts) |
| 2026-10-23 | **INJ** | S-1/A | Canary Staked INJ ETF | +1% (+18 pts) |

**Tokens avec un ETF en préparation ou en lancement :** INJ (🟢 8-A12B le 2026-11-03), SEI (🟢 8-A12B le 2026-10-28), TAO (📝 S-1/A le 2026-10-23), PEPE (📝 S-1/A le 2026-10-02), NEAR (🟢 8-A12B le 2026-09-24), BCH (📝 S-3/A le 2026-09-11), LTC (📝 S-3/A le 2026-09-11)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 37 | +0.087 | 58% | 55% | 49% | 52% | 50% | 43% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 2 nov 2026 | 🟠 Bitcoin domine (court terme) | 13 | -8.4% | SOL, WIN, DOGE |
| 3 nov 2026 | 🟠 Bitcoin domine (court terme) | 12 | -9.2% | SOL, ETH, DOGE |
| 4 nov 2026 | 🟠 Bitcoin domine (court terme) | 13 | -7.3% | ETH, ADA, TAO |
| 5 nov 2026 | 🟠 Bitcoin domine (court terme) | 11 | -10.3% | TAO, SOL, ADA |
| 6 nov 2026 | 🟠 Bitcoin domine (court terme) | 17 | -9.0% | XLM, SHIB, SOL |
| 7 nov 2026 | 🟠 Bitcoin domine (court terme) | 11 | -8.0% | XRP, DOGE, SOL |
| 8 nov 2026 | 🟠 Bitcoin domine (court terme) | 14 | -8.1% | SOL, DOGE, XRP |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 51.1% (8 nov 2026) — -34.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 39.7% (8 nov 2026) — +3.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 58.6% (8 nov 2026) — -10.7% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 47.7% (8 nov 2026) — +23.9% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 56.4% (8 nov 2026) — -19.0% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **55279 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0250 |
| momentum | 0.0056 |
| risk | 0.0133 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 8 nov 2026

**Régime :** 🟠 Bitcoin domine (court terme) (indice altseason 30 j : 14.1)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **SOL** | Etabli | 60.5% | +1.1pp | 3 |  |
| **DOGE** | Etabli | 60.2% | +0.8pp | 3 |  |
| **XRP** | Etabli | 60.1% | +0.7pp | ⚠️ 5 |  |
| **BTC** | Etabli | 59.4% | +0.0pp | ⚠️ 5 | 🔥 Trending #7 sur CoinGecko |
| **WIN** | Mid | 58.8% | -0.6pp | ⚠️ 5 |  |
| **SHIB** | Etabli | 58.6% | -0.8pp | ⚠️ 5 |  |
| **ADA** | Etabli | 58.3% | -1.1pp | ⚠️ 5 |  |
| **BNB** | Etabli | 58.2% | -1.2pp | ⚠️ 5 |  |
| **XLM** | Etabli | 58.1% | -1.3pp | 3 |  |
| **BCH** | Etabli | 57.9% | -1.5pp | 3 |  |
| **GRAM** | Etabli | 57.8% | -1.6pp | 3 |  |
| **PEPE** | Etabli | 57.7% | -1.7pp | ⚠️ 6 |  |
