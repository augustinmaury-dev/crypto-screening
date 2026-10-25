# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 25 oct 2026*

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

- **Indice altseason** : 20.0 sur 30 j, 53.1 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : -4.7 % sur 30 j · **Tokens au-dessus de leur MA50** : 12.0 %
- *Deux seuils différents : l'**étiquette** du régime suit les seuils classiques (≥ 75 = altseason, ≤ 25 = saison Bitcoin) ; le **mode altseason** du classement s'active dès que l'indice 30 j atteint 60.* Aujourd'hui : mode altseason **inactif** (indice 30 j = 20.0).
- **Modèle dédié à l'altseason : prêt** (36 jours d'altseason mesurés, seuil 30). Il est utilisé seulement les jours où le mode altseason est actif — aujourd'hui : **non utilisé** (`ml_gb`).

### Mon modèle aujourd'hui : `ml_gb`

- Entraîné sur 63667 observations (161 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **60%** du temps (règle simple « grosses caps peu volatiles » : 62% ; hasard : 50 %)
- Confiance (calibration) : k = 0.58 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 82 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `vol_30d_ann` (−), `log_rank` (−), `corr_btc_90d` (+)

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `squeeze_breakout` à 49.3%
**Signaux baissiers fiables (>50%) :** 10 / 11

**Mon top 20 quotidien, jugé à 7 j :** 3255 prédictions mesurées — 44% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché (50% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 61.0% | 4131 | → |
| `evening_star_4h` | 60.6% | 1096 | 📈 |
| `bearish_engulfing_4h` | 57.3% | 1193 | 📈 |
| `downtrend` | 56.8% | 18351 | → |
| `rsi_bearish_divergence` | 56.0% | 1929 | → |
| `macd_bearish_cross` | 54.8% | 9972 | 📈 |
| `breakdown_30d` | 54.4% | 149 | → |
| `shooting_star_4h` | 52.9% | 357 | → |
| `resistance_test` | 51.9% | 2556 | → |
| `death_cross` | 50.9% | 438 | → |
| `bear_flag` | 48.2% | 604 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 49.3% | 572 | 📉 |
| `hammer_4h` | 45.1% | 364 | → |
| `uptrend` | 44.4% | 15499 | 📉 |
| `rsi_bullish_divergence` | 44.3% | 2586 | → |
| `support_bounce` | 43.6% | 2784 | → |
| `macd_bullish_cross` | 43.5% | 10045 | → |
| `bullish_engulfing_4h` | 43.3% | 1358 | → |
| `double_bottom_90d` | 42.5% | 2849 | → |
| `morning_star_4h` | 37.7% | 1004 | → |
| `golden_cross` | 37.0% | 1280 | 📉 |
| `breakout_30d` | 35.0% | 620 | → |
| `bull_flag` | 34.5% | 412 | 📉 |

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
| 2026-10 | Modèle appris | 365 | 17% | 49% | -6.0% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 18 oct 2026 | **IOTA** | 55% | 0.045 | -4.7% | ❌ -0.1pp | … |
| 18 oct 2026 | **HOT** | 55% | 0.000366 | -6.0% | ❌ -1.4pp | … |
| 18 oct 2026 | **PEPE** | 55% | 3.88e-06 | +14.9% | ✅ +19.6pp | … |
| 18 oct 2026 | **NEO** | 54% | 2.214 | -6.0% | ❌ -1.4pp | … |
| 18 oct 2026 | **WIF** | 54% | 0.1968 | -9.8% | ❌ -5.2pp | … |
| 18 oct 2026 | **SUI** | 54% | 0.9802 | -6.5% | ❌ -1.8pp | … |
| 18 oct 2026 | **FLOKI** | 54% | 2.349e-05 | -2.1% | ✅ +2.5pp | … |
| 18 oct 2026 | **CHIP** | 54% | 0.04166 | +8.6% | ✅ +13.2pp | … |
| 18 oct 2026 | **DYDX** | 54% | 0.11535 | -8.4% | ❌ -3.8pp | … |
| 18 oct 2026 | **GALA** | 54% | 0.001929 | -10.5% | ❌ -5.9pp | … |
| 18 oct 2026 | **PNUT** | 54% | 0.0438 | -6.4% | ❌ -1.8pp | … |
| 18 oct 2026 | **ENS** | 54% | 5.5 | -4.2% | ✅ +0.4pp | … |
| 18 oct 2026 | **ADA** | 53% | 0.22 | -7.1% | ❌ -2.5pp | … |
| 18 oct 2026 | **BIO** | 53% | 0.02377 | -6.2% | ❌ -1.6pp | … |
| 18 oct 2026 | **VET** | 53% | 0.006753 | -0.3% | ✅ +4.3pp | … |
| 18 oct 2026 | **BERA** | 53% | 0.1723 | -12.6% | ❌ -8.0pp | … |
| 18 oct 2026 | **BONK** | 53% | 2.94e-06 | +2.0% | ✅ +6.6pp | … |
| 18 oct 2026 | **TRUMP** | 53% | 1.731 | -4.7% | ❌ -0.1pp | … |
| 18 oct 2026 | **AXS** | 53% | 1.015 | -8.3% | ❌ -3.7pp | … |
| 18 oct 2026 | **THETA** | 53% | 0.1893 | -3.6% | ✅ +1.0pp | … |

**145 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1097 | 47% | 23% (hasard : 10 %) | +4.3 pts | -1.3 pts |
| Altseason (indice 30 j ≥ 60) | 316 | 44% | 18% (hasard : 10 %) | +0.8 pts | -2.4 pts |
| Hors altseason | 652 | 49% | 25% (hasard : 10 %) | +4.9 pts | -1.1 pts |
| **En direct** (depuis le 29/09/2026) | 147 | 46% | 22% (hasard : 10 %) | +2.2 pts | -1.6 pts |
| Reconstitués (avant le 29/09/2026) | 950 | 48% | 23% (hasard : 10 %) | +4.6 pts | -1.2 pts |

**Leaders aujourd'hui — 🎲 Leader (spéculatif)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **PARTI** | Speculative | +28% | 49.6% | ⚠️ 5 |
| 2 | **JST** | Etabli | +19% | 53.3% | ⚠️ 5 |
| 3 | **BABY** | Mid | +8% | 46.4% | 2 |
| 4 | **KAVA** | Mid | +3% | 49.4% | ⚠️ 5 |
| 5 | **BTTC** | Speculative | +3% | 50.4% | 3 |
| 6 | **GMX** | Mid | +3% | 47.9% | 3 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : WIN. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée est le taux de réussite **réellement observé** pour la tranche de classement du token.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-05-29 au 2026-09-25 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 67% | +0.199 |
| Règle simple | 68% | +0.170 |
| Mélange ✅ | 67% | +0.201 |

⚠️ Sur cette période, le token médian a fait **+1.6 %** en 30 j et seuls **50%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `runup180` (−), `vtrend` (−), `dd90` (−), `r90` (+)

**Suivi réel** : 285 prédictions en attente — premiers résultats à partir du 11 nov 2026.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **TRX** | Etabli | 67 % | 54.3 % | -2 % |
| 2 | **BTC** | Etabli | 66 % | 58.0 % | -5 % |
| 3 | **BNB** | Etabli | 66 % | 54.9 % | -5 % |
| 4 | **SOL** | Etabli | 66 % | 56.4 % | -16 % |
| 5 | **ASTER** | Etabli | 66 % | 54.2 % | -4 % |
| 6 | **JST** | Etabli | 66 % | 53.3 % | +19 % |
| 7 | **ETH** | Etabli | 66 % | 60.0 % | -14 % |
| 8 | **WLFI** | Etabli | 66 % | 56.6 % | -7 % |
| 9 | **SUN** | Mid | 66 % | 52.1 % | -6 % |
| 10 | **DOGE** | Etabli | 66 % | 60.1 % | -22 % |
| 11 | **XRP** | Etabli | 66 % | 58.1 % | -20 % |
| 12 | **LTC** | Etabli | 66 % | 56.2 % | -20 % |

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
| 2026-10-23 | **TAO** | S-1/A | Grayscale Bittensor Trust (TAO)  (GTAO) | -5% (+0 pts) |
| 2026-10-23 | **INJ** | S-1/A | Canary Staked INJ ETF | -5% (+0 pts) |
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | -0% (+19 pts) |

**Tokens avec un ETF en préparation ou en lancement :** TAO (📝 S-1/A le 2026-10-23), INJ (📝 S-1/A le 2026-10-23), PEPE (📝 S-1/A le 2026-10-02), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), LTC (📝 S-3/A le 2026-09-11), BCH (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 23 | +0.084 | 50% | 54% | 50% | 51% | 51% | 44% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 22 oct 2026 | 🟡 Neutre | 53 | -4.8% | DOGE, WIN, BTC |
| 23 oct 2026 | 🟡 Neutre | 40 | -4.5% | BTC, TAO, XRP |
| 24 oct 2026 | 🟡 Neutre | 34 | -3.5% | TAO, XRP, BTC |
| 25 oct 2026 | 🟠 Bitcoin domine (court terme) | 20 | -4.7% | DOGE, ETH, ADA |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.2% (25 oct 2026) — -36.9% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.3% (25 oct 2026) — +7.7% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.8% (25 oct 2026) — -12.5% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 49.3% (25 oct 2026) — +25.5% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 56.0% (25 oct 2026) — -19.4% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **50765 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0240 |
| momentum | 0.0117 |
| risk | 0.0141 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 25 oct 2026

**Régime :** 🟠 Bitcoin domine (court terme) (indice altseason 30 j : 20.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **DOGE** | Etabli | 60.1% | +2.1pp | 3 |  |
| **ETH** | Etabli | 60.0% | +2.0pp | 3 |  |
| **ADA** | Etabli | 59.8% | +1.8pp | 3 |  |
| **WIN** | Mid | 59.7% | +1.7pp | ⚠️ 4 |  |
| **SHIB** | Etabli | 59.6% | +1.6pp | ⚠️ 5 |  |
| **ETC** | Etabli | 59.4% | +1.4pp | 3 |  |
| **TAO** | Etabli | 58.6% | +0.6pp | 3 |  |
| **1INCH** | Mid | 58.4% | +0.4pp | 3 |  |
| **XLM** | Etabli | 58.2% | +0.2pp | 3 |  |
| **XRP** | Etabli | 58.1% | +0.1pp | 3 |  |
| **WIF** | Mid | 58.1% | +0.1pp | 3 |  |
| **BTC** | Etabli | 58.0% | +0.0pp | 3 | 🔥 Trending #4 sur CoinGecko |
