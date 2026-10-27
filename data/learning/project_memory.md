# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 27 oct 2026*

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

- **Indice altseason** : 18.2 sur 30 j, 60.8 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : -5.3 % sur 30 j · **Tokens au-dessus de leur MA50** : 14.0 %
- *Deux seuils différents : l'**étiquette** du régime suit les seuils classiques (≥ 75 = altseason, ≤ 25 = saison Bitcoin) ; le **mode altseason** du classement s'active dès que l'indice 30 j atteint 60.* Aujourd'hui : mode altseason **inactif** (indice 30 j = 18.2).
- **Modèle dédié à l'altseason : prêt** (36 jours d'altseason mesurés, seuil 30). Il est utilisé seulement les jours où le mode altseason est actif — aujourd'hui : **non utilisé** (`ml_gb`).

### Mon modèle aujourd'hui : `ml_gb`

- Entraîné sur 64453 observations (163 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **58%** du temps (règle simple « grosses caps peu volatiles » : 64% ; hasard : 50 %)
- Confiance (calibration) : k = 0.54 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 85 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `vol_30d_ann` (−), `pat_bear_flag` (−), `log_rank` (−)

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 48.5%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Mon top 20 quotidien, jugé à 7 j :** 3300 prédictions mesurées — 44% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché (51% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 61.5% | 4188 | → |
| `evening_star_4h` | 60.7% | 1103 | 📈 |
| `breakdown_30d` | 59.2% | 169 | 📈 |
| `bearish_engulfing_4h` | 57.4% | 1203 | → |
| `downtrend` | 57.0% | 18479 | → |
| `rsi_bearish_divergence` | 56.3% | 1955 | → |
| `macd_bearish_cross` | 55.2% | 10093 | 📈 |
| `shooting_star_4h` | 53.1% | 358 | → |
| `resistance_test` | 52.0% | 2593 | → |
| `death_cross` | 51.2% | 441 | → |
| `bear_flag` | 48.4% | 607 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 48.5% | 592 | 📉 |
| `hammer_4h` | 44.9% | 365 | → |
| `rsi_bullish_divergence` | 43.8% | 2621 | → |
| `support_bounce` | 43.7% | 2804 | → |
| `uptrend` | 43.6% | 15849 | 📉 |
| `macd_bullish_cross` | 43.3% | 10120 | → |
| `bullish_engulfing_4h` | 42.5% | 1395 | 📉 |
| `double_bottom_90d` | 42.5% | 2862 | → |
| `morning_star_4h` | 37.7% | 1011 | → |
| `golden_cross` | 35.8% | 1327 | 📉 |
| `bull_flag` | 34.8% | 414 | → |
| `breakout_30d` | 34.7% | 629 | → |

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
| 2026-10 | Modèle appris | 410 | 16% | 51% | -5.6% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 20 oct 2026 | **ENS** | 55% | 5.44 | -5.5% | ✅ +0.8pp | … |
| 20 oct 2026 | **ADA** | 55% | 0.2177 | -5.6% | ✅ +0.7pp | … |
| 20 oct 2026 | **POL** | 55% | 0.09416 | -4.0% | ✅ +2.3pp | … |
| 20 oct 2026 | **FLOKI** | 55% | 2.369e-05 | -3.3% | ✅ +3.0pp | … |
| 20 oct 2026 | **SHIB** | 55% | 4.98e-06 | -2.0% | ✅ +4.3pp | … |
| 20 oct 2026 | **TRUMP** | 55% | 1.703 | -0.5% | ✅ +5.8pp | … |
| 20 oct 2026 | **NEXO** | 54% | 0.814 | -1.1% | ✅ +5.2pp | … |
| 20 oct 2026 | **XLM** | 54% | 0.1766 | -4.2% | ✅ +2.1pp | … |
| 20 oct 2026 | **1INCH** | 54% | 0.0917 | -4.4% | ✅ +1.9pp | … |
| 20 oct 2026 | **ICP** | 54% | 2.835 | -8.0% | ❌ -1.8pp | … |
| 20 oct 2026 | **STX** | 54% | 0.3461 | -11.2% | ❌ -5.0pp | … |
| 20 oct 2026 | **YFI** | 54% | 2193 | -3.7% | ✅ +2.5pp | … |
| 20 oct 2026 | **TAO** | 54% | 265 | -5.0% | ✅ +1.3pp | … |
| 20 oct 2026 | **ETH** | 54% | 2442.01 | -4.2% | ✅ +2.1pp | … |
| 20 oct 2026 | **HOT** | 54% | 0.000361 | -4.7% | ✅ +1.6pp | … |
| 20 oct 2026 | **LUNC** | 54% | 4.698e-05 | -4.7% | ✅ +1.6pp | … |
| 20 oct 2026 | **XRP** | 54% | 1.3014 | +1.4% | ✅ +7.7pp | … |
| 20 oct 2026 | **CHZ** | 54% | 0.01346 | -4.0% | ✅ +2.3pp | … |
| 20 oct 2026 | **ETC** | 54% | 7.74 | -2.2% | ✅ +4.1pp | … |
| 20 oct 2026 | **FIL** | 54% | 1.0395 | -13.3% | ❌ -7.0pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1119 | 47% | 23% (hasard : 10 %) | +4.2 pts | -1.4 pts |
| Altseason (indice 30 j ≥ 60) | 338 | 43% | 18% (hasard : 10 %) | +0.8 pts | -2.6 pts |
| Hors altseason | 639 | 49% | 25% (hasard : 10 %) | +5.0 pts | -1.1 pts |
| **En direct** (depuis le 29/09/2026) | 169 | 45% | 22% (hasard : 10 %) | +2.1 pts | -1.9 pts |
| Reconstitués (avant le 29/09/2026) | 950 | 48% | 23% (hasard : 10 %) | +4.6 pts | -1.2 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **BEAMX** | Speculative | +55% | 50.5% | ⚠️ 5 |
| 2 | **PARTI** | Speculative | +39% | 56.5% | 2 |
| 3 | **ERA** | Speculative | +24% | 40.2% | 2 |
| 4 | **REZ** | Mid | +21% | 40.9% | ⚠️ 4 |
| 5 | **HAEDAL** | Speculative | +16% | 42.7% | ⚠️ 4 |
| 6 | **JST** | Etabli | +10% | 55.7% | ⚠️ 5 |
| 7 | **KAVA** | Mid | +2% | 51.8% | ⚠️ 5 |
| 8 | **BABY** | Mid | -1% | 44.8% | 2 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : INIT, OSMO, WIN. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée est le taux de réussite **réellement observé** pour la tranche de classement du token.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-05-31 au 2026-09-27 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 67% | +0.210 |
| Règle simple | 68% | +0.174 |
| Mélange ✅ | 68% | +0.209 |

⚠️ Sur cette période, le token médian a fait **+1.6 %** en 30 j et seuls **50%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `runup180` (−), `vtrend` (−), `dd90` (−), `r90` (+)

**Suivi réel** : 325 prédictions en attente — premiers résultats à partir du 11 nov 2026.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **TRX** | Etabli | 67 % | 55.0 % | -2 % |
| 2 | **BTC** | Etabli | 67 % | 60.7 % | -5 % |
| 3 | **BNB** | Etabli | 67 % | 53.7 % | -5 % |
| 4 | **SOL** | Etabli | 67 % | 61.7 % | -18 % |
| 5 | **ASTER** | Etabli | 67 % | 54.7 % | -4 % |
| 6 | **JST** | Etabli | 67 % | 55.7 % | +10 % |
| 7 | **DOGE** | Etabli | 67 % | 60.3 % | -21 % |
| 8 | **WLFI** | Etabli | 67 % | 55.7 % | -10 % |
| 9 | **ETH** | Etabli | 67 % | 61.0 % | -14 % |
| 10 | **SUN** | Mid | 66 % | 53.2 % | -6 % |
| 11 | **NEXO** | Etabli | 66 % | 57.6 % | -7 % |
| 12 | **LTC** | Etabli | 66 % | 57.0 % | -21 % |

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
| 2026-10-23 | **INJ** | S-1/A | Canary Staked INJ ETF | +1% (+6 pts) |
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | -3% (+16 pts) |

**Tokens avec un ETF en préparation ou en lancement :** TAO (📝 S-1/A le 2026-10-23), INJ (📝 S-1/A le 2026-10-23), PEPE (📝 S-1/A le 2026-10-02), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), LTC (📝 S-3/A le 2026-09-11), BCH (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 25 | +0.084 | 50% | 53% | 50% | 52% | 51% | 43% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 22 oct 2026 | 🟡 Neutre | 53 | -4.8% | DOGE, WIN, BTC |
| 23 oct 2026 | 🟡 Neutre | 40 | -4.5% | BTC, TAO, XRP |
| 24 oct 2026 | 🟡 Neutre | 34 | -3.5% | TAO, XRP, BTC |
| 25 oct 2026 | 🟠 Bitcoin domine (court terme) | 20 | -4.7% | DOGE, ETH, ADA |
| 26 oct 2026 | 🟠 Bitcoin domine (court terme) | 20 | -5.4% | BTC, ETH, SHIB |
| 27 oct 2026 | 🟠 Bitcoin domine (court terme) | 18 | -5.3% | SOL, ETH, BTC |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.4% (27 oct 2026) — -36.7% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 43.8% (27 oct 2026) — +7.2% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 57.0% (27 oct 2026) — -12.3% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 48.5% (27 oct 2026) — +24.7% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 56.3% (27 oct 2026) — -19.1% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **51448 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0245 |
| momentum | 0.0062 |
| risk | 0.0129 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 27 oct 2026

**Régime :** 🟠 Bitcoin domine (court terme) (indice altseason 30 j : 18.2)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **SOL** | Etabli | 61.7% | +1.0pp | 3 | 🔥 Trending #10 sur CoinGecko |
| **ETH** | Etabli | 61.0% | +0.3pp | 3 |  |
| **BTC** | Etabli | 60.7% | +0.0pp | 3 | 🔥 Trending #2 sur CoinGecko |
| **DOGE** | Etabli | 60.3% | -0.4pp | 3 |  |
| **XRP** | Etabli | 60.1% | -0.6pp | 3 | 🔥 Trending #15 sur CoinGecko |
| **SHIB** | Etabli | 59.4% | -1.3pp | ⚠️ 5 |  |
| **ETC** | Etabli | 59.0% | -1.7pp | 3 |  |
| **ADA** | Etabli | 58.9% | -1.8pp | 3 |  |
| **AAVE** | Etabli | 58.8% | -1.9pp | 1 |  |
| **TAO** | Etabli | 58.8% | -1.9pp | 3 | 🔥 Trending #11 sur CoinGecko |
| **XLM** | Etabli | 58.7% | -2.0pp | 3 |  |
| **1INCH** | Mid | 58.7% | -2.0pp | 3 |  |
