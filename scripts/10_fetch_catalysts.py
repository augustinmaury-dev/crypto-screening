"""Collecte de catalyseurs externes — enrichit l'analyse avec des signaux non-techniques.

Sources :
  1. Fear & Greed index (alternative.me) — sentiment global du marché crypto
  2. CoinGecko Trending — tokens les plus recherchés en ce moment
  3. Détection de spikes volume — tokens avec volume anormalement élevé vs médiane
  4. Détection de spikes GitHub — projets avec activité dev récente anormale
  5. CoinMarketCal (optionnel) — événements à venir (listing, mainnet, burn…)
     → Nécessite une clé gratuite : https://coinmarketcal.com/en/developer

Sortie : data/computed/catalysts.json
"""
from __future__ import annotations
from common import http_get, cache_get, cache_put, COMPUTED, ROOT, TODAY, setup_logger
import json, os
from pathlib import Path
from datetime import datetime, timezone, timedelta

log = setup_logger("10_catalysts")

# ── Clé CoinMarketCal (optionnelle) ──────────────────────────────────────────
# Pour l'activer : créer scripts/config.json avec {"coinmarketcal_key": "VOTRE_CLE"}
def _load_config() -> dict:
    cfg_path = Path(__file__).parent / "config.json"
    if cfg_path.exists():
        try:
            return json.loads(cfg_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


# ── 1. Fear & Greed Index ─────────────────────────────────────────────────────
def fetch_fear_greed() -> dict:
    """Retourne le Fear & Greed index actuel (0 = peur extrême, 100 = avidité extrême)."""
    try:
        data = http_get("https://api.alternative.me/fng/", params={"limit": 7})
        entries = data.get("data", [])
        if not entries:
            return {}
        current = entries[0]
        value = int(current.get("value", 50))
        classification = current.get("value_classification", "Neutral")
        # Historique 7 jours
        history = [{"date": e.get("timestamp"), "value": int(e.get("value", 50)),
                    "label": e.get("value_classification", "")} for e in entries]
        result = {
            "value": value,
            "classification": classification,
            "classification_fr": _fng_fr(value),
            "history_7d": history,
            "trend": _fng_trend(history),
        }
        log.info(f"Fear & Greed : {value} ({classification})")
        return result
    except Exception as e:
        log.warning(f"Fear & Greed fetch échoué : {e}")
        return {}

def _fng_fr(v: int) -> str:
    if v <= 25: return "Peur extrême"
    if v <= 40: return "Peur"
    if v <= 60: return "Neutre"
    if v <= 75: return "Avidité"
    return "Avidité extrême"

def _fng_trend(history: list) -> str:
    """Calcule la tendance sur 7 jours : montant / descendant / stable."""
    if len(history) < 2: return "stable"
    delta = history[0]["value"] - history[-1]["value"]
    if delta >= 10: return "montant"
    if delta <= -10: return "descendant"
    return "stable"


# ── 2. CoinGecko Trending ─────────────────────────────────────────────────────
def fetch_trending() -> list:
    """Retourne les 7 tokens les plus tendance sur CoinGecko."""
    try:
        data = http_get("https://api.coingecko.com/api/v3/search/trending")
        coins = data.get("coins", [])
        result = []
        for c in coins:
            item = c.get("item", {})
            result.append({
                "id":     item.get("id"),
                "symbol": item.get("symbol", "").upper(),
                "name":   item.get("name"),
                "rank":   item.get("market_cap_rank"),
                "score":  item.get("score", 0),
            })
        log.info(f"CoinGecko Trending : {[r['symbol'] for r in result]}")
        return result
    except Exception as e:
        log.warning(f"CoinGecko Trending fetch échoué : {e}")
        return []


# ── 3. Spikes de volume ───────────────────────────────────────────────────────
def detect_volume_spikes(threshold: float = 3.0) -> list:
    """Détecte les tokens avec un volume 3× supérieur à leur médiane 90j."""
    try:
        ind_cache = cache_get("binance", "indicators", 24 * 7)
        indicators = ind_cache.get("data", ind_cache) if isinstance(ind_cache, dict) else ind_cache
        if not indicators:
            return []
        spikes = []
        for ind in indicators:
            ratio = ind.get("vol_ratio_vs_med90")
            if ratio and ratio >= threshold:
                spikes.append({
                    "symbol":    ind["symbol"],
                    "vol_ratio": round(ratio, 2),
                    "rsi":       round(ind.get("rsi_14") or 0, 1),
                    "bias":      ind.get("bias", "neutre"),
                })
        spikes.sort(key=lambda x: -x["vol_ratio"])
        log.info(f"Volume spikes (≥{threshold}×) : {len(spikes)} tokens")
        return spikes[:20]
    except Exception as e:
        log.warning(f"Volume spike detection échoué : {e}")
        return []


# ── 4. Spikes GitHub ──────────────────────────────────────────────────────────
def detect_github_spikes(min_commits: int = 20, ratio_threshold: float = 2.0) -> list:
    """Détecte les projets avec une activité GitHub anormalement élevée."""
    try:
        uni_cache = cache_get("binance", "universe", 24 * 7)
        universe = uni_cache.get("data", uni_cache) if isinstance(uni_cache, dict) else uni_cache
        if not universe:
            return []

        spikes = []
        for u in universe:
            sym = u.get("symbol", "")
            enrich_cache = cache_get("project", f"enrich_{sym}", 24 * 7)
            enrich = enrich_cache.get("data", enrich_cache) if isinstance(enrich_cache, dict) else enrich_cache
            if not enrich:
                continue
            gh = enrich.get("github") or {}
            commits_30d = gh.get("commits_30d") or 0
            contrib = gh.get("active_contributors_90d") or 0
            if commits_30d >= min_commits and contrib >= 3:
                spikes.append({
                    "symbol":      sym,
                    "commits_30d": commits_30d,
                    "contributors": contrib,
                    "last_release_age": gh.get("last_release_age_days"),
                })
        spikes.sort(key=lambda x: -x["commits_30d"])
        log.info(f"GitHub spikes (≥{min_commits} commits) : {len(spikes)} projets")
        return spikes[:15]
    except Exception as e:
        log.warning(f"GitHub spike detection échoué : {e}")
        return []


# ── 5. CoinMarketCal (optionnel) ──────────────────────────────────────────────
def fetch_coinmarketcal(api_key: str) -> list:
    """Récupère les événements crypto des 30 prochains jours."""
    try:
        now = datetime.now(timezone.utc)
        date_from = now.strftime("%Y-%m-%d")
        date_to   = (now + timedelta(days=30)).strftime("%Y-%m-%d")
        data = http_get(
            "https://developers.coinmarketcal.com/v1/events",
            params={
                "dateRangeStart": date_from,
                "dateRangeEnd":   date_to,
                "sortBy":         "hot_score",
                "page":           1,
                "max":            50,
            },
            headers={"x-api-key": api_key, "Accept-Encoding": "deflate, gzip",
                     "Accept": "application/json"},
        )
        events = data.get("body", [])
        result = []
        for ev in events:
            coins = ev.get("coins", [])
            for coin in coins:
                result.append({
                    "symbol":      coin.get("fullname", "").upper(),
                    "title":       ev.get("title", {}).get("en", ""),
                    "date":        ev.get("date_event", ""),
                    "categories":  [c.get("name") for c in ev.get("categories", [])],
                    "hot_score":   ev.get("hot_score", 0),
                    "source":      ev.get("source", ""),
                })
        log.info(f"CoinMarketCal : {len(result)} événements chargés")
        return result
    except Exception as e:
        log.warning(f"CoinMarketCal fetch échoué : {e}")
        return []


# ── Agrégation par symbole ────────────────────────────────────────────────────
def build_symbol_index(trending: list, vol_spikes: list,
                        gh_spikes: list, cmc_events: list) -> dict:
    """Construit un index {symbol: {catalysts}} pour enrichir le scoring."""
    index = {}

    # Trending CoinGecko
    for i, t in enumerate(trending):
        sym = t["symbol"] + "USDT"
        index.setdefault(sym, {"flags": [], "events": [], "trending_rank": None,
                                "vol_spike": None, "gh_spike": None})
        index[sym]["trending_rank"] = i + 1
        index[sym]["flags"].append(f"🔥 Trending #{i+1} sur CoinGecko")

    # Volume spikes
    for s in vol_spikes:
        sym = s["symbol"]
        index.setdefault(sym, {"flags": [], "events": [], "trending_rank": None,
                                "vol_spike": None, "gh_spike": None})
        index[sym]["vol_spike"] = s["vol_ratio"]
        index[sym]["flags"].append(f"⚡ Volume ×{s['vol_ratio']:.1f} vs médiane")

    # GitHub spikes
    for g in gh_spikes:
        sym = g["symbol"]
        index.setdefault(sym, {"flags": [], "events": [], "trending_rank": None,
                                "vol_spike": None, "gh_spike": None})
        index[sym]["gh_spike"] = g["commits_30d"]
        index[sym]["flags"].append(f"💻 {g['commits_30d']} commits GitHub / 30j ({g['contributors']} contributeurs)")

    # CoinMarketCal events
    for ev in cmc_events:
        raw_sym = ev["symbol"].replace(" ", "").upper()
        sym = raw_sym + "USDT" if not raw_sym.endswith("USDT") else raw_sym
        index.setdefault(sym, {"flags": [], "events": [], "trending_rank": None,
                                "vol_spike": None, "gh_spike": None})
        days_left = ""
        try:
            d = datetime.fromisoformat(ev["date"].replace("Z", "+00:00"))
            n = (d - datetime.now(timezone.utc)).days
            days_left = f" (dans {n}j)" if n >= 0 else ""
        except Exception:
            pass
        label = f"🗓️ {ev['title']}{days_left}"
        index[sym]["events"].append({
            "title":      ev["title"],
            "date":       ev["date"],
            "categories": ev["categories"],
            "hot_score":  ev["hot_score"],
            "source":     ev["source"],
        })
        index[sym]["flags"].append(label)

    return index


# ── Score catalyseur ──────────────────────────────────────────────────────────
def compute_catalyst_score(sym_data: dict | None) -> int:
    """Score 0–20 basé sur le nombre et la qualité des catalyseurs."""
    if not sym_data:
        return 0
    score = 0
    tr = sym_data.get("trending_rank")
    if tr:
        score += max(0, 8 - tr)   # #1 → +7, #7 → +1
    if sym_data.get("vol_spike"):
        r = sym_data["vol_spike"]
        score += 3 if r >= 5 else 2 if r >= 3 else 1
    if sym_data.get("gh_spike"):
        score += 3
    score += min(5, len(sym_data.get("events", [])) * 2)
    return min(20, score)


# ── Run ───────────────────────────────────────────────────────────────────────
def run() -> dict:
    cfg = _load_config()

    log.info("=== Fetch catalysts ===")

    fg      = fetch_fear_greed()
    trending = fetch_trending()
    vol_spikes = detect_volume_spikes(threshold=3.0)
    gh_spikes  = detect_github_spikes()

    cmc_events = []
    cmc_key = cfg.get("coinmarketcal_key") or os.environ.get("COINMARKETCAL_KEY")
    if cmc_key:
        cmc_events = fetch_coinmarketcal(cmc_key)
    else:
        log.info("CoinMarketCal : pas de clé API — ignoré (voir scripts/config.json)")

    symbol_index = build_symbol_index(trending, vol_spikes, gh_spikes, cmc_events)

    result = {
        "generated": TODAY,
        "fear_greed": fg,
        "trending":   trending,
        "vol_spikes": vol_spikes,
        "gh_spikes":  gh_spikes,
        "cmc_events": cmc_events,
        "by_symbol":  symbol_index,
    }

    out = COMPUTED / "catalysts.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    log.info(f"catalysts.json écrit — {len(symbol_index)} tokens avec catalyseurs")
    return result


if __name__ == "__main__":
    run()
