# Méthodologie de scoring — Crypto USDT Binance

> Ce document est la **source de vérité** de la formule. Toute modification doit être tracée ici.
> Version : 1.2 — 2026-04-18

## Avertissement
Le score n'est **pas un signal d'achat**. C'est un agrégat d'indicateurs publics (marché, fondamentaux, technique, signaux de risque) destiné à hiérarchiser un univers large pour un examen humain.

## Univers
- Source : `/api/v3/exchangeInfo` (Binance) filtré sur `quoteAsset == "USDT"` et `status == "TRADING"`.
- Croisement avec CoinGecko `/coins/markets` (top 1000 par market cap).
- Tous les tokens conservés. Trois tiers :
  - **Établi** : market cap rank ≤ 100
  - **Mid** : 101 ≤ rank ≤ 500
  - **Speculative** : rank > 500 ou hors CoinGecko

## Filtre SUSPECT (exclusion automatique du classement principal)
Un token est marqué `SUSPECT` si **au moins 2 conditions sur 3** :
1. Équipe non identifiable (pas de LinkedIn / pas de noms publics dans la doc)
2. Promesses de rendement détectées (regex `\b(guaranteed|100x|1000x|moonshot|risk-?free|passive income)\b` dans description CoinGecko ou site)
3. Âge < 180 jours (genesis_date CoinGecko ou première bougie Binance)

Un seul des 3 → flag `WATCH`, reste classé.

## Score composite — 0 à 100
Somme pondérée de 5 sous-scores, chacun normalisé sur 0–100.

**Formule v1.2 (prédictive)**
```
SCORE = 0.20 × Solidité + 0.30 × Momentum + 0.15 × Signal + 0.15 × Risque/Qualité + 0.20 × AntiScam
```

Philosophie : le momentum en cours et les patterns directionnels (signal) sont plus prédictifs de la performance future que la solidité fondamentale ou les métriques de risque passé. L'anti-scam reste inchangé à 20 % pour filtrer les tokens frauduleux.

### 1. Solidité fondamentale (poids 20 %)
| Composant | Poids interne | Calcul |
|---|---|---|
| Tier mcap | 35 % | Établi=100, Mid=60, Speculative=20, hors CG=0 |
| Âge du projet | 20 % | min(100, jours_depuis_genesis / 365 × 50) — plafond à 100 = 2 ans+ |
| Audits | 20 % | Audit récent (≤24 mois) par CertiK/Hacken/Trail of Bits/OpenZeppelin/Quantstamp = 100, audit ancien = 60, mention sans preuve = 30, rien = 0 |
| Activité GitHub | 25 % | f(commits_30j, contributeurs_actifs) — voir détail ci-dessous |

GitHub :
```
github_score = min(100,
    40 × min(1, commits_30j / 30)
  + 40 × min(1, contributeurs_actifs_90j / 5)
  + 20 × (1 if last_release_age_days < 90 else 0)
)
```
Si pas de repo connu → 0.

### 2. Momentum technique (poids 30 %)
| Composant | Poids | Calcul |
|---|---|---|
| Position vs MA | 40 % | prix > MA50 > MA200 = 100, prix > MA50 < MA200 = 60, prix < MA50 > MA200 = 30, prix < MA50 < MA200 = 10 |
| RSI zone saine | 30 % | 45–65 = 100, 35–45 ou 65–75 = 70, 25–35 ou 75–85 = 40, extrêmes = 10 |
| Confirmation volume | 30 % | volume_24h / médiane_90j > 1.5 = 100, > 1.0 = 70, > 0.5 = 40, sinon 10 |

### 3. Signal directionnel (poids 15 %)
Axe **prédictif** basé sur le biais net des patterns techniques détectés.

```
net_bull = bull_signals - bear_signals
total    = bull_signals + bear_signals
ratio    = net_bull / total              # ∈ [-1, +1]
conviction = min(1.0, total / 4)        # pleine conviction à 4+ signaux
score_signal = clamp(50 + ratio × 50 × conviction, 0, 100)
```

Interprétation :
- score > 50 → biais haussier (plus il est élevé, plus les patterns convergent à la hausse)
- score = 50 → neutre (aucun signal ou signaux contradictoires)
- score < 50 → biais baissier

Exemples :
- 4 bull, 0 bear → score = 100
- 2 bull, 1 bear → score ≈ 67
- 0 signal → score = 50
- 0 bull, 3 bear → score ≈ 13

### 4. Risque / qualité (poids 15 %)
| Composant | Poids | Calcul |
|---|---|---|
| Volatilité 30j annualisée | 35 % | < 60 % = 100, 60–100 % = 70, 100–150 % = 40, > 150 % = 10 |
| Drawdown 90j | 30 % | < 25 % = 100, 25–50 % = 60, 50–75 % = 30, > 75 % = 10 |
| Distance au plus haut 90j | 15 % | < 10 % = 100, 10–30 % = 70, 30–50 % = 40, > 50 % = 10 |
| Corrélation 90j à BTC | 20 % | 0.3 ≤ ρ ≤ 0.7 = 100 (diversifiant), 0.7 < ρ ≤ 0.9 = 60, > 0.9 = 30, < 0.3 = 70 (pertinent si justifié) |

### 5. Anti-scam / qualité de marché (poids 20 %)
| Composant | Poids | Calcul |
|---|---|---|
| Liquidité réelle | 35 % | volume_24h_USDT > 5M = 100, 1M–5M = 70, 500k–1M = 40, < 500k = 10 |
| Stabilité de la liquidité | 25 % | écart-type(volume_30j) / moyenne < 0.5 = 100, < 1 = 70, < 2 = 40, sinon 10 |
| Identifiabilité équipe | 20 % | Équipe publique avec LinkedIn = 100, partiellement publique = 60, anonyme déclaré = 30, anonyme caché = 0 |
| Absence de red flags langage | 20 % | 0 red flag = 100, 1 = 60, 2 = 20, 3+ = 0 |

## Patterns techniques détectés (signaux séparés du score)
Annotés sur le token, **n'entrent pas dans le score**. Classés en haussiers / baissiers / neutres.

### Signaux haussiers
| Pattern | Condition |
|---|---|
| Breakout 30j | Clôture > max(high 30j) ET volume > 1.5× médiane 30j |
| Divergence RSI haussière | Prix fait nouveau bas 14j, RSI fait nouveau haut 14j |
| Golden Cross | MA50 croise MA200 par le haut (≤ 5 bougies) |
| Croisement MACD haussier | MACD croise signal par le haut (≤ 5 bougies) |
| Double fond 90j | Deux creux à ±3% sur 90j, reprise entre les deux |
| Bull flag | Hausse >10% (mât), consolidation <10% de range à volume décroissant |
| Structure haussière (HH+HL) | Plus haut swing high ET plus haut swing low sur 60j |
| Rebond sur support | Prix près du support médian 90j avec reprise sur 3j |
| Marteau 4h | Longue mèche basse, petit corps, dans contexte baissier |
| Engulfing haussier 4h | Bougie verte englobe la bougie rouge précédente |
| Morning star 4h | 3 bougies : rouge, petit corps, grande verte dépassant mi-corps rouge |

### Signaux baissiers
| Pattern | Condition |
|---|---|
| Breakdown 30j | Clôture < min(low 30j) ET volume > 1.5× médiane 30j |
| Divergence RSI baissière | Prix fait nouveau haut 14j, RSI fait nouveau bas 14j |
| Death Cross | MA50 croise MA200 par le bas (≤ 5 bougies) |
| Croisement MACD baissier | MACD croise signal par le bas (≤ 5 bougies) |
| Double sommet 90j | Deux sommets à ±3% sur 90j, repli entre les deux |
| Bear flag | Baisse >10% (mât), consolidation <10% de range à volume décroissant |
| Structure baissière (LH+LL) | Plus bas swing high ET plus bas swing low sur 60j |
| Test de résistance | Prix près du plus haut swing des 90j |
| Étoile filante 4h | Longue mèche haute, petit corps, dans contexte haussier |
| Engulfing baissier 4h | Bougie rouge englobe la bougie verte précédente |
| Evening star 4h | 3 bougies : verte, petit corps, grande rouge passant sous mi-corps vert |

### Biais directionnel
Calculé par token : `bull_signals` (nb signaux haussiers) vs `bear_signals` (nb baissiers).
- `haussier` : bull > bear
- `baissier` : bear > bull
- `mixte` : bull == bear > 0
- `neutre` : aucun signal

## Indicateurs techniques — formules
- **RSI 14** : Wilder's smoothing classique
- **MACD** : EMA12 − EMA26, signal = EMA9(MACD), histogramme = MACD − signal
- **Volatilité réalisée 30j annualisée** : `std(log_returns_30j) × sqrt(365)`
- **Drawdown 90j** : `(min(close_90j) - max(close_90j_avant_min)) / max(close_90j_avant_min)`
- **Corrélation BTC** : Pearson sur log-returns journaliers, fenêtre 90 jours

## Versioning
| Version | Date | Changements |
|---|---|---|
| 1.0 | 2026-04-15 | Initial |
| 1.1 | 2026-04-18 | Ajout patterns enrichis : double fond/sommet, bull/bear flag, structure tendance, rebond support, test résistance, bougies 4h (marteau, shooting star, engulfing, morning/evening star), biais directionnel bull/bear par token |
| 1.2 | 2026-04-18 | Formule prédictive : ajout axe Signal directionnel 15%, Momentum 25%→30%, Solidité 30%→20%, Risque 25%→15%, Anti-scam inchangé 20% |
| 1.3 | 2026-04-18 | Système d'apprentissage adaptatif (08_learn.py) : mesure quotidienne du hit_rate par pattern sur J+7/14/30, mise à jour des poids dans pattern_weights.json |
| 1.4 | 2026-04-19 | Signal Marché Global Crypto vs EUR : score composite -10→+10 sur 6 indicateurs macro. Exclusion stablecoins. Corrections patterns. |
| 1.5 | 2026-04-19 | Système entièrement adaptatif : (1) pattern_weights.json — poids par hit_rate 14j ; (2) formula_weights.json — poids de la formule composite calibrés par corrélation de Pearson avec les vrais retours, blend défauts→appris proportionnel à n_données ; (3) explosion_profile.json — scoring prospectif basé sur distributions de fréquences réelles, bonus patterns pondérés par poids appris. |
