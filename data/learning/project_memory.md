# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 30 sep 2026*

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

- **Indice altseason** : 88.0 sur 30 j, 64.3 sur 90 j (= % des 100 plus grosses altcoins qui ont fait mieux que BTC ; ≥ 75 = altseason, ≤ 25 = saison Bitcoin)
- **BTC** : 8.8 % sur 30 j · **Tokens au-dessus de leur MA50** : 93.1 %
- ⚠️ **En altseason, les règles changent** : la prime aux grosses caps peu volatiles (ce que j'ai surtout appris) s'efface et le momentum redevient payant. J'intègre donc une part de momentum dans le classement, et j'entraînerai un modèle dédié à l'altseason dès que j'aurai 30 jours d'altseason mesurés (actuellement : 12).

### Mon modèle aujourd'hui : `ml_gb+alt_blend`

- Entraîné sur 54139 observations (136 jours), horizon 7 j
- **Test sur les 5 dernières semaines (données jamais vues)** : mon top 20 a battu la médiane **53%** du temps (règle simple « grosses caps peu volatiles » : 47% ; hasard : 50 %)
- Confiance (calibration) : k = 0.40 — plus k est bas, plus mes probabilités sont ramenées vers 50 % parce que je me suis trompé récemment
- 71 tokens dérivés exclus du classement (actions/ETF tokenisés, versions wrapped/stakées) — liste dans `model_report.json`
- Ce qui compte le plus en ce moment : `rsi_14` (+), `catalyst_score` (−), `p_ma50` (−), `corr_btc_90d` (+), `log_rank` (−), `trend_rank` (+)

**Signaux haussiers fiables (>50%) :** squeeze_breakout ✅
**Signaux baissiers fiables (>50%) :** 8 / 11

**Mon top 20 quotidien, jugé à 7 j :** 2680 prédictions mesurées — 47% ont monté, **50% ont battu la médiane du marché** (50% = hasard)

### ⏳ Le modèle appris est trop récent pour être jugé en conditions réelles (il faut ≥ 10 jours mesurés).
Ce classement sert à réfléchir, pas à acheter : même un bon modèle se trompe souvent sur 7 jours.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `double_top_90d` | 60.3% | 3621 | 📉 |
| `downtrend` | 56.9% | 16430 | → |
| `bearish_engulfing_4h` | 52.9% | 940 | 📉 |
| `shooting_star_4h` | 52.8% | 307 | 📉 |
| `breakdown_30d` | 52.7% | 129 | 📉 |
| `evening_star_4h` | 51.8% | 805 | 📉 |
| `rsi_bearish_divergence` | 51.4% | 1130 | 📉 |
| `death_cross` | 50.7% | 367 | → |
| `resistance_test` | 50.0% | 1847 | → |
| `macd_bearish_cross` | 48.3% | 7832 | 📉 |
| `bear_flag` | 47.9% | 599 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `squeeze_breakout` | 54.5% | 396 | 📈 |
| `golden_cross` | 47.9% | 654 | 📈 |
| `uptrend` | 47.9% | 11184 | 📈 |
| `hammer_4h` | 46.1% | 297 | 📈 |
| `rsi_bullish_divergence` | 44.6% | 2492 | → |
| `bullish_engulfing_4h` | 44.2% | 1103 | 📈 |
| `bull_flag` | 44.0% | 293 | → |
| `double_bottom_90d` | 43.0% | 2398 | → |
| `support_bounce` | 42.9% | 2551 | → |
| `macd_bullish_cross` | 39.9% | 8219 | → |
| `morning_star_4h` | 38.0% | 888 | 📈 |
| `breakout_30d` | 34.8% | 419 | 📈 |

---

## Mes prédictions passées et leurs résultats

*Une prédiction = un des 20 tokens les mieux classés un jour donné. Jugée à 7 j et à 14 j. « Bat le marché » = a fait mieux que la médiane de tous les tokens sur la même période.*

| Mois | Modèle | Prédictions | Ont monté (7 j) | Ont battu le marché (7 j) | Return médian (7 j) |
|------|--------|-------------|-----------------|---------------------------|---------------------|
| 2026-05 | Ancienne formule | 481 | 32% | 61% | -4.3% |
| 2026-06 | Ancienne formule | 480 | 47% | 46% | -0.6% |
| 2026-07 | Ancienne formule | 621 | 43% | 54% | -1.0% |
| 2026-08 | Ancienne formule | 630 | 53% | 42% | +0.4% |
| 2026-09 | Ancienne formule | 468 | 62% | 47% | +3.2% |

**Dernières prédictions mesurées :**

| Date | Token | Score | Prix prédit | Return 7 j | vs marché | Return 14 j |
|------|-------|-------|-------------|------------|-----------|-------------|
| 23 sep 2026 | **BROCCOLI714** | 80% | 0.02316 | +15.9% | ✅ +14.7pp | … |
| 23 sep 2026 | **PENGU** | 80% | 0.010131 | +3.2% | ✅ +2.1pp | … |
| 23 sep 2026 | **WIN** | 80% | 3.973e-05 | +20.0% | ✅ +18.9pp | … |
| 23 sep 2026 | **ASTER** | 78% | 0.7123 | +8.8% | ✅ +7.7pp | … |
| 23 sep 2026 | **XVS** | 77% | 3.366 | +10.6% | ✅ +9.5pp | … |
| 23 sep 2026 | **API3** | 76% | 0.2767 | +6.5% | ✅ +5.4pp | … |
| 23 sep 2026 | **NOT** | 76% | 0.0005 | +1.8% | ✅ +0.6pp | … |
| 23 sep 2026 | **SUSHI** | 76% | 0.2747 | -0.6% | ❌ -1.8pp | … |
| 23 sep 2026 | **UNI** | 76% | 9.744 | -6.0% | ❌ -7.2pp | … |
| 23 sep 2026 | **XRP** | 76% | 1.5665 | -1.9% | ❌ -3.1pp | … |
| 23 sep 2026 | **ZEN** | 76% | 8.126 | -7.0% | ❌ -8.2pp | … |
| 23 sep 2026 | **AT** | 75% | 0.1645 | -6.7% | ❌ -7.9pp | … |
| 23 sep 2026 | **CAKE** | 75% | 2.61 | +2.0% | ✅ +0.8pp | … |
| 23 sep 2026 | **NMR** | 75% | 9.9 | +15.7% | ✅ +14.5pp | … |
| 23 sep 2026 | **ORCA** | 75% | 1.566 | +4.6% | ✅ +3.4pp | … |
| 23 sep 2026 | **WLD** | 75% | 0.455 | +23.6% | ✅ +22.5pp | … |
| 23 sep 2026 | **XNO** | 75% | 0.377 | -2.9% | ❌ -4.1pp | … |
| 23 sep 2026 | **DOLO** | 74% | 0.03024 | +3.6% | ✅ +2.5pp | … |
| 23 sep 2026 | **TWT** | 74% | 0.5717 | +5.3% | ✅ +4.1pp | … |
| 23 sep 2026 | **VET** | 74% | 0.009492 | -3.1% | ❌ -4.3pp | … |

**165 prédictions en attente de résultat (< 7 jours).**

---

## 🚀 Les leaders du moment (2e liste, indépendante du score)

*Règle : perf 30 j dans le top 10 % de l'univers **et** à moins de 5 % de son plus haut 90 j. Le score principal est prudent et évite les tokens qui explosent ; cette liste fait l'inverse. Hors altseason, c'est un pari « loterie » : la plupart retombent, quelques-uns explosent. En altseason, les leaders ont historiquement surperformé nettement (backtest : 67 % battent le marché à 14 j).*

**Suivi réel des leaders (jugés à 14 j) :**

| Régime au moment du signal | Signaux | Ont battu le marché | Sont devenus des top 10 % | Excès moyen | Excès médian |
|---|---|---|---|---|---|
| Tous | 782 | 49% | 25% (hasard : 10 %) | +5.7 pts | -0.2 pts |
| Altseason (indice 30 j ≥ 60) | 41 | 66% | 24% (hasard : 10 %) | +22.5 pts | +4.8 pts |
| Hors altseason | 731 | 49% | 25% (hasard : 10 %) | +4.9 pts | -0.8 pts |

**Leaders aujourd'hui — 🚀 Leader (altseason)** :

| # | Token | Tier | Perf 30 j | Score principal | Exit risk |
|---|-------|------|-----------|-----------------|-----------|
| 1 | **QNT** | Etabli | +395% | 46.2% | ⚠️ 8 |
| 2 | **ARK** | Mid | +252% | 46.1% | ⚠️ 6 |
| 3 | **NEAR** | Etabli | +186% | 48.3% | ⚠️ 4 |
| 4 | **RAY** | Mid | +160% | 47.7% | ⚠️ 5 |
| 5 | **NIGHT** | Mid | +104% | 46.3% | ⚠️ 6 |
| 6 | **MOVR** | Speculative | +93% | 46.0% | ⚠️ 4 |
| 7 | **SOMI** | Speculative | +87% | 46.8% | ⚠️ 6 |
| 8 | **SUPER** | Mid | +86% | 48.4% | ⚠️ 4 |
| 9 | **INIT** | Speculative | +82% | 47.0% | ⚠️ 6 |
| 10 | **ENA** | Etabli | +77% | 47.7% | 2 |
| 11 | **AERO** | Etabli | +74% | 48.9% | ⚠️ 4 |
| 12 | **ZRO** | Mid | +72% | 47.1% | ⚠️ 6 |
| 13 | **RUNE** | Mid | +69% | 48.3% | ⚠️ 6 |
| 14 | **RED** | Mid | +69% | 48.6% | ⚠️ 4 |
| 15 | **PYTH** | Mid | +68% | 47.5% | ⚠️ 4 |

*Exit risk élevé = surachat / essoufflement possible. Un leader peut perdre 30 % en quelques jours.*

---

## 📑 Annonces d'ETF crypto (SEC EDGAR)

*Tout ETF crypto américain dépose ses documents à la SEC avant son lancement : dossier S-1/S-3 et ses amendements, puis enregistrement en bourse (8-A12B) quelques jours avant la cotation. ZEC et NEAR ont fortement monté autour de leurs ETF. Étude du 29/09/2026 : après un dépôt de dossier, 75 % des tokens ont battu le marché à 7 et 14 j ; avant un 8-A12B, la hausse était souvent déjà faite (+33 pts sur les 14 j précédents). Petit échantillon : suivi réel ci-dessous.*

---

## Mon classement distingue-t-il les gagnants des perdants ?

*Mesuré sur **tout l'univers**, à 7 jours. Q1 = les 20 % de tokens les mieux notés du jour, Q5 = les 20 % les moins bien notés. Si le classement fonctionne, Q1 bat le marché plus souvent que Q5.*

| Modèle | Jours | Corrélation de rang | Top 20 bat le marché | Q1 | Q2 | Q3 | Q4 | Q5 |
|--------|-------|---------------------|----------------------|----|----|----|----|----|
| Ancienne formule | 133 | +0.002 | 50% | 50% | 51% | 51% | 50% | 48% |

*(Pourcentages Q1…Q5 = part des tokens du groupe qui ont battu la médiane du marché. Hasard = 50 %.)*

---

## Comment j'évolue et comment je m'adapte

### Évolution du régime de marché

| Date | Régime | Indice altseason 30 j | BTC 30 j | Top tokens |
|------|--------|-----------------------|----------|-----------|
| 1 sep 2026 | 🟢 Haussier | — | (bull_prob 56.0%) | STRAX, NOT, SOMI |
| 2 sep 2026 | 🟢 Haussier | — | (bull_prob 67.0%) | ANKR, SOPH, TUSD |
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

*Avant le 26/09/2026, le régime était déduit de la bull_prob de BTC (ancienne formule).*

### Évolution des patterns clés

**`bear_flag`** (baissier) : 85.1% (17 août 2026) → 47.9% (30 sep 2026) — -37.2% 📉
**`rsi_bullish_divergence`** (haussier) : 36.6% (17 août 2026) → 44.6% (30 sep 2026) — +8.0% 📈
**`downtrend`** (baissier) : 69.3% (17 août 2026) → 56.9% (30 sep 2026) — -12.4% 📉
**`squeeze_breakout`** (haussier) : 23.8% (17 août 2026) → 54.5% (30 sep 2026) — +30.7% 📈
**`rsi_bearish_divergence`** (baissier) : 75.4% (17 août 2026) → 51.4% (30 sep 2026) — -24.0% 📉

### Ce que ça signifie

- Les signaux baissiers **perdent en précision** : le marché sort progressivement du régime baissier.
- Les signaux haussiers **progressent** : le marché commence à répondre aux patterns d'achat.

---

## Le score composite est-il utile ?

J'ai analysé **41330 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0144 |
| momentum | 0.0330 |
| risk | 0.0147 |
| antiscam | 0.0000 |
| signal | 0.0119 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi le score principal vient désormais d'un modèle appris (voir plus haut).

---

## Aujourd'hui — 30 sep 2026

**Régime :** 🌱 Altseason en formation (indice altseason 30 j : 88.0)

**Top 12 du jour** — score = probabilité de battre la médiane du marché sur 7 j (modèle : `ml_gb+alt_blend`) :

| Token | Tier | Score | vs BTC | Exit risk | Catalyseurs |
|-------|------|-------|--------|-----------|-------------|
| **RENDER** | Etabli | 57.0% | +1.8pp | 2 |  |
| **ENS** | Mid | 56.4% | +1.2pp | ⚠️ 4 |  |
| **SOL** | Etabli | 56.3% | +1.1pp | ⚠️ 4 |  |
| **XLM** | Etabli | 55.9% | +0.7pp | 2 |  |
| **TAO** | Etabli | 55.8% | +0.6pp | 2 |  |
| **WIF** | Mid | 55.5% | +0.3pp | ⚠️ 4 |  |
| **KAIA** | Mid | 55.5% | +0.3pp | 2 |  |
| **ADA** | Etabli | 55.3% | +0.1pp | ⚠️ 4 |  |
| **NEO** | Mid | 55.2% | +0.0pp | ⚠️ 4 |  |
| **BTC** | Etabli | 55.2% | +0.0pp | ⚠️ 5 | 🔥 Trending #11 sur CoinGecko |
| **WOO** | Speculative | 55.1% | -0.1pp | 2 |  |
| **AXL** | Mid | 55.0% | -0.2pp | 2 |  |
