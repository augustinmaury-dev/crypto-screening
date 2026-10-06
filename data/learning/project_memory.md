# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 6 oct 2026*

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

- **Indice altseason** : 76.0 sur 30 j, 67.3 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 8.1 % sur 30 j · **Tokens au-dessus de leur MA50** : 90.3 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 18).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 56502 observations (142 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **52%** du temps (règle simple « grosses caps peu volatiles » : 46% ; hasard : 50 %)
- Confiance (calibration) : k = 0.43 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 75 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `log_rank` (−), `pat_bear_flag` (−)

**Signaux haussiers fiables (>50%) :** uptrend, squeeze_breakout, golden_cross ✅
**Signaux baissiers fiables (>50%) :** 7 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2825 prédictions mesurées — 48% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 58.3% | 3759 | 📉 |
| `downtrend` | 55.9% | 16924 | → |
| `breakdown_30d` | 53.4% | 131 | → |
| `bearish_engulfing_4h` | 52.5% | 957 | → |
| `evening_star_4h` | 51.7% | 816 | → |
| `shooting_star_4h` | 50.9% | 324 | → |
| `death_cross` | 50.8% | 388 | → |
| `resistance_test` | 49.1% | 2006 | → |
| `bear_flag` | 47.9% | 599 | → |
| `macd_bearish_cross` | 47.7% | 8004 | → |
| `rsi_bearish_divergence` | 46.3% | 1343 | 📉 |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 57.0% | 453 | 📈 |
| `uptrend` | 50.6% | 12167 | 📈 |
| `golden_cross` | 50.3% | 734 | 📈 |
| `hammer_4h` | 48.4% | 312 | 📈 |
| `bullish_engulfing_4h` | 46.6% | 1188 | 📈 |
| `bull_flag` | 44.8% | 297 | → |
| `rsi_bullish_divergence` | 44.7% | 2501 | → |
| `macd_bullish_cross` | 44.5% | 9372 | 📈 |
| `double_bottom_90d` | 44.3% | 2468 | → |
| `support_bounce` | 43.7% | 2641 | → |
| `morning_star_4h` | 39.5% | 919 | → |
| `breakout_30d` | 38.2% | 484 | 📈 |

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
| 2026-09 | Modèle appris | 103 | 57% | 56% | +1.3% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 29 sep 2026 | **RENDER** | 57% | 1.889 | +15.2% | ✅ +12.5pp | … |
| 29 sep 2026 | **XLM** | 57% | 0.221 | -2.4% | ❌ -5.1pp | … |
| 29 sep 2026 | **AXL** | 57% | 0.0518 | +5.4% | ✅ +2.7pp | … |
| 29 sep 2026 | **BAT** | 57% | 0.0901 | +15.5% | ✅ +12.8pp | … |
| 29 sep 2026 | **ETC** | 57% | 9.01 | -0.8% | ❌ -3.5pp | … |
| 29 sep 2026 | **BCH** | 56% | 306.8 | +3.2% | ✅ +0.5pp | … |
| 29 sep 2026 | **WOO** | 56% | 0.01311 | +4.0% | ✅ +1.3pp | … |
| 29 sep 2026 | **ENS** | 56% | 7.01 | -2.0% | ❌ -4.7pp | … |
| 29 sep 2026 | **CFX** | 56% | 0.05455 | +1.5% | ❌ -1.2pp | … |
| 29 sep 2026 | **CAKE** | 56% | 2.537 | -2.8% | ❌ -5.5pp | … |
| 29 sep 2026 | **HIVE** | 55% | 0.0554 | +4.2% | ✅ +1.4pp | … |
| 29 sep 2026 | **ZK** | 55% | 0.01203 | +7.9% | ✅ +5.2pp | … |
| 29 sep 2026 | **1INCH** | 55% | 0.1022 | +2.0% | ❌ -0.8pp | … |
| 29 sep 2026 | **LTC** | 55% | 67.33 | +3.9% | ✅ +1.2pp | … |
| 29 sep 2026 | **POLYX** | 55% | 0.0427 | +0.5% | ❌ -2.2pp | … |
| 29 sep 2026 | **VET** | 54% | 0.008697 | -0.0% | ❌ -2.7pp | … |
| 29 sep 2026 | **THETA** | 54% | 0.2222 | +7.5% | ✅ +4.8pp | … |
| 29 sep 2026 | **CKB** | 54% | 0.001302 | +2.8% | ✅ +0.1pp | … |
| 29 sep 2026 | **MSTRB** | 54% | 158.08 | +6.5% | ✅ +3.8pp | … |
| 29 sep 2026 | **NEXO** | 54% | 0.843 | +1.5% | ❌ -1.2pp | … |

**147 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 871 | 48% | 24% (hasard : 10 %) | +5.0 pts | -1.1 pts |
| Altseason (indice 30 j ≥ 60) | 104 | 45% | 17% (hasard : 10 %) | +6.1 pts | -2.6 pts |
| Hors altseason | 738 | 49% | 25% (hasard : 10 %) | +5.2 pts | -0.4 pts |

**Leaders aujourd'hui — 🚀 Leader (altseason)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **RLC** | Mid | +177% | 45.8% | ⚠️ 6 |
| 2 | **NEAR** | Etabli | +115% | 49.2% | ⚠️ 5 |
| 3 | **NIGHT** | Etabli | +115% | 48.1% | ⚠️ 4 |
| 4 | **ZRO** | Etabli | +101% | 48.2% | ⚠️ 6 |
| 5 | **SENT** | Mid | +88% | 50.8% | ⚠️ 6 |
| 6 | **INIT** | Speculative | +77% | 48.9% | ⚠️ 6 |
| 7 | **NMR** | Mid | +77% | 45.6% | ⚠️ 6 |
| 8 | **FLUX** | Speculative | +70% | 48.6% | ⚠️ 8 |
| 9 | **SOMI** | Speculative | +66% | 50.5% | ⚠️ 5 |
| 10 | **C** | Speculative | +61% | 48.8% | 2 |
| 11 | **0G** | Mid | +58% | 52.3% | ⚠️ 6 |
| 12 | **RUNE** | Mid | +58% | 52.4% | ⚠️ 4 |
| 13 | **AR** | Mid | +57% | 49.9% | 3 |
| 14 | **BEAMX** | Speculative | +56% | 47.8% | ⚠️ 4 |
| 15 | **RAD** | Speculative | +50% | 46.4% | ⚠️ 6 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : INJ, MUBARAK, ORCA, PUMP, RAY. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

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
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | -2% (-2 pts) |
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | -1% (-7 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +17% (+11 pts) |
| 2026-09-18 | **INJ** | S-1/A | 21Shares Injective ETF | +18% (+2 pts) |
| 2026-09-16 | **NEAR** | S-1/A | Bitwise NEAR ETF | +110% (+85 pts) |
| 2026-09-15 | **SEI** | S-1/A | Canary Staked SEI ETF | +69% (+50 pts) |
| 2026-09-11 | **LTC** | S-3/A | Grayscale Litecoin Trust (LTC)  (LTCN) | +33% (+10 pts) |
| 2026-09-11 | **BCH** | S-3/A | Grayscale Bitcoin Cash Trust (BCH)  (BCHG) | +41% (+17 pts) |
| 2026-09-08 | **TRX** | 8-A12B | Canary Staked TRX ETF  (TRXS) | -1% (-15 pts) |

**Tokens avec un ETF en préparation ou en lancement :** PEPE (📝 S-1/A le 2026-10-02), INJ (📝 S-1/A le 2026-09-24), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), BCH (📝 S-3/A le 2026-09-11), LTC (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24), ETH (📝 S-3/A le 2026-08-19)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.003 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 4 | +0.129 | 57% | 55% | 52% | 55% | 47% | 41% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 6 oct 2026 | 🌱 Altseason en formation | 76 | +8.1% | ADA, ENJ, WIF |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 47.9% (6 oct 2026) — -37.2% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.7% (6 oct 2026) — +8.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 55.9% (6 oct 2026) — -13.4% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 57.0% (6 oct 2026) — +33.2% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 46.3% (6 oct 2026) — -29.1% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **43618 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0172 |
| momentum | 0.0497 |
| risk | 0.0229 |
| antiscam | 0.0000 |
| signal | 0.0270 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 6 oct 2026

**Régime :** 🌱 Altseason en formation (indice altseason 30 j : 76.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **ADA** | Etabli | 57.6% | +4.7pp | 2 |  |
| **ENJ** | Mid | 57.6% | +4.7pp | 2 |  |
| **WIF** | Mid | 57.4% | +4.5pp | ⚠️ 5 |  |
| **KAIA** | Mid | 57.2% | +4.3pp | ⚠️ 4 |  |
| **SOL** | Etabli | 57.1% | +4.2pp | ⚠️ 5 | 🔥 Trending #11 sur CoinGecko |
| **FLOKI** | Mid | 56.9% | +4.0pp | ⚠️ 6 |  |
| **APT** | Etabli | 56.4% | +3.5pp | 3 |  |
| **HOT** | Mid | 56.1% | +3.2pp | ⚠️ 9 |  |
| **BONK** | Mid | 55.9% | +3.0pp | 2 |  |
| **BCH** | Etabli | 55.9% | +3.0pp | ⚠️ 5 |  |
| **SEI** | Mid | 55.6% | +2.7pp | 3 |  |
| **AXL** | Mid | 55.5% | +2.6pp | 3 |  |
