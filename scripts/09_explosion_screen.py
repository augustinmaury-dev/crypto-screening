"""Détection de candidats à une explosion de prix — analyse rétrospective + scoring prospectif.

Méthodologie :
  1. Pour chaque token avec 180+ jours d'historique, identifie toutes les fenêtres où le prix
     a progressé de +40% ou plus en 30 jours (seuil ajustable).
  2. Enregistre l'état de 8 indicateurs au DÉBUT de chaque fenêtre pré-explosion.
  3. Agrège pour construire un "profil pré-explosion" par tier.
  4. Score chaque token actuel selon sa ressemblance avec ce profil.
  5. Produit une colonne `explosion_score` (0–15) dans le CSV des scores.

Indicateurs étudiés à T=0 (avant l'explosion) :
  - RSI 14  (zone : <40 récup / 40-55 build / 55-65 momentum / >65 déjà parti)
  - Vol ratio 7j / médiane 30j  (squeeze < 0.7 / normal / build > 1.2)
  - Price vs MA50  (sous / dessus)
  - Price vs MA200 (sous / dessus)
  - Drawdown 90j  (<30 / 30-50 / >50 %)
  - Volatilité annualisée 30j  (squeeze <60% / normal / élevée >120%)
  - Return des 7j précédents  (baisse / neutre / légère hausse)
  - Distance au plus bas 90j  (proche du fond / milieu / proche des hauts)

Notes :
  - Seuil explosion : +40% en 30j pour Speculative, +25% pour Mid, +20% pour Etabli
  - Profil sauvé dans data/learning/explosion_profile.json
  - Candidats sauvés dans data/computed/explosion_candidates_TODAY.csv
"""
from __future__ import annotations
from common import cache_get, COMPUTED, HISTORY, ROOT, TODAY, setup_logger
import csv, json, math
from pathlib import Path

def _load_pattern_weights() -> dict:
    """Charge les poids adaptatifs des patterns depuis pattern_weights.json."""
    try:
        f = ROOT / "data" / "learning" / "pattern_weights.json"
        if f.exists():
            data = json.loads(f.read_text(encoding="utf-8"))
            return {p: float(v.get("weight", 1.0))
                    for p, v in data.items() if isinstance(v, dict)}
    except Exception:
        pass
    return {}

log = setup_logger("09_explosion")

LEARNING = ROOT / "data" / "learning"

# Seuils d'explosion (return minimal en N jours)
EXPLOSION_CONFIGS = [
    ("forte",  0.40, 30),    # +40% en 30j — explosion notable
    ("majeure",0.80, 30),    # +80% en 30j — explosion majeure
    ("epique", 1.50, 90),    # +150% en 90j — mouvement épique
]

# Indicateurs retenus pour le profil
INDICATOR_KEYS = [
    "rsi_zone",          # 0=<35  1=35-45  2=45-55  3=55-65  4=>65
    "vol_regime",        # 0=squeeze(<0.7)  1=normal  2=build(>1.2)  3=surge(>2.0)
    "above_ma50",        # bool
    "above_ma200",       # bool
    "dd_zone",           # 0=<20%  1=20-40%  2=40-60%  3=>60%
    "vol_squeeze",       # bool : vol annualisée < 70% (pre-explosion silence)
    "recent_7d_neg",     # bool : return 7j < -5% (dip before rip)
    "dist_low_zone",     # 0=proche du fond(<20%)  1=milieu  2=proche des hauts(>70%)
]


# ──────────────────── helpers ────────────────────────────────────────────────

def sma(arr, n):
    return sum(arr[-n:]) / n if len(arr) >= n else None

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

def realized_vol(closes, n=30):
    if len(closes) < n + 1: return None
    rets = [math.log(closes[i]/closes[i-1]) for i in range(-n, 0) if closes[i-1] > 0]
    if len(rets) < 5: return None
    m = sum(rets)/len(rets)
    return math.sqrt(sum((r-m)**2 for r in rets)/(len(rets)-1)) * math.sqrt(365)

def snapshot_indicators(closes, vols, idx):
    """Calcule les indicateurs à t=idx (inclusif) sur la fenêtre [0..idx]."""
    c = closes[:idx+1]
    v = vols[:idx+1]
    if len(c) < 50: return None

    price = c[-1]
    rsi   = rsi_val(c)
    ma50  = sma(c, 50)
    ma200 = sma(c, 200) if len(c) >= 200 else None
    vol_ann = realized_vol(c, 30)

    # Médiane vol 30j
    vv = v[-30:] if len(v) >= 30 else v
    med_vol = sorted(vv)[len(vv)//2] if vv else 0
    vol7_avg = sum(v[-7:]) / 7 if len(v) >= 7 else (sum(v)/len(v) if v else 0)
    vol_ratio = (vol7_avg / med_vol) if med_vol > 0 else 1.0

    # Drawdown 90j
    w = c[-90:] if len(c) >= 90 else c
    pk = w[0]
    dd = 0
    for x in w:
        if x > pk: pk = x
        d = (x - pk) / pk
        if d < dd: dd = d
    dd = abs(dd)

    # Return 7j
    ret7 = (c[-1] - c[-8]) / c[-8] if len(c) >= 8 and c[-8] > 0 else 0

    # Distance au plus bas 90j
    lo = min(w)
    hi = max(w)
    dist_low = (price - lo) / (hi - lo) if hi > lo else 0.5

    # Zones discrètes
    if rsi is None:   rsi_zone = 2
    elif rsi < 35:    rsi_zone = 0
    elif rsi < 45:    rsi_zone = 1
    elif rsi < 55:    rsi_zone = 2
    elif rsi < 65:    rsi_zone = 3
    else:             rsi_zone = 4

    if vol_ratio < 0.7:   vol_regime = 0
    elif vol_ratio < 1.2: vol_regime = 1
    elif vol_ratio < 2.0: vol_regime = 2
    else:                 vol_regime = 3

    if dd < 0.20:   dd_zone = 0
    elif dd < 0.40: dd_zone = 1
    elif dd < 0.60: dd_zone = 2
    else:           dd_zone = 3

    if dist_low < 0.20:   dist_low_zone = 0
    elif dist_low < 0.70: dist_low_zone = 1
    else:                 dist_low_zone = 2

    return {
        "rsi":          rsi,
        "rsi_zone":     rsi_zone,
        "vol_ratio":    vol_ratio,
        "vol_regime":   vol_regime,
        "above_ma50":   int(price > ma50) if ma50 else 0,
        "above_ma200":  int(price > ma200) if ma200 else 0,
        "dd":           dd,
        "dd_zone":      dd_zone,
        "vol_ann":      vol_ann,
        "vol_squeeze":  int((vol_ann or 1.0) < 0.70),
        "ret7":         ret7,
        "recent_7d_neg":int(ret7 < -0.05),
        "dist_low_zone":dist_low_zone,
    }


# ──────────────────── analyse rétrospective ──────────────────────────────────

def find_pre_explosion_states(closes, vols, threshold=0.40, window=30, lead=14):
    """Pour chaque fenêtre où le prix explose de +threshold% en window jours,
    retourne les indicateurs lead jours AVANT le début de la fenêtre.
    """
    results = []
    for i in range(lead, len(closes) - window - 1):
        if closes[i] <= 0: continue
        ret = (closes[i + window] - closes[i]) / closes[i]
        if ret >= threshold:
            # Indicateurs à t = i - lead (avant que ça commence)
            snap_idx = i - lead
            if snap_idx < 50: continue
            ind = snapshot_indicators(closes, vols, snap_idx)
            if ind:
                ind["ret_actual"] = round(ret, 3)
                ind["explosion_type"] = f"+{threshold*100:.0f}%/{window}j"
                results.append(ind)
    return results


def build_profile(observations: list) -> dict:
    """Agrège les observations pré-explosion en un profil de fréquences."""
    if not observations:
        return {}
    n = len(observations)
    profile = {"n_observations": n}

    for key in INDICATOR_KEYS:
        vals = [o[key] for o in observations if key in o]
        if not vals: continue
        # Fréquence de chaque valeur
        from collections import Counter
        cnt = Counter(vals)
        # Valeur la plus fréquente = signal dominant
        mode = cnt.most_common(1)[0][0]
        freq = cnt.most_common(1)[0][1] / len(vals)
        profile[key] = {"mode": mode, "freq": round(freq, 3), "dist": dict(cnt)}

    # Métriques continues (RSI, vol)
    rsils = [o["rsi"] for o in observations if o.get("rsi") is not None]
    if rsils:
        profile["rsi_median"] = round(sorted(rsils)[len(rsils)//2], 1)
        profile["rsi_p25"]    = round(sorted(rsils)[len(rsils)//4], 1)
        profile["rsi_p75"]    = round(sorted(rsils)[3*len(rsils)//4], 1)

    vol_rs = [o["vol_ratio"] for o in observations]
    if vol_rs:
        profile["vol_ratio_median"] = round(sorted(vol_rs)[len(vol_rs)//2], 3)

    return profile


# ──────────────────── scoring prospectif ─────────────────────────────────────

def score_explosion_candidate(current_ind: dict, profile: dict, tier: str) -> tuple[int, list]:
    """Score entièrement piloté par les fréquences réelles du profil pré-explosion.

    Pour chaque indicateur discret (rsi_zone, vol_regime, dd_zone, etc.) :
      - Récupère la distribution de fréquences dans les pré-explosions historiques
      - Attribue un bonus proportionnel à la fréquence observée pour la valeur actuelle
        freq ≥ 50% → +3   freq ≥ 35% → +2   freq ≥ 20% → +1   sinon 0
    Plus le profil est riche en données, plus les seuils sont fiables.
    """
    if not profile or not current_ind:
        return 0, []

    score = 0
    reasons = []
    n_obs = profile.get("n_observations", 0)

    # ── Indicateurs discrets — score pilote par les fréquences du profil ──
    DISCRETE_KEYS = [
        ("rsi_zone",       "RSI zone"),
        ("vol_regime",     "Volume regime"),
        ("above_ma50",     "Position vs MA50"),
        ("above_ma200",    "Position vs MA200"),
        ("dd_zone",        "Drawdown zone"),
        ("vol_squeeze",    "Compression vol"),
        ("recent_7d_neg",  "Dip 7j"),
        ("dist_low_zone",  "Distance au bas 90j"),
    ]
    for key, label in DISCRETE_KEYS:
        pinfo = profile.get(key, {})
        if not pinfo or not isinstance(pinfo, dict): continue
        dist = pinfo.get("dist", {})
        total = sum(dist.values()) if dist else 0
        if total < 3: continue  # pas assez d'observations pour ce critère

        current_val = current_ind.get(key)
        if current_val is None: continue

        # Fréquence de cette valeur dans les pré-explosions
        freq = dist.get(current_val, 0) / total

        if freq >= 0.50:
            pts = 3
        elif freq >= 0.35:
            pts = 2
        elif freq >= 0.20:
            pts = 1
        else:
            pts = 0

        if pts > 0:
            score += pts
            # Libellé explicatif selon la clé
            if key == "rsi_zone":
                labels = {0:"<35 (survente)",1:"35-45 (bas)",2:"45-55 (neutre)",3:"55-65 (momentum)",4:">65 (élevé)"}
                reasons.append(f"RSI {labels.get(current_val,current_val)} présent dans {freq*100:.0f}% des pré-explosions (+{pts})")
            elif key == "vol_squeeze" and current_val:
                reasons.append(f"Squeeze de volatilité — présent dans {freq*100:.0f}% des pré-explosions (+{pts})")
            elif key == "dd_zone":
                labels = {0:"<20%",1:"20-40%",2:"40-60%",3:">60%"}
                reasons.append(f"Drawdown {labels.get(current_val,current_val)} — {freq*100:.0f}% des pré-explosions (+{pts})")
            elif key == "recent_7d_neg" and current_val:
                reasons.append(f"Dip récent ('dip before rip') — {freq*100:.0f}% des pré-explosions (+{pts})")
            elif key == "above_ma50":
                pos = "au-dessus" if current_val else "en-dessous"
                reasons.append(f"Prix {pos} MA50 — {freq*100:.0f}% des pré-explosions (+{pts})")
            elif pts >= 2:
                reasons.append(f"{label} conforme au profil ({freq*100:.0f}%, +{pts})")

    # ── RSI absolu : zone de construction 35-55 reste un bonus universel ──
    rsi_cur = current_ind.get("rsi")
    if rsi_cur and 35 <= rsi_cur <= 55:
        score += 1
        reasons.append(f"RSI {rsi_cur:.1f} — zone de momentum naissant")

    # ── Bonus tier (données marché : small caps explosent plus fort) ───────
    tier_bonus = {"Speculative": 2, "Mid": 1, "Etabli": 0}
    tb = tier_bonus.get(tier, 0)
    if tb:
        score += tb
        reasons.append(f"Tier {tier} — historiquement plus explosif (+{tb})")

    # ── Confiance du profil ────────────────────────────────────────────────
    # Quand peu d'observations, on réduit le score pour éviter les faux positifs
    if n_obs < 20:
        score = max(0, score - 2)
        reasons.append(f"(Profil peu fourni : {n_obs} obs — score réduit de 2)")

    return score, reasons


# ──────────────────── run principal ──────────────────────────────────────────

def run():
    LEARNING.mkdir(parents=True, exist_ok=True)

    # Charge le CSV de scores pour avoir tier, patterns, etc.
    # Note : 06_score.py écrit data/computed/scores.csv (sans date) et
    #        data/history/scores_{TODAY}.csv — on lit le fichier principal.
    scores_path = COMPUTED / "scores.csv"
    if not scores_path.exists():
        log.warning("Pas de scores.csv dans computed — explosion screen ignore")
        return

    with open(scores_path, encoding="utf-8") as f:
        score_rows = {r["symbol"]: r for r in csv.DictReader(f)}

    # ── Phase 1 : collecte des observations pré-explosion (tous tokens) ──
    all_observations_forte  = []
    all_observations_majeure = []
    processed = 0

    log.info("Phase 1 : collecte des explosions historiques...")
    for sym, row in score_rows.items():
        if row.get("suspect") == "True" or row.get("stablecoin") == "True":
            continue
        kd = cache_get("binance", f"klines_1d_{sym}", max_age_hours=24)
        if not kd: continue
        kd = kd.get("data", kd) if isinstance(kd, dict) else kd
        if len(kd) < 180: continue

        closes = [float(k[4]) for k in kd]
        vols   = [float(k[5]) for k in kd]
        tier   = row.get("tier", "Speculative")

        # Seuil adapté au tier
        thr_forte  = 0.25 if tier == "Etabli" else (0.35 if tier == "Mid" else 0.45)
        thr_majeure = 0.50 if tier == "Etabli" else (0.70 if tier == "Mid" else 1.00)

        obs_f = find_pre_explosion_states(closes, vols, threshold=thr_forte, window=30)
        obs_m = find_pre_explosion_states(closes, vols, threshold=thr_majeure, window=30)
        all_observations_forte  += obs_f
        all_observations_majeure += obs_m
        processed += 1
        if processed % 50 == 0:
            log.info(f"  {processed} tokens traites — {len(all_observations_forte)} obs forte")

    log.info(f"Phase 1 terminée : {len(all_observations_forte)} obs forte, "
             f"{len(all_observations_majeure)} obs majeure sur {processed} tokens")

    if len(all_observations_forte) < 10:
        log.warning("Pas assez d'observations historiques — ajuste les seuils ou attends plus de données")

    # ── Phase 2 : construction des profils ────────────────────────────────
    profile_forte  = build_profile(all_observations_forte)
    profile_majeure = build_profile(all_observations_majeure)

    profiles = {
        "forte":   profile_forte,
        "majeure": profile_majeure,
        "generated_date": TODAY,
        "n_tokens_analyzed": processed,
    }
    (LEARNING / "explosion_profile.json").write_text(
        json.dumps(profiles, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    log.info(f"Profils sauvés : forte n={profile_forte.get('n_observations',0)}, "
             f"majeure n={profile_majeure.get('n_observations',0)}")

    # ── Phase 3 : scoring prospectif ─────────────────────────────────────
    log.info("Phase 3 : scoring des candidats actuels...")
    candidates = []

    for sym, row in score_rows.items():
        if row.get("suspect") == "True" or row.get("stablecoin") == "True":
            continue
        kd = cache_get("binance", f"klines_1d_{sym}", max_age_hours=24)
        if not kd: continue
        kd = kd.get("data", kd) if isinstance(kd, dict) else kd
        if len(kd) < 50: continue

        closes = [float(k[4]) for k in kd]
        vols   = [float(k[5]) for k in kd]
        tier   = row.get("tier", "Speculative")

        # Indicateurs actuels
        ind = snapshot_indicators(closes, vols, len(closes) - 1)
        if not ind: continue

        score_f, reasons_f = score_explosion_candidate(ind, profile_forte, tier)
        score_m, reasons_m = score_explosion_candidate(ind, profile_majeure, tier)
        expl_score = max(score_f, score_m)

        # Bonus patterns — pondérés par les poids APPRIS (pas hardcodés)
        pat_weights = _load_pattern_weights()
        # Poids par défaut si pas encore de données (calibrés sur littérature)
        PAT_DEFAULTS = {
            "breakout_30d": 2.0, "golden_cross": 2.0, "bull_flag": 2.0,
            "double_bottom_90d": 1.5, "macd_bullish_cross": 1.5,
            "squeeze_breakout": 2.5,    # signal précoce fort : dormant → réveil + volume
            "uptrend": 1.0, "support_bounce": 1.0,
            "bullish_engulfing_4h": 0.8, "morning_star_4h": 0.8,
            "rsi_bullish_divergence": 1.2,
        }
        patterns_str = row.get("patterns", "")
        bonus_pats = []
        for pat, default_w in PAT_DEFAULTS.items():
            if pat not in patterns_str: continue
            # Poids appris si disponible, sinon défaut hardcodé
            learned_w = pat_weights.get(pat, default_w)
            pts = max(0, round(learned_w))
            if pts > 0:
                expl_score += pts
                label = pat.replace("_", " ")
                bonus_pats.append(f"{label} (w={learned_w:.1f})")

        all_reasons = reasons_f + bonus_pats
        expl_label = (
            "🔥 Fort"     if expl_score >= 9 else
            "⚡ Modéré"   if expl_score >= 6 else
            "👀 À surveiller" if expl_score >= 4 else
            ""
        )

        candidates.append({
            "symbol":        sym,
            "tier":          tier,
            "score_global":  row.get("score"),
            "explosion_score": expl_score,
            "explosion_label": expl_label,
            "rsi":           round(ind["rsi"], 1) if ind["rsi"] else "",
            "vol_ratio":     round(ind["vol_ratio"], 2),
            "vol_squeeze":   ind["vol_squeeze"],
            "dd_pct":        round(ind["dd"] * 100, 1),
            "above_ma50":    ind["above_ma50"],
            "above_ma200":   ind["above_ma200"],
            "reasons":       " | ".join(all_reasons[:5]),
            "patterns":      patterns_str,
        })

    candidates.sort(key=lambda x: -x["explosion_score"])

    # Sauvegarde CSV candidats
    out_path = COMPUTED / f"explosion_candidates_{TODAY}.csv"
    if candidates:
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(candidates[0].keys()))
            w.writeheader(); w.writerows(candidates)
    log.info(f"Candidats explosion : {len([c for c in candidates if c['explosion_score']>=6])} forts, "
             f"{len([c for c in candidates if 4<=c['explosion_score']<6])} modérés — {out_path}")

    # Ajoute explosion_score au CSV de scores principal
    _merge_explosion_into_scores(score_rows, candidates, scores_path)

    return candidates


def _merge_explosion_into_scores(score_rows, candidates, scores_path):
    """Ajoute la colonne explosion_score au CSV de scores existant."""
    try:
        expl_map = {c["symbol"]: c for c in candidates}
        with open(scores_path, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
            fieldnames = rows[0].keys() if rows else []

        # Ajoute colonnes si absentes
        for r in rows:
            c = expl_map.get(r["symbol"], {})
            r["explosion_score"] = c.get("explosion_score", 0)
            r["explosion_label"] = c.get("explosion_label", "")

        all_fields = list(fieldnames)
        if "explosion_score" not in all_fields: all_fields += ["explosion_score", "explosion_label"]

        with open(scores_path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=all_fields, extrasaction="ignore")
            w.writeheader(); w.writerows(rows)
    except Exception as e:
        log.warning(f"Merge explosion scores: {e}")


if __name__ == "__main__":
    run()
