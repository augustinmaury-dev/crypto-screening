"""Compile l'historique des scores sur 30 jours.

Lit tous les fichiers data/history/scores_YYYY-MM-DD.csv
et produit data/computed/score_history.json :
{
  "dates": ["2024-01-01", ...],   // 30 derniers jours disponibles
  "tokens": {
    "BTCUSDT": {
      "scores":  [72, 75, 71, ...],   // score par date (None si absent)
      "ranks":   [1, 1, 2, ...],
      "prices":  [42000, 43000, ...]  // prix de clôture si dispo
    },
    ...
  }
}
"""
from __future__ import annotations
import csv, json, os
from pathlib import Path
from datetime import date, timedelta
from common import COMPUTED, setup_logger

log = setup_logger("12_history")

HISTORY_DIR = Path(__file__).parent.parent / "data" / "history"
OUT_FILE    = COMPUTED / "score_history.json"
DAYS        = 30


def _available_dates() -> list[str]:
    """Retourne les dates disponibles dans data/history/ (tri croissant)."""
    if not HISTORY_DIR.exists():
        return []
    dates = []
    for f in HISTORY_DIR.glob("scores_*.csv"):
        stem = f.stem  # "scores_2024-01-15"
        d = stem.replace("scores_", "")
        try:
            date.fromisoformat(d)
            dates.append(d)
        except ValueError:
            pass
    return sorted(dates)[-DAYS:]


def _read_day(csv_path: Path) -> dict[str, dict]:
    """Lit un CSV de scores et retourne {symbol: {score, rank, price}}."""
    result: dict[str, dict] = {}
    try:
        with open(csv_path, encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, 1):
                sym = row.get("symbol", "")
                if not sym:
                    continue
                try:
                    score = int(float(row.get("score", 0)))
                except (ValueError, TypeError):
                    score = 0
                try:
                    price = float(row.get("price", 0) or 0)
                except (ValueError, TypeError):
                    price = 0.0
                result[sym] = {
                    "score": score,
                    "rank":  i,
                    "price": round(price, 6) if price else None,
                }
    except Exception as e:
        log.warning(f"Lecture {csv_path.name} échouée : {e}")
    return result


def run() -> dict:
    log.info("=== Build score history ===")

    dates = _available_dates()
    if not dates:
        log.warning("Aucun fichier historique trouvé dans data/history/")
        # Créer un fichier vide valide quand même
        empty = {"dates": [], "tokens": {}}
        OUT_FILE.write_text(json.dumps(empty, ensure_ascii=False), encoding="utf-8")
        return empty

    log.info(f"Dates disponibles : {len(dates)} ({dates[0]} → {dates[-1]})")

    # Collecte toutes les données par date
    day_data: dict[str, dict[str, dict]] = {}
    all_symbols: set[str] = set()
    for d in dates:
        path = HISTORY_DIR / f"scores_{d}.csv"
        data = _read_day(path)
        day_data[d] = data
        all_symbols.update(data.keys())

    # Construit la structure par token
    tokens: dict[str, dict] = {}
    for sym in sorted(all_symbols):
        scores, ranks, prices = [], [], []
        for d in dates:
            row = day_data.get(d, {}).get(sym)
            scores.append(row["score"] if row else None)
            ranks.append(row["rank"]  if row else None)
            prices.append(row["price"] if row else None)

        # Inclure seulement si au moins 2 points de données
        non_null = sum(1 for s in scores if s is not None)
        if non_null >= 2:
            tokens[sym] = {
                "scores": scores,
                "ranks":  ranks,
                "prices": prices,
            }

    result = {"dates": dates, "tokens": tokens}
    OUT_FILE.write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
    log.info(f"score_history.json ecrit — {len(dates)} dates, {len(tokens)} tokens")
    return result


if __name__ == "__main__":
    run()
