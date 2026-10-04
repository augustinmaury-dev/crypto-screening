# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 4 oct 2026*

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

- **Indice altseason** : 81.0 sur 30 j, 64.3 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 4.7 % sur 30 j · **Tokens au-dessus de leur MA50** : 90.9 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 16).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 55715 observations (140 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **55%** du temps (règle simple « grosses caps peu volatiles » : 48% ; hasard : 50 %)
- Confiance (calibration) : k = 0.45 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 71 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `log_rank` (−), `macd_n` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout, uptrend ✅
**Signaux baissiers fiables (>50%) :** 7 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2765 prédictions mesurées — 47% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 58.6% | 3729 | 📉 |
| `downtrend` | 56.3% | 16678 | → |
| `breakdown_30d` | 53.1% | 130 | → |
| `bearish_engulfing_4h` | 52.8% | 945 | → |
| `shooting_star_4h` | 52.2% | 314 | → |
| `evening_star_4h` | 51.7% | 809 | → |
| `death_cross` | 50.4% | 383 | → |
| `resistance_test` | 49.5% | 1941 | → |
| `bear_flag` | 47.9% | 599 | → |
| `macd_bearish_cross` | 47.7% | 7982 | 📉 |
| `rsi_bearish_divergence` | 47.5% | 1268 | 📉 |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 56.4% | 424 | 📈 |
| `uptrend` | 50.1% | 11853 | 📈 |
| `golden_cross` | 49.5% | 699 | 📈 |
| `hammer_4h` | 47.4% | 304 | 📈 |
| `bullish_engulfing_4h` | 46.4% | 1179 | 📈 |
| `bull_flag` | 44.8% | 297 | → |
| `rsi_bullish_divergence` | 44.7% | 2498 | → |
| `double_bottom_90d` | 43.8% | 2435 | → |
| `support_bounce` | 43.7% | 2631 | → |
| `macd_bullish_cross` | 42.4% | 8721 | 📈 |
| `morning_star_4h` | 39.4% | 916 | 📈 |
| `breakout_30d` | 35.9% | 448 | → |

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
| 2026-09 | Modèle appris | 43 | 30% | 67% | -2.0% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 27 sep 2026 | **LINK** | 57% | 14.326 | -1.6% | ✅ +1.8pp | … |
| 27 sep 2026 | **SOL** | 56% | 124.13 | -2.3% | ✅ +1.1pp | … |
| 27 sep 2026 | **TAO** | 56% | 335.5 | -9.6% | ❌ -6.2pp | … |
| 27 sep 2026 | **BNSOL** | 55% | 140.3 | -2.1% | ✅ +1.3pp | … |
| 27 sep 2026 | **ENS** | 55% | 7.11 | -4.4% | ❌ -1.0pp | … |
| 27 sep 2026 | **WIF** | 55% | 0.2506 | -1.5% | ✅ +1.9pp | … |
| 27 sep 2026 | **AAVE** | 55% | 156.18 | +15.6% | ✅ +19.0pp | … |
| 27 sep 2026 | **KAIA** | 55% | 0.0361 | +3.9% | ✅ +7.3pp | … |
| 27 sep 2026 | **WOO** | 54% | 0.01358 | +1.2% | ✅ +4.6pp | … |
| 27 sep 2026 | **ETC** | 54% | 9.55 | -7.5% | ❌ -4.1pp | … |
| 27 sep 2026 | **ADA** | 54% | 0.258 | -5.1% | ❌ -1.7pp | … |
| 27 sep 2026 | **NEO** | 54% | 2.684 | -5.2% | ❌ -1.9pp | … |
| 27 sep 2026 | **BNT** | 54% | 0.3536 | -2.4% | ✅ +1.0pp | … |
| 27 sep 2026 | **LPT** | 54% | 1.777 | -2.9% | ✅ +0.5pp | … |
| 27 sep 2026 | **AVAX** | 53% | 11.023 | -0.3% | ✅ +3.1pp | … |
| 27 sep 2026 | **POLYX** | 53% | 0.0455 | -7.5% | ❌ -4.1pp | … |
| 27 sep 2026 | **DOGE** | 53% | 0.0986 | -5.3% | ❌ -1.9pp | … |
| 27 sep 2026 | **HBAR** | 53% | 0.09558 | +6.3% | ✅ +9.7pp | … |
| 27 sep 2026 | **MSTRB** | 53% | 162.36 | +0.7% | ✅ +4.0pp | … |
| 27 sep 2026 | **PEPE** | 53% | 4.46e-06 | -4.3% | ❌ -0.9pp | … |

**167 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 841 | 49% | 24% (hasard : 10 %) | +5.3 pts | -0.9 pts |
| Altseason (indice 30 j ≥ 60) | 74 | 47% | 19% (hasard : 10 %) | +9.2 pts | -2.0 pts |
| Hors altseason | 745 | 49% | 25% (hasard : 10 %) | +5.0 pts | -0.8 pts |

**Leaders aujourd'hui — 🚀 Leader (altseason)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **RAY** | Mid | +146% | 46.5% | 3 |
| 2 | **NIGHT** | Etabli | +126% | 47.6% | ⚠️ 8 |
| 3 | **MINA** | Mid | +119% | 50.6% | ⚠️ 6 |
| 4 | **STRK** | Mid | +103% | 46.9% | ⚠️ 4 |
| 5 | **SAND** | Mid | +94% | 46.6% | ⚠️ 6 |
| 6 | **SOMI** | Speculative | +88% | 50.2% | ⚠️ 7 |
| 7 | **INIT** | Speculative | +87% | 48.8% | ⚠️ 8 |
| 8 | **ZRO** | Etabli | +81% | 48.9% | ⚠️ 4 |
| 9 | **SENT** | Mid | +81% | 50.5% | ⚠️ 4 |
| 10 | **BEAMX** | Speculative | +76% | 46.2% | ⚠️ 6 |
| 11 | **NOM** | Speculative | +75% | 46.2% | 2 |
| 12 | **C** | Speculative | +71% | 48.2% | ⚠️ 6 |
| 13 | **AERO** | Etabli | +68% | 50.5% | ⚠️ 4 |
| 14 | **RUNE** | Mid | +63% | 48.4% | 2 |
| 15 | **HUMA** | Mid | +61% | 50.4% | ⚠️ 4 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

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
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | -4% (-3 pts) |
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | -6% (-10 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +10% (+6 pts) |
| 2026-09-18 | **INJ** | S-1/A | 21Shares Injective ETF | +13% (-0 pts) |
| 2026-09-16 | **NEAR** | S-1/A | Bitwise NEAR ETF | +97% (+76 pts) |
| 2026-09-15 | **SEI** | S-1/A | Canary Staked SEI ETF | +68% (+50 pts) |
| 2026-09-11 | **LTC** | S-3/A | Grayscale Litecoin Trust (LTC)  (LTCN) | +36% (+15 pts) |
| 2026-09-11 | **BCH** | S-3/A | Grayscale Bitcoin Cash Trust (BCH)  (BCHG) | +41% (+20 pts) |
| 2026-09-08 | **TRX** | 8-A12B | Canary Staked TRX ETF  (TRXS) | -1% (-13 pts) |

**Tokens avec un ETF en préparation ou en lancement :** PEPE (📝 S-1/A le 2026-10-02), INJ (📝 S-1/A le 2026-09-24), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), BCH (📝 S-3/A le 2026-09-11), LTC (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24), ETH (📝 S-3/A le 2026-08-19)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.003 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 2 | +0.160 | 65% | 60% | 50% | 52% | 49% | 39% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 4 oct 2026 | 🌱 Altseason en formation | 81 | +4.7% | KAIA, RENDER, SUI |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 47.9% (4 oct 2026) — -37.2% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.7% (4 oct 2026) — +8.1% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.3% (4 oct 2026) — -13.0% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 56.4% (4 oct 2026) — +32.6% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 47.5% (4 oct 2026) — -27.9% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **42750 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0166 |
| momentum | 0.0456 |
| risk | 0.0196 |
| antiscam | 0.0000 |
| signal | 0.0233 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 4 oct 2026

**Régime :** 🌱 Altseason en formation (indice altseason 30 j : 81.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **KAIA** | Mid | 58.4% | +3.3pp | ⚠️ 6 |  |
| **RENDER** | Etabli | 58.1% | +3.0pp | 2 |  |
| **SUI** | Etabli | 57.9% | +2.8pp | 2 |  |
| **WIF** | Mid | 57.3% | +2.2pp | ⚠️ 4 |  |
| **BCH** | Etabli | 56.8% | +1.7pp | ⚠️ 5 |  |
| **GLM** | Mid | 56.7% | +1.6pp | ⚠️ 7 |  |
| **BNB** | Etabli | 56.5% | +1.4pp | ⚠️ 5 |  |
| **WOO** | Speculative | 56.0% | +0.9pp | ⚠️ 4 |  |
| **1INCH** | Mid | 55.6% | +0.5pp | ⚠️ 4 |  |
| **CHZ** | Mid | 55.5% | +0.4pp | 2 |  |
| **XLM** | Etabli | 55.4% | +0.3pp | ⚠️ 5 |  |
| **0G** | Mid | 55.4% | +0.3pp | 2 |  |
