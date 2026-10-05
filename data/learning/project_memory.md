# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 5 oct 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.).
Depuis le 26/09/2026, mon `score` est la **probabilité qu'un token fasse mieux que la médiane du marché sur 7 jours**,
calculée par un modèle réentraîné chaque jour sur toutes mes prédictions passées déjà mesurées (`06b_ml_score.py`).
Je surveille aussi le **régime de marché** (altseason ou saison Bitcoin), car ce qui marche change selon le régime.

---

## Mon auto-évaluation

### Régime de marché : 🌱 Altseason en formation

- **Indice altseason** : 77.0 sur 30 j, 64.3 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 7.4 % sur 30 j · **Tokens au-dessus de leur MA50** : 90.6 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 17).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 56109 observations (141 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **54%** du temps (règle simple « grosses caps peu volatiles » : 47% ; hasard : 50 %)
- Confiance (calibration) : k = 0.47 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 75 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `log_rank` (−), `pat_bear_flag` (−)

**Signaux haussiers fiables (>50%) :** uptrend, squeeze_breakout, golden_cross ✅
**Signaux baissiers fiables (>50%) :** 7 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2787 prédictions mesurées — 48% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 58.5% | 3745 | 📉 |
| `downtrend` | 56.1% | 16801 | → |
| `breakdown_30d` | 53.4% | 131 | → |
| `bearish_engulfing_4h` | 52.5% | 954 | → |
| `evening_star_4h` | 51.7% | 810 | → |
| `shooting_star_4h` | 51.1% | 323 | 📉 |
| `death_cross` | 50.5% | 386 | → |
| `resistance_test` | 49.3% | 1975 | → |
| `bear_flag` | 47.9% | 599 | → |
| `macd_bearish_cross` | 47.7% | 7991 | → |
| `rsi_bearish_divergence` | 46.4% | 1330 | 📉 |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 56.7% | 443 | 📈 |
| `uptrend` | 50.3% | 12010 | 📈 |
| `golden_cross` | 50.1% | 715 | 📈 |
| `hammer_4h` | 47.4% | 304 | → |
| `bullish_engulfing_4h` | 46.6% | 1183 | 📈 |
| `bull_flag` | 44.8% | 297 | → |
| `rsi_bullish_divergence` | 44.7% | 2500 | → |
| `double_bottom_90d` | 44.1% | 2451 | → |
| `support_bounce` | 43.7% | 2636 | → |
| `macd_bullish_cross` | 43.4% | 9048 | 📈 |
| `morning_star_4h` | 39.4% | 916 | 📈 |
| `breakout_30d` | 37.9% | 470 | 📈 |

---

## Mes prédictions passées et leurs résultats

*Une prédiction = un des 20 tokens les mieux classés un jour donné. Jugée à 7 j et à 14 j. « Bat le marché » = a fait mieux que la médiane de tous les tokens sur la même période.*

| Mois | Modèle | Prédictions | Ont monté (7 j) | Ont battu le marché (7 j) | Return médian (7 j) |
|------|--------|-------------|-----------------|---------------------------|---------------------|
| 2026-05 | Ancienne formule | 481 | 32% | 61% | -4.3% |
| 2026-06 | Ancienne formule | 480 | 47% | 46% | -0.6% |
| 2026-07 | Ancienne formule | 621 | 43% | 54% | -1.0% |
| 2026-08 | Ancienne formule | 630 | 53% | 42% | +0.4% |
| 2026-09 | Ancienne formule | 510 | 62% | 47% | +2.8% |
| 2026-09 | Modèle appris | 65 | 49% | 58% | -0.1% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 28 sep 2026 | **SOL** | 54% | 117.58 | +1.8% | ❌ -2.1pp | … |
| 28 sep 2026 | **LINK** | 54% | 14.17 | -2.4% | ❌ -6.2pp | … |
| 28 sep 2026 | **TAO** | 54% | 298.6 | +0.6% | ❌ -3.2pp | … |
| 28 sep 2026 | **XLM** | 54% | 0.2155 | -0.9% | ❌ -4.8pp | … |
| 28 sep 2026 | **ADA** | 54% | 0.2405 | +11.3% | ✅ +7.4pp | … |
| 28 sep 2026 | **KAIA** | 53% | 0.0329 | +20.7% | ✅ +16.8pp | … |
| 28 sep 2026 | **BNSOL** | 53% | 133.1 | +1.8% | ❌ -2.0pp | … |
| 28 sep 2026 | **ETH** | 53% | 2657.03 | +1.8% | ❌ -2.1pp | … |
| 28 sep 2026 | **VET** | 53% | 0.008679 | -0.1% | ❌ -4.0pp | … |
| 28 sep 2026 | **XRP** | 53% | 1.48 | +1.3% | ❌ -2.6pp | … |
| 28 sep 2026 | **ENS** | 53% | 6.54 | +4.1% | ✅ +0.3pp | … |
| 28 sep 2026 | **DOT** | 53% | 1.156 | +3.6% | ❌ -0.2pp | … |
| 28 sep 2026 | **ENJ** | 53% | 0.0287 | +15.0% | ✅ +11.1pp | … |
| 28 sep 2026 | **LPT** | 53% | 1.66 | +4.8% | ✅ +0.9pp | … |
| 28 sep 2026 | **AVAX** | 53% | 10.209 | +7.1% | ✅ +3.2pp | … |
| 28 sep 2026 | **WIF** | 53% | 0.2247 | +13.8% | ✅ +9.9pp | … |
| 28 sep 2026 | **RENDER** | 53% | 1.906 | +3.6% | ❌ -0.2pp | … |
| 28 sep 2026 | **WOO** | 53% | 0.0129 | +3.6% | ❌ -0.2pp | … |
| 28 sep 2026 | **BTC** | 53% | 82737.5 | +3.4% | ❌ -0.5pp | … |
| 28 sep 2026 | **PEPE** | 53% | 4.14e-06 | +7.0% | ✅ +3.1pp | … |

**165 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 856 | 49% | 24% (hasard : 10 %) | +5.2 pts | -0.9 pts |
| Altseason (indice 30 j ≥ 60) | 89 | 48% | 19% (hasard : 10 %) | +8.0 pts | -1.6 pts |
| Hors altseason | 741 | 49% | 25% (hasard : 10 %) | +5.2 pts | -0.4 pts |

**Leaders aujourd'hui — 🚀 Leader (altseason)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **GTC** | Speculative | +162% | 45.4% | ⚠️ 8 |
| 2 | **NIGHT** | Etabli | +119% | 48.2% | ⚠️ 4 |
| 3 | **ZRO** | Etabli | +92% | 48.4% | ⚠️ 6 |
| 4 | **SENT** | Mid | +81% | 52.1% | ⚠️ 8 |
| 5 | **RLC** | Mid | +76% | 45.7% | ⚠️ 6 |
| 6 | **INIT** | Speculative | +75% | 48.7% | ⚠️ 4 |
| 7 | **C** | Speculative | +73% | 47.4% | ⚠️ 6 |
| 8 | **AERO** | Etabli | +66% | 51.6% | ⚠️ 6 |
| 9 | **RUNE** | Mid | +62% | 50.2% | 2 |
| 10 | **BEAMX** | Speculative | +60% | 46.5% | ⚠️ 4 |
| 11 | **FLUX** | Speculative | +57% | 49.4% | ⚠️ 6 |
| 12 | **VELODROME** | Speculative | +56% | 47.3% | 2 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : MINA, MUBARAK, ORCA. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 📑 Annonces d'ETF crypto (SEC EDGAR)

*Tout ETF crypto américain dépose ses documents à la SEC avant son lancement : dossier S-1/S-3 et ses amendements, puis enregistrement en bourse (8-A12B) quelques jours avant la cotation. ZEC et NEAR ont fortement monté autour de leurs ETF. Étude du 29/09/2026 : après un dépôt de dossier, 75 % des tokens ont battu le marché à 7 et 14 j ; avant un 8-A12B, la hausse était souvent déjà faite (+33 pts sur les 14 j précédents). Petit échantillon : suivi réel ci-dessous.*

| Type de dépôt | Événements | Battent le marché à 7 j | Excès médian 7 j | Battent le marché à 14 j | Excès médian 14 j |
|---|---|---|---|---|---|
| Dossier / amendement (S-1, S-3) | 34 | 76% | +3.7 pts | 84% | +5.6 pts |
| Enregistrement en bourse (8-A12B) | 9 | 56% | +2.2 pts | 62% | +1.9 pts |

**Dépôts des 30 derniers jours :**

| Date | Token | Dépôt | Fonds | Depuis le dépôt (vs marché) |
|---|---|---|---|---|
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | -1% (+0 pts) |
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | -6% (-11 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +14% (+9 pts) |
| 2026-09-18 | **INJ** | S-1/A | 21Shares Injective ETF | +12% (-1 pts) |
| 2026-09-16 | **NEAR** | S-1/A | Bitwise NEAR ETF | +104% (+81 pts) |
| 2026-09-15 | **SEI** | S-1/A | Canary Staked SEI ETF | +66% (+47 pts) |
| 2026-09-11 | **LTC** | S-3/A | Grayscale Litecoin Trust (LTC)  (LTCN) | +36% (+15 pts) |
| 2026-09-11 | **BCH** | S-3/A | Grayscale Bitcoin Cash Trust (BCH)  (BCHG) | +40% (+19 pts) |
| 2026-09-08 | **TRX** | 8-A12B | Canary Staked TRX ETF  (TRXS) | -1% (-13 pts) |

**Tokens avec un ETF en préparation ou en lancement :** PEPE (📝 S-1/A le 2026-10-02), INJ (📝 S-1/A le 2026-09-24), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), BCH (📝 S-3/A le 2026-09-11), LTC (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24), ETH (📝 S-3/A le 2026-08-19)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.003 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 3 | +0.149 | 58% | 56% | 52% | 54% | 49% | 39% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
| 6 sep 2026 | 🟡 Neutre | — | (bull_prob 54.0%) | XVS, WOO, T |
| 7 sep 2026 | 🟢 Haussier | — | (bull_prob 64.0%) | YGG, USTC, ILV |
| 8 sep 2026 | 🟢 Haussier | — | (bull_prob 69.0%) | ORCA, 1000CAT, UMA |
| 9 sep 2026 | 🟢 Haussier | — | (bull_prob 69.0%) | HOLO, ORCA, GLM |
| 10 sep 2026 | 🟢 Haussier | — | (bull_prob 69.0%) | BFUSD, GLM, NEWT |
| 11 sep 2026 | 🟢 Haussier | — | (bull_prob 69.0%) | MET, ORCA, THETA |
| 12 sep 2026 | 🟢 Haussier | — | (bull_prob 66.0%) | MET, THE, ORCA |
| 13 sep 2026 | 🟢 Haussier | — | (bull_prob 67.0%) | ILV, MET, GLM |
| 14 sep 2026 | 🟢 Haussier | — | (bull_prob 73.0%) | GLM, API3, THE |
| 15 sep 2026 | 🟢 Haussier | — | (bull_prob 76.0%) | AXL, AWE, GLM |
| 16 sep 2026 | 🟢 Haussier | — | (bull_prob 67.0%) | ASTR, POL, HIVE |
| 17 sep 2026 | 🟢 Haussier | — | (bull_prob 67.0%) | A, ASTR, BNSOL |
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

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 47.9% (5 oct 2026) — -37.2% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.7% (5 oct 2026) — +8.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.1% (5 oct 2026) — -13.2% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 56.7% (5 oct 2026) — +32.9% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 46.4% (5 oct 2026) — -29.0% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **43184 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0169 |
| momentum | 0.0477 |
| risk | 0.0209 |
| antiscam | 0.0000 |
| signal | 0.0247 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 5 oct 2026

**Régime :** 🌱 Altseason en formation (indice altseason 30 j : 77.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **RENDER** | Etabli | 57.9% | +4.4pp | 2 |  |
| **EIGEN** | Mid | 57.6% | +4.1pp | 3 |  |
| **CHZ** | Mid | 57.2% | +3.7pp | ⚠️ 4 |  |
| **SUI** | Etabli | 56.5% | +3.0pp | 2 |  |
| **BCH** | Etabli | 56.4% | +2.9pp | 3 |  |
| **APT** | Etabli | 56.1% | +2.6pp | 3 |  |
| **AXL** | Mid | 55.9% | +2.4pp | ⚠️ 5 |  |
| **BONK** | Mid | 55.7% | +2.2pp | 0 | 🔥 Trending #13 sur CoinGecko |
| **GLM** | Mid | 55.7% | +2.2pp | ⚠️ 5 |  |
| **HOT** | Mid | 55.6% | +2.1pp | ⚠️ 7 |  |
| **ENS** | Mid | 55.6% | +2.1pp | ⚠️ 5 |  |
| **TAO** | Etabli | 55.3% | +1.8pp | ⚠️ 5 |  |
