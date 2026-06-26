"""Score composite — voir methodology.md (version 1.2)."""
from __future__ import annotations
from common import cache_get, cache_put, COMPUTED, TODAY, setup_logger, ROOT
import csv, sys, json
log = setup_logger("06_score")

# ─── Patterns pour le score signal ──────────────────────────────────────────
_BULLISH_SET = {
    "breakout_30d", "rsi_bullish_divergence", "golden_cross",
    "macd_bullish_cross", "double_bottom_90d", "bull_flag",
    "uptrend", "support_bounce", "hammer_4h", "bullish_engulfing_4h",
    "morning_star_4h", "squeeze_breakout",
}
_BEARISH_SET = {
    "breakdown_30d", "rsi_bearish_divergence", "death_cross",
    "macd_bearish_cross", "double_top_90d", "bear_flag",
    "downtrend", "resistance_test", "shooting_star_4h",
    "bearish_engulfing_4h", "evening_star_4h",
}

def _load_pattern_weights() -> dict:
    """Charge les poids adaptatifs depuis data/learning/pattern_weights.json."""
    try:
        f = ROOT / "data" / "learning" / "pattern_weights.json"
        if f.exists():
            data = json.loads(f.read_text(encoding="utf-8"))
            return {p: float(v.get("weight", 1.0))
                    for p, v in data.items() if isinstance(v, dict)}
    except Exception:
        pass
    return {}

# Poids de formule par défaut (v1.2) — remplacés par les poids appris dès que possible
_DEFAULT_FW = {"solidity": 0.20, "momentum": 0.30, "risk": 0.15, "antiscam": 0.20, "signal": 0.15}

def _load_formula_weights() -> dict:
    """Charge les poids de formule calibrés depuis data/learning/formula_weights.json.
    Retourne les défauts si pas encore de données suffisantes.
    Le blend_factor indique à quel point les données priment sur les défauts (0→100%).
    """
    try:
        f = ROOT / "data" / "learning" / "formula_weights.json"
        if f.exists():
            data = json.loads(f.read_text(encoding="utf-8"))
            w = data.get("weights", {})
            if w and abs(sum(w.values()) - 1.0) < 0.05:
                return w
    except Exception:
        pass
    return _DEFAULT_FW.copy()

def tier(rank):
    if rank is None: return "Speculative"
    if rank <= 100: return "Etabli"
    if rank <= 500: return "Mid"
    return "Speculative"

def clamp(x, lo=0, hi=100):
    if x is None: return 0
    return max(lo, min(hi, x))

def score_solidity(tier_, age_days, audit_score, gh):
    s_tier = {"Etabli": 100, "Mid": 60, "Speculative": 20}.get(tier_, 0)
    s_age = min(100, (age_days or 0) / 365 * 50) if age_days else 0
    if not gh:
        s_gh = 0
    else:
        commits = gh.get("commits_30d") or 0
        contrib = gh.get("active_contributors_90d") or 0
        rel_age = gh.get("last_release_age_days")
        s_gh = min(100, 40 * min(1, commits/30) + 40 * min(1, contrib/5) + (20 if rel_age is not None and rel_age < 90 else 0))
    return 0.35*s_tier + 0.20*s_age + 0.20*audit_score + 0.25*s_gh

def score_momentum(price, ma50, ma200, rsi, vol_ratio):
    if price and ma50 and ma200:
        if price > ma50 > ma200: s_ma = 100
        elif price > ma50 and ma50 < ma200: s_ma = 60
        elif price < ma50 and ma50 > ma200: s_ma = 30
        else: s_ma = 10
    else:
        s_ma = 30
    if rsi is None: s_rsi = 30
    elif 45 <= rsi <= 65: s_rsi = 100
    elif 35 <= rsi < 45 or 65 < rsi <= 75: s_rsi = 70
    elif 25 <= rsi < 35 or 75 < rsi <= 85: s_rsi = 40
    else: s_rsi = 10
    if vol_ratio is None: s_vol = 30
    elif vol_ratio > 1.5: s_vol = 100
    elif vol_ratio > 1.0: s_vol = 70
    elif vol_ratio > 0.5: s_vol = 40
    else: s_vol = 10
    return 0.40*s_ma + 0.30*s_rsi + 0.30*s_vol

def score_risk(vol_30, dd_90, dist_90, corr_btc):
    if vol_30 is None: s_v = 30
    elif vol_30 < 0.6: s_v = 100
    elif vol_30 < 1.0: s_v = 70
    elif vol_30 < 1.5: s_v = 40
    else: s_v = 10
    if dd_90 is None: s_dd = 30
    elif dd_90 < 0.25: s_dd = 100
    elif dd_90 < 0.50: s_dd = 60
    elif dd_90 < 0.75: s_dd = 30
    else: s_dd = 10
    if dist_90 is None: s_dist = 30
    elif dist_90 < 0.10: s_dist = 100
    elif dist_90 < 0.30: s_dist = 70
    elif dist_90 < 0.50: s_dist = 40
    else: s_dist = 10
    if corr_btc is None: s_c = 50
    elif 0.3 <= corr_btc <= 0.7: s_c = 100
    elif 0.7 < corr_btc <= 0.9: s_c = 60
    elif corr_btc > 0.9: s_c = 30
    else: s_c = 70
    return 0.35*s_v + 0.30*s_dd + 0.15*s_dist + 0.20*s_c

def compute_market_regime(indicators: list) -> float:
    """Calcule le score de régime macro (-10 à +10) depuis les indicateurs du jour.

    Composantes (identiques au signal marché du rapport) :
      BTC vs MAs, RSI BTC, drawdown BTC, breadth (% tokens haussiers),
      structures tendance (uptrend vs downtrend), volume BTC.

    Sauvegarde dans data/computed/market_regime.json pour le dashboard.
    Retourne 0.0 si données insuffisantes (neutre = pas de biais).
    """
    try:
        btc = next((x for x in indicators if isinstance(x, dict) and x.get("symbol") == "BTCUSDT"), None)
        score = 0.0

        if btc:
            price, ma50, ma200 = btc.get("price"), btc.get("ma_50"), btc.get("ma_200")
            if price and ma50 and ma200:
                if price > ma50 > ma200:   score += 2
                elif price > ma50:         score += 1
                elif price < ma50 < ma200: score -= 2
                else:                      score -= 1

            rsi = btc.get("rsi_14")
            if rsi:
                if rsi > 60:   score += 1
                elif rsi < 40: score -= 1

            dd = btc.get("drawdown_90d")
            if dd is not None:
                if dd < 0.15:  score += 1
                elif dd > 0.40: score -= 1

            vol = btc.get("vol_ratio_vs_med90")
            if vol is not None:
                if vol > 1.5:  score += 1
                elif vol < 0.5: score -= 1

        # Breadth et structures sur l'ensemble de l'univers
        valid = [x for x in indicators if isinstance(x, dict) and x.get("patterns") is not None]
        if valid:
            n = len(valid)
            uptrend_n   = sum(1 for x in valid if "uptrend"   in (x.get("patterns") or []))
            downtrend_n = sum(1 for x in valid if "downtrend" in (x.get("patterns") or []))
            breadth     = uptrend_n / n

            if breadth > 0.40:   score += 1
            elif breadth < 0.25: score -= 1

            if downtrend_n > uptrend_n * 1.5: score -= 1
            elif uptrend_n > downtrend_n * 1.5: score += 1

        regime = float(max(-10.0, min(10.0, score)))

        # Sauvegarde pour le dashboard
        try:
            regime_data = {"score": regime, "date": str(TODAY), "components": {
                "btc_vs_mas": score, "breadth_pct": round(breadth * 100, 1) if valid else None
            }}
            (COMPUTED / "market_regime.json").write_text(
                json.dumps(regime_data, ensure_ascii=False), encoding="utf-8"
            )
        except Exception:
            pass

        return regime
    except Exception:
        return 0.0


def _regime_multipliers(regime_score: float) -> tuple:
    """Multiplicateurs bull/bear asymétriques selon le régime de marché.

    Asymétrie intentionnelle :
      - Marché baissier : bull réduit MAX -15% (préserve la sensibilité au retournement)
      - Marché haussier : bull amplifié MAX +40% (récompense le changement de tendance)
      - Bear : réduit MAX -30% en marché baissier, amplifié MAX +15% en haussier

    regime -10 → bull x0.85, bear x1.30
    regime   0 → bull x1.00, bear x1.00  (neutre)
    regime +10 → bull x1.40, bear x0.85
    """
    factor = regime_score / 10.0   # -1.0 à +1.0
    if factor >= 0:
        # Marché haussier : amplifier bull fortement, réduire bear légèrement
        bull_mult = 1.0 + factor * 0.40
        bear_mult = 1.0 - factor * 0.15
    else:
        # Marché baissier : réduire bull doucement, amplifier bear normalement
        bull_mult = 1.0 + factor * 0.15   # factor négatif → réduction max 15%
        bear_mult = 1.0 - factor * 0.30   # factor négatif → amplification max 30%
    return bull_mult, bear_mult


def score_signal(patterns: list, bull_signals, bear_signals, regime_score: float = 0.0):
    """Score directionnel pondéré par les poids adaptatifs + régime macro.

    Chaque pattern a un poids ajusté quotidiennement par 08_learn.py selon
    son taux de bonne prédiction sur 14 jours.

    Multiplicateur de régime ASYMÉTRIQUE :
      - Baissier : bull signals -15% max → le système reste prêt au retournement
      - Haussier : bull signals +40% max → réactive les patterns dormants
      - Le seuil DEAD_WEIGHT s'abaisse en marché haussier pour réveiller
        les patterns bull qui ont appris en période baissière

    - score > 50 → biais haussier pondéré
    - score = 50 → neutre
    - score < 50 → biais baissier pondéré
    """
    weights = _load_pattern_weights()
    # Seuil adaptatif : en marché haussier, abaisser pour réactiver les patterns
    # bull dormants (ex: macd_bullish_cross à 0.1 redevient actif à +5/10)
    if regime_score >= 5:
        DEAD_WEIGHT_THRESHOLD = 0.08   # réactive patterns à poids 0.1
    elif regime_score >= 2:
        DEAD_WEIGHT_THRESHOLD = 0.12
    else:
        DEAD_WEIGHT_THRESHOLD = 0.15   # défaut (marché baissier ou neutre)

    w_bull = sum(weights.get(p, 1.0) for p in patterns if p in _BULLISH_SET and weights.get(p, 1.0) > DEAD_WEIGHT_THRESHOLD)
    w_bear = sum(weights.get(p, 1.0) for p in patterns if p in _BEARISH_SET and weights.get(p, 1.0) > DEAD_WEIGHT_THRESHOLD)

    # Multiplicateur asymétrique
    bull_mult, bear_mult = _regime_multipliers(regime_score)
    w_bull *= bull_mult
    w_bear *= bear_mult

    total = w_bull + w_bear
    if total == 0:
        return 50
    net = w_bull - w_bear
    ratio = net / total           # -1 à +1
    conviction = min(1.0, total / 4.0)   # pleine conviction à 4 unités pondérées
    return clamp(50 + ratio * 50 * conviction)

def score_antiscam(volume_24h_quote, volume_history_quote, team_score, n_red_flags):
    if volume_24h_quote is None: s_l = 0
    elif volume_24h_quote > 5_000_000: s_l = 100
    elif volume_24h_quote > 1_000_000: s_l = 70
    elif volume_24h_quote > 500_000: s_l = 40
    else: s_l = 10
    # stabilité = on prend un proxy : ratio actuel/médiane via vol_ratio (clé ailleurs)
    s_stab = 70  # par défaut, sera affiné si on a des stats vol stables
    if n_red_flags == 0: s_rf = 100
    elif n_red_flags == 1: s_rf = 60
    elif n_red_flags == 2: s_rf = 20
    else: s_rf = 0
    return 0.35*s_l + 0.25*s_stab + 0.20*team_score + 0.20*s_rf

def detect_team_score(enrich):
    """Heuristique pauvre faute de scraping LinkedIn. À enrichir avec GitHub si actif."""
    if not enrich: return 30
    gh = enrich.get("github") or {}
    if (gh.get("active_contributors_90d") or 0) >= 3: return 70
    if enrich.get("homepage") and enrich.get("whitepaper"): return 60
    return 30

def detect_audit_score(enrich):
    if not enrich: return 0
    if enrich.get("audit_mentions"):
        return 60  # mention sans preuve formelle
    return 0

def is_stablecoin(vol_30d, drawdown_90d, symbol=""):
    """Détecte les stablecoins : volatilité annualisée < 3% ET drawdown 90j < 2%.
    Ils sont retirés du classement principal (biais artificiel sur les métriques de risque).
    """
    # Stablecoins connus par nom (USD + P3 : ajout EUR-pegged)
    known = {"USDEUSDT", "RLUSDUSDT", "FDUSDUSDT", "USDCUSDT", "BUSDUSDT",
             "USDTUSDT", "DAIUSDT", "FRAXUSDT", "TUSDUSDT", "USDDUSDT",
             "SUSDUSDT", "USTUSDT", "EURCUSDT", "PYUSDUSDT", "USDPUSDT",
             "AEUSDUSDT", "XUSDUSDT", "CUSDUSDT",
             # P3 — stablecoins EUR non filtrés (polluaient top Speculative/Mid)
             "EURUSDT", "EURIUSDT", "AEURUSDT",
             # P3 — autres quasi-stables détectés (avg |return| < 0.2%)
             "BFUSDUSDT", "USD1USDT", "UUSDT"}
    if symbol in known:
        return True
    # Détection par métriques — seuils relâchés pour capter les EUR-pegged
    # (vol légèrement > USD-pegged mais drawdown quasi nul)
    if vol_30d is not None and drawdown_90d is not None:
        return vol_30d < 0.08 and drawdown_90d < 0.05
    return False

def is_suspect(tier_, enrich, age_days):
    flags = 0
    if enrich and not (enrich.get("github") and (enrich["github"].get("active_contributors_90d") or 0) >= 1):
        if not enrich.get("homepage"): flags += 1
    if enrich and len(enrich.get("red_flags") or []) > 0:
        flags += 1
    if age_days is not None and age_days < 180:
        flags += 1
    return flags >= 2

def _unwrap(x):
    if x is None: return None
    return x.get("data", x) if isinstance(x, dict) and "data" in x else x

def _load_catalysts() -> dict:
    """Charge catalysts.json généré par 10_fetch_catalysts.py."""
    try:
        p = COMPUTED / "catalysts.json"
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        pass
    return {}

def predict_bull_prob_7d(s_mom, s_sig, s_risk, rsi, vol_ratio, catalyst_score) -> int:
    """Probabilité haussière sur 7 jours — 0 à 100 %.
    Basée sur les sous-scores calibrés + catalyseurs détectés.
    Affichée avec une marge d'incertitude explicite dans le dashboard.
    """
    # Base 50 % (incertitude maximale)
    p = 50.0
    # Momentum : fort momentum → +15 max
    p += (s_mom - 50) * 0.30
    # Signal directionnel : biais bull/bear → +12 max
    p += (s_sig - 50) * 0.24
    # Risque : risque élevé pénalise → ±8
    p += (s_risk - 50) * 0.16
    # RSI : surachat / survente
    if rsi is not None:
        if rsi > 75:  p -= 8
        elif rsi < 30: p += 6
        elif 45 <= rsi <= 65: p += 3
    # Volume anormal positif
    if vol_ratio and vol_ratio > 2.0: p += 4
    # Catalyseurs externes
    p += min(10, catalyst_score * 1.5)
    return int(clamp(round(p), 20, 80))  # plafonné 20–80 : on n'est jamais certain

def _load_tvl() -> dict:
    """Charge tvl.json généré par 11_fetch_defi.py."""
    try:
        p = COMPUTED / "tvl.json"
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        pass
    return {}

def run():
    catalysts = _load_catalysts()
    tvl_map   = _load_tvl()
    universe  = _unwrap(cache_get("binance",    "universe",          24))    or []
    indicators= _unwrap(cache_get("binance",    "indicators",        24))    or []
    cg_map    = _unwrap(cache_get("coingecko",  "binance_to_cg_map", 24*7)) or {}
    markets   = _unwrap(cache_get("coingecko",  "markets_top1000",   24*7)) or []

    market_by_id = {m["id"]: m for m in markets if isinstance(m, dict) and m.get("id")}
    ind_by_sym   = {x["symbol"]: x for x in indicators if isinstance(x, dict)}
    uni_by_sym   = {u["symbol"]: u for u in universe   if isinstance(u, dict)}

    # Régime macro — calculé une fois pour tout l'univers
    regime_score = compute_market_regime(indicators)
    bull_m, bear_m = _regime_multipliers(regime_score)
    log.info(f"Régime macro : {regime_score:+.1f}/10 → bull ×{bull_m:.2f}, bear ×{bear_m:.2f}")

    rows = []
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc)
    for sym, u in uni_by_sym.items():
        ind = ind_by_sym.get(sym)
        if not ind: continue
        cg_id = (cg_map or {}).get(sym)
        m = market_by_id.get(cg_id) if cg_id else None
        rank = (m or {}).get("market_cap_rank")
        tier_ = tier(rank)
        enrich_cache = cache_get("project", f"enrich_{sym}", 24*7)
        enrich = enrich_cache["data"] if isinstance(enrich_cache, dict) and "data" in enrich_cache else enrich_cache

        # âge : preferer genesis_date, sinon nb de jours d'historique de prix
        age_days = None
        if enrich and enrich.get("genesis_date"):
            try:
                age_days = (now - datetime.fromisoformat(enrich["genesis_date"]).replace(tzinfo=timezone.utc)).days
            except Exception: pass
        if age_days is None:
            age_days = ind.get("n_days_history")

        audit_score = detect_audit_score(enrich)
        team_score = detect_team_score(enrich)
        n_rf = len((enrich or {}).get("red_flags") or [])

        s_sol = score_solidity(tier_, age_days, audit_score, (enrich or {}).get("github"))
        s_mom = score_momentum(ind["price"], ind["ma_50"], ind["ma_200"], ind["rsi_14"], ind["vol_ratio_vs_med90"])
        s_risk = score_risk(ind["vol_30d_annualized"], ind["drawdown_90d"], ind["distance_to_90d_high"], ind["corr_btc_90d"])
        s_anti = score_antiscam(u["volume_24h_quote"], None, team_score, n_rf)
        s_sig = score_signal(ind.get("patterns", []), ind.get("bull_signals", 0), ind.get("bear_signals", 0), regime_score)
        # Poids lus depuis formula_weights.json (appris) ou défauts si pas encore de données
        fw = _load_formula_weights()
        score = round(
            fw["solidity"]*s_sol + fw["momentum"]*s_mom +
            fw["risk"]*s_risk   + fw["antiscam"]*s_anti +
            fw["signal"]*s_sig,
        2)

        suspect = is_suspect(tier_, enrich, age_days)
        stablecoin = is_stablecoin(ind.get("vol_30d_annualized"), ind.get("drawdown_90d"), sym)

        # ── Tokenomics (depuis CoinGecko markets) ──
        market_cap        = (m or {}).get("market_cap")
        fdv               = (m or {}).get("fully_diluted_valuation")
        circulating_supply= (m or {}).get("circulating_supply")
        total_supply      = (m or {}).get("total_supply")
        max_supply        = (m or {}).get("max_supply")
        # ratio circulation : % de l'offre totale en circulation (dilution)
        circ_ratio = None
        if circulating_supply and total_supply and total_supply > 0:
            circ_ratio = round(circulating_supply / total_supply * 100, 1)

        # ── TVL (depuis DefiLlama) ──
        tvl_data = tvl_map.get(sym, {})
        tvl      = tvl_data.get("tvl")
        tvl_fmt  = tvl_data.get("tvl_fmt")
        tvl_change_7d = tvl_data.get("change_7d")

        # ── Catalyseurs ──
        cats_data = catalysts.get("by_symbol", {}).get(sym, {})
        from importlib import import_module as _im
        try:
            _cat_mod = _im("10_fetch_catalysts")
            catalyst_score = _cat_mod.compute_catalyst_score(cats_data)
        except Exception:
            catalyst_score = 0
        catalyst_flags = "|".join((cats_data.get("flags") or [])[:5])
        trending_rank  = cats_data.get("trending_rank")
        vol_spike      = cats_data.get("vol_spike")

        # ── Prédiction ──
        bull_prob_7d = predict_bull_prob_7d(
            s_mom, s_sig, s_risk,
            ind.get("rsi_14"), ind.get("vol_ratio_vs_med90"),
            catalyst_score
        )

        rows.append({
            "symbol": sym, "base": u["base"], "tier": tier_, "rank_mcap": rank,
            "price": u["price"], "vol_24h_usd": u["volume_24h_quote"],
            "change_24h_pct": u["change_pct_24h"],
            "rsi_14": ind["rsi_14"], "macd_hist": ind["macd_hist"],
            "ma_50": ind["ma_50"], "ma_200": ind["ma_200"],
            "vol_30d_ann": ind["vol_30d_annualized"],
            "drawdown_90d": ind["drawdown_90d"], "dist_to_high_90d": ind["distance_to_90d_high"],
            "vol_ratio_vs_med90": ind["vol_ratio_vs_med90"],
            "corr_btc_90d": ind["corr_btc_90d"],
            "support_90d": ind.get("support_90d"),
            "resistance_90d": ind.get("resistance_90d"),
            "patterns": "|".join(ind.get("patterns", [])),
            "bull_signals": ind.get("bull_signals", 0),
            "bear_signals": ind.get("bear_signals", 0),
            "bias": ind.get("bias", "neutre"),
            "age_days": age_days,
            "n_red_flags": n_rf, "audit_score": audit_score, "team_score": team_score,
            "github_commits_30d": ((enrich or {}).get("github") or {}).get("commits_30d"),
            "github_contrib_90d": ((enrich or {}).get("github") or {}).get("active_contributors_90d"),
            "score_solidity": round(s_sol, 1),
            "score_momentum": round(s_mom, 1),
            "score_risk": round(s_risk, 1),
            "score_antiscam": round(s_anti, 1),
            "score_signal": round(s_sig, 1),
            "score": score,
            "suspect": suspect,
            "stablecoin": stablecoin,
            "categories": "|".join(((enrich or {}).get("categories") or [])[:5]),
            # Catalyseurs
            "catalyst_score":  catalyst_score,
            "catalyst_flags":  catalyst_flags,
            "trending_rank":   trending_rank,
            "vol_spike_ratio": vol_spike,
            # Prédiction
            "bull_prob_7d": bull_prob_7d,
            # Tokenomics
            "market_cap": market_cap,
            "fdv": fdv,
            "circulating_supply": circulating_supply,
            "total_supply": total_supply,
            "max_supply": max_supply,
            "circ_ratio_pct": circ_ratio,
            # TVL DefiLlama
            "tvl": tvl,
            "tvl_fmt": tvl_fmt,
            "tvl_change_7d": tvl_change_7d,
        })
    # Stablecoins triés en bas — ils ne doivent pas polluer le classement principal
    rows.sort(key=lambda r: (1 if r["stablecoin"] else 0, -r["score"], r["tier"]))
    # Fichier principal unique (écrasé à chaque run)
    out_path = COMPUTED / "scores.csv"
    if rows:
        with out_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)
    log.info(f"Scoring terminé : {len(rows)} tokens → {out_path}")
    # Snapshot daté dans history/ pour le système d'apprentissage (08_learn.py)
    from common import HISTORY
    HISTORY.mkdir(exist_ok=True)
    hist_path = HISTORY / f"scores_{TODAY}.csv"
    if rows:
        hist_path.write_text(out_path.read_text(encoding="utf-8"), encoding="utf-8")
    return r