"""Orchestrateur : exécute l'intégralité du pipeline.

Usage :
    python run_pipeline.py                    # run complet
    python run_pipeline.py --pilot 30         # pilote 30 tokens
    python run_pipeline.py --pilot 30 --no-cg-detail  # pilote rapide sans détails CG
    python run_pipeline.py --skip-fetch       # recalcule depuis cache
"""
import sys, os, importlib, argparse, time, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import setup_logger, purge_old_raw, cache_get, cache_put
log = setup_logger("pipeline")

ERRORS = []

def step(name, fn):
    try:
        log.info(f"--- Etape : {name} ---")
        fn()
    except Exception as e:
        msg = f"[ERREUR] Etape '{name}' : {e}\n{traceback.format_exc()}"
        log.error(msg)
        ERRORS.append(msg)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", type=int, default=0)
    ap.add_argument("--skip-fetch", action="store_true")
    ap.add_argument("--no-cg-detail", action="store_true",
                    help="Saute les appels CG detail (plus rapide, tier depuis markets seulement)")
    args = ap.parse_args()

    t0 = time.time()
    log.info(f"=== Pipeline start (pilot={args.pilot}, skip_fetch={args.skip_fetch}, no_cg_detail={args.no_cg_detail}) ===")

    # --- 01 Univers Binance ---
    if not args.skip_fetch:
        u = importlib.import_module("01_fetch_universe")
        step("fetch_universe", u.fetch)

    universe = cache_get("binance", "universe", 24)
    if not universe:
        log.error("Pas d'univers en cache. Abandon."); return
    universe = universe.get("data", universe) if isinstance(universe, dict) else universe

    syms = [x["symbol"] for x in universe]
    # BTCUSDT toujours en premier (référence corrélation BTC)
    syms = ["BTCUSDT"] + [s for s in syms if s != "BTCUSDT"]
    if args.pilot > 0:
        syms = syms[:args.pilot]
    log.info(f"Pipeline sur {len(syms)} symboles : {syms[:5]}...")

    # --- 02 Klines ---
    if not args.skip_fetch:
        k = importlib.import_module("02_fetch_klines")
        step("fetch_klines", lambda: k.fetch_for_symbols(syms))

    # --- 03 CoinGecko markets (classement tiers) ---
    markets = []
    if not args.skip_fetch:
        cg = importlib.import_module("03_fetch_coingecko")
        def do_cg():
            nonlocal markets
            markets = cg.fetch_markets_top1000()
            mapping = cg.map_binance_to_cg(
                [u for u in universe if u["symbol"] in syms], markets
            )
            cg_map_to_save = {s: (mapping.get(s) or {}).get("id") for s in syms}
            cache_put("coingecko", "binance_to_cg_map", cg_map_to_save)
            log.info(f"CG map sauvegardee : {sum(1 for v in cg_map_to_save.values() if v)}/{len(syms)} tokens mappes")
        step("fetch_cg_markets", do_cg)

    # Charge markets depuis cache si vide
    if not markets:
        c = cache_get("coingecko", "markets_top1000", 24*7)
        markets = (c.get("data", c) if isinstance(c, dict) else c) or []
        if markets:
            log.info(f"Markets depuis cache : {len(markets)} coins")

    # --- 03b CoinGecko details (optionnel, lent) ---
    if not args.skip_fetch and not args.no_cg_detail and markets:
        cg = importlib.import_module("03_fetch_coingecko")
        cg_map_c = cache_get("coingecko", "binance_to_cg_map", 24*7)
        cg_map = (cg_map_c.get("data", cg_map_c) if isinstance(cg_map_c, dict) else cg_map_c) or {}
        ok_d = 0
        for i, s in enumerate(syms, 1):
            cid = cg_map.get(s)
            if cid:
                try: cg.fetch_detail(cid); ok_d += 1
                except Exception as e: log.warning(f"detail {s}: {e}")
            if i % 10 == 0:
                log.info(f"  CG detail: {i}/{len(syms)} ok={ok_d}")
        log.info(f"CG details : {ok_d}/{len(syms)} ok")

        # --- 04 Project info (GitHub + red flags) ---
        pi = importlib.import_module("04_fetch_project_info")
        cg_map_c2 = cache_get("coingecko", "binance_to_cg_map", 24*7)
        cg_map2 = (cg_map_c2.get("data", cg_map_c2) if isinstance(cg_map_c2, dict) else cg_map_c2) or {}
        ok_e = 0
        for s in syms:
            cid = cg_map2.get(s)
            if cid:
                try: pi.enrich_for_token(s, cid); ok_e += 1
                except Exception as e: log.warning(f"enrich {s}: {e}")
        log.info(f"Project enrich : {ok_e}/{len(syms)}")

    # --- 11 TVL DefiLlama (optionnel, pas bloquant) ---
    if not args.skip_fetch:
        try:
            defi = importlib.import_module("11_fetch_defi")
            step("fetch_defi_tvl", lambda: defi.run(syms))
        except Exception as e:
            log.warning(f"11_fetch_defi ignoré : {e}")

    # --- 05 Indicateurs techniques ---
    ind = importlib.import_module("05_compute_indicators")
    step("compute_indicators", lambda: ind.run(syms))

    # --- 10 Catalyseurs (Fear&Greed, Trending, Volume spikes, GitHub spikes) ---
    cat = importlib.import_module("10_fetch_catalysts")
    step("fetch_catalysts", cat.run)

    # --- 06 Scoring (lit catalysts.json produit à l'étape 10) ---
    sc = importlib.import_module("06_score")
    step("score", sc.run)

    # --- 09 Explosion screen (avant le report pour enrichir le CSV) ---
    expl = importlib.import_module("09_explosion_screen")
    step("explosion_screen", expl.run)

    # --- 09b Score Explosif — modele separe sans biais fondamental ---
    expl2 = importlib.import_module("09b_score_explosive")
    step("score_explosive", expl2.run)

    # --- 07 Report ---
    rep = importlib.import_module("07_report")
    step("report", rep.main)

    # --- 08 Apprentissage adaptatif des patterns ---
    lrn = importlib.import_module("08_learn")
    step("learn", lrn.run)

    # --- 12 Historique des scores (30 derniers jours) ---
    hist = importlib.import_module("12_build_history")
    step("build_history", hist.run)

    # Purge raw > 30j
    try:
        purged = purge_old_raw(days=30)
        log.info(f"Purge raw >30j : {purged} fichiers")
    except Exception: pass

    elapsed = time.time() - t0
    if ERRORS:
        log.warning(f"Pipeline termine avec {len(ERRORS)} erreur(s) en {elapsed:.1f}s")
        for e 