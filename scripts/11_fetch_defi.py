"""Récupère les données TVL (Total Value Locked) depuis DefiLlama.

Sources :
  - DefiLlama /protocols — liste tous les protocoles DeFi avec TVL actuel et historique
  - DefiLlama /tvl/{protocol} — TVL détaillé par protocole

Sortie : data/raw/defillama/tvl_map.json  (cache 24h)
         data/computed/tvl.json           (index par symbol Binance)

Docs : https://defillama.com/docs/api (gratuit, pas de clé requise)
"""
from __future__ import annotations
from common import http_get, cache_get, cache_put, COMPUTED, setup_logger
import json
from pathlib import Path

log = setup_logger("11_defi")

DEFILLAMA_PROTOCOLS = "https://api.llama.fi/protocols"

# Mapping manuel symbol Binance → slug DefiLlama pour les cas ambigus
MANUAL_MAP: dict[str, str] = {
    "AAVEUSDT":   "aave",
    "UNIUSDT":    "uniswap",
    "CRVUSDT":    "curve-dex",
    "MKRUSDT":    "makerdao",
    "COMPUSDT":   "compound-finance",
    "SNXUSDT":    "synthetix",
    "YFIUSDT":    "yearn-finance",
    "SUSHIUSDT":  "sushiswap",
    "1INCHUSDT":  "1inch-network",
    "LDOUSDT":    "lido",
    "RPLUSDT":    "rocket-pool",
    "STETHUSDT":  "lido",
    "WBTCUSDT":   "wbtc",
    "FRAXUSDT":   "frax",
    "GMXUSDT":    "gmx",
    "DYDXUSDT":   "dydx",
    "PERPUSDT":   "perpetual-protocol",
    "BALUSDT":    "balancer",
    "CVXUSDT":    "convex-finance",
    "ANKRUSDT":   "ankr",
    "STGUSDT":    "stargate-finance",
    "PENUSDT":    "pendle",
    "PENDLEUSDT": "pendle",
    "EIGUSDT":    "eigenlayer",
    "ENAAUSDT":   "ethena",
    "SUSDEUSDT":  "ethena",
    "EZETHUSDT":  "renzo",
    "RSETHUSDT":  "kelp-dao",
    "WEETHUSDT":  "ether.fi",
    "ETHFIUSDT":  "ether.fi",
}


def fetch_protocols() -> list:
    """Télécharge la liste complète des protocoles DefiLlama."""
    cached = cache_get("defillama", "protocols", max_age_hours=24)
    if cached:
        data = cached.get("data", cached) if isinstance(cached, dict) else cached
        if data:
            log.info(f"Protocols depuis cache : {len(data)} protocoles")
            return data

    log.info("Fetch DefiLlama protocols...")
    data = http_get(DEFILLAMA_PROTOCOLS)
    if isinstance(data, list) and data:
        cache_put("defillama", "protocols", data)
        log.info(f"DefiLlama : {len(data)} protocoles chargés")
        return data
    return []


def build_tvl_map(protocols: list, symbols: list[str]) -> dict:
    """
    Construit un index {binance_symbol: {tvl, tvl_7d_change, category, chains, slug}}
    pour tous les symboles Binance reconnus.
    """
    if not protocols:
        return {}

    # Index par slug et par ticker (lowercase)
    by_slug: dict[str, dict] = {}
    by_ticker: dict[str, list[dict]] = {}

    for p in protocols:
        slug = (p.get("slug") or p.get("name", "")).lower().replace(" ", "-")
        ticker = (p.get("symbol") or "").upper()
        by_slug[slug] = p
        if ticker:
            by_ticker.setdefault(ticker, []).append(p)

    result: dict[str, dict] = {}

    for sym in symbols:
        base = sym.replace("USDT", "").replace("BUSD", "").replace("BTC", "")
        proto = None

        # 1. Mapping manuel
        if sym in MANUAL_MAP:
            proto = by_slug.get(MANUAL_MAP[sym])

        # 2. Par ticker exact
        if not proto and base in by_ticker:
            candidates = by_ticker[base]
            # Prendre celui avec le plus gros TVL
            proto = max(candidates, key=lambda x: x.get("tvl") or 0)

        if not proto:
            continue

        tvl = proto.get("tvl") or 0
        if tvl < 1_000_000:  # ignore < $1M TVL
            continue

        # Variation TVL sur 1j et 7j
        change_1d = proto.get("change_1d") or proto.get("change1d") or 0
        change_7d = proto.get("change_7d") or proto.get("change7d") or 0

        result[sym] = {
            "tvl":          round(tvl),
            "tvl_fmt":      _fmt_tvl(tvl),
            "change_1d":    round(change_1d, 2) if change_1d else None,
            "change_7d":    round(change_7d, 2) if change_7d else None,
            "category":     proto.get("category", ""),
            "chains":       proto.get("chains", [])[:5],
            "slug":         proto.get("slug") or proto.get("name", ""),
            "name":         proto.get("name", ""),
        }

    log.info(f"TVL map : {len(result)}/{len(symbols)} tokens mappés")
    return result


def _fmt_tvl(v: float) -> str:
    """Formate la TVL en $1.2B / $450M / $12M."""
    if v >= 1e9:
        return f"${v/1e9:.1f}B"
    if v >= 1e6:
        return f"${v/1e6:.0f}M"
    return f"${v/1e3:.0f}K"


def run(symbols: list[str] | None = None) -> dict:
    """Point d'entrée principal."""
    log.info("=== Fetch DefiLlama TVL ===")

    protocols = fetch_protocols()
    if not protocols:
        log.warning("Aucun protocole DefiLlama — TVL ignoré")
        return {}

    # Si pas de liste fournie, utiliser les symboles du cache univers
    if not symbols:
        from common import cache_get as _cg
        uni = _cg("binance", "universe", 24 * 7)
        uni = uni.get("data", uni) if isinstance(uni, dict) else uni
        symbols = [u["symbol"] for u in (uni or [])]

    tvl_map = build_tvl_map(protocols, symbols)

    out = COMPUTED / "tvl.json"
    import json as _json
    out.write_text(_json.dumps(tvl_map, ensure_ascii=False, indent=2), encoding="utf-8")
    log.info(f"tvl.json écrit — {len(tvl_map)} tokens avec TVL")
    return tvl_map


if __name__ == "__main__":
    run()
