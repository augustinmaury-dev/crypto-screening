# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 2 oct 2026*

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

- **Indice altseason** : 82.0 sur 30 j, 60.2 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 13.0 % sur 30 j · **Tokens au-dessus de leur MA50** : 93.4 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 14).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 54927 observations (138 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **51%** du temps (règle simple « grosses caps peu volatiles » : 46% ; hasard : 50 %)
- Confiance (calibration) : k = 0.40 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 71 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `log_rank` (−), `macd_n` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 7 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2722 prédictions mesurées — 48% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 59.3% | 3682 | 📉 |
| `downtrend` | 56.5% | 16552 | → |
| `breakdown_30d` | 53.1% | 130 | → |
| `bearish_engulfing_4h` | 52.8% | 942 | 📉 |
| `shooting_star_4h` | 52.6% | 310 | → |
| `evening_star_4h` | 51.7% | 807 | 📉 |
| `death_cross` | 50.4% | 377 | → |
| `rsi_bearish_divergence` | 50.0% | 1185 | 📉 |
| `resistance_test` | 49.9% | 1880 | → |
| `bear_flag` | 47.9% | 599 | → |
| `macd_bearish_cross` | 47.7% | 7958 | 📉 |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 55.2% | 406 | 📈 |
| `uptrend` | 49.2% | 11508 | 📈 |
| `golden_cross` | 48.3% | 671 | 📈 |
| `hammer_4h` | 46.7% | 300 | 📈 |
| `bullish_engulfing_4h` | 45.0% | 1119 | 📈 |
| `rsi_bullish_divergence` | 44.7% | 2498 | → |
| `bull_flag` | 44.0% | 293 | → |
| `support_bounce` | 43.6% | 2610 | → |
| `double_bottom_90d` | 43.3% | 2412 | → |
| `macd_bullish_cross` | 40.2% | 8287 | → |
| `morning_star_4h` | 38.5% | 898 | 📈 |
| `breakout_30d` | 35.0% | 426 | → |

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

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 25 sep 2026 | **IQ** | 78% | 0.000976 | -6.5% | ❌ -7.3pp | … |
| 25 sep 2026 | **ONDO** | 77% | 0.5452 | -6.4% | ❌ -7.3pp | … |
| 25 sep 2026 | **AT** | 75% | 0.1514 | +1.1% | ✅ +0.2pp | … |
| 25 sep 2026 | **EIGEN** | 75% | 0.2458 | +6.6% | ✅ +5.8pp | … |
| 25 sep 2026 | **QTUM** | 75% | 1.034 | -1.0% | ❌ -1.9pp | … |
| 25 sep 2026 | **LINK** | 74% | 13.959 | +2.8% | ✅ +1.9pp | … |
| 25 sep 2026 | **MUBARAK** | 73% | 0.04543 | +37.0% | ✅ +36.1pp | … |
| 25 sep 2026 | **NEAR** | 73% | 5.042 | -2.8% | ❌ -3.7pp | … |
| 25 sep 2026 | **NMR** | 73% | 9.72 | +17.2% | ✅ +16.3pp | … |
| 25 sep 2026 | **NVDAB** | 73% | 225.99 | +4.5% | ✅ +3.6pp | … |
| 25 sep 2026 | **XRP** | 73% | 1.6138 | -4.7% | ❌ -5.6pp | … |
| 25 sep 2026 | **1INCH** | 72% | 0.1025 | +3.1% | ✅ +2.2pp | … |
| 25 sep 2026 | **AI** | 72% | 0.0197 | -3.0% | ❌ -3.9pp | … |
| 25 sep 2026 | **CVC** | 72% | 0.03047 | +1.9% | ✅ +1.0pp | … |
| 25 sep 2026 | **FLOW** | 72% | 0.03209 | +1.1% | ✅ +0.2pp | … |
| 25 sep 2026 | **LSK** | 72% | 0.3477 | -18.0% | ❌ -18.9pp | … |
| 25 sep 2026 | **REZ** | 72% | 0.004165 | +5.3% | ✅ +4.4pp | … |
| 25 sep 2026 | **RONIN** | 72% | 0.0676 | +2.7% | ✅ +1.8pp | … |
| 25 sep 2026 | **SUSHI** | 72% | 0.2602 | +1.8% | ✅ +0.9pp | … |
| 25 sep 2026 | **THETA** | 72% | 0.2271 | +2.1% | ✅ +1.2pp | … |

**170 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 811 | 49% | 25% (hasard : 10 %) | +5.7 pts | -0.3 pts |
| Altseason (indice 30 j ≥ 60) | 56 | 57% | 23% (hasard : 10 %) | +16.7 pts | +2.2 pts |
| Hors altseason | 745 | 49% | 25% (hasard : 10 %) | +5.0 pts | -0.8 pts |

**Leaders aujourd'hui — 🚀 Leader (altseason)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **NIGHT** | Etabli | +164% | 47.2% | ⚠️ 6 |
| 2 | **MINA** | Mid | +130% | 51.8% | ⚠️ 6 |
| 3 | **SUPER** | Mid | +113% | 48.3% | ⚠️ 6 |
| 4 | **ZRO** | Etabli | +90% | 48.9% | ⚠️ 6 |
| 5 | **SAND** | Mid | +80% | 46.5% | ⚠️ 6 |
| 6 | **RUNE** | Mid | +70% | 51.3% | ⚠️ 4 |
| 7 | **INIT** | Speculative | +69% | 49.9% | 2 |
| 8 | **SUI** | Etabli | +68% | 50.8% | 2 |
| 9 | **C** | Speculative | +65% | 49.0% | ⚠️ 6 |
| 10 | **HUMA** | Mid | +63% | 49.1% | ⚠️ 4 |
| 11 | **CHR** | Speculative | +60% | 50.0% | ⚠️ 4 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : WLD. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

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
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | -6% (-12 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +11% (+5 pts) |
| 2026-09-18 | **INJ** | S-1/A | 21Shares Injective ETF | +12% (-3 pts) |
| 2026-09-16 | **NEAR** | S-1/A | Bitwise NEAR ETF | +99% (+75 pts) |
| 2026-09-15 | **SEI** | S-1/A | Canary Staked SEI ETF | +65% (+45 pts) |
| 2026-09-11 | **LTC** | S-3/A | Grayscale Litecoin Trust (LTC)  (LTCN) | +34% (+10 pts) |
| 2026-09-11 | **BCH** | S-3/A | Grayscale Bitcoin Cash Trust (BCH)  (BCHG) | +40% (+16 pts) |
| 2026-09-08 | **TRX** | 8-A12B | Canary Staked TRX ETF  (TRXS) | -1% (-16 pts) |

**Tokens avec un ETF en préparation ou en lancement :** INJ (📝 S-1/A le 2026-09-24), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), BCH (📝 S-3/A le 2026-09-11), LTC (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24), ETH (📝 S-3/A le 2026-08-19)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.003 | 50% | 50% | 50% | 51% | 50% | 48% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
| 3 sep 2026 | 🟢 Haussier | — | (bull_prob 56.0%) | PROM, RED, COMP |
| 4 sep 2026 | 🟡 Neutre | — | (bull_prob 51.0%) | HIVE, PROM, ZKP |
| 5 sep 2026 | 🟢 Haussier | — | (bull_prob 58.0%) | AIXBT, 1000CAT, ZKP |
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

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 47.9% (2 oct 2026) — -37.2% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.7% (2 oct 2026) — +8.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.5% (2 oct 2026) — -12.8% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 55.2% (2 oct 2026) — +31.4% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 50.0% (2 oct 2026) — -25.4% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **41968 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0159 |
| momentum | 0.0399 |
| risk | 0.0164 |
| antiscam | 0.0000 |
| signal | 0.0170 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 2 oct 2026

**Régime :** 🌱 Altseason en formation (indice altseason 30 j : 82.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **RENDER** | Etabli | 58.5% | +2.8pp | 2 |  |
| **KAIA** | Mid | 58.1% | +2.4pp | ⚠️ 4 |  |
| **LPT** | Mid | 57.4% | +1.7pp | 2 |  |
| **WIF** | Mid | 57.3% | +1.6pp | 2 |  |
| **IOTA** | Mid | 57.2% | +1.5pp | 2 |  |
| **WOO** | Speculative | 56.9% | +1.2pp | 2 |  |
| **TAO** | Etabli | 56.8% | +1.1pp | 2 |  |
| **ENS** | Mid | 56.7% | +1.0pp | ⚠️ 4 |  |
| **ADA** | Etabli | 56.6% | +0.9pp | 2 |  |
| **BONK** | Mid | 56.6% | +0.9pp | 2 |  |
| **SOL** | Etabli | 56.4% | +0.7pp | ⚠️ 7 |  |
| **BNT** | Speculative | 56.3% | +0.6pp | ⚠️ 4 |  |
