# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 30 oct 2026*

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

- **Indice altseason** : 14.1 sur 30 j, 48.5 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC)
- **BTC** : -8.4 % sur 30 j · **Tokens au-dessus de leur MA50** : 8.4 %
- *Échelle unique (depuis le 26/10/2026) : indice 90 j ≥ 75 → 🚀 Altseason ; indice 30 j ≥ 75 → 🌱 Altseason en formation ; indice 30 j ≥ 60 → 🌤️ Altseason modérée ; ≤ 25 → saison Bitcoin. Le **mode altseason** du classement et le groupe « Altseason » des leaders utilisent le même seuil (indice 30 j ≥ 60) : 🌱 et 🌤️ = mode altseason actif ; seule l'étiquette 🚀 (fondée sur 90 j) peut coexister avec un mode inactif si le court terme s'essouffle.* Aujourd'hui : mode altseason **inactif** (indice 30 j = 14.1).
- **Modèle dédié à l'altseason : prêt** (36 jours d'altseason mesurés, seuil 30). Il est utilisé seulement les jours où le mode altseason est actif — aujourd'hui : **non utilisé** (`ml_gb`).

### Mon modèle aujourd'hui : `ml_gb`

- Entraîné sur 65626 observations (166 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **62%** du temps (règle simple « grosses caps peu volatiles » : 69% ; hasard : 50 %)
- Confiance (calibration) : k = 0.56 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 85 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `vol_30d_ann` (−), `log_rank` (−), `pat_bear_flag` (−)

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 48.3%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Mon top 20 quotidien, jugé à 7 j :** 3360 prédictions mesurées — 43% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché (52% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 62.1% | 4275 | → |
| `evening_star_4h` | 61.1% | 1135 | → |
| `breakdown_30d` | 59.0% | 188 | 📈 |
| `bearish_engulfing_4h` | 58.0% | 1224 | → |
| `downtrend` | 57.2% | 18718 | → |
| `rsi_bearish_divergence` | 56.4% | 1982 | → |
| `macd_bearish_cross` | 55.7% | 10271 | → |
| `shooting_star_4h` | 53.3% | 360 | → |
| `resistance_test` | 52.0% | 2636 | → |
| `death_cross` | 51.7% | 451 | → |
| `bear_flag` | 48.4% | 609 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 48.3% | 596 | 📉 |
| `hammer_4h` | 44.5% | 373 | → |
| `support_bounce` | 43.4% | 2837 | → |
| `rsi_bullish_divergence` | 43.2% | 2688 | → |
| `macd_bullish_cross` | 43.2% | 10180 | → |
| `uptrend` | 42.7% | 16360 | 📉 |
| `double_bottom_90d` | 42.7% | 2874 | → |
| `bullish_engulfing_4h` | 42.5% | 1399 | → |
| `morning_star_4h` | 37.6% | 1013 | → |
| `bull_flag` | 35.0% | 417 | → |
| `golden_cross` | 34.6% | 1380 | 📉 |
| `breakout_30d` | 34.6% | 633 | → |

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
| 2026-10 | Modèle appris | 470 | 16% | 52% | -5.7% |

**Modèle appris selon le régime de marché** (indice altseason 30 j le jour de la prédiction ; mode altseason actif à partir de 60) :

| Régime le jour de la prédiction | Jours | Prédictions | Ont battu le marché (7 j) | Return médian (7 j) |
|---|---|---|---|---|
| Mode altseason actif (indice ≥ 60) | 22 | 475 | 51% | -4.5% |
| Mode altseason inactif (indice < 60) | 6 | 125 | 58% | -4.9% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 23 oct 2026 | **BTC** | 60% | 81624 | -5.7% | ✅ +4.9pp | … |
| 23 oct 2026 | **TAO** | 60% | 260.7 | -11.4% | ❌ -0.8pp | … |
| 23 oct 2026 | **XRP** | 60% | 1.3187 | -6.1% | ✅ +4.5pp | … |
| 23 oct 2026 | **ETH** | 59% | 2399.1 | -7.5% | ✅ +3.2pp | … |
| 23 oct 2026 | **ADA** | 59% | 0.2167 | -11.9% | ❌ -1.3pp | … |
| 23 oct 2026 | **DOGE** | 59% | 0.08024 | -6.3% | ✅ +4.3pp | … |
| 23 oct 2026 | **ICP** | 59% | 2.756 | -11.0% | ❌ -0.4pp | … |
| 23 oct 2026 | **AVAX** | 58% | 9.172 | -10.1% | ✅ +0.6pp | … |
| 23 oct 2026 | **WIN** | 58% | 5.941e-05 | +7.6% | ✅ +18.3pp | … |
| 23 oct 2026 | **ASTER** | 58% | 0.7086 | -4.2% | ✅ +6.4pp | … |
| 23 oct 2026 | **TRX** | 58% | 0.3303 | +0.5% | ✅ +11.1pp | … |
| 23 oct 2026 | **ETC** | 58% | 7.88 | -9.4% | ✅ +1.2pp | … |
| 23 oct 2026 | **NEXO** | 58% | 0.802 | -3.1% | ✅ +7.5pp | … |
| 23 oct 2026 | **ALGO** | 58% | 0.1078 | -12.5% | ❌ -1.9pp | … |
| 23 oct 2026 | **ENS** | 58% | 5.58 | -13.8% | ❌ -3.2pp | … |
| 23 oct 2026 | **ONDO** | 58% | 0.4332 | -10.3% | ✅ +0.3pp | … |
| 23 oct 2026 | **STX** | 57% | 0.3164 | -11.6% | ❌ -1.0pp | … |
| 23 oct 2026 | **1INCH** | 57% | 0.0918 | -14.8% | ❌ -4.2pp | … |
| 23 oct 2026 | **AAVE** | 57% | 147.86 | -16.5% | ❌ -5.8pp | … |
| 23 oct 2026 | **JST** | 57% | 0.14033 | -2.4% | ✅ +8.2pp | … |

**143 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. Le backtest initial (juin→sept. 2026) annonçait 67 % de réussite en altseason ; le suivi réel ci-dessous ne le confirme pas : jugez sur la ligne « En direct ».*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1140 | 47% | 23% (hasard : 10 %) | +4.4 pts | -1.4 pts |
| Altseason (indice 30 j ≥ 60) | 395 | 45% | 20% (hasard : 10 %) | +3.4 pts | -2.3 pts |
| Hors altseason | 735 | 49% | 25% (hasard : 10 %) | +5.1 pts | -1.0 pts |
| Régime inconnu (indice pas encore calculable) | 10 | 30% | 10% (hasard : 10 %) | -5.7 pts | -9.3 pts |
| **En direct** (depuis le 29/09/2026) | 190 | 45% | 25% (hasard : 10 %) | +3.4 pts | -2.0 pts |
| Reconstitués (avant le 29/09/2026) | 950 | 48% | 23% (hasard : 10 %) | +4.6 pts | -1.2 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **BEAMX** | Speculative | +167% | 43.4% | ⚠️ 6 |
| 2 | **JST** | Etabli | +3% | 52.8% | ⚠️ 5 |
| 3 | **KAVA** | Mid | +2% | 49.2% | 3 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : PEPE, SOLV, WIN. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée découle du **rang** du token : c'est le taux de réussite **réellement observé** pour ce niveau de classement (courbe lissée rang → réussite, ajustée sur les 120 jours de test). Deux tokens voisins dans le classement ont donc des probabilités voisines (≈ 0,1 pt d'écart par rang) : c'est voulu, ce n'est pas une sortie brute du modèle.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-06-03 au 2026-09-30 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 67% | +0.212 |
| Règle simple | 68% | +0.181 |
| Mélange ✅ | 68% | +0.215 |

⚠️ Sur cette période, le token médian a fait **+1.7 %** en 30 j et seuls **50%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `runup180` (−), `vtrend` (−), `dd90` (−), `r90` (+)

**Suivi réel** : 386 prédictions en attente — premiers résultats à partir du 11 nov 2026.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **TRX** | Etabli | 68 % | 46.5 % | -2 % |
| 2 | **BNB** | Etabli | 68 % | 54.6 % | -9 % |
| 3 | **BTC** | Etabli | 68 % | 59.1 % | -8 % |
| 4 | **WLFI** | Etabli | 68 % | 53.5 % | -10 % |
| 5 | **SOL** | Etabli | 68 % | 62.4 % | -20 % |
| 6 | **ASTER** | Etabli | 67 % | 52.7 % | -10 % |
| 7 | **ETH** | Etabli | 67 % | 62.5 % | -17 % |
| 8 | **SUN** | Mid | 67 % | 48.4 % | -6 % |
| 9 | **JST** | Etabli | 67 % | 52.8 % | +3 % |
| 10 | **DOGE** | Etabli | 67 % | 61.3 % | -20 % |
| 11 | **NEXO** | Etabli | 67 % | 52.1 % | -8 % |
| 12 | **JUV** | Speculative | 67 % | 47.9 % | -18 % |

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
| 2026-10-28 | **SEI** | 8-A12B | SEI Exchange Traded Funds | -9% (-2 pts) |
| 2026-10-23 | **TAO** | S-1/A | Grayscale Bittensor Trust (TAO)  (GTAO) | -11% (-1 pts) |
| 2026-10-23 | **INJ** | S-1/A | Canary Staked INJ ETF | -12% (-1 pts) |
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | +15% (+39 pts) |

**Tokens avec un ETF en préparation ou en lancement :** SEI (🟢 8-A12B le 2026-10-28), TAO (📝 S-1/A le 2026-10-23), INJ (📝 S-1/A le 2026-10-23), PEPE (📝 S-1/A le 2026-10-02), NEAR (🟢 8-A12B le 2026-09-24), LTC (📝 S-3/A le 2026-09-11), BCH (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 28 | +0.069 | 51% | 52% | 50% | 53% | 51% | 44% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 29 oct 2026 | 🟠 Bitcoin domine (court terme) | 18 | -3.9% | BTC, NEXO, ASTER |
| 30 oct 2026 | 🟠 Bitcoin domine (court terme) | 14 | -8.4% | ETH, SOL, XRP |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.4% (30 oct 2026) — -36.7% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.2% (30 oct 2026) — +6.6% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 57.2% (30 oct 2026) — -12.1% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 48.3% (30 oct 2026) — +24.5% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 56.4% (30 oct 2026) — -19.0% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **52462 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0238 |
| momentum | 0.0042 |
| risk | 0.0120 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 30 oct 2026

**Régime :** 🟠 Bitcoin domine (court terme) (indice altseason 30 j : 14.1)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **ETH** | Etabli | 62.5% | +3.4pp | 1 |  |
| **SOL** | Etabli | 62.4% | +3.3pp | 1 | 🔥 Trending #6 sur CoinGecko |
| **XRP** | Etabli | 62.0% | +2.9pp | 1 |  |
| **ADA** | Etabli | 61.4% | +2.3pp | 1 |  |
| **SHIB** | Etabli | 61.4% | +2.3pp | 3 |  |
| **DOGE** | Etabli | 61.3% | +2.2pp | 3 |  |
| **TAO** | Etabli | 60.1% | +1.0pp | 1 |  |
| **WIN** | Mid | 59.9% | +0.8pp | 2 |  |
| **ALGO** | Etabli | 59.7% | +0.6pp | ⚠️ 5 |  |
| **BTC** | Etabli | 59.1% | +0.0pp | 1 | 🔥 Trending #2 sur CoinGecko |
| **WIF** | Mid | 58.8% | -0.3pp | 1 |  |
| **ETC** | Etabli | 58.8% | -0.3pp | 1 |  |
