# Crypto Screening — USDT Binance

Système d'analyse multidimensionnel des paires USDT de Binance.
**Pas un signal d'achat. Un classement transparent à examiner.**

## Pipeline
```
01_fetch_universe   → liste USDT + ticker 24h
02_fetch_klines     → klines 1d × 365 + 4h × 30
03_fetch_coingecko  → markets top 1000 + détails (rate-limited 25/min)
04_fetch_project    → GitHub activity + détection red flags
05_compute          → RSI, MACD, MA, vol, drawdown, corrélation BTC
06_score            → 4 axes pondérés (cf methodology.md)
07_report           → report.md + diff vs veille
```

## Lancer

```bash
cd scripts
python run_pipeline.py --pilot 30   # validation
python run_pipeline.py              # univers complet (~45-60 min première fois)
python run_pipeline.py --skip-fetch # recalcule scores depuis cache
```

## Sorties
- `data/computed/scores_YYYYMMDD.csv` — tableau complet
- `report.md` — synthèse markdown
- `dashboard.html` — explorateur local (charge le CSV)
- `methodology.md` — formule de scoring (versionnée)
- `data/raw/` — JSON bruts (purge auto > 30j)
- `data/history/` — snapshots quotidiens des scores pour les diffs

## Pré-requis réseau
Domaines à autoriser dans Settings → Capabilities :
- `api.binance.com`
- `api.coingecko.com`
- `api.github.com`

## Aucune clé API requise
Endpoints publics uniquement.
