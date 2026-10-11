# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 11 oct 2026*

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

- **Indice altseason** : 76.0 sur 30 j, 65.3 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 7.9 % sur 30 j · **Tokens au-dessus de leur MA50** : 74.6 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 23).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 58467 observations (147 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **54%** du temps (règle simple « grosses caps peu volatiles » : 48% ; hasard : 50 %)
- Confiance (calibration) : k = 0.42 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 75 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `vol_30d_ann` (−), `bear_signals` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 8 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2932 prédictions mesurées — 47% ont monté, **49% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 58.5% | 3802 | → |
| `downtrend` | 56.1% | 17524 | → |
| `breakdown_30d` | 53.4% | 133 | → |
| `bearish_engulfing_4h` | 52.5% | 974 | → |
| `evening_star_4h` | 52.1% | 840 | → |
| `rsi_bearish_divergence` | 51.4% | 1655 | 📈 |
| `shooting_star_4h` | 50.9% | 330 | → |
| `resistance_test` | 50.1% | 2187 | → |
| `death_cross` | 49.9% | 399 | → |
| `bear_flag` | 47.9% | 599 | → |
| `macd_bearish_cross` | 47.9% | 8117 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 56.5% | 471 | → |
| `uptrend` | 49.3% | 12945 | → |
| `hammer_4h` | 47.9% | 336 | → |
| `golden_cross` | 46.7% | 863 | 📉 |
| `bullish_engulfing_4h` | 46.3% | 1210 | → |
| `bull_flag` | 44.8% | 297 | → |
| `rsi_bullish_divergence` | 44.6% | 2514 | → |
| `macd_bullish_cross` | 44.0% | 9785 | → |
| `double_bottom_90d` | 43.9% | 2590 | → |
| `support_bounce` | 43.6% | 2691 | → |
| `morning_star_4h` | 39.4% | 930 | → |
| `breakout_30d` | 36.9% | 544 | → |

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
| 2026-09 | Modèle appris | 130 | 48% | 52% | -0.1% |
| 2026-10 | Modèle appris | 80 | 15% | 29% | -6.1% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 4 oct 2026 | **KAIA** | 58% | 0.0375 | +41.9% | ✅ +45.7pp | … |
| 4 oct 2026 | **RENDER** | 58% | 1.942 | -1.2% | ✅ +2.6pp | … |
| 4 oct 2026 | **SUI** | 58% | 1.1824 | -6.7% | ❌ -2.8pp | … |
| 4 oct 2026 | **WIF** | 57% | 0.2469 | -11.4% | ❌ -7.5pp | … |
| 4 oct 2026 | **BCH** | 57% | 318.2 | -12.3% | ❌ -8.5pp | … |
| 4 oct 2026 | **GLM** | 57% | 0.1287 | +3.0% | ✅ +6.9pp | … |
| 4 oct 2026 | **BNB** | 56% | 788.75 | -5.0% | ❌ -1.1pp | … |
| 4 oct 2026 | **WOO** | 56% | 0.01374 | -4.1% | ❌ -0.2pp | … |
| 4 oct 2026 | **1INCH** | 56% | 0.1059 | -7.8% | ❌ -4.0pp | … |
| 4 oct 2026 | **CHZ** | 56% | 0.01697 | -9.1% | ❌ -5.3pp | … |
| 4 oct 2026 | **0G** | 55% | 0.2937 | -9.9% | ❌ -6.1pp | … |
| 4 oct 2026 | **XLM** | 55% | 0.2157 | -7.9% | ❌ -4.1pp | … |
| 4 oct 2026 | **ADA** | 55% | 0.2449 | +1.4% | ✅ +5.3pp | … |
| 4 oct 2026 | **BTC** | 55% | 85127.9 | -2.4% | ✅ +1.5pp | … |
| 4 oct 2026 | **HOT** | 55% | 0.000449 | -6.7% | ❌ -2.8pp | … |
| 4 oct 2026 | **ENS** | 55% | 6.8 | -9.1% | ❌ -5.2pp | … |
| 4 oct 2026 | **APT** | 55% | 0.7961 | +9.6% | ✅ +13.5pp | … |
| 4 oct 2026 | **DOT** | 55% | 1.194 | +3.5% | ✅ +7.4pp | … |
| 4 oct 2026 | **TAO** | 55% | 303.2 | -5.3% | ❌ -1.4pp | … |
| 4 oct 2026 | **PEPE** | 54% | 4.27e-06 | -5.4% | ❌ -1.5pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 946 | 48% | 23% (hasard : 10 %) | +4.7 pts | -1.2 pts |
| Altseason (indice 30 j ≥ 60) | 179 | 44% | 15% (hasard : 10 %) | +3.7 pts | -3.6 pts |
| Hors altseason | 723 | 50% | 26% (hasard : 10 %) | +5.7 pts | -0.2 pts |

**Leaders aujourd'hui — 🚀 Leader (altseason)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **STRK** | Etabli | +294% | 47.6% | ⚠️ 6 |
| 2 | **RLC** | Mid | +291% | 46.8% | ⚠️ 8 |
| 3 | **MAGIC** | Speculative | +189% | 46.4% | ⚠️ 6 |
| 4 | **BAT** | Mid | +101% | 47.8% | ⚠️ 6 |
| 5 | **LUMIA** | Speculative | +100% | 47.1% | ⚠️ 4 |
| 6 | **S** | Mid | +87% | 47.5% | 2 |
| 7 | **W** | Mid | +84% | 49.1% | 2 |
| 8 | **C** | Speculative | +82% | 51.1% | ⚠️ 7 |
| 9 | **AERO** | Etabli | +79% | 47.5% | ⚠️ 6 |
| 10 | **BEAMX** | Speculative | +78% | 50.1% | ⚠️ 6 |
| 11 | **INIT** | Speculative | +75% | 49.7% | ⚠️ 7 |
| 12 | **ZK** | Mid | +72% | 46.9% | 2 |
| 13 | **FLUX** | Speculative | +66% | 51.1% | ⚠️ 7 |
| 14 | **IMX** | Mid | +65% | 49.4% | 2 |
| 15 | **CKB** | Mid | +64% | 46.3% | ⚠️ 4 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : NEAR, VELODROME. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

---

## 📑 Annonces d'ETF crypto (SEC EDGAR)

*Tout ETF crypto américain dépose ses documents à la SEC avant son lancement : dossier S-1/S-3 et ses amendements, puis enregistrement en bourse (8-A12B) quelques jours avant la cotation. ZEC et NEAR ont fortement monté autour de leurs ETF. Étude du 29/09/2026 : après un dépôt de dossier, 75 % des tokens ont battu le marché à 7 et 14 j ; avant un 8-A12B, la hausse était souvent déjà faite (+33 pts sur les 14 j précédents). Petit échantillon : suivi réel ci-dessous.*

| Type de dépôt | Événements | Battent le marché à 7 j | Excès médian 7 j | Battent le marché à 14 j | Excès médian 14 j |
|---|---|---|---|---|---|
| Dossier / amendement (S-1, S-3) | 35 | 74% | +3.5 pts | 81% | +5.3 pts |
| Enregistrement en bourse (8-A12B) | 9 | 56% | +2.2 pts | 67% | +2.7 pts |

**Dépôts des 30 derniers jours :**

| Date | Token | Dépôt | Fonds | Depuis le dépôt (vs marché) |
|---|---|---|---|---|
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | -10% (-5 pts) |
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | -4% (-5 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +22% (+21 pts) |
| 2026-09-18 | **INJ** | S-1/A | 21Shares Injective ETF | +15% (+5 pts) |
| 2026-09-16 | **NEAR** | S-1/A | Bitwise NEAR ETF | +119% (+99 pts) |
| 2026-09-15 | **SEI** | S-1/A | Canary Staked SEI ETF | +57% (+43 pts) |
| 2026-09-11 | **LTC** | S-3/A | Grayscale Litecoin Trust (LTC)  (LTCN) | +22% (+4 pts) |
| 2026-09-11 | **BCH** | S-3/A | Grayscale Bitcoin Cash Trust (BCH)  (BCHG) | +24% (+6 pts) |

**Tokens avec un ETF en préparation ou en lancement :** PEPE (📝 S-1/A le 2026-10-02), INJ (📝 S-1/A le 2026-09-24), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), LTC (📝 S-3/A le 2026-09-11), BCH (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24), ETH (📝 S-3/A le 2026-08-19)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.003 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 9 | +0.009 | 44% | 49% | 50% | 52% | 49% | 50% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 6 oct 2026 | 🌱 Altseason en formation | 76 | +8.1% | ADA, ENJ, WIF |
| 7 oct 2026 | 🟡 Neutre | 64 | +4.6% | KAIA, IOTA, JASMY |
| 8 oct 2026 | 🟡 Neutre | 60 | +5.3% | IOTA, ENJ, SUI |
| 9 oct 2026 | 🟡 Neutre | 58 | +4.2% | SUI, ENJ, DOGE |
| 10 oct 2026 | 🟡 Neutre | 71 | +6.4% | PARTI, JUV, ENJ |
| 11 oct 2026 | 🌱 Altseason en formation | 76 | +7.9% | PARTI, ADA, RENDER |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 47.9% (11 oct 2026) — -37.2% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.6% (11 oct 2026) — +8.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.1% (11 oct 2026) — -13.2% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 56.5% (11 oct 2026) — +32.7% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 51.4% (11 oct 2026) — -24.0% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **45539 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0171 |
| momentum | 0.0441 |
| risk | 0.0239 |
| antiscam | 0.0000 |
| signal | 0.0222 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 11 oct 2026

**Régime :** 🌱 Altseason en formation (indice altseason 30 j : 76.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **PARTI** | Speculative | 56.3% | +2.4pp | ⚠️ 6 |  |
| **ADA** | Etabli | 55.2% | +1.3pp | ⚠️ 5 |  |
| **RENDER** | Etabli | 55.0% | +1.1pp | ⚠️ 5 |  |
| **SUI** | Etabli | 54.8% | +0.9pp | 3 | 🔥 Trending #7 sur CoinGecko |
| **JST** | Etabli | 54.7% | +0.8pp | 3 |  |
| **JUV** | Speculative | 54.6% | +0.7pp | ⚠️ 4 |  |
| **SEI** | Mid | 54.3% | +0.4pp | 3 |  |
| **SCR** | Speculative | 54.3% | +0.4pp | ⚠️ 5 |  |
| **AVAX** | Etabli | 54.2% | +0.3pp | 3 |  |
| **IOTA** | Mid | 54.2% | +0.3pp | ⚠️ 5 |  |
| **AXS** | Mid | 54.1% | +0.2pp | 3 |  |
| **JOE** | Speculative | 54.1% | +0.2pp | ⚠️ 5 |  |
