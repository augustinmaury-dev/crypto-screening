# Auto-revue — 2026-05-01

## Résumé exécutif

Le système de screening fonctionne mais présente plusieurs anomalies structurelles. Le pattern `double_bottom_90d` est sur-détecté (présent chez ~50% des tokens dans les top listes), ce qui dilue fortement son pouvoir discriminant. Deux stablecoins (USDEUSDT, RLUSDUSDT) apparaissent dans le top 20 Etabli malgré la fonction `is_stablecoin` — probable désynchronisation entre le code actuel et le dernier rapport (daté du 18 avril). Le fichier `outcomes.csv` n'existe pas encore : aucune analyse de performance réelle n'est possible. Cette revue se concentre donc sur l'analyse structurelle.

## Problèmes identifiés

🔴 **1. `double_bottom_90d` sur-représenté — perte de pouvoir discriminant**
Dans les top 20 par tier : 6/20 Etabli (30%), 7/20 Mid (35%), 13/20 Speculative (65%). Ce pattern est détecté sur la majorité des tokens spéculatifs. Un pattern présent chez >30% des tokens est du bruit, pas un signal. Cause probable : `swing_lows(w, order=7)` avec `tol=0.02` et `recovery>0.10` reste trop permissif — dans un marché volatile, presque tout token a deux creux proches sur 90 jours.

🔴 **2. Stablecoins dans le classement principal**
USDEUSDT est #1 Etabli (score 76.7) et RLUSDUSDT est #18 (score 64.3). Les deux sont dans la liste `known` de `is_stablecoin()`. La fonction existe dans `06_score.py` (ligne 169-183) et le tri les pousse en bas (ligne 282). Hypothèse : le rapport `report.md` a été généré avant l'ajout de cette logique, ou le script de génération du rapport (`07_report.py` ou similaire) ne filtre pas le flag `stablecoin`. **Ce problème fausse le classement entier du tier Etabli.**

🟡 **3. ARPAUSDT cumule `double_bottom_90d` ET `double_top_90d`**
Le code actuel de `05_compute_indicators.py` (lignes 447-451) empêche explicitement cette combinaison (`if has_db and not has_dt`). Mais ARPAUSDT l'affiche dans le rapport. Cela confirme que le rapport du 18 avril a été généré avec une version antérieure du code. **Action : re-générer le rapport avec le code actuel pour vérifier la correction.**

🟡 **4. `double_bottom_90d` + `downtrend` = contradiction fréquente**
Tokens concernés : FILUSDT, APTUSDT, ICPUSDT, FLOKIUSDT. Un double fond dans une tendance baissière structurelle (LH+LL) est un signal de renversement prématuré. Le score_signal les traite comme +1 bull + -1 bear = neutre, ce qui est correct arithmétiquement, mais le double_bottom booste le score_signal à tort puisque la structure de tendance est encore baissière.

🟡 **5. Signaux MACD contradictoires sur USDEUSDT**
USDEUSDT affiche `macd_bullish_cross` ET `macd_bearish_cross` simultanément. Le code actuel (lignes 438-441) devrait empêcher cela. Même cause que le problème #3 — rapport généré avec ancien code. Mais au-delà, détecter des croisements MACD sur un stablecoin est fondamentalement absurde (les variations de prix sont du bruit de 0.01%).

🟢 **6. Absence de données d'apprentissage**
`outcomes.csv` et `pattern_weights.json` n'existent pas. Tous les poids de patterns sont à 1.0 (défaut), et les poids de formule sont les défauts (solidity 20%, momentum 30%, risk 15%, antiscam 20%, signal 15%). Le système d'apprentissage (`08_learn.py`) n'a pas encore de matière première.

## Performance des patterns

**Pas de données d'outcomes disponibles.** Analyse structurelle à la place :

| Pattern | Fréquence estimée (top 60) | Pouvoir discriminant | Verdict |
|---|---|---|---|
| `double_bottom_90d` | ~43% (26/60) | 🔴 Très faible | Sur-détecté, seuils à resserrer |
| `uptrend` | ~25% (15/60) | 🟡 Modéré | Acceptable mais à surveiller |
| `macd_bullish_cross` | ~18% (11/60) | 🟢 Correct | Fenêtre 5j est raisonnable |
| `doji_4h` | ~12% (7/60) | 🟡 Faible seul | OK comme confirmation, pas comme signal primaire |
| `downtrend` | ~10% (6/60) | 🟢 Correct | Bien calibré |
| `double_top_90d` | ~8% (5/60) | 🟢 Correct | Seuils OK |
| `breakout_30d` | ~5% (3/60) | 🟢 Correct | Filtre volume 1.5x fonctionne |

## Propositions de correction (triées par priorité)

### 1. 🔴 Resserrer `pat_double_bottom` — PRIORITÉ HAUTE

**Problème :** Détecté chez ~43% des tokens, donc inutile comme signal.

**Correction proposée dans `05_compute_indicators.py` :**
```python
# pat_double_bottom() — ligne 188
# Changer :
def pat_double_bottom(lows, closes, tol=0.02, window=90):
# En :
def pat_double_bottom(lows, closes, tol=0.015, window=90):
```
ET dans le corps de la fonction :
```python
# Ligne 199 — changer la séparation minimale :
if i2 - i1 < 10: return False
# En :
if i2 - i1 < 15: return False

# Ligne 204 — changer le seuil de reprise :
recovery = (mid_high - min(l1, l2)) / min(l1, l2) > 0.10
# En :
recovery = (mid_high - min(l1, l2)) / min(l1, l2) > 0.15
```

**Effet attendu :** Réduire la détection de ~43% à ~15-20% des tokens, en ne gardant que les vrais doubles fonds (creux bien définis, séparés, avec vraie reprise entre les deux).

### 2. 🔴 Vérifier que le rapport filtre les stablecoins

**Problème :** USDEUSDT et RLUSDUSDT dans le classement malgré `is_stablecoin`.

**Correction :** Vérifier le script de génération du rapport (probablement `07_report.py` ou similaire). Chercher si le flag `stablecoin` est utilisé pour filtrer les tokens affichés dans les tableaux de top 20. Si non, ajouter :
```python
# Dans la boucle qui génère les top 20 par tier :
rows_tier = [r for r in rows_tier if not r.get("stablecoin")]
```

### 3. 🟡 Pénaliser la combinaison `double_bottom_90d` + `downtrend`

**Problème :** Un double fond dans une tendance baissière structurelle est un signal prématuré.

**Correction proposée dans `06_score.py`, fonction `score_signal()` :**
```python
# Après la ligne 131 (calcul de w_bull) :
# Réduire le poids du double_bottom si downtrend est aussi présent
if "double_bottom_90d" in patterns and "downtrend" in patterns:
    w_bull -= weights.get("double_bottom_90d", 1.0) * 0.5  # demi-poids seulement
```

**Effet attendu :** Les tokens avec double_bottom + downtrend auront un score_signal plus conservateur, évitant les faux signaux haussiers.

### 4. 🟡 Exclure les patterns sur stablecoins en amont

**Problème :** USDEUSDT génère des patterns techniques (MACD cross, support/resistance) qui sont du pur bruit sur un actif à 0.01% de variation.

**Correction proposée dans `05_compute_indicators.py`, fonction `compute_for_symbol()` :**
```python
# Après la ligne 402 (opens, closes, highs, lows, vols = ...) :
# Skip technique patterns pour stablecoins (vol < 3% annualisée)
vol_check = realized_vol_30d(closes)
if vol_check is not None and vol_check < 0.05:
    return {
        "symbol": symbol, "price": closes[-1],
        "rsi_14": rsi_val(closes), "macd": None, "macd_signal": None,
        "macd_hist": None, "ma_20": sma(closes, 20), "ma_50": sma(closes, 50),
        "ma_200": sma(closes, 200), "vol_30d_annualized": vol_check,
        "drawdown_90d": drawdown_90d(closes)[0],
        "distance_to_90d_high": drawdown_90d(closes)[1],
        "vol_ratio_vs_med90": None, "corr_btc_90d": None,
        "support_90d": closes[-1], "resistance_90d": closes[-1],
        "patterns": [], "bull_signals": 0, "bear_signals": 0,
        "bias": "neutre", "n_days_history": len(closes),
    }
```

### 5. 🟢 Re-générer le rapport avec le code corrigé

**Action :** Relancer le pipeline complet pour produire un rapport à jour. Le rapport actuel date du 18 avril (13 jours) et a été généré avec une version antérieure du code (preuve : ARPAUSDT avec double_bottom + double_top simultanés, USDEUSDT avec double MACD cross). Plusieurs corrections (filtrage des signaux contradictoires) sont déjà dans le code mais pas reflétées dans le dernier rapport.

## À valider par l'utilisateur avant implémentation

1. **Resserrer `double_bottom` :** tol 0.02→0.015, séparation 10→15, recovery 0.10→0.15. Risque : manquer quelques vrais doubles fonds. Gain : éliminer ~60% des faux positifs.
2. **Pénaliser double_bottom + downtrend :** réduction de 50% du poids. Alternative : ignorer complètement le double_bottom si downtrend est présent (plus agressif).
3. **Skip patterns sur stablecoins :** seuil à vol < 5% annualisée. Vérifier que ça ne capture pas des tokens légitimes à faible volatilité temporaire.
4. **Re-run du pipeline** pour avoir un rapport à jour reflétant le code actuel.

---
_Prochaine revue automatique prévue lundi prochain. Les données d'outcomes commenceront à s'accumuler si le pipeline tourne régulièrement, permettant une analyse quantitative réelle._
