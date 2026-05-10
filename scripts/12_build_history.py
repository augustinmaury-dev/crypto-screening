"""Compile l historique des scores sur 30 jours.
Produit data/computed/score_history.json.
"""
from __future__ import annotations
import csv, json
from pathlib import Path
from datetime import date
from common import COMPUTED, HISTORY, setup_logger

log = setup_logger("12_history")
HISTORY_DIR = HISTORY
OUT_FILE = COMPUTED / "score_history.json"
DAYS = 30


def _available_dates():
    if not HISTORY_DIR.exists():
        log.warning(f"Dossier history introuvable : {HISTORY_DIR}")
        return []
    dates = []
    for f in HISTORY_DIR.glob("scores_*.csv"):
        d = f.stem.replace("scores_", "")
        try:
            date.fromisoformat(d)
            dates.append(d)
            continue
        except ValueError:
            pass
        try:
            if len(d) == 8:
                date(int(d[0:4]), int(d[4:6]), int(d[6:8]))
                dates.append(d)
        except (ValueError, IndexError):
            pass
    result = sorted(dates)[-DAYS:]
    log.info(f"Dates disponibles : {len(result)}")
    return result


def _read_day(csv_path):
    result = {}
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
                result[sym] = {"score": score, "rank": i, "price": round(price, 6) if price else None}
    except Exception as e:
        log.warning(f"Lecture {csv_path.name} echouee : {e}")
    return result


def run():
    log.info("=== Build score history ===")
    log.info(f"HISTORY_DIR = {HISTORY_DIR}")
    dates = _available_dates()
    if not dates:
        log.warning("Aucun fichier historique trouve")
        empty = {"dates": [], "tokens": {}}
        OUT_FILE.write_text(json.dumps(empty, ensure_ascii=False), encoding="utf-8")
        return empty
    log.info(f"Periode : {dates[0]} -> {dates[-1]} ({len(dates)} jours)")
    day_data = {}
    all_symbols = set()
    for d in dates:
        path = HISTORY_DIR / f"scores_{d}.csv"
        data = _read_day(path)
        day_data[d] = data
        all_symbols.update(data.keys())
    tokens = {}
    for sym in sorted(all_symbols):
        scores, ranks, prices = [], [], []
        for d in dates:
            row = day_data.get(d, {}).get(sym)
            scores.append(row["score"] if row else None)
            ranks.append(row["rank"] if row else None)
            prices.append(row["price"] if row else None)
        if sum(1 for s in scores if s is not None) >= 2:
            tokens[sym] = {"scores": scores, "ranks": ranks, "prices": prices}
    result = {"dates": dates, "tokens": tokens}
    OUT_FILE.write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
    log.info(f"score_history.json ecrit — {len(dates)} dates, {len(tokens)} tokens")
    return result


if __name__ == "__main__":
    run()
