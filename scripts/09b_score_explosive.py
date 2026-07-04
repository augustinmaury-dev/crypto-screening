"""Score explosif — modele separe pour detecter les tokens a fort potentiel de hausse rapide.

Philosophie :
  Ce modele ne cherche PAS les projets de qualite. Il cherche les tokens
  qui ressemblent a ce que font les tokens JUSTE AVANT d'exploser :
  momentum en acceleration, volume anormal, setup technique bullish,
  catalyseurs externes. La solidite fondamentale n'est PAS prise en compte.

Formule explosive :
  SCORE_EXPL = 0.40 x Momentum + 0.40 x Signal_Bull + 0.15 x Catalyseurs + 0.05 x AntiScam

Filtres minimum (non-negotiables) :
  - Volume 24h > $1M (liquidite minimum)
  - Non stablecoin
  - Non suspect (scam flags)
  - RSI entre 35 et 82 (pas en chute libre, pas completement surachete)

Poids des patterns bull : floor a 0.5 (meme si le learning les a reduits
  car le marche etait baissier, les patterns bullish restent pertinents
  pour detecter une pre-explosion).

Sortie : data/computed/scores_explosive.csv (top 50 brut)
         data/computed/top_explosive.json  (top 20 pour le dashboard)
"""
from __future__ import annotations
from common import cache_get, COMPUTED, ROOT, TODAY, setup_logger
import csv, json

log = setup_logger("09b_explosive")

_BULLISH_PATTERNS = {
    "breakout_30d", "golden_cross", "macd_bullish_cross",
    "double_bottom_90d", "bull_flag", "uptrend",
    "support_bounce", "bullish_engulfing_4h", "morning_star_4h",
    "hammer_4h", "rsi_bullish_divergence", "squeeze_breakout",
}
_BEARISH_PATTERNS = {
    "breakdown_30d", "death_cross", "macd_bearish_cross",
    "double_top_90d", "bear_flag", "downtrend",
    "bearish_engulfing_4h", "evening_star_4h", "shooting_star_4h",
    "rsi_bearish_divergence",
}

BULL_WEIGHT_FLOOR = 0.5   # floor pour patterns bull dans ce modele


def _load_pattern_weights() -> dict:
    try:
        f = ROOT / "data" / "learning" / "pattern_weights.json"
        if f.exists():
            data = json.loads(f.read_text(encoding="utf-8"))
            return {p: float(v.get("weight", 1.0)) for p, v in data.items() if isinstance(v, dict)}
    except Exception:
        pass
    return {}


def _clamp(x, lo=0, hi=100):
    if x is None: return 0
    return max(lo, min(hi, x))


def score_momentum_expl(price, ma50, ma200, rsi, vol_ratio, change_24h):
    """Momentum oriente explosion : acceleration recente + volume + position MA."""
    # Position par rapport aux MAs
    if price and ma50 and ma200:
        if price > ma50 > ma200:    s_ma = 100   # tendance haussiere confirmee
        elif price > ma50:          s_ma = 75    # au-dessus MA50, reconstruction
        elif price < ma50 < ma200:  s_ma = 20    # sous les deux MAs
        else:                       s_ma = 40    # mixte
    else:
        s_ma = 40

    # RSI : zone ideale pre-explosion = 50-72 (momentum sans surachat)
    if rsi is None:       s_rsi = 30
    elif 55 <= rsi <= 72: s_rsi = 100   # zone ideale
    elif 45 <= rsi < 55:  s_rsi = 80    # en build
    elif 72 < rsi <= 82:  s_rsi = 55    # momentum fort, attention surachat
    elif 35 <= rsi < 45:  s_rsi = 45    # rebond possible
    else:                 s_rsi = 10    # extremes

    # Volume : cle des explosions — un spike de volume precede souvent le move
    if vol_ratio is None:    s_vol = 20
    elif vol_ratio > 3.0:    s_vol = 100  # spike majeur
    elif vol_ratio > 2.0:    s_vol = 85
    elif vol_ratio > 1.5:    s_vol = 70
    elif vol_ratio > 1.0:    s_vol = 50
    elif vol_ratio > 0.7:    s_vol = 30
    else:                    s_vol = 10   # volume mort

    # Momentum 24h : acceleration recente (ni trop ni pas assez)
    c = change_24h or 0
    if 3 <= c <= 15:    s_c = 100   # hausse moderee saine
    elif 1 <= c < 3:    s_c = 70
    elif 15 < c <= 30:  s_c = 60    # deja en train d'exploser
    elif c > 30:        s_c = 30    # peut-etre trop tard
    elif -2 <= c < 1:   s_c = 40
    else:               s_c = 20   # baisse

    return _clamp(0.30*s_ma + 0.30*s_rsi + 0.25*s_vol + 0.15*s_c)


def score_signal_expl(patterns: list) -> float:
    """Score signal bull oriente explosion.
    
    Floor 0.5 sur les poids bull : les patterns haussiers gardent leur signification
    meme si le learning global les a reduits (apprentissage en marche baissier).
    Les patterns bearish sont des penalites directes.
    """
    weights = _load_pattern_weights()

    w_bull = 0.0
    for p in patterns:
        if p in _BULLISH_PATTERNS:
            w = max(BULL_WEIGHT_FLOOR, weights.get(p, 1.0))   # floor 0.5
            w_bull += w

    w_bear = 0.0
    for p in patterns:
        if p in _BEARISH_PATTERNS:
            w = weights.get(p, 1.0)
            w_bear += w

    if w_bull == 0 and w_bear == 0:
        return 50.0   # neutre

    total = w_bull + w_bear
    net = w_bull - w_bear
    ratio = net / total
    conviction = min(1.0, total / 5.0)
    return _clamp(50 + ratio * 50 * conviction)


def score_catalysts_expl(catalyst_score, vol_spike, trending_rank) -> float:
    """Catalyseurs externes : trending, volume spike, evenements."""
    s = 30.0   # base neutre

    # Score catalyseur general (events, listings, etc.)
    s += min(30, (catalyst_score or 0) * 4)

    # Spike de volume : signal fort pre-explosion
    vs = vol_spike or 1.0
    if vs > 5.0:   s += 30
    elif vs > 3.0: s += 20
    elif vs > 2.0: s += 12
    elif vs > 1.5: s += 5

    # Trending sur CoinGecko
    if trending_rank is not None:
        if trending_rank <= 3:    s += 15
        elif trending_rank <= 7:  s += 10
        elif trending_rank <= 15: s += 5

    return _clamp(s)


def compute_exit_risk_expl(rsi, vol_ratio, dist_to_high, patterns: list, macd_hist) -> tuple:
    """Signal de sortie pour les tokens en portefeuille (0–10).

    Quand un token explosif qu'on détient commence à s'épuiser :
      RSI > 72      → +2, > 80 → +4
      Volume < 0.6  → +2 (épuisement du move)
      Près du haut  → +2 (résistance 90j)
      Patterns bear → +2 chacun (max +4)
      MACD hist < 0 → +1

    0–3 = OK | 4–6 = ⚠️ Surveiller | 7+ = 🔴 Sortie
    """
    risk = 0
    reasons = []
    if rsi is not None:
        if rsi > 80:   risk += 4; reasons.append(f"RSI {rsi:.0f} extrême")
        elif rsi > 72: risk += 2; reasons.append(f"RSI {rsi:.0f} surachat")
    if vol_ratio is not None and vol_ratio < 0.6:
        risk += 2; reasons.append(f"Volume ×{vol_ratio:.1f} épuisé")
    if dist_to_high is not None and dist_to_high < 0.05:
        risk += 2; reasons.append("Près résistance 90j")
    BEARISH_EXIT = [
        ("rsi_bearish_divergence","Div RSI"),("double_top_90d","Double sommet"),
        ("shooting_star_4h","Étoile filante"),("evening_star_4h","Étoile soir"),
        ("bearish_engulfing_4h","Engloutissement"),("macd_bearish_cross","MACD bear"),
    ]
    pat_added = 0
    for pat, label in BEARISH_EXIT:
        if pat in patterns and pat_added < 4:
            risk += 2; pat_added += 2; reasons.append(label)
    if macd_hist is not None and macd_hist < 0:
        risk += 1
    risk = min(10, risk)
    label = "🔴 Sortie" if risk >= 7 else ("⚠️ Surveiller" if risk >= 4 else "✅ OK")
    return risk, label, "|".join(reasons[:3])


def score_antiscam_expl(volume_24h, n_red_flags) -> float:
    """Filtre minimum anti-scam — plus permissif que le modele principal."""
    if n_red_flags >= 3:   return 0    # scam evident
    if n_red_flags == 2:   return 30
    if volume_24h and volume_24h > 10_000_000: s_vol = 100
    elif volume_24h and volume_24h > 3_000_000: s_vol = 70
    else:                  s_vol = 50
    penalty = n_red_flags * 20
    return _clamp(s_vol - penalty)


def _unwrap(x):
    if x is None: return None
    return x.get("data", x) if isinstance(x, dict) and "data" in x else x


def run():
    log.info("=== Score Explosif (09b) ===")

    universe   = _unwrap(cache_get("binance", "universe",   24)) or []
    indicators = _unwrap(cache_get("binance", "indicators", 24)) or []
    cg_map     = _unwrap(cache_get("coingecko", "binance_to_cg_map", 24*7)) or {}
    markets    = _unwrap(cache_get("coingecko", "markets_top1000",   24*7)) or []

    market_by_id = {m["id"]: m for m in markets if isinstance(m, dict) and m.get("id")}
    ind_by_sym   = {x["symbol"]: x for x in indicators if isinstance(x, dict)}
    uni_by_sym   = {u["symbol"]: u for u in universe if isinstance(u, dict)}

    # Charger catalysts
    try:
        cats_all = json.loads((COMPUTED / "catalysts.json").read_text(encoding="utf-8"))
        cats_by_sym = cats_all.get("by_symbol", {})
    except Exception:
        cats_by_sym = {}

    rows = []
    skipped_volume = skipped_rsi = skipped_stable = skipped_suspect = 0

    for sym, u in uni_by_sym.items():
        ind = ind_by_sym.get(sym)
        if not ind:
            continue

        vol_24h = u.get("volume_24h_quote") or 0
        rsi     = ind.get("rsi_14")

        # ── Filtres minimum ──────────────────────────────────────────────
        if vol_24h < 1_000_000:
            skipped_volume += 1; continue

        # Detecter stablecoins (vol annualisee + drawdown)
        vol_ann = ind.get("vol_30d_annualized") or 0
        dd_90   = ind.get("drawdown_90d") or 0
        if vol_ann < 0.08 and dd_90 < 0.05:
            skipped_stable += 1; continue
        known_stable = {"EURUSDT","EURIUSDT","AEURUSDT","USDEUSDT","USDCUSDT",
                        "FDUSDUSDT","RLUSDUSDT","BFUSDUSDT","USD1USDT","UUSDT"}
        if sym in known_stable:
            skipped_stable += 1; continue

        if rsi is not None and (rsi < 35 or rsi > 82):
            skipped_rsi += 1; continue

        # Red flags
        cg_id  = cg_map.get(sym)
        m      = market_by_id.get(cg_id) if cg_id else None
        n_rf   = 0  # simplifie : pas d'enrich disponible ici

        # ── Scores ───────────────────────────────────────────────────────
        change_24h = u.get("change_pct_24h") or 0
        patterns   = ind.get("patterns") or []

        cats_data     = cats_by_sym.get(sym, {})
        catalyst_score = cats_data.get("catalyst_score") or 0
        vol_spike      = cats_data.get("vol_spike")
        trending_rank  = cats_data.get("trending_rank")

        s_mom  = score_momentum_expl(
            ind.get("price"), ind.get("ma_50"), ind.get("ma_200"),
            rsi, ind.get("vol_ratio_vs_med90"), change_24h
        )
        s_sig  = score_signal_expl(patterns)
        s_cat  = score_catalysts_expl(catalyst_score, vol_spike, trending_rank)
        s_anti = score_antiscam_expl(vol_24h, n_rf)

        score_expl = round(
            0.40*s_mom + 0.40*s_sig + 0.15*s_cat + 0.05*s_anti, 2
        )

        # Tier market cap
        rank = (m or {}).get("market_cap_rank")
        if rank is None:   tier = "Speculative"
        elif rank <= 100:  tier = "Etabli"
        elif rank <= 500:  tier = "Mid"
        else:              tier = "Speculative"

        bull_p = [p for p in patterns if p in _BULLISH_PATTERNS]
        bear_p = [p for p in patterns if p in _BEARISH_PATTERNS]

        exit_risk, exit_label, exit_reasons = compute_exit_risk_expl(
            rsi,
            ind.get("vol_ratio_vs_med90"),
            ind.get("distance_to_90d_high"),
            patterns,
            ind.get("macd_hist"),
        )

        rows.append({
            "symbol":         sym,
            "tier":           tier,
            "rank_mcap":      rank,
            "score_explosif": score_expl,
            "score_momentum": round(s_mom, 1),
            "score_signal":   round(s_sig, 1),
            "score_catalysts":round(s_cat, 1),
            "price":          u.get("price"),
            "vol_24h_usd":    vol_24h,
            "change_24h_pct": change_24h,
            "rsi_14":         rsi,
            "vol_ratio":      ind.get("vol_ratio_vs_med90"),
            "drawdown_90d":   dd_90,
            "ma_50":          ind.get("ma_50"),
            "ma_200":         ind.get("ma_200"),
            "patterns_bull":  "|".join(bull_p),
            "patterns_bear":  "|".join(bear_p),
            "catalyst_score": catalyst_score,
            "trending_rank":  trending_rank,
            "vol_spike":      vol_spike,
            "support_90d":    ind.get("support_90d"),
            "resistance_90d": ind.get("resistance_90d"),
            "exit_risk":      exit_risk,
            "exit_label":     exit_label,
            "exit_reasons":   exit_reasons,
        })

    rows.sort(key=lambda r: -r["score_explosif"])
    log.info(f"Tokens evalues : {len(rows)} | Filtres : vol={skipped_volume} rsi={skipped_rsi} stable={skipped_stable}")

    # CSV complet (top 50)
    top50 = rows[:50]
    out_csv = COMPUTED / "scores_explosive.csv"
    if top50:
        with out_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(top50[0].keys()))
            w.writeheader(); w.writerows(top50)

    # JSON top 20 pour le dashboard
    top20 = rows[:20]
    out_json = COMPUTED / "top_explosive.json"
    out_json.write_text(
        json.dumps({"date": str(TODAY), "tokens": top20}, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    log.info(f"scores_explosive.csv ({len(top50)}) + top_explosive.json ({len(top20)}) ecrits")
    if top20:
        log.info(f"Top 3 explosifs : {top20[0]['symbol']} ({top20[0]['score_explosif']}) | "
                 f"{top20[1]['symbol']} ({top20[1]['score_explosif']}) | "
                 f"{top20[2]['symbol']} ({top20[2]['score_explosif']})")
    return rows


if __name__ == "__main__":
    run()
