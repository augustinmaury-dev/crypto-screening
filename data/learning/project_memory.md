# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 26 oct 2026*

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

- **Indice altseason** : 20.0 sur 30 j, 56.1 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : -5.4 % sur 30 j · **Tokens au-dessus de leur MA50** : 10.2 %
- *Deux seuils différents : l'**étiquette** du régime suit les seuils classiques (≥ 75 = altseason, ≤ 25 = saison Bitcoin) ; le **mode altseason** du classement s'active dès que l'indice 30 j atteint 60.* Aujourd'hui : mode altseason **inactif** (indice 30 j = 20.0).
- **Modèle dédié à l'altseason : prêt** (36 jours d'altseason mesurés, seuil 30). Il est utilisé seulement les jours où le mode altseason est actif — aujourd'hui : **non utilisé** (`ml_gb`).

### Mon modèle aujourd'hui : `ml_gb`

- Entraîné sur 64060 observations (162 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **58%** du temps (règle simple « grosses caps peu volatiles » : 62% ; hasard : 50 %)
- Confiance (calibration) : k = 0.56 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 85 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `vol_30d_ann` (−), `log_rank` (−), `corr_btc_90d` (+)

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 48.6%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Mon top 20 quotidien, jugé à 7 j :** 3275 prédictions mesurées — 44% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché (50% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 61.2% | 4160 | → |
| `evening_star_4h` | 60.7% | 1100 | 📈 |
| `bearish_engulfing_4h` | 57.4% | 1198 | 📈 |
| `downtrend` | 56.9% | 18402 | → |
| `breakdown_30d` | 56.4% | 156 | 📈 |
| `rsi_bearish_divergence` | 56.2% | 1943 | → |
| `macd_bearish_cross` | 55.1% | 10045 | 📈 |
| `shooting_star_4h` | 52.9% | 357 | → |
| `resistance_test` | 52.0% | 2574 | → |
| `death_cross` | 51.0% | 439 | → |
| `bear_flag` | 48.3% | 605 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 48.6% | 586 | 📉 |
| `hammer_4h` | 44.9% | 365 | → |
| `rsi_bullish_divergence` | 44.0% | 2609 | → |
| `uptrend` | 43.9% | 15679 | 📉 |
| `support_bounce` | 43.7% | 2794 | → |
| `macd_bullish_cross` | 43.4% | 10087 | → |
| `bullish_engulfing_4h` | 43.2% | 1361 | → |
| `double_bottom_90d` | 42.5% | 2855 | → |
| `morning_star_4h` | 37.8% | 1006 | → |
| `golden_cross` | 36.3% | 1304 | 📉 |
| `breakout_30d` | 34.8% | 626 | → |
| `bull_flag` | 34.6% | 413 | 📉 |

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
| 2026-10 | Modèle appris | 385 | 17% | 49% | -5.9% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 19 oct 2026 | **IOTA** | 55% | 0.0445 | -4.9% | ❌ -0.8pp | … |
| 19 oct 2026 | **XLM** | 55% | 0.176 | -4.2% | ❌ -0.0pp | … |
| 19 oct 2026 | **CHIP** | 54% | 0.04106 | +17.4% | ✅ +21.5pp | … |
| 19 oct 2026 | **ADA** | 54% | 0.2175 | -6.6% | ❌ -2.5pp | … |
| 19 oct 2026 | **ENS** | 54% | 5.48 | -5.5% | ❌ -1.4pp | … |
| 19 oct 2026 | **HOT** | 54% | 0.000358 | -3.4% | ✅ +0.8pp | … |
| 19 oct 2026 | **BERA** | 54% | 0.1655 | -9.8% | ❌ -5.7pp | … |
| 19 oct 2026 | **FLOKI** | 54% | 2.349e-05 | -3.3% | ✅ +0.8pp | … |
| 19 oct 2026 | **VET** | 54% | 0.006722 | -2.4% | ✅ +1.8pp | … |
| 19 oct 2026 | **FIL** | 54% | 1.0204 | -10.8% | ❌ -6.7pp | … |
| 19 oct 2026 | **BTC** | 54% | 82266 | -3.2% | ✅ +0.9pp | … |
| 19 oct 2026 | **DOGE** | 54% | 0.07925 | -3.1% | ✅ +1.0pp | … |
| 19 oct 2026 | **WIF** | 54% | 0.1988 | -9.9% | ❌ -5.8pp | … |
| 19 oct 2026 | **ETC** | 53% | 7.72 | -2.7% | ✅ +1.4pp | … |
| 19 oct 2026 | **XPL** | 53% | 0.07678 | -5.3% | ❌ -1.2pp | … |
| 19 oct 2026 | **ALGO** | 53% | 0.1089 | -4.5% | ❌ -0.4pp | … |
| 19 oct 2026 | **GALA** | 53% | 0.001883 | -7.5% | ❌ -3.4pp | … |
| 19 oct 2026 | **ICP** | 53% | 2.866 | -9.3% | ❌ -5.2pp | … |
| 19 oct 2026 | **SHIB** | 53% | 5.01e-06 | -3.4% | ✅ +0.7pp | … |
| 19 oct 2026 | **TRUMP** | 53% | 1.714 | -3.0% | ✅ +1.1pp | … |

**145 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1109 | 47% | 23% (hasard : 10 %) | +4.2 pts | -1.4 pts |
| Altseason (indice 30 j ≥ 60) | 328 | 43% | 18% (hasard : 10 %) | +0.6 pts | -2.6 pts |
| Hors altseason | 644 | 49% | 25% (hasard : 10 %) | +4.9 pts | -1.1 pts |
| **En direct** (depuis le 29/09/2026) | 159 | 45% | 22% (hasard : 10 %) | +1.8 pts | -1.9 pts |
| Reconstitués (avant le 29/09/2026) | 950 | 48% | 23% (hasard : 10 %) | +4.6 pts | -1.2 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **BEAMX** | Speculative | +50% | 48.4% | ⚠️ 5 |
| 2 | **PARTI** | Speculative | +32% | 52.6% | ⚠️ 5 |
| 3 | **ERA** | Speculative | +19% | 39.1% | 2 |
| 4 | **JST** | Etabli | +15% | 57.3% | ⚠️ 7 |
| 5 | **BABY** | Mid | +5% | 41.5% | 2 |
| 6 | **KAVA** | Mid | +2% | 50.3% | 3 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : WIN. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée est le taux de réussite **réellement observé** pour la tranche de classement du token.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-05-30 au 2026-09-26 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 67% | +0.200 |
| Règle simple | 68% | +0.172 |
| Mélange ✅ | 67% | +0.200 |

⚠️ Sur cette période, le token médian a fait **+1.6 %** en 30 j et seuls **50%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `runup180` (−), `vtrend` (−), `dd90` (−), `r90` (+)

**Suivi réel** : 305 prédictions en attente — premiers résultats à partir du 11 nov 2026.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **BTC** | Etabli | 68 % | 61.4 % | -5 % |
| 2 | **TRX** | Etabli | 68 % | 54.5 % | -2 % |
| 3 | **BNB** | Etabli | 67 % | 55.4 % | -5 % |
| 4 | **WLFI** | Etabli | 67 % | 55.0 % | -9 % |
| 5 | **ASTER** | Etabli | 67 % | 55.4 % | -3 % |
| 6 | **JST** | Etabli | 67 % | 57.3 % | +15 % |
| 7 | **SOL** | Etabli | 67 % | 57.3 % | -17 % |
| 8 | **ETH** | Etabli | 67 % | 61.4 % | -14 % |
| 9 | **DOGE** | Etabli | 67 % | 60.1 % | -21 % |
| 10 | **SUN** | Mid | 67 % | 53.8 % | -5 % |
| 11 | **NEXO** | Etabli | 66 % | 56.9 % | -8 % |
| 12 | **LTC** | Etabli | 66 % | 58.3 % | -23 % |

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
| 2026-10-23 | **TAO** | S-1/A | Grayscale Bittensor Trust (TAO)  (GTAO) | -4% (+1 pts) |
| 2026-10-23 | **INJ** | S-1/A | Canary Staked INJ ETF | -3% (+2 pts) |
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | -3% (+16 pts) |

**Tokens avec un ETF en préparation ou en lancement :** TAO (📝 S-1/A le 2026-10-23), INJ (📝 S-1/A le 2026-10-23), PEPE (📝 S-1/A le 2026-10-02), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), LTC (📝 S-3/A le 2026-09-11), BCH (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 24 | +0.087 | 50% | 53% | 50% | 52% | 51% | 43% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 22 oct 2026 | 🟡 Neutre | 53 | -4.8% | DOGE, WIN, BTC |
| 23 oct 2026 | 🟡 Neutre | 40 | -4.5% | BTC, TAO, XRP |
| 24 oct 2026 | 🟡 Neutre | 34 | -3.5% | TAO, XRP, BTC |
| 25 oct 2026 | 🟠 Bitcoin domine (court terme) | 20 | -4.7% | DOGE, ETH, ADA |
| 26 oct 2026 | 🟠 Bitcoin domine (court terme) | 20 | -5.4% | BTC, ETH, SHIB |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.3% (26 oct 2026) — -36.8% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.0% (26 oct 2026) — +7.4% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.9% (26 oct 2026) — -12.4% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 48.6% (26 oct 2026) — +24.8% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 56.2% (26 oct 2026) — -19.2% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **51104 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0244 |
| momentum | 0.0086 |
| risk | 0.0134 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 26 oct 2026

**Régime :** 🟠 Bitcoin domine (court terme) (indice altseason 30 j : 20.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **BTC** | Etabli | 61.4% | +0.0pp | 3 | 🔥 Trending #2 sur CoinGecko|🔥 Trending #11 sur Coi |
| **ETH** | Etabli | 61.4% | +0.0pp | 3 |  |
| **SHIB** | Etabli | 60.4% | -1.0pp | ⚠️ 5 |  |
| **ADA** | Etabli | 60.1% | -1.3pp | 3 |  |
| **DOGE** | Etabli | 60.1% | -1.3pp | 3 |  |
| **XRP** | Etabli | 59.8% | -1.6pp | 3 |  |
| **WIN** | Mid | 59.7% | -1.7pp | ⚠️ 4 |  |
| **TAO** | Etabli | 59.7% | -1.7pp | 3 | 🔥 Trending #10 sur CoinGecko |
| **ETC** | Etabli | 59.1% | -2.3pp | 1 |  |
| **XLM** | Etabli | 59.1% | -2.3pp | 3 |  |
| **AAVE** | Etabli | 58.9% | -2.5pp | 3 | 🔥 Trending #13 sur CoinGecko |
| **1INCH** | Mid | 58.5% | -2.9pp | ⚠️ 5 |  |
