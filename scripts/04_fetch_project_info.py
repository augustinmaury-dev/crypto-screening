"""Enrichissement projet : GitHub activity + détection red flags.

GitHub : on extrait owner/repo depuis les liens CoinGecko, on appelle l'API GitHub publique
(60 req/h sans token, mais on a un cache 7j).
Audits / équipe : on parse la description CoinGecko + on cherche des red flags.
"""
from common import http_get, cache_put, cache_get, setup_logger, RateLimiter
import sys, re, time
log = setup_logger("04_project")

GH_RL = RateLimiter(calls_per_minute=50)  # 60/h sans token, on lisse

RED_FLAG_PATTERNS = [
    r"\bguaranteed\b", r"\b100x\b", r"\b1000x\b", r"\bmoonshot\b",
    r"\brisk[- ]?free\b", r"\bpassive income\b", r"\bget rich\b",
    r"\bensured returns?\b", r"\bdouble your\b",
]
AUDIT_PATTERNS = [
    r"\bcertik\b", r"\bhacken\b", r"\btrail of bits\b",
    r"\bopenzeppelin\b", r"\bquantstamp\b", r"\bpeckshield\b", r"\bslowmist\b",
]

def parse_github_repo(detail: dict):
    links = detail.get("links", {}) or {}
    repos = (links.get("repos_url") or {}).get("github") or []
    for u in repos:
        m = re.match(r"https?://github\.com/([\w.-]+)/([\w.-]+)/?", u)
        if m:
            return m.group(1), m.group(2).rstrip(".git")
    return None, None

def fetch_github(owner: str, repo: str):
    name = f"{owner}__{repo}"
    cached = cache_get("project", f"gh_{name}", max_age_hours=24*7)
    if cached:
        return cached["data"] if isinstance(cached, dict) and "data" in cached else cached
    GH_RL.wait()
    try:
        info = http_get(f"https://api.github.com/repos/{owner}/{repo}")
        GH_RL.wait()
        commits = http_get(f"https://api.github.com/repos/{owner}/{repo}/commits",
                           {"per_page": 100})
        GH_RL.wait()
        try:
            release = http_get(f"https://api.github.com/repos/{owner}/{repo}/releases/latest")
        except Exception:
            release = None
        # commits du dernier mois
        from datetime import datetime, timezone, timedelta
        cutoff_30 = datetime.now(timezone.utc) - timedelta(days=30)
        cutoff_90 = datetime.now(timezone.utc) - timedelta(days=90)
        commits_30 = 0; authors_90 = set()
        for c in commits:
            d = c.get("commit", {}).get("author", {}).get("date")
            if not d: continue
            t = datetime.fromisoformat(d.replace("Z", "+00:00"))
            if t > cutoff_30: commits_30 += 1
            if t > cutoff_90: authors_90.add((c.get("author") or {}).get("login") or c["commit"]["author"].get("name"))
        last_release_age = None
        if release and release.get("published_at"):
            t = datetime.fromisoformat(release["published_at"].replace("Z", "+00:00"))
            last_release_age = (datetime.now(timezone.utc) - t).days
        result = {
            "owner": owner, "repo": repo,
            "stars": info.get("stargazers_count"),
            "forks": info.get("forks_count"),
            "open_issues": info.get("open_issues_count"),
            "pushed_at": info.get("pushed_at"),
            "created_at": info.get("created_at"),
            "commits_30d": commits_30,
            "active_contributors_90d": len(authors_90),
            "last_release_age_days": last_release_age,
            "license": (info.get("license") or {}).get("spdx_id"),
        }
        cache_put("project", f"gh_{name}", result)
        return result
    except Exception as e:
        log.warning(f"GitHub fail {owner}/{repo}: {e}")
        return None

def detect_red_flags(detail: dict):
    """Cherche des red flags dans la description CoinGecko."""
    desc = (((detail.get("description") or {}).get("en")) or "").lower()
    flags = []
    for p in RED_FLAG_PATTERNS:
        if re.search(p, desc):
            flags.append(p.strip(r"\b"))
    audits = [p.strip(r"\b") for p in AUDIT_PATTERNS if re.search(p, desc)]
    return {"red_flags": flags, "audit_mentions": audits, "description_length": len(desc)}

def enrich_for_token(symbol: str, cg_id: str):
    detail_cache = cache_get("coingecko", f"detail_{cg_id}", max_age_hours=24*7)
    if not detail_cache:
        return None
    detail = detail_cache["data"] if isinstance(detail_cache, dict) and "data" in detail_cache else detail_cache

    owner, repo = parse_github_repo(detail)
    gh = fetch_github(owner, repo) if owner else None
    flags = detect_red_flags(detail)

    enrich = {
        "symbol": symbol,
        "cg_id": cg_id,
        "genesis_date": detail.get("genesis_date"),
        "categories": detail.get("categories") or [],
        "homepage": ((detail.get("links") or {}).get("homepage") or [None])[0],
        "whitepaper": ((detail.get("links") or {}).get("whitepaper")) or None,
        "github": gh,
        **flags,
    }
    cache_put("project", f"enrich_{symbol}", enrich)
    return enrich

if __name__ == "__main__":
    cg_map = cache_get("coingecko", "binance_to_cg_map", max_age_hours=24*7)
    cg_map = cg_map["data"] if isinstance(cg_map, dict) and "data" in cg_map else cg_map
    if not cg_map:
        log.error("Lance 03_fetch_coingecko.py d'abord"); sys.exit(1)
    items = [(s, cid) for s, cid in cg_map.items() if cid]
    n = int(sys.argv[1]) if len(sys.argv) > 1 else len(items)
    items = items[:n]
    log.info(f"Enrichissement projet : {len(items)} tokens")
    for i, (sym, cid) in enumerate(items, 1):
        enrich_for_token(sym, cid)
        if i % 10 == 0:
            log.info(f"  enrich: {i}/{len(items)}")
