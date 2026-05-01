"""Récupère l'univers USDT Binance + ticker 24h."""
from common import http_get, cache_put, cache_get, setup_logger
log = setup_logger("01_universe")

def fetch():
    log.info("Fetch exchangeInfo...")
    info = http_get("https://data-api.binance.vision/api/v3/exchangeInfo")
    pairs = [s for s in info["symbols"]
             if s["quoteAsset"] == "USDT" and s["status"] == "TRADING"
             and not s["symbol"].endswith(("UPUSDT", "DOWNUSDT", "BULLUSDT", "BEARUSDT"))]
    log.info(f"{len(pairs)} paires USDT actives")

    log.info("Fetch ticker 24h...")
    tickers = http_get("https://data-api.binance.vision/api/v3/ticker/24hr")
    by_sym = {t["symbol"]: t for t in tickers}

    universe = []
    for s in pairs:
        sym = s["symbol"]; t = by_sym.get(sym, {})
        universe.append({
            "symbol": sym,
            "base": s["baseAsset"],
            "quote": s["quoteAsset"],
            "price": float(t.get("lastPrice", 0) or 0),
            "volume_24h_quote": float(t.get("quoteVolume", 0) or 0),  # en USDT
            "volume_24h_base": float(t.get("volume", 0) or 0),
            "change_pct_24h": float(t.get("priceChangePercent", 0) or 0),
            "high_24h": float(t.get("highPrice", 0) or 0),
            "low_24h": float(t.get("lowPrice", 0) or 0),
            "trade_count_24h": int(t.get("count", 0) or 0),
        })
    universe.sort(key=lambda x: x["volume_24h_quote"], reverse=True)
    cache_put("binance", "universe", universe)
    log.info(f"Sauvegardé {len(universe)} entrées univers (top vol: {universe[0]['symbol']} = {universe[0]['volume_24h_quote']:,.0f}$)")
    return universe

if __name__ == "__main__":
    fetch()
