"""
10b_etf_filings.py — Suivi des annonces d'ETF crypto via la SEC (EDGAR, recherche plein texte).

Pourquoi : les hausses de ZEC (+290 %) et NEAR (+181 %) de l'été 2026 ont été portées par des ETF spot.
Tout ETF crypto américain dépose obligatoirement ses documents à la SEC avant son lancement :
  - S-1 / S-3 (et amendements /A) : dossier d'ETF déposé ou qui avance
  - 424B3 / 424B4               : prospectus définitif
  - 8-A12B                      : enregistrement en bourse → lancement dans les jours qui suivent
Source officielle, gratuite, sans clé API : https://efts.sec.gov/LATEST/search-index

Étude du 29/09/2026 (avril→sept. 2026, 24 dépôts « dossier » sur ~10 tokens de l'univers) :
  après un dépôt/amendement : 75 % des tokens battent le marché à 7 j et à 14 j (excès médian +3 à +5 pts) ;
  avant un 8-A12B (lancement) : +33 pts sur les 14 jours précédents → la hausse est souvent déjà faite.
  Petit échantillon, période favorable aux altcoins : à suivre en conditions réelles (13_memory.py).

Produit :
  data/learning/etf_filings.json  — tous les dépôts crypto rattachés à un token (cumulatif, clé = n° de dépôt)
  data/computed/scores.csv        — colonnes etf_stage, etf_last_form, etf_last_date, etf_days_since, etf_issuers
Tourne après 06b_ml_score.py. En cas d'échec réseau : log + on garde les dépôts déjà connus.
"""
from __future__ import annotations
import csv, json, os, re, time
from datetime import datetime, timedelta
from common import ROOT, TODAY, COMPUTED, HISTORY, http_get, setup_logger

log = setup_logger("10b_etf")
LEARNING = ROOT / "data" / "learning"
STORE = LEARNING / "etf_filings.json"

EFTS = "https://efts.sec.gov/LATEST/search-index"
# La SEC demande un User-Agent identifiant le demandeur. Ajoute un e-mail via la variable
# d'environnement SEC_CONTACT (secret GitHub) si la SEC se met à refuser les requêtes.
UA = {"User-Agent": f"crypto-screening research (github.com/augustinmaury-dev/crypto-screening) {os.environ.get('SEC_CONTACT', '')}".strip()}
LOOKBACK_DAYS = 180
ACTIVE_DAYS   = 60      # un dossier est « actif » s'il a bougé dans les 60 derniers jours
QUERIES = [             # (texte, formulaires)
    ('"digital asset"', "S-1,S-1/A,S-3,S-3/A,424B3,424B4"),
    ('"ETF"',           "8-A12B"),          # (ajouter "8-A12B/A" fausse le filtre de la SEC : 31 résultats au lieu de 564)
]
FORM_KIND = {"8-A12B": "listing", "8-A12B/A": "listing", "424B3": "prospectus", "424B4": "prospectus"}

# Nom → ticker Binance (ordre important : « bitcoin cash » avant « bitcoin »)
NAME_TO_TICKER = [
    ("bitcoin cash", "BCH"), ("ethereum classic", "ETC"), ("bitcoin", "BTC"), ("ethereum", "ETH"), ("ether", "ETH"),
    ("solana", "SOL"), ("ripple", "XRP"), ("dogecoin", "DOGE"), ("cardano", "ADA"), ("chainlink", "LINK"),
    ("avalanche", "AVAX"), ("polkadot", "DOT"), ("litecoin", "LTC"), ("hedera", "HBAR"), ("aptos", "APT"),
    ("uniswap", "UNI"), ("zcash", "ZEC"), ("tron", "TRX"), ("injective", "INJ"), ("hyperliquid", "HYPE"),
    ("stellar", "XLM"), ("bittensor", "TAO"), ("ondo", "ONDO"), ("aave", "AAVE"), ("cronos", "CRO"),
    ("pudgy penguins", "PENGU"), ("shiba inu", "SHIB"), ("bonk", "BONK"), ("polygon", "POL"), ("arbitrum", "ARB"),
    ("optimism", "OP"), ("celestia", "TIA"), ("render", "RENDER"), ("filecoin", "FIL"), ("cosmos", "ATOM"),
    ("algorand", "ALGO"), ("tezos", "XTZ"), ("toncoin", "TON"), ("ethena", "ENA"), ("pendle", "PENDLE"),
    ("jupiter", "JUP"), ("worldcoin", "WLD"), ("kaspa", "KAS"), ("near", "NEAR"), ("sui", "SUI"), ("sei", "SEI"),
    ("mantra", "OM"), ("flare", "FLR"), ("monero", "XMR"), ("berachain", "BERA"), ("story", "IP"),
]
STOP = {"ETF", "TRUST", "FUND", "FUNDS", "USD", "THE", "NEW", "ONE", "INC", "LLC", "CIK", "SERIES", "SHARES",
        "STAKED", "STAKING", "INCOME", "PREMIUM", "ACTIVE", "CRYPTO", "DIGITAL", "INDEX", "AND", "FOR", "ALL"}


def fetch_filings() -> list[dict]:
    start = (datetime.strptime(TODAY, "%Y%m%d") - timedelta(days=LOOKBACK_DAYS)).strftime("%Y-%m-%d")
    end = datetime.strptime(TODAY, "%Y%m%d").strftime("%Y-%m-%d")
    out = []
    for q, forms in QUERIES:
        for frm in range(0, 2000, 100):
            j = http_get(EFTS, {"q": q, "forms": forms, "dateRange": "custom", "startdt": start, "enddt": end, "from": frm},
                         headers=UA, timeout=30)
            hits = (j.get("hits") or {}).get("hits") or []
            for h in hits:
                s = h.get("_source", {})
                out.append({"adsh": s.get("adsh"), "form": s.get("form"), "date": s.get("file_date"),
                            "entity": ((s.get("display_names") or [""])[0])})
            time.sleep(0.25)            # la SEC limite à 10 requêtes/s
            if len(hits) < 100:
                break
    return out


def match_tokens(entity: str, universe: set[str]) -> list[str]:
    """Tokens de l'univers mentionnés dans le nom d'un fonds (ex. « Grayscale Near Trust (NEAR) » → NEAR)."""
    name = re.sub(r"\(CIK[^)]*\)", "", entity)
    if not re.search(r"ETF|TRUST|FUND", name, re.I):
        return []
    low = name.lower(); found = []
    for kw, tk in NAME_TO_TICKER:
        if re.search(rf"\b{re.escape(kw)}\b", low):
            found.append(tk); low = re.sub(rf"\b{re.escape(kw)}\b", " ", low)
    for w in re.findall(r"\b[A-Z0-9]{3,10}\b", name):      # tickers écrits en clair (« Canary Staked INJ ETF »)
        if w in universe and w not in STOP and w not in found:
            found.append(w)
    found = [t for t in dict.fromkeys(found) if t in universe]
    return found if 1 <= len(found) <= 2 else []            # fonds multi-actifs ignorés


def run():
    scores_path = COMPUTED / "scores.csv"
    if not scores_path.exists():
        log.warning("Pas de scores.csv — étape ignorée"); return
    with open(scores_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    universe = {r["symbol"].replace("USDT", "") for r in rows}

    store = {}
    if STORE.exists():
        try: store = json.loads(STORE.read_text(encoding="utf-8"))
        except Exception: store = {}
    try:
        raw = fetch_filings()
        new = 0
        for fl in raw:
            toks = match_tokens(fl["entity"], universe)
            if not toks or not fl.get("adsh") or not fl.get("date"):
                continue
            key = f"{fl['adsh']}|{fl['form']}"
            if key not in store:
                new += 1
            store[key] = {**fl, "tokens": toks, "kind": FORM_KIND.get(fl["form"], "dossier"),
                          "issuer": fl["entity"].split(" ")[0]}
        log.info(f"SEC EDGAR : {len(raw)} dépôts lus, {new} nouveaux dépôts crypto rattachés à un token")
    except Exception as e:
        log.warning(f"SEC EDGAR injoignable ({e}) — dépôts déjà connus conservés")
    LEARNING.mkdir(parents=True, exist_ok=True)
    STORE.write_text(json.dumps(dict(sorted(store.items(), key=lambda kv: kv[1]["date"])), ensure_ascii=False, indent=1),
                     encoding="utf-8")

    # ── annotation de scores.csv ─────────────────────────────────────────
    today = datetime.strptime(TODAY, "%Y%m%d")
    by_tok: dict[str, list[dict]] = {}
    for fl in store.values():
        for t in fl["tokens"]:
            by_tok.setdefault(t, []).append(fl)
    fields = list(rows[0].keys()) if rows else []
    for extra in ("etf_stage", "etf_last_form", "etf_last_date", "etf_days_since", "etf_issuers"):
        if extra not in fields: fields.append(extra)
    n_active = 0
    for r in rows:
        fls = sorted(by_tok.get(r["symbol"].replace("USDT", ""), []), key=lambda x: x["date"])
        r.update({"etf_stage": "", "etf_last_form": "", "etf_last_date": "", "etf_days_since": "", "etf_issuers": ""})
        if not fls:
            continue
        last = fls[-1]; days = (today - datetime.strptime(last["date"], "%Y-%m-%d")).days
        listed = [x for x in fls if x["kind"] == "listing"]
        if listed and (today - datetime.strptime(listed[-1]["date"], "%Y-%m-%d")).days <= ACTIVE_DAYS:
            stage = "🟢 ETF en cours de lancement / lancé"
        elif days <= ACTIVE_DAYS:
            stage = "📝 Dossier ETF actif"
        else:
            stage = "📁 Dossier ETF ancien"
        r["etf_stage"] = stage; r["etf_last_form"] = last["form"]; r["etf_last_date"] = last["date"]
        r["etf_days_since"] = days
        r["etf_issuers"] = "|".join(sorted({x["issuer"] for x in fls if (today - datetime.strptime(x["date"], "%Y-%m-%d")).days <= ACTIVE_DAYS}))
        n_active += stage != "📁 Dossier ETF ancien"
    with open(scores_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    (HISTORY / f"scores_{TODAY}.csv").write_text(scores_path.read_text(encoding="utf-8"), encoding="utf-8")
    log.info(f"Tokens avec un dossier ETF actif : {n_active}")


if __name__ == "__main__":
    run()
