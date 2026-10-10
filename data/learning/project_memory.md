# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 10 oct 2026*

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

### Régime de marché : 🟡 Neutre

- **Indice altseason** : 71.0 sur 30 j, 64.3 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 6.4 % sur 30 j · **Tokens au-dessus de leur MA50** : 75.1 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 22).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 58074 observations (146 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **55%** du temps (règle simple « grosses caps peu volatiles » : 48% ; hasard : 50 %)
- Confiance (calibration) : k = 0.41 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 75 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `vol_30d_ann` (−), `bear_signals` (−)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 7 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2912 prédictions mesurées — 47% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 58.4% | 3795 | → |
| `downtrend` | 56.0% | 17408 | → |
| `breakdown_30d` | 53.4% | 133 | → |
| `bearish_engulfing_4h` | 52.4% | 973 | → |
| `evening_star_4h` | 52.0% | 834 | → |
| `shooting_star_4h` | 50.9% | 328 | → |
| `rsi_bearish_divergence` | 50.2% | 1565 | 📈 |
| `resistance_test` | 50.0% | 2152 | → |
| `death_cross` | 49.9% | 397 | → |
| `bear_flag` | 47.9% | 599 | → |
| `macd_bearish_cross` | 47.8% | 8094 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 56.7% | 469 | → |
| `uptrend` | 49.6% | 12789 | → |
| `hammer_4h` | 47.8% | 335 | → |
| `golden_cross` | 47.2% | 836 | → |
| `bullish_engulfing_4h` | 46.5% | 1201 | → |
| `bull_flag` | 44.8% | 297 | → |
| `rsi_bullish_divergence` | 44.6% | 2512 | → |
| `double_bottom_90d` | 44.0% | 2565 | → |
| `macd_bullish_cross` | 44.0% | 9767 | 📈 |
| `support_bounce` | 43.5% | 2682 | → |
| `morning_star_4h` | 39.4% | 930 | → |
| `breakout_30d` | 36.8% | 532 | → |

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
| 2026-10 | Modèle appris | 60 | 12% | 27% | -6.2% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 3 oct 2026 | **BTC** | 59% | 84687.3 | -2.2% | ✅ +0.6pp | … |
| 3 oct 2026 | **RENDER** | 59% | 1.978 | -3.6% | ❌ -0.8pp | … |
| 3 oct 2026 | **SOL** | 59% | 119.4 | -8.0% | ❌ -5.1pp | … |
| 3 oct 2026 | **WIF** | 58% | 0.2476 | -12.6% | ❌ -9.7pp | … |
| 3 oct 2026 | **ETH** | 58% | 2683.59 | -6.9% | ❌ -4.1pp | … |
| 3 oct 2026 | **BONK** | 58% | 3.68e-06 | -7.9% | ❌ -5.0pp | … |
| 3 oct 2026 | **XLM** | 58% | 0.2151 | -8.4% | ❌ -5.6pp | … |
| 3 oct 2026 | **PEPE** | 57% | 4.3e-06 | -6.3% | ❌ -3.4pp | … |
| 3 oct 2026 | **BCH** | 57% | 311.7 | -10.5% | ❌ -7.6pp | … |
| 3 oct 2026 | **ADA** | 57% | 0.2456 | +3.7% | ✅ +6.5pp | … |
| 3 oct 2026 | **AXL** | 57% | 0.0529 | +0.9% | ✅ +3.8pp | … |
| 3 oct 2026 | **LINK** | 57% | 13.923 | -6.7% | ❌ -3.9pp | … |
| 3 oct 2026 | **ENS** | 56% | 6.8 | -6.9% | ❌ -4.1pp | … |
| 3 oct 2026 | **BNB** | 56% | 770.74 | -2.9% | ❌ -0.1pp | … |
| 3 oct 2026 | **XRP** | 56% | 1.4882 | -5.7% | ❌ -2.8pp | … |
| 3 oct 2026 | **VIRTUAL** | 56% | 0.7857 | -6.6% | ❌ -3.8pp | … |
| 3 oct 2026 | **SHIB** | 56% | 5.69e-06 | -4.2% | ❌ -1.4pp | … |
| 3 oct 2026 | **ETC** | 55% | 8.86 | -6.2% | ❌ -3.4pp | … |
| 3 oct 2026 | **THETA** | 55% | 0.2248 | +0.7% | ✅ +3.5pp | … |
| 3 oct 2026 | **TAO** | 55% | 291.1 | -3.1% | ❌ -0.2pp | … |

**140 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 931 | 48% | 23% (hasard : 10 %) | +4.7 pts | -1.1 pts |
| Altseason (indice 30 j ≥ 60) | 164 | 45% | 15% (hasard : 10 %) | +4.1 pts | -3.1 pts |
| Hors altseason | 725 | 50% | 26% (hasard : 10 %) | +5.7 pts | -0.2 pts |

**Leaders aujourd'hui — 🚀 Leader (altseason)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **STRK** | Mid | +144% | 48.4% | ⚠️ 4 |
| 2 | **INIT** | Speculative | +83% | 49.8% | ⚠️ 5 |
| 3 | **W** | Mid | +81% | 48.8% | ⚠️ 6 |
| 4 | **BAT** | Mid | +78% | 47.6% | ⚠️ 6 |
| 5 | **BEAMX** | Speculative | +75% | 54.3% | ⚠️ 4 |
| 6 | **FLUX** | Speculative | +63% | 49.9% | 2 |
| 7 | **AERO** | Etabli | +62% | 50.8% | ⚠️ 9 |
| 8 | **IMX** | Mid | +59% | 48.6% | 2 |
| 9 | **S** | Mid | +58% | 51.5% | ⚠️ 5 |
| 10 | **LUMIA** | Speculative | +54% | 47.2% | 2 |
| 11 | **OPG** | Speculative | +52% | 47.7% | ⚠️ 6 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

**Écartés aujourd'hui — « 2e vague »** (déjà +100 % ou plus dans les 6 mois avant la hausse actuelle) : MUBARAK, NEAR, RAY, VELODROME. *Sur 2 ans de données, ces leaders n'ont battu le marché que 43 % du temps à 7 j (32 % à 30 j), contre 50 % / 51 % pour les leaders dans leur 1re hausse.*

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
| 2026-10-02 | **PEPE** | S-1/A | Canary PEPE ETF | -10% (-4 pts) |
| 2026-09-24 | **INJ** | S-1/A | Canary Staked INJ ETF | -9% (-9 pts) |
| 2026-09-24 | **NEAR** | 8-A12B | Bitwise NEAR ETF  (NRR) | +21% (+21 pts) |
| 2026-09-18 | **INJ** | S-1/A | 21Shares Injective ETF | +9% (-0 pts) |
| 2026-09-16 | **NEAR** | S-1/A | Bitwise NEAR ETF | +116% (+98 pts) |
| 2026-09-15 | **SEI** | S-1/A | Canary Staked SEI ETF | +56% (+42 pts) |
| 2026-09-11 | **LTC** | S-3/A | Grayscale Litecoin Trust (LTC)  (LTCN) | +22% (+6 pts) |
| 2026-09-11 | **BCH** | S-3/A | Grayscale Bitcoin Cash Trust (BCH)  (BCHG) | +24% (+8 pts) |

**Tokens avec un ETF en préparation ou en lancement :** PEPE (📝 S-1/A le 2026-10-02), INJ (📝 S-1/A le 2026-09-24), NEAR (🟢 8-A12B le 2026-09-24), SEI (📝 S-1/A le 2026-09-15), LTC (📝 S-3/A le 2026-09-11), BCH (📝 S-3/A le 2026-09-11), TRX (🟢 8-A12B/A le 2026-09-08), ZEC (🟢 8-A12B le 2026-08-24), ETH (📝 S-3/A le 2026-08-19)

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 135 | +0.003 | 50% | 50% | 50% | 51% | 50% | 48% |
| Modèle appris | 8 | +0.017 | 45% | 49% | 50% | 52% | 49% | 49% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
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
| 7 oct 2026 | 🟡 Neutre | 64 | +4.6% | KAIA, IOTA, JASMY |
| 8 oct 2026 | 🟡 Neutre | 60 | +5.3% | IOTA, ENJ, SUI |
| 9 oct 2026 | 🟡 Neutre | 58 | +4.2% | SUI, ENJ, DOGE |
| 10 oct 2026 | 🟡 Neutre | 71 | +6.4% | PARTI, JUV, ENJ |

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 47.9% (10 oct 2026) — -37.2% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.6% (10 oct 2026) — +8.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.0% (10 oct 2026) — -13.3% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 56.7% (10 oct 2026) — +32.9% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 50.2% (10 oct 2026) — -25.2% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **45160 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0172 |
| momentum | 0.0455 |
| risk | 0.0240 |
| antiscam | 0.0000 |
| signal | 0.0233 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 10 oct 2026

**Régime :** 🟡 Neutre (indice altseason 30 j : 71.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **PARTI** | Speculative | 58.0% | +6.0pp | ⚠️ 6 |  |
| **JUV** | Speculative | 56.2% | +4.2pp | ⚠️ 4 |  |
| **ENJ** | Mid | 55.9% | +3.9pp | 3 |  |
| **SCR** | Speculative | 55.2% | +3.2pp | ⚠️ 5 |  |
| **LAZIO** | Speculative | 54.9% | +2.9pp | ⚠️ 4 |  |
| **IOTA** | Mid | 54.9% | +2.9pp | ⚠️ 5 |  |
| **SEI** | Mid | 54.8% | +2.8pp | 3 |  |
| **SUI** | Etabli | 54.8% | +2.8pp | ⚠️ 5 |  |
| **RENDER** | Etabli | 54.7% | +2.7pp | ⚠️ 5 |  |
| **FLOKI** | Mid | 54.5% | +2.5pp | ⚠️ 5 |  |
| **AAVE** | Etabli | 54.5% | +2.5pp | 3 | 🔥 Trending #12 sur CoinGecko |
| **JASMY** | Mid | 54.4% | +2.4pp | ⚠️ 5 |  |
