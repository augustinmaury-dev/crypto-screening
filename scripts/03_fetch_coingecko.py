"""CoinGecko : markets top 1000 + détail par token."""
from common import http_get, cache_put, cache_get, setup_logger, RateLimiter
import sys, time
log = setup_logger("03_coingecko")
rl = RateLimiter(calls_per_minute=25)  # marge sous les 30/min free tier

CG = "https://api.coingecko.com/api/v3"

def fetch_markets_top1000():
    # Vérifie cache complet d'abord
    cached = cache_get("coingecko", "markets_top1000", max_age_hours=12)
    if cached:
        data = cached["data"] if isinstance(cached, dict) and "data" in cached else cached
        if len(data) >= 500:
            log.info(f"Cache markets valide ({len(data)} coins)")
            return data

    log.info("Fetch CoinGecko markets top 1000 (4 pages)...")
    all_rows = []
    for page in range(1, 5):
        try:
            rl.wait()
            rows = http_get(f"{CG}/coins/markets",
                            {"vs_currency": "usd", "order": "market_cap_desc",
                             "per_page": 250, "page": page, "sparkline": "false"})
            if not rows:
                log.warning(f"  page {page}: réponse vide, arrêt")
                break
            log.info(f"  page {page}: {len(rows)} coins")
            all_rows.extend(rows)
            # Sauvegarde incrémentale après chaque page
            cache_put("coingecko", "markets_top1000", all_rows)
        except Exception as e:
            log.warning(f"  page {page} échouée : {e} — on continue avec {len(all_rows)} coins déjà récupérés")
            break
    log.info(f"Total markets récupérés : {len(all_rows)}")
    return all_rows

def fetch_detail(coin_id: str):
    cached = cache_get("coingecko", f"detail_{coin_id}", max_age_hours=24*7)
    if cached:
        return cached["data"] if isinstance(cached, dict) and "data" in cached else cached
    rl.wait()
    data = http_get(f"{CG}/coins/{coin_id}",
                    {"localization": "false", "tickers": "false", "market_data": "false",
                     "community_data": "false", "developer_data": "true", "sparkline": "false"})
    cache_put("coingecko", f"detail_{coin_id}", data)
    return data

def map_binance_to_cg(universe, markets):
    """Heuristique : match par symbol (uppercase). Conflits → garde le plus haut market cap rank."""
    by_sym = {}
    for m in markets:
        s = (m.get("symbol") or "").upper()
        if not s: continue
        if s not in by_sym or (by_sym[s].get("market_cap_rank") or 9999) > (m.get("market_cap_rank") or 9999):
            by_sym[s] = m
    mapping = {}
    for u in universe:
        m = by_sym.get(u["base"])
        mapping[u["symbol"]] = m
    matched = sum(1 for v in mapping.values() if v)
    log.info(f"Mapping Binance->CG : {matched}/{len(universe)} matches")
    return mapping

if __name__ == "__main__":
    universe_cache = cache_get("binance", "universe", max_age_hours=24)
    universe = universe_cache["data"] if isinstance(universe_cache, dict) and "data" in universe_cache else universe_cache
    if not universe:
        log.error("Pas d'univers"); sys.exit(1)
    markets = fetch_markets_top1000()
    mapping = map_binance_to_cg(universe, markets)
    cache_put("coingecko", "binance_to_cg_map", {u["symbol"]: (m or {}).get("id") for u, m in zip(universe, [mapping[u['symbol']] for u in universe])})

    # Limit pour pilote
    n = int(sys.argv[1]) if len(sys.argv) > 1 else len(universe)
    targets = [(u["symbol"], (mapping[u["symbol"]] or {}).get("id")) for u in universe[:n]]
    targets = [(s, cid) for s, cid in targets if cid]
    log.info(f"D\u00e9tails CoinGecko \u00e0 fetch : {len(targets)} (cache 7j)")
    for i, (sym, cid) in enumerate(targets, 1):
        try:
            fetch_detail(cid)
            if i % 10 == 0:
                log.info(f"  detail: {i}/{len(targets)}")
        except Exception as e:
            log.warning(f"Detail fail {sym}/{cid}: {e}")
