# CLAUDE.md — Crypto Screening Project
> Fichier de contexte pour Claude (Cowork). Mis à jour le 25/09/2026.
> En cas de résumé de session ou perte de contexte, lire ce fichier en priorité.

---

## Propriétaire
**Augustin Maury** — augustin.maury@gmail.com
Repo GitHub : https://github.com/augustinmaury-dev/crypto-screening
Dashboard live : https://augustinmaury-dev.github.io/crypto-screening/dashboard.html

---

## Philosophie du projet
Système de **screening crypto automatisé** sur l'**intégralité des paires USDT de Binance**.

**Objectif principal :** analyser chaque token disponible (projet, solidité, courbes de prix, indicateurs techniques, on-chain) pour produire un **classement des cryptos les plus prometteuses** sur les horizons suivants :
- **Court terme** (jours) : signaux techniques, momentum, catalyseurs imminents
- **Moyen terme** (semaines) : patterns de structure, breakouts, accumulation
- **Long terme** (mois) : fondamentaux, activité GitHub, TVL, adoption

**Objectif secondaire — détection des explosions :** identifier et apprendre les **patterns caractéristiques des tokens qui explosent** (pré-explosion) afin de pouvoir les reconnaître à l'avance sur de nouveaux tokens. Le système doit s'auto-améliorer à mesure qu'il accumule des données de performance réelle.

**Usage :** Augustin utilise ce classement pour débattre et itérer sur le projet avec Claude à tout moment — améliorer les formules, ajuster les poids, affiner la détection de patterns, challenger les résultats.

- Ce n'est **pas** un signal d'achat automatique — c'est un classement transparent pour examen et décision humaine
- Aucune clé API requise (endpoints publics uniquement)
- Pipeline quotidien via **GitHub Actions** qui commit automatiquement ses résultats dans `data/history/`

---

## Architecture — Pipeline en 12 étapes

```
01_fetch_universe.py     → Liste toutes les paires USDT actives sur Binance
02_fetch_klines.py       → Klines 1d × 365j + 4h × 30j
03_fetch_coingecko.py    → Top 1000 par market cap + détails (rate-limited 25/min)
04_fetch_project_info.py → Activité GitHub + détection red flags
05_compute_indicators.py → RSI, MACD, MA, vol, drawdown, corrélation BTC, patterns
06_score.py              → Sous-scores 5 axes + ancienne formule bull_prob_7d (gardée en bull_prob_7d_legacy)
06b_ml_score.py          → SCORE PRINCIPAL : modèle appris + régime de marché / altseason (depuis le 25/09/2026)
07_report.py             → report.md + diff vs veille
08_learn.py              → Mise à jour des poids via outcomes réels
09_explosion_screen.py   → Détection de tokens en pré-explosion
10_fetch_catalysts.py    → Catalyseurs externes (événements, listings, etc.)
11_fetch_defi.py         → TVL via DefiLlama
12_build_history.py      → Snapshots quotidiens pour analyse historique 30j
13_memory.py             → Journal project_memory.md, suivi des prédictions (top 20/jour), calibration
run_pipeline.py          → Orchestrateur principal
```

### Commandes principales
```bash
python run_pipeline.py --pilot 30    # test sur 30 tokens
python run_pipeline.py               # univers complet (~45-60 min)
python run_pipeline.py --skip-fetch  # recalcule scores depuis cache
```

---

## Score principal depuis le 25/09/2026 — modèle appris (06b_ml_score.py)

- `score` = `outperf_prob_7d` = probabilité (%) qu'un token fasse **mieux que la médiane du marché sur 7 jours**.
  `bull_prob_7d` contient la même valeur (compatibilité dashboard) ; l'ancienne formule est dans `bull_prob_7d_legacy`.
- Modèle : gradient boosting (scikit-learn) sur ~40 features du pipeline, normalisées en rang par jour.
  **Réentraîné à chaque run** sur tout l'historique `data/history/` dont le résultat à 7 j est connu.
- Probabilités **calibrées** (ramenées vers 50 % selon les erreurs des 5 dernières semaines, facteur k dans model_report.json).
- Garde-fou : si le top 20 bat la médiane < 45 % sur les 5 dernières semaines → règle simple (grosses caps peu volatiles).
- Recherche (walk-forward avril→sept. 2026) : top 20 qui bat la médiane à 7 j — ancienne formule 41 %, modèle 64 %,
  règle naïve « grosses caps peu volatiles » 61 %. 7 j = meilleur horizon testé (3/7/14/30). Paramètre `HORIZON`.
- Point faible connu : chute à ~35-40 % pendant les changements de régime (mi-août 2026), puis remontée.

### Altseason (régime de marché)
- Indice = % des 100 plus grosses altcoins (hors BTC/stables) qui ont fait mieux que BTC sur 30 j et 90 j.
  90 j ≥ 75 → Altseason ; ≤ 25 → Saison Bitcoin ; 30 j ≥ 75 → « Altseason en formation ». → `data/computed/market_regime.json`
- En régime alt (indice 30 j ≥ 60) : la prime aux grosses caps s'efface et le momentum redevient payant.
  → tant que < 30 jours d'altseason mesurés : mélange 25 % momentum (p_ma50, ret 7 j, RSI) dans le classement ;
  → dès 30 jours mesurés : modèle dédié entraîné uniquement sur les jours d'altseason (automatique).
- Fin septembre 2026 : indice 30 j ≈ 79 (altseason en formation), seulement 7 jours alt mesurés.

### Suivi des prédictions (13_memory.py)
- Une prédiction = un des 20 premiers du classement du jour ; jugée à 7 j et 14 j vs médiane du marché.
- Backfill automatique depuis data/history/ ; comparaison « Ancienne formule » vs « Modèle appris » (quintiles, corrélation de rang).
- Bug corrigé le 25/09/2026 : les prédictions en attente étaient limitées à 300 → jamais mesurées.

## Ancienne formule de scoring v1.2 (conservée pour les sous-scores — source of truth → methodology.md)

```
SCORE = 0.20 × Solidité + 0.30 × Momentum + 0.15 × Signal + 0.15 × Risque/Qualité + 0.20 × AntiScam
```

**Tiers :**
- **Établi** : market cap rank ≤ 100
- **Mid** : rank 101–500
- **Speculative** : rank > 500 ou hors CoinGecko

**Filtre SUSPECT** : exclusion automatique si ≥ 2 des 3 conditions :
1. Équipe non identifiable
2. Promesses de rendement (regex)
3. Âge < 180 jours

---

## Fichiers clés

| Fichier | Rôle |
|---|---|
| `data/learning/model_report.json` | Modèle du jour : auto-évaluation, calibration, facteurs dominants, régime |
| `data/learning/calibration.json` | Pouvoir de classement mesuré (ancienne formule vs modèle) |
| `data/computed/market_regime.json` | Indice altseason 30/90 j, perf BTC, largeur du marché (historique 120 j) |
| `requirements.txt` | numpy, pandas, scikit-learn (installés par GitHub Actions) |
| `methodology.md` | Source de vérité de la formule (versionnée) |
| `report.md` | Dernier rapport généré par le pipeline |
| `dashboard.html` | Explorateur interactif (charge le CSV) |
| `data/computed/scores_YYYYMMDD.csv` | Scores complets du jour |
| `data/history/` | Snapshots quotidiens pour diffs et historique 30j |
| `data/learning/formula_weights.json` | Poids appris des 5 axes |
| `data/learning/pattern_weights.json` | Poids appris par pattern technique |
| `data/raw/` | JSON bruts Binance/CoinGecko (purge auto > 30j) |
| `auto_review_YYYYMMDD.md` | Auto-analyse générée périodiquement |

---

## État actuel du projet (14/05/2026)

### ✅ Ce qui fonctionne
- Pipeline GitHub Actions tourne **quotidiennement** et commit ses résultats automatiquement
- Système de scoring multi-axes opérationnel
- Dashboard HTML avec historique 30j, TVL DefiLlama, tokenomics, watchlist, graphique de prix
- Système d'apprentissage des poids (formula_weights, pattern_weights) actif — **outcomes.csv opérationnel depuis le 11/05 (2886 observations)**
- Détection de catalyseurs externes (script 10)
- Intégration TVL DefiLlama (script 11)

### ✅ Corrections appliquées le 14/05/2026 (issues auto_review_20260511.md)
- **P1** — `06_score.py` : `DEAD_WEIGHT_THRESHOLD = 0.15` dans `score_signal()` — neutralise `breakout_30d`, `support_bounce`, `rsi_bullish_divergence` (contra-indicateurs à poids ≤ 0.1)
- **P2** — `05_compute_indicators.py` : `pat_double_bottom()` — reprise 10%→15% + filtre MA20 de confirmation (réduction ~29%→~15% des tokens touchés)
- **P3** — `06_score.py` : `is_stablecoin()` — ajout EURUSDT, EURIUSDT, AEURUSDT, BFUSDUSDT, USD1USDT, UUSDT + seuils vol/dd relâchés (0.03→0.08, 0.02→0.05)
- **P4** — `pattern_weights.json` : `hammer_4h` et `bearish_engulfing_4h` → poids 0.1 (0% et 25% hit rate sur 4 obs chacun)

### 🟡 Améliorations identifiées mais non implementées
- Multiplicateur macro global : utiliser le signal marché (-2/+10) pour réduire l'influence des patterns haussiers en régime baissier
- Ajouter l'Inde comme univers secondaire (hors scope actuel)

### 🟡 Pistes ouvertes (25/09/2026)
- Actions tokenisées (MSTRB, NVDAB…) et tokens de staking (BNSOL) remontent dans le top : les exclure de l'univers ?
- Stablecoins qui passent le filtre (TUSD, BFUSD, USTC vus en tête avant le modèle)
- report.md n'est plus régénéré depuis le 26/06/2026 (à investiguer)
- Git absent sur le PC Windows → push via l'interface web GitHub en attendant (winget install Git.Git)

### 🔴 Problèmes connus résiduels
- Contradictions MACD sur certains tokens (croisements bull+bear simultanés) — anciens rapports affectés

---

## GitHub Actions

Le workflow `.github/workflows/pipeline.yml` :
- Tourne automatiquement chaque jour
- Commit les résultats (`scores_YYYYMMDD.csv`, `report.md`) dans le repo
- **Important** : GitHub Actions peut avoir des commits d'avance sur le local — toujours faire `git pull --rebase` avant de push

### Procédure de push depuis Windows
```bash
cd "C:\Users\PC\Dropbox\Dossier familial\Augustin\Claude\Claude cowork\crypto-screening"
git pull origin main --rebase
git push origin main
```
⚠️ Le sandbox Linux de Cowork peut corrompre l'index git si les deux environnements accèdent simultanément au repo. Toujours push depuis le terminal Windows si le sandbox pose problème.

---

## Domaines réseau requis (Settings → Capabilities)
- `api.binance.com` / `data-api.binance.vision`
- `api.coingecko.com`
- `api.github.com`
- `api.llama.fi` (DefiLlama)

---

## Contexte de la collaboration
- Cette conversation Cowork est **dédiée au projet crypto**
- Les autres sujets (portfolio boursier, analyses sectorielles) sont traités dans d'autres conversations
- Augustin a aussi un portfolio d'actions Tech/IA/Semis, un PEA (MSCI World, DAX, Grèce, Japon TOPIX), des cryptos, et de l'immobilier via LaPremiereBrique — mais cela ne concerne pas cette conversation
