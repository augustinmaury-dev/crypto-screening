# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 3 oct 2026*

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

- **Indice altseason** : 81.0 sur 30 j, 61.2 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 8.7 % sur 30 j · **Tokens au-dessus de leur MA50** : 88.8 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 15).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 55321 observations (139 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **53%** du temps (règle simple « grosses caps peu volatiles » : 47% ; hasard : 50 %)
- Confiance (calibration) : k = 0.49 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 71 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `log_rank` (−), `macd_n` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 7 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2743 prédictions mesurées — 47% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 59.0% | 3705 | 📉 |
| `downtrend` | 56.4% | 16612 | → |
| `breakdown_30d` | 53.1% | 130 | → |
| `bearish_engulfing_4h` | 52.8% | 943 | → |
| `shooting_star_4h` | 52.2% | 314 | → |
| `evening_star_4h` | 51.7% | 808 | → |
| `death_cross` | 50.5% | 380 | → |
| `resistance_test` | 49.7% | 1914 | → |
| `bear_flag` | 47.9% | 599 | → |
| `rsi_bearish_divergence` | 47.8% | 1258 | 📉 |
| `macd_bearish_cross` | 47.7% | 7971 | 📉 |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 55.9% | 417 | 📈 |
| `uptrend` | 49.6% | 11683 | 📈 |
| `golden_cross` | 48.8% | 683 | 📈 |
| `hammer_4h` | 46.8% | 301 | 📈 |
| `bullish_engulfing_4h` | 46.4% | 1179 | 📈 |
| `rsi_bullish_divergence` | 44.7% | 2498 | → |
| `bull_flag` | 44.4% | 295 | → |
| `support_bounce` | 43.7% | 2619 | → |
| `double_bottom_90d` | 43.6% | 2425 | → |
| `macd_bullish_cross` | 41.1% | 8477 | → |
| `morning_star_4h` | 39.3% | 912 | 📈 |
| `breakout_30d` | 35.9% | 443 | 📈 |

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
| 2026-09 | Modèle appris | 21 | 29% | 71% | -1.5% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 26 sep 2026 | **RENDER** | 57% | 1.992 | -0.7% | ✅ +3.6pp | … |
| 26 sep 2026 | **ENS** | 56% | 7.12 | -4.5% | ❌ -0.2pp | … |
| 26 sep 2026 | **LINK** | 56% | 14.29 | -2.6% | ✅ +1.8pp | … |
| 26 sep 2026 | **WIF** | 56% | 0.2496 | -0.8% | ✅ +3.5pp | … |
| 26 sep 2026 | **SOL** | 55% | 121.25 | -1.5% | ✅ +2.8pp | … |
| 26 sep 2026 | **BNSOL** | 55% | 137.3 | -1.4% | ✅ +3.0pp | … |
| 26 sep 2026 | **KAIA** | 55% | 0.0346 | +5.5% | ✅ +9.8pp | … |
| 26 sep 2026 | **AXL** | 55% | 0.0535 | -1.1% | ✅ +3.2pp | … |
| 26 sep 2026 | **ETC** | 55% | 9.55 | -7.2% | ❌ -2.9pp | … |
| 26 sep 2026 | **PEPE** | 55% | 4.41e-06 | -2.5% | ✅ +1.8pp | … |
| 26 sep 2026 | **HBAR** | 54% | 0.09407 | +8.1% | ✅ +12.4pp | … |
| 26 sep 2026 | **WOO** | 54% | 0.01344 | +4.0% | ✅ +8.3pp | … |
| 26 sep 2026 | **POLYX** | 54% | 0.0459 | -8.1% | ❌ -3.7pp | … |
| 26 sep 2026 | **NEO** | 54% | 2.69 | -6.2% | ❌ -1.9pp | … |
| 26 sep 2026 | **AAVE** | 54% | 154.23 | +17.9% | ✅ +22.2pp | … |
| 26 sep 2026 | **IOTA** | 54% | 0.0507 | +6.1% | ✅ +10.4pp | … |
| 26 sep 2026 | **PENGU** | 54% | 0.01015 | -10.1% | ❌ -5.8pp | … |
| 26 sep 2026 | **ADA** | 53% | 0.2571 | -4.5% | ❌ -0.1pp | … |
| 26 sep 2026 | **XRP** | 53% | 1.5464 | -3.8% | ✅ +0.6pp | … |
| 26 sep 2026 | **AVAX** | 53% | 10.951 | +1.6% | ✅ +5.9pp | … |

**169 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 826 | 49% | 24% (hasard : 10 %) | +5.5 pts | -0.4 pts |
| Altseason (indice 30 j ≥ 60) | 71 | 54% | 20% (hasard : 10 %) | +12.2 pts | +1.0 pts |
| Hors altseason | 745 | 49% | 25% (hasard : 10 %) | +5.0 pts | -0.8 pts |

**Leaders aujourd'hui — 🚀 Leader (altseason)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **RAY** | Mid | +155% | 49.4% | ⚠️ 5 |
| 2 | **NIGHT** | Etabli | +137% | 46.2% | ⚠️ 6 |
| 3 | **SUPER** | Mid | +136% | 47.5% | ⚠️ 6 |
| 4 | **MINA** | Mid | +124% | 50.4% | ⚠️ 4 |
| 5 | **GLMR** | Speculative | +96% | 45.6% | ⚠️ 4 |
| 6 | **ZRO** | Etabli | +90% | 48.3% | ⚠️ 4 |
| 7 | **SAND** | Mid | +88% | 45.6% | ⚠️ 6 |
| 8 | **AR** | Mid | +86% | 47.7% | ⚠️ 5 |
| 9 | **INIT** | Speculative | +81% | 48.7% | ⚠️ 4 |
| 10 | **C** | Speculative | +66% | 46.9% | ⚠️ 6 |
| 11 | **VELODROME** | Speculative | +54% | 44.0% | 2 |
| 12 | **CHR** | Speculative | +54% | 49.6% | 2 |
| 13 | **FLUX** | Speculative | +53% | 51.4% | ⚠️ 4 |

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
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | -5% (-8 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +6% (+3 pts) |
| 2026-09-18 | **INJ** | S-1/A | 21Shares Injective ETF | +14% (+2 pts) |
| 2026-09-16 | **NEAR** | S-1/A | Bitwise NEAR ETF | +89% (+68 pts) |
| 2026-09-15 | **SEI** | S-1/A | Canary Staked SEI ETF | +64% (+48 pts) |
| 2026-09-11 | **LTC** | S-3/A | Grayscale Litecoin Trust (LTC)  (LTCN) | +33% (+14 pts) |
| 2026-09-11 | **BCH** | S-3/A | Grayscale Bitcoin Cash Trust (BCH)  (BCHG) | +38% (+19 pts) |
| 2026-09-08 | **TRX** | 8-A12B | Canary Staked TRX ETF  (TRXS) | -1% (-12 pts) |

**Tokens avec un ETF en préparation ou en lancement :** NEAR (🟢 8-A12B le 2026-09-24), INJ (📝 S-1/A le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), BCH (📝 S-3/A le 2026-09-11), LTC (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24), ETH (📝 S-3/A le 2026-08-19)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.003 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 1 | +0.196 | 70% | 65% | 54% | 51% | 42% | 38% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 3 oct 2026 | 🌱 Altseason en formation | 81 | +8.7% | BTC, RENDER, SOL |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 47.9% (3 oct 2026) — -37.2% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.7% (3 oct 2026) — +8.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.4% (3 oct 2026) — -12.9% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 55.9% (3 oct 2026) — +32.1% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 47.8% (3 oct 2026) — -27.6% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **42361 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0162 |
| momentum | 0.0420 |
| risk | 0.0176 |
| antiscam | 0.0000 |
| signal | 0.0193 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 3 oct 2026

**Régime :** 🌱 Altseason en formation (indice altseason 30 j : 81.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **BTC** | Etabli | 59.4% | +0.0pp | ⚠️ 7 | 🔥 Trending #9 sur CoinGecko |
| **RENDER** | Etabli | 59.4% | +0.0pp | ⚠️ 4 |  |
| **SOL** | Etabli | 59.2% | -0.2pp | ⚠️ 7 |  |
| **WIF** | Mid | 58.3% | -1.1pp | ⚠️ 4 |  |
| **ETH** | Etabli | 58.2% | -1.2pp | ⚠️ 5 |  |
| **BONK** | Mid | 57.9% | -1.5pp | 2 |  |
| **XLM** | Etabli | 57.8% | -1.6pp | ⚠️ 5 |  |
| **PEPE** | Etabli | 57.3% | -2.1pp | ⚠️ 5 |  |
| **BCH** | Etabli | 57.0% | -2.4pp | ⚠️ 5 |  |
| **ADA** | Etabli | 56.8% | -2.6pp | ⚠️ 5 |  |
| **LINK** | Etabli | 56.7% | -2.7pp | 2 |  |
| **AXL** | Mid | 56.7% | -2.7pp | ⚠️ 7 |  |
