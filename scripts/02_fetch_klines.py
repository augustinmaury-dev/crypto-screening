"""Récupère les klines journalières (365j) et 4h (30j) pour les tokens donnés."""
from common import http_get, cache_put, cache_get, setup_logger
import sys, time
log = setup_logger("02_klines")

def fetch_klines(symbol: str, interval: str, limit: int):
    return http_get("https://api.binance.com/api/v3/klines",
                    {"symbol": symbol, "interval": interval, "limit": limit})

def fetch_for_symbols(symbols: list[str], force: bool = False):
    ok, ko = 0, 0
    for i, sym in enumerate(symbols, 1):
        try:
            cached_d = cache_get("binance", f"klines_1d_{sym}", max_age_hours=12) if not force else None
            cached_h = cache_get("binance", f"klines_4h_{sym}", max_age_hours=4) if not force else None
            if cached_d is None:
                data = fetch_klines(sym, "1d", 365)
                cache_put("binance", f"klines_1d_{sym}", data)
                time.sleep(0.05)  # ménage les rate limits Binance (1200/min)
            if cached_h is None:
                data = fetch_klines(sym, "4h", 180)  # 30 jours = 180 barres 4h
                cache_put("binance", f"klines_4h_{sym}", data)
                time.sleep(0.05)
            ok += 1
            if i % 25 == 0:
                log.info(f"  klines: {i}/{len(symbols)} ok={ok} ko={ko}")
        except Exception as e:
            log.warning(f"Klines fail {sym}: {e}")
            ko += 1
    log.info(f"Klines termin\u00e9 : ok={ok} ko={ko}")
    return ok, ko

if __name__ == "__main__":
    from common import cache_get
    universe = cache_get("binance", "universe", max_age_hours=24)
    if not universe:
        log.error("Pas d'univers en cache, lance 01_fetch_universe.py d'abord"); sys.exit(1)
    universe = universe["data"] if isinstance(universe, dict) and "data" in universe else universe
    syms = [u["symbol"] for u in universe]
    if len(sys.argv) > 1:
        syms = syms[:int(sys.argv[1])]
    fetch_for_symbols(syms)
