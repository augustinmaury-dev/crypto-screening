"""Utilitaires partagés : config, logging, HTTP avec rate limit, paths."""
from __future__ import annotations
import json, os, time, logging, urllib.request, urllib.error, urllib.parse
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RAW = DATA / "raw"
COMPUTED = DATA / "computed"
HISTORY = DATA / "history"
LOGS = ROOT / "logs"
for p in (RAW / "binance", RAW / "coingecko", RAW / "project", COMPUTED, HISTORY, LOGS):
    p.mkdir(parents=True, exist_ok=True)

TODAY = datetime.now().strftime("%Y%m%d")

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s", "%H:%M:%S")
    # StreamHandler avec encodage UTF-8 forcé pour Windows
    import sys
    sh = logging.StreamHandler(stream=open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1, closefd=False))
    sh.setFormatter(fmt); logger.addHandler(sh)
    fh = logging.FileHandler(LOGS / f"{name}_{TODAY}.log", encoding="utf-8"); fh.setFormatter(fmt); logger.addHandler(fh)
    return logger

class RateLimiter:
    def __init__(self, calls_per_minute: int):
        self.interval = 60.0 / calls_per_minute
        self.last = 0.0
    def wait(self):
        delta = time.time() - self.last
        if delta < self.interval:
            time.sleep(self.interval - delta)
        self.last = time.time()

def http_get(url: str, params: dict | None = None, headers: dict | None = None,
             timeout: int = 20, retries: int = 3, backoff: float = 2.0) -> dict | list:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "crypto-screen/1.0", **(headers or {})})
    last_err = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (429, 502, 503, 504):
                time.sleep(backoff ** (attempt + 1))
                continue
            raise
        except Exception as e:
            last_err = e
            time.sleep(backoff ** (attempt + 1))
    raise RuntimeError(f"http_get failed for {url}: {last_err}")

def save_json(path: Path, payload, with_meta: bool = True):
    path.parent.mkdir(parents=True, exist_ok=True)
    if with_meta and isinstance(payload, (dict, list)):
        wrapped = {"_fetched_at": datetime.now(timezone.utc).isoformat(), "data": payload}
    else:
        wrapped = payload
    path.write_text(json.dumps(wrapped, ensure_ascii=False), encoding="utf-8")

def load_json(path: Path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None

def cache_get(category: str, name: str, max_age_hours: float = 24.0):
    """Lit le cache JSON le plus récent pour ce nom dans cette catégorie."""
    folder = RAW / category
    folder.mkdir(parents=True, exist_ok=True)
    candidates = sorted(folder.glob(f"{name}_*.json"), reverse=True)
    if not candidates:
        return None
    latest = candidates[0]
    age = (time.time() - latest.stat().st_mtime) / 3600
    if age > max_age_hours:
        return None
    return load_json(latest)

def cache_put(category: str, name: str, payload):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_json(RAW / category / f"{name}_{ts}.json", payload)

def purge_old_raw(days: int = 30):
    """Supprime les fichiers raw plus vieux que N jours."""
    cutoff = time.time() - days * 86400
    removed = 0
    for f in RAW.rglob("*.json"):
        if f.stat().st_mtime < cutoff:
            f.unlink(); removed += 1
    return removed
