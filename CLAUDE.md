# CLAUDE.md — Crypto Screening Project
> Fichier de contexte pour Claude (Cowork). Mis à jour le 09/05/2026.
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
06_score.py              → Score composite 4 axes (cf. Formule ci-dessous)
07_report.py             → report.md + diff vs veille
08_learn.py              → Mise à jour des poids via outcomes réels
09_explosion_screen.py   → Détection de tokens en pré-explosion
10_fetch_catalysts.py    → Catalyseurs externes (événements, listings, etc.)
11_fetch_defi.py         → TVL via DefiLlama
12_build_history.py      → Snapshots quotidiens pour analyse historique 30j
run_pipeline.py          → Orchestrateur principal
```

### Commandes principales
```bash
python run_pipeline.py --pilot 30    # test sur 30 tokens
python run_pipeline.py               # univers complet (~45-60 min)
python run_pipeline.py --skip-fetch  # recalcule scores depuis cache
```

---

## Formule de scoring v1.2 (source of truth → methodology.md)

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

## État actuel du projet (09/05/2026)

### ✅ Ce qui fonctionne
- Pipeline GitHub Actions tourne **quotidiennement** et commit ses résultats automatiquement
- Système de scoring multi-axes opérationnel
- Dashboard HTML avec historique 30j, TVL DefiLlama, tokenomics, watchlist, graphique de prix
- Système d'apprentissage des poids (formula_weights, pattern_weights) actif
- Détection de catalyseurs externes (script 10)
- Intégration TVL DefiLlama (script 11)

### 🔴 Problèmes connus (identifiés dans auto_review_20260501.md)
1. **`double_bottom_90d` sur-détecté** (~43% des tokens) — seuils à resserrer (`tol=0.02 → 0.015`, séparation min `10 → 15 jours`)
2. **Stablecoins dans le classement** — filtre `is_stablecoin()` présent mais parfois contourné selon la version du code
3. **Contradictions MACD** sur certains tokens (croisements bull+bear simultanés) — code corrigé mais anciens rapports affectés
4. **`outcomes.csv` absent** — le système d'apprentissage n'a pas encore de données de performance réelle pour s'auto-calibrer

### 🟡 Améliorations identifiées mais non implementées
- Resserrer les seuils `double_bottom_90d` (voir auto_review_20260501.md pour le code exact)
- Créer le système `outcomes.csv` pour mesurer la performance prédictive réelle des patterns
- Ajouter l'Inde comme univers secondaire (hors scope actuel)

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
