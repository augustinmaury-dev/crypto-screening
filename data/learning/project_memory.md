# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 17 oct 2026*

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

- **Indice altseason** : 68.0 sur 30 j, 65.3 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 6.0 % sur 30 j · **Tokens au-dessus de leur MA50** : 34.6 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 29).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 60524 observations (153 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **52%** du temps (règle simple « grosses caps peu volatiles » : 55% ; hasard : 50 %)
- Confiance (calibration) : k = 0.36 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 80 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `vol_30d_ann` (−), `log_rank` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 10 / 11

**Mon top 20 quotidien, jugé à 7 j :** 3090 prédictions mesurées — 45% ont monté, **49% ont battu la médiane du marché** (50% = hasard)

### ⚠️ En conditions réelles, mon classement ne bat pas clairement le marché (43% de mon top 20).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 59.3% | 3914 | → |
| `downtrend` | 56.3% | 17984 | → |
| `bearish_engulfing_4h` | 54.5% | 1100 | 📈 |
| `evening_star_4h` | 54.3% | 920 | 📈 |
| `rsi_bearish_divergence` | 53.4% | 1784 | 📈 |
| `breakdown_30d` | 52.9% | 138 | → |
| `shooting_star_4h` | 52.0% | 344 | → |
| `resistance_test` | 51.0% | 2377 | → |
| `macd_bearish_cross` | 50.9% | 8951 | 📈 |
| `death_cross` | 50.8% | 419 | → |
| `bear_flag` | 48.1% | 601 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 54.0% | 496 | 📉 |
| `uptrend` | 47.8% | 13957 | → |
| `hammer_4h` | 47.0% | 345 | → |
| `bullish_engulfing_4h` | 45.4% | 1261 | → |
| `rsi_bullish_divergence` | 44.4% | 2535 | → |
| `macd_bullish_cross` | 43.9% | 9858 | → |
| `support_bounce` | 43.6% | 2721 | → |
| `double_bottom_90d` | 43.3% | 2731 | → |
| `golden_cross` | 42.1% | 1024 | 📉 |
| `bull_flag` | 42.0% | 333 | 📉 |
| `morning_star_4h` | 38.8% | 957 | → |
| `breakout_30d` | 35.9% | 582 | → |

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
| 2026-10 | Modèle appris | 200 | 16% | 38% | -6.8% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 10 oct 2026 | **PARTI** | 58% | 0.0341 | -8.5% | ❌ -0.1pp | … |
| 10 oct 2026 | **JUV** | 56% | 0.332 | -7.8% | ✅ +0.6pp | … |
| 10 oct 2026 | **ENJ** | 56% | 0.0319 | -9.3% | ❌ -0.9pp | … |
| 10 oct 2026 | **SCR** | 55% | 0.02548 | -16.2% | ❌ -7.8pp | … |
| 10 oct 2026 | **IOTA** | 55% | 0.0513 | -8.0% | ✅ +0.4pp | … |
| 10 oct 2026 | **LAZIO** | 55% | 0.421 | -1.9% | ✅ +6.5pp | … |
| 10 oct 2026 | **SEI** | 55% | 0.06792 | -6.6% | ✅ +1.8pp | … |
| 10 oct 2026 | **SUI** | 55% | 1.1114 | -9.7% | ❌ -1.3pp | … |
| 10 oct 2026 | **RENDER** | 55% | 1.907 | -0.4% | ✅ +8.0pp | … |
| 10 oct 2026 | **AAVE** | 54% | 172.15 | -9.6% | ❌ -1.2pp | … |
| 10 oct 2026 | **FLOKI** | 54% | 2.73e-05 | -12.4% | ❌ -4.0pp | … |
| 10 oct 2026 | **JASMY** | 54% | 0.00502 | -7.2% | ✅ +1.2pp | … |
| 10 oct 2026 | **BABY** | 54% | 0.01346 | -10.5% | ❌ -2.1pp | … |
| 10 oct 2026 | **BEAMX** | 54% | 0.002636 | +12.0% | ✅ +20.4pp | … |
| 10 oct 2026 | **RUNE** | 54% | 0.691 | -7.2% | ✅ +1.1pp | … |
| 10 oct 2026 | **TAO** | 54% | 282.2 | -3.0% | ✅ +5.4pp | … |
| 10 oct 2026 | **TKO** | 54% | 0.0579 | -9.7% | ❌ -1.3pp | … |
| 10 oct 2026 | **GRT** | 54% | 0.02703 | -9.7% | ❌ -1.3pp | … |
| 10 oct 2026 | **JOE** | 54% | 0.0393 | -15.3% | ❌ -6.9pp | … |
| 10 oct 2026 | **SANTOS** | 54% | 0.523 | -9.0% | ❌ -0.6pp | … |

**145 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 1005 | 47% | 22% (hasard : 10 %) | +4.3 pts | -1.2 pts |
| Altseason (indice 30 j ≥ 60) | 234 | 42% | 15% (hasard : 10 %) | -0.1 pts | -2.8 pts |
| Hors altseason | 704 | 49% | 25% (hasard : 10 %) | +5.3 pts | -0.6 pts |

**Leaders aujourd'hui — 🚀 Leader (altseason)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **TIA** | Mid | +90% | 48.1% | ⚠️ 4 |
| 2 | **BEAMX** | Speculative | +80% | 49.9% | 2 |
| 3 | **INJ** | Etabli | +56% | 48.2% | ⚠️ 4 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : EDU, VELODROME. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 🗓️ Prévision à 30 jours

*Même principe que le score à 7 j, sur 30 j : variables techniques → apprentissage sur ~1000 jours de cours Binance → analyse des erreurs. Chaque jour, le modèle appris et une règle simple (« peu volatil + gros volume ») sont testés sur les 120 derniers jours déjà mesurables ; le meilleur est utilisé (mélange des deux s'ils sont proches). La probabilité affichée est le taux de réussite **réellement observé** pour la tranche de classement du token.*

**Méthode du jour : mélange modèle + règle** — auto-évaluation du 2026-05-21 au 2026-09-17 (120 jours jamais vus) :

| Candidat | Top 20 bat le marché à 30 j | Corrélation de rang |
|---|---|---|
| Modèle appris | 68% | +0.186 |
| Règle simple | 68% | +0.164 |
| Mélange ✅ | 68% | +0.190 |

⚠️ Sur cette période, le token médian a fait **+1.6 %** en 30 j et seuls **48%** des tokens ont fini en hausse : « battre le marché » peut vouloir dire « perdre moins ».

Ce qui compte le plus à 30 j : `vol90` (−), `vol30` (−), `runup180` (−), `vtrend` (−), `dd90` (−), `r90` (+)

**Suivi réel** : 122 prédictions en attente — premiers résultats à partir du 11 nov 2026.

| # | Token | Tier | Prob. de battre le marché à 30 j | Score 7 j | Perf 30 j passée |
|---|---|---|---|---|---|
| 1 | **BTC** | Etabli | 68 % | 54.3 % | +6 % |
| 2 | **TRX** | Etabli | 68 % | 48.7 % | +0 % |
| 3 | **BNB** | Etabli | 68 % | 53.9 % | -2 % |
| 4 | **SOL** | Etabli | 68 % | 53.2 % | +4 % |
| 5 | **ASTER** | Etabli | 68 % | 51.0 % | -5 % |
| 6 | **ETH** | Etabli | 68 % | 53.1 % | -1 % |
| 7 | **JST** | Etabli | 68 % | 52.3 % | +15 % |
| 8 | **WLFI** | Etabli | 68 % | 50.2 % | -4 % |
| 9 | **XRP** | Etabli | 68 % | 52.8 % | -0 % |
| 10 | **NEXO** | Etabli | 68 % | 53.6 % | +2 % |
| 11 | **DOGE** | Etabli | 68 % | 52.0 % | -2 % |
| 12 | **OG** | Speculative | 68 % | 47.9 % | -1 % |

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
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | -11% (+3 pts) |
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | +9% (+16 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +17% (+24 pts) |
| 2026-09-18 | **INJ** | S-1/A | 21Shares Injective ETF | +31% (+31 pts) |

**Tokens avec un ETF en préparation ou en lancement :** PEPE (📝 S-1/A le 2026-10-02), NEAR (🟢 8-A12B le 2026-09-24), INJ (📝 S-1/A le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), BCH (📝 S-3/A le 2026-09-11), LTC (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24), ETH (📝 S-3/A le 2026-08-19)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.002 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 15 | +0.059 | 44% | 51% | 51% | 51% | 51% | 45% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
| 18 sep 2026 | 🟢 Haussier | — | (bull_prob 70.0%) | ROSE, ENSO, LSK |
| 19 sep 2026 | 🟢 Haussier | — | (bull_prob 60.0%) | ESP, SLP, C98 |
| 20 sep 2026 | 🟢 Haussier | — | (bull_prob 66.0%) | KMNO, HOT, JOE |
| 21 sep 2026 | 🟢 Haussier | — | (bull_prob 67.0%) | ASTER, FLOW, NMR |
| 22 sep 2026 | 🟢 Haussier | — | (bull_prob 64.0%) | ASTER, PENGU, FORM |
| 23 sep 2026 | 🟢 Haussier | — | (bull_prob 65.0%) | PENGU, BROCCOLI714, WIN |
| 24 sep 2026 | 🟢 Haussier | — | (bull_prob 67.0%) | ONDO, COMP, AI |
| 25 sep 2026 | 🟢 Haussier | — | (bull_prob 65.0%) | IQ, ONDO, EIGEN |
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

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 48.1% (17 oct 2026) — -37.0% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.4% (17 oct 2026) — +7.8% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.3% (17 oct 2026) — -13.0% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 54.0% (17 oct 2026) — +30.2% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 53.4% (17 oct 2026) — -22.0% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **47825 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0196 |
| momentum | 0.0317 |
| risk | 0.0223 |
| antiscam | 0.0000 |
| signal | 0.0123 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 17 oct 2026

**Régime :** 🟡 Neutre (indice altseason 30 j : 68.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **APT** | Etabli | 54.8% | +0.5pp | 1 |  |
| **BTC** | Etabli | 54.3% | +0.0pp | 3 | 🔥 Trending #7 sur CoinGecko |
| **PEPE** | Etabli | 54.3% | +0.0pp | 3 |  |
| **IOTA** | Mid | 54.2% | -0.1pp | 3 |  |
| **TAO** | Etabli | 54.0% | -0.3pp | 3 |  |
| **SUI** | Etabli | 54.0% | -0.3pp | 3 |  |
| **NEO** | Mid | 54.0% | -0.3pp | 3 |  |
| **1INCH** | Mid | 53.9% | -0.4pp | 3 |  |
| **BNB** | Etabli | 53.9% | -0.4pp | ⚠️ 7 |  |
| **AAVE** | Etabli | 53.8% | -0.5pp | ⚠️ 5 |  |
| **ATOM** | Etabli | 53.6% | -0.7pp | ⚠️ 5 |  |
| **YFI** | Mid | 53.6% | -0.7pp | 3 |  |
