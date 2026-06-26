"""Calcule les indicateurs techniques à partir des klines en cache."""
from __future__ import annotations
from common import cache_get, cache_put, setup_logger
import math, sys
log = setup_logger("05_indicators")

# ─────────────────────────── helpers de base ───────────────────────────────

def klines_to_arrays(klines: list):
    """Binance kline: [openTime, open, high, low, close, volume, ...]"""
    opens  = [float(k[1]) for k in klines]
    closes = [float(k[4]) for k in klines]
    highs  = [float(k[2]) for k in klines]
    lows   = [float(k[3]) for k in klines]
    vols   = [float(k[5]) for k in klines]
    return opens, closes, highs, lows, vols

def sma(arr, n):
    if len(arr) < n: return None
    return sum(arr[-n:]) / n

def ema(arr, n):
    if len(arr) < n: return None
    k = 2 / (n + 1); e = sum(arr[:n]) / n
    for x in arr[n:]: e = x * k + e * (1 - k)
    return e

def ema_series(arr, n):
    if len(arr) < n: return []
    k = 2 / (n + 1); e = sum(arr[:n]) / n
    out = [None] * (n - 1) + [e]
    for x in arr[n:]: e = x * k + e * (1 - k); out.append(e)
    return out

def rsi_val(closes, n=14):
    if len(closes) < n + 1: return None
    g = l = 0.0
    for i in range(1, n + 1):
        d = closes[i] - closes[i-1]
        if d > 0: g += d
        else: l -= d
    ag, al = g / n, l / n
    for i in range(n + 1, len(closes)):
        d = closes[i] - closes[i-1]
        ag = (ag * (n-1) + max(d, 0)) / n
        al = (al * (n-1) + max(-d, 0)) / n
    return (100 - 100 / (1 + ag/al)) if al else 100.0

def rsi_series(closes, n=14):
    if len(closes) < n + 1: return []
    out = [None] * n
    g = sum(max(closes[i] - closes[i-1], 0) for i in range(1, n+1))
    l = sum(max(closes[i-1] - closes[i], 0) for i in range(1, n+1))
    ag, al = g / n, l / n
    out.append(100 - 100/(1 + ag/al) if al else 100.0)
    for i in range(n+1, len(closes)):
        d = closes[i] - closes[i-1]
        ag = (ag*(n-1) + max(d, 0)) / n
        al = (al*(n-1) + max(-d, 0)) / n
        out.append(100 - 100/(1 + ag/al) if al else 100.0)
    return out

def macd_calc(closes):
    s12 = ema_series(closes, 12); s26 = ema_series(closes, 26)
    ml = [(a - b) if a is not None and b is not None else None for a, b in zip(s12, s26)]
    valid = [x for x in ml if x is not None]
    if len(valid) < 9: return None, None, None, ml
    sig_val = ema(valid, 9)
    sig_ser = ema_series(valid, 9)
    # Aligne sig_ser avec ml
    n_none = sum(1 for x in ml if x is None)
    sig_full = [None] * (n_none + 8) + sig_ser  # 8 = n-1 pour EMA9
    hist = ml[-1] - sig_val if ml[-1] is not None else None
    return ml[-1], sig_val, hist, ml, sig_full

# ─────────────────────────── stats de base ─────────────────────────────────

def realized_vol_30d(closes):
    if len(closes) < 31: return None
    rets = [math.log(closes[i]/closes[i-1]) for i in range(-30, 0) if closes[i-1] > 0]
    if len(rets) < 2: return None
    m = sum(rets)/len(rets)
    return math.sqrt(sum((r-m)**2 for r in rets)/(len(rets)-1)) * math.sqrt(365)

def drawdown_90d(closes):
    if len(closes) < 30: return None, None
    w = closes[-90:] if len(closes) >= 90 else closes
    peak = w[0]; max_dd = 0
    for c in w:
        if c > peak: peak = c
        dd = (c - peak) / peak
        if dd < max_dd: max_dd = dd
    return abs(max_dd), abs((w[-1] - max(w)) / max(w))

def corr_btc(closes_tok, closes_btc, n=90):
    if len(closes_tok) < n+1 or len(closes_btc) < n+1: return None
    t = [math.log(closes_tok[i]/closes_tok[i-1]) for i in range(-n, 0)]
    b = [math.log(closes_btc[i]/closes_btc[i-1]) for i in range(-n, 0)]
    mt, mb = sum(t)/len(t), sum(b)/len(b)
    num = sum((ti-mt)*(bi-mb) for ti, bi in zip(t, b))
    dt = math.sqrt(sum((x-mt)**2 for x in t)); db = math.sqrt(sum((x-mb)**2 for x in b))
    return (num / (dt * db)) if dt and db else None

# ─────────────────────────── détection de swings ───────────────────────────

def swing_highs(highs, order=3):
    """Indices des sommets locaux (chaque point est le max sur ±order voisins)."""
    out = []
    for i in range(order, len(highs) - order):
        w = highs[i-order:i+order+1]
        if highs[i] == max(w): out.append(i)
    return out

def swing_lows(lows, order=3):
    """Indices des creux locaux."""
    out = []
    for i in range(order, len(lows) - order):
        w = lows[i-order:i+order+1]
        if lows[i] == min(w): out.append(i)
    return out

def key_levels(highs, lows, closes, n=90):
    """Support et résistance principaux sur n jours, regroupés par cluster."""
    w_h = highs[-n:]; w_l = lows[-n:]
    sup = min(w_l); res = max(w_h)
    # Clustering simple : cherche le cluster le plus dense
    all_pts = sorted(w_l + w_h)
    if not all_pts: return sup, res
    # Support = médiane des 20% plus bas points
    n20 = max(1, len(all_pts)//5)
    sup = sum(all_pts[:n20]) / n20
    res = sum(all_pts[-n20:]) / n20
    return sup, res

# ─────────────────────────── patterns chartistes ───────────────────────────

def pat_breakout(closes, highs, vols):
    """Cassure au-dessus du plus haut 30j sur volume élevé."""
    if len(closes) < 31: return False
    max_30 = max(highs[-31:-1])
    med_vol = sorted(vols[-30:])[15]
    return closes[-1] > max_30 and vols[-1] > 1.5 * med_vol

def pat_breakdown(closes, lows, vols):
    """Cassure sous le plus bas 30j sur volume élevé."""
    if len(closes) < 31: return False
    min_30 = min(lows[-31:-1])
    med_vol = sorted(vols[-30:])[15]
    return closes[-1] < min_30 and vols[-1] > 1.5 * med_vol

def pat_rsi_divergence(closes, rsi_ser):
    """Divergences RSI/prix sur 14j."""
    bull = bear = False
    if len(closes) < 14 or len(rsi_ser) < 14: return bull, bear
    rc = closes[-14:]; rr = [x for x in rsi_ser[-14:] if x is not None]
    if not rr: return bull, bear
    if closes[-1] <= min(rc) and rr[-1] > min(rr): bull = True
    if closes[-1] >= max(rc) and rr[-1] < max(rr): bear = True
    return bull, bear

def pat_macd_cross(ml, sig_full):
    """Croisement MACD/signal dans les 5 dernières bougies."""
    bull = bear = False
    if not ml or not sig_full: return bull, bear
    for k in range(1, 6):
        try:
            m_prev, m_now = ml[-k-1], ml[-k]
            s_prev, s_now = sig_full[-k-1], sig_full[-k]
            if None in (m_prev, m_now, s_prev, s_now): continue
            if m_prev <= s_prev and m_now > s_now: bull = True
            if m_prev >= s_prev and m_now < s_now: bear = True
        except IndexError: break
    return bull, bear

def pat_ma_cross(ma50_ser, ma200_ser):
    """Croisement MA50/MA200 dans les 5 dernières bougies."""
    golden = death = False
    for k in range(1, 6):
        try:
            a0, a1 = ma50_ser[-k-1], ma50_ser[-k]
            b0, b1 = ma200_ser[-k-1], ma200_ser[-k]
            if None in (a0, a1, b0, b1): continue
            if a0 <= b0 and a1 > b1: golden = True
            if a0 >= b0 and a1 < b1: death = True
        except IndexError: break
    return golden, death

def pat_double_bottom(lows, closes, tol=0.02, window=90):
    """Double fond : deux creux proches (±2%) séparés par une reprise ≥15%.
    Critères resserrés v1.4 : reprise 10%→15%, + filtre MA20 de confirmation.
    P2 — réduction du taux de déclenchement (~29%→~15%) et du bruit (41.4% hit).
    Critères v1.3 : tol 3%→2%, swing order 5→7, séparation min 10 bougies.
    """
    if len(lows) < window: return False
    w = lows[-window:]
    sh = swing_lows(w, order=7)
    if len(sh) < 2: return False
    sh_sorted = sorted(sh, key=lambda i: w[i])[:2]
    i1, i2 = sorted(sh_sorted)
    if i2 - i1 < 10: return False          # séparation minimale
    l1, l2 = w[i1], w[i2]
    if l1 == 0: return False
    same_level = abs(l1 - l2) / l1 < tol
    mid_high = max(w[i1:i2+1]) if i2 > i1 else 0
    recovery = (mid_high - min(l1, l2)) / min(l1, l2) > 0.15  # 10%→15%
    above = closes[-1] > min(l1, l2) * (1 + tol)
    # P2 — filtre MA20 : le prix doit être au-dessus de la MA20 pour confirmer le rebond
    ma20 = sum(closes[-20:]) / 20 if len(closes) >= 20 else closes[-1]
    above_ma = closes[-1] > ma20
    return same_level and recovery and above and above_ma

def pat_double_top(highs, closes, tol=0.02, window=90):
    """Double sommet : deux sommets proches (±2%) séparés par un repli ≥10%.
    Critères resserrés v1.3 : tol 3%→2%, repli 5%→10%, swing order 5→7,
    séparation minimale de 10 bougies.
    """
    if len(highs) < window: return False
    w = highs[-window:]
    sh = swing_highs(w, order=7)
    if len(sh) < 2: return False
    sh_sorted = sorted(sh, key=lambda i: w[i], reverse=True)[:2]
    i1, i2 = sorted(sh_sorted)
    if i2 - i1 < 10: return False
    h1, h2 = w[i1], w[i2]
    if h1 == 0: return False
    same_level = abs(h1 - h2) / h1 < tol
    mid_low = min(w[i1:i2+1]) if i2 > i1 else 0
    pullback = (max(h1, h2) - mid_low) / max(h1, h2) > 0.10  # 5%→10%
    below = closes[-1] < max(h1, h2) * (1 - tol)
    return same_level and pullback and below

def pat_bull_flag(closes, highs, lows, vols, pole_days=10, flag_days=10):
    """Bull flag : hausse forte puis consolidation étroite à volume décroissant."""
    if len(closes) < pole_days + flag_days: return False
    pole = closes[-(pole_days+flag_days):-flag_days]
    flag_c = closes[-flag_days:]
    flag_h = highs[-flag_days:]
    flag_l = lows[-flag_days:]
    flag_v = vols[-flag_days:]
    if not pole or len(pole) < 2: return False
    pole_gain = (pole[-1] - pole[0]) / pole[0] if pole[0] else 0
    if pole_gain < 0.10: return False  # Hausse > 10% sur le mât
    flag_range = (max(flag_h) - min(flag_l)) / max(flag_h) if max(flag_h) else 1
    if flag_range > 0.10: return False  # Consolidation < 10% de range
    # Volume décroissant pendant le flag
    vol_start = sum(flag_v[:len(flag_v)//2]) / (len(flag_v)//2 or 1)
    vol_end   = sum(flag_v[len(flag_v)//2:]) / (len(flag_v) - len(flag_v)//2 or 1)
    vol_declining = vol_end < vol_start * 1.1
    # Prix dans la moitié haute du mât
    upper_half = closes[-1] > (max(pole) + min(pole)) / 2
    return vol_declining and upper_half

def pat_bear_flag(closes, highs, lows, vols, pole_days=10, flag_days=10):
    """Bear flag : baisse forte puis consolidation étroite à volume décroissant."""
    if len(closes) < pole_days + flag_days: return False
    pole = closes[-(pole_days+flag_days):-flag_days]
    flag_c = closes[-flag_days:]
    flag_h = highs[-flag_days:]
    flag_l = lows[-flag_days:]
    flag_v = vols[-flag_days:]
    if not pole or len(pole) < 2: return False
    pole_drop = (pole[0] - pole[-1]) / pole[0] if pole[0] else 0
    if pole_drop < 0.10: return False
    flag_range = (max(flag_h) - min(flag_l)) / max(flag_h) if max(flag_h) else 1
    if flag_range > 0.10: return False
    vol_start = sum(flag_v[:len(flag_v)//2]) / (len(flag_v)//2 or 1)
    vol_end   = sum(flag_v[len(flag_v)//2:]) / (len(flag_v) - len(flag_v)//2 or 1)
    vol_declining = vol_end < vol_start * 1.1
    lower_half = closes[-1] < (max(pole) + min(pole)) / 2
    return vol_declining and lower_half

def pat_trend_structure(closes, highs, lows, window=60):
    """Structure de tendance : HH+HL = uptrend, LH+LL = downtrend."""
    if len(closes) < window: return None
    w_h = highs[-window:]; w_l = lows[-window:]
    sh = swing_highs(w_h, order=5); sl = swing_lows(w_l, order=5)
    if len(sh) < 2 or len(sl) < 2: return None
    # Higher highs et higher lows
    hh = w_h[sh[-1]] > w_h[sh[-2]]
    hl = w_l[sl[-1]] > w_l[sl[-2]]
    lh = w_h[sh[-1]] < w_h[sh[-2]]
    ll = w_l[sl[-1]] < w_l[sl[-2]]
    if hh and hl: return "uptrend"
    if lh and ll: return "downtrend"
    return None

def pat_support_bounce(closes, lows, window=90, tol=0.02):
    """Rebond sur support : prix revient sur un niveau de support et repart à la hausse."""
    if len(closes) < window: return False
    w_l = lows[-window:]
    sl = swing_lows(w_l, order=5)
    if not sl: return False
    # Support = médiane des creux significatifs
    support_lvl = sorted([w_l[i] for i in sl])[len(sl)//2]
    near_support = abs(closes[-1] - support_lvl) / support_lvl < tol
    bouncing = closes[-1] > closes[-3]  # hausse sur 3 derniers jours
    return near_support and bouncing

def pat_resistance_test(closes, highs, window=90, tol=0.02):
    """Test de résistance : prix arrive sur un niveau de résistance."""
    if len(closes) < window: return False
    w_h = highs[-window:]
    sh = swing_highs(w_h, order=5)
    if not sh: return False
    res_lvl = sorted([w_h[i] for i in sh], reverse=True)[0]
    near_res = abs(closes[-1] - res_lvl) / res_lvl < tol
    return near_res

def pat_squeeze_breakout(closes, vols, squeeze_days=14):
    """Sortie de compression de volatilité (squeeze breakout).

    Phase compression (squeeze_days jours précédents) :
      Prix dans un range étroit : (max-min) / médiane < 15%.
      Typique des altcoins dormants avant un move majeur (profil ALLO, ATM).

    Phase étincelle (bougie actuelle) :
      • Prix ≥ 98% du haut de la zone de compression (sortie par le haut)
      • Volume ≥ 1.5× médiane 30j (volume qui s'éveille)
      • Momentum haussier court terme : close[-1] > close[-3]

    Capture le premier jour de réveil d'un token calme — avant que le move
    soit visible dans le score_momentum ou le RSI.
    """
    if len(closes) < squeeze_days + 3 or len(vols) < 30:
        return False

    # Zone de compression = les squeeze_days bougies AVANT la dernière
    sq = closes[-(squeeze_days + 1):-1]
    if len(sq) < squeeze_days // 2:
        return False

    sq_med = sorted(sq)[len(sq) // 2]
    if sq_med == 0:
        return False
    sq_max = max(sq)
    sq_min = min(sq)

    # 1. Range étroit (< 15% de la médiane)
    if (sq_max - sq_min) / sq_med >= 0.15:
        return False

    # 2. Cassure par le haut (prix actuel ≥ 98% du max de la compression)
    if closes[-1] < sq_max * 0.98:
        return False

    # 3. Volume spike (≥ 1.5× médiane 30j)
    med_vol = sorted(vols[-30:])[15]
    if not med_vol or vols[-1] < med_vol * 1.5:
        return False

    # 4. Momentum positif court terme
    return closes[-1] > closes[-3]

# ─────────────────────────── patterns sur bougies 4h ──────────────────────

def candle_patterns_4h(opens4, closes4, highs4, lows4, n=20):
    """Détecte des patterns de bougies sur les n dernières bougies 4h."""
    patterns = []
    if len(closes4) < 3: return patterns
    # Calcule corps et mèches
    def body(i): return abs(closes4[i] - opens4[i])
    def upper_wick(i): return highs4[i] - max(opens4[i], closes4[i])
    def lower_wick(i): return min(opens4[i], closes4[i]) - lows4[i]
    def rng(i): return highs4[i] - lows4[i] if highs4[i] != lows4[i] else 1e-10

    # Marteau (hammer) : longue mèche basse, petit corps en haut, dans downtrend
    i = -1
    if (lower_wick(i) > 2 * body(i) and
        upper_wick(i) < body(i) * 0.3 and
        body(i) / rng(i) < 0.35 and
        closes4[-3] > closes4[-2] > closes4[-1]):  # contexte baissier
        patterns.append("hammer_4h")

    # Étoile filante (shooting star) : longue mèche haute, petit corps en bas, dans uptrend
    if (upper_wick(i) > 2 * body(i) and
        lower_wick(i) < body(i) * 0.3 and
        body(i) / rng(i) < 0.35 and
        closes4[-3] < closes4[-2] < closes4[-1]):  # contexte haussier
        patterns.append("shooting_star_4h")

    # Engulfing haussier : bougie rouge suivie d'une bougie verte qui l'englobe
    i2 = -2
    if (closes4[i2] < opens4[i2] and      # rouge avant
        closes4[i] > opens4[i] and         # verte maintenant
        closes4[i] > opens4[i2] and        # englobe le haut
        opens4[i] < closes4[i2]):          # englobe le bas
        patterns.append("bullish_engulfing_4h")

    # Engulfing baissier
    if (closes4[i2] > opens4[i2] and
        closes4[i] < opens4[i] and
        opens4[i] > closes4[i2] and
        closes4[i] < opens4[i2]):
        patterns.append("bearish_engulfing_4h")

    # Doji : corps très petit (indécision)
    if body(i) / rng(i) < 0.10 and rng(i) > 0:
        patterns.append("doji_4h")

    # Morning star (3 bougies) : grande bougie rouge, petit corps, grande bougie verte
    if len(closes4) >= 3:
        i0, i1, i2_ = -3, -2, -1
        if (closes4[i0] < opens4[i0] and               # rouge
            body(-2) < body(-3) * 0.3 and              # petit corps
            closes4[i2_] > opens4[i2_] and             # verte
            closes4[i2_] > (opens4[i0] + closes4[i0])/2):  # dépasse mi-corps
            patterns.append("morning_star_4h")

    # Evening star (inverse)
    if len(closes4) >= 3:
        if (closes4[-3] > opens4[-3] and
            body(-2) < body(-3) * 0.3 and
            closes4[-1] < opens4[-1] and
            closes4[-1] < (opens4[-3] + closes4[-3])/2):
            patterns.append("evening_star_4h")

    return patterns

# ─────────────────────────── bilan directionnel ────────────────────────────

BULLISH_SIGNALS = {
    "breakout_30d", "rsi_bullish_divergence", "golden_cross",
    "macd_bullish_cross", "double_bottom_90d", "bull_flag",
    "uptrend", "support_bounce", "hammer_4h", "bullish_engulfing_4h",
    "morning_star_4h", "squeeze_breakout",
}
BEARISH_SIGNALS = {
    "breakdown_30d", "rsi_bearish_divergence", "death_cross",
    "macd_bearish_cross", "double_top_90d", "bear_flag",
    "downtrend", "resistance_test", "shooting_star_4h",
    "bearish_engulfing_4h", "evening_star_4h",
}

def directional_bias(patterns: list[str]) -> dict:
    bull = sum(1 for p in patterns if p in BULLISH_SIGNALS)
    bear = sum(1 for p in patterns if p in BEARISH_SIGNALS)
    if bull == 0 and bear == 0: bias = "neutre"
    elif bull > bear: bias = "haussier"
    elif bear > bull: bias = "baissier"
    else: bias = "mixte"
    return {"bull_signals": bull, "bear_signals": bear, "bias": bias}

# ─────────────────────────── calcul principal ──────────────────────────────

def compute_for_symbol(symbol: str, btc_closes: list):
    # Klines journalières
    kd = cache_get("binance", f"klines_1d_{symbol}", max_age_hours=24)
    if not kd: return None
    kd = kd.get("data", kd) if isinstance(kd, dict) else kd
    if len(kd) < 30: return None
    opens, closes, highs, lows, vols = klines_to_arrays(kd)

    # Klines 4h
    k4h = cache_get("binance", f"klines_4h_{symbol}", max_age_hours=6)
    if k4h:
        k4h = k4h.get("data", k4h) if isinstance(k4h, dict) else k4h
    opens4, closes4, highs4, lows4, vols4 = klines_to_arrays(k4h) if k4h and len(k4h) >= 3 else ([],[],[],[],[])

    # Indicateurs
    rsi_v   = rsi_val(closes)
    rsi_ser = rsi_series(closes)
    macd_v, macd_s, macd_h, ml, sig_full = macd_calc(closes)
    ma20  = sma(closes, 20)
    ma50  = sma(closes, 50)
    ma200 = sma(closes, 200)
    ma50_full  = [sma(closes[:i+1], 50)  for i in range(len(closes))]
    ma200_full = [sma(closes[:i+1], 200) for i in range(len(closes))]
    vol    = realized_vol_30d(closes)
    dd, dist = drawdown_90d(closes)
    c_btc  = corr_btc(closes, btc_closes) if btc_closes else None
    med_vol_90 = sorted(vols[-90:])[45] if len(vols) >= 90 else (sum(vols)/len(vols) if vols else 0)
    vol_ratio  = (vols[-1] / med_vol_90) if med_vol_90 else None

    # Trend structure
    trend = pat_trend_structure(closes, highs, lows)

    # Patterns journaliers
    patterns = []
    if pat_breakout(closes, highs, vols):      patterns.append("breakout_30d")
    if pat_breakdown(closes, lows, vols):      patterns.append("breakdown_30d")

    bull_div, bear_div = pat_rsi_divergence(closes, rsi_ser)
    if bull_div: patterns.append("rsi_bullish_divergence")
    if bear_div: patterns.append("rsi_bearish_divergence")

    bull_macd, bear_macd = pat_macd_cross(ml, sig_full)
    # Si les deux croisements MACD sont dans la même fenêtre → marché choppy, signal annulé
    if bull_macd and not bear_macd: patterns.append("macd_bullish_cross")
    if bear_macd and not bull_macd: patterns.append("macd_bearish_cross")

    golden, death = pat_ma_cross(ma50_full, ma200_full)
    # Un golden cross et un death cross simultanés = impossible en pratique → ignore
    if golden and not death: patterns.append("golden_cross")
    if death and not golden: patterns.append("death_cross")

    has_db = pat_double_bottom(lows, closes)
    has_dt = pat_double_top(highs, closes)
    # Double fond ET double sommet simultanés = signal contradictoire → ignore les deux
    if has_db and not has_dt: patterns.append("double_bottom_90d")
    if has_dt and not has_db: patterns.append("double_top_90d")
    if pat_bull_flag(closes, highs, lows, vols): patterns.append("bull_flag")
    if pat_bear_flag(closes, highs, lows, vols): patterns.append("bear_flag")
    if pat_support_bounce(closes, lows):         patterns.append("support_bounce")
    if pat_resistance_test(closes, highs):       patterns.append("resistance_test")
    if pat_squeeze_breakout(closes, vols):       patterns.append("squeeze_breakout")
    if trend: patterns.append(trend)

    # Patterns 4h
    if closes4:
        patterns += candle_patterns_4h(opens4, closes4, highs4, lows4)

    bias = directional_bias(patterns)
    sup, res = key_levels(highs, lows, closes)

    return {
        "symbol": symbol,
        "price": closes[-1],
        "rsi_14": rsi_v,
        "macd": macd_v, "macd_signal": macd_s, "macd_hist": macd_h,
        "ma_20": ma20, "ma_50": ma50, "ma_200": ma200,
        "vol_30d_annualized": vol,
        "drawdown_90d": dd,
        "distance_to_90d_high": dist,
        "vol_ratio_vs_med90": vol_ratio,
        "corr_btc_90d": c_btc,
        "support_90d": sup,
        "resistance_90d": res,
        "patterns": patterns,
        "bull_signals": bias["bull_signals"],
        "bear_signals": bias["bear_signals"],
        "bias": bias["bias"],
        "n_days_history": len(closes),
    }

def run(symbols: list[str]):
    btc = cache_get("binance", "klines_1d_BTCUSDT", max_age_hours=24)
    btc_closes = []
    if btc:
        btc_data = btc.get("data", btc) if isinstance(btc, dict) else btc
        btc_closes = [float(k[4]) for k in btc_data]
    out = []
    for i, s in enumerate(symbols, 1):
        try:
            r = compute_for_symbol(s, btc_closes)
            if r: out.append(r)
        except Exception as e:
            log.warning(f"Indicateurs fail {s}: {e}")
        if i % 50 == 0: log.info(f"  indicators: {i}/{len(symbols)}")
    cache_put("binance", "indicators", out)
    log.info(f"Indicateurs calcules pour {len(out)}/{len(symbols)} tokens")
    return out

if __name__ == "__main__":
    universe = cache_get("binance", "universe", max_age_hours=24)
    universe = universe.get("data", universe) if isinstance(universe, dict) else universe
    syms = [u["symbol"] for u in universe]
    if len(sys.argv) > 1: syms = syms[:int(sys.argv[1])]
    run(syms)
