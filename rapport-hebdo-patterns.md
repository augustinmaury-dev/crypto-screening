# Rapport hebdomadaire — Performance des patterns techniques

**Date :** 11 mai 2026 (lundi)
**Période d'apprentissage :** 15 jours (du 18 avril au 3 mai 2026)
**Observations totales :** 2 886 (dont 1 120 à horizon 14 jours)

> Ce rapport est purement informatif sur des indicateurs passés. Ce n'est pas un conseil financier.

---

## 📊 Patterns les plus fiables (hit rate 14j)

Patterns avec ≥ 5 observations, triés par hit rate décroissant :

| Pattern | Direction | Poids actuel | Hit rate 14j | Nb obs. |
|---|---|---|---|---|
| evening_star_4h | Bear | 2.429 | **85.7%** | 7 |
| macd_bearish_cross | Bear | 2.268 | **81.7%** | 71 |
| rsi_bearish_divergence | Bear | 1.667 | **66.7%** | 15 |
| double_top_90d | Bear | 1.441 | **61.0%** | 118 |
| downtrend | Bear | 1.359 | **59.0%** | 217 |

Constat marquant : les cinq patterns les plus fiables sont tous baissiers. Le système a appris pendant une phase de marché majoritairement défavorable (score macro entre -2 et +2), ce qui explique ce biais. Les patterns haussiers n'ont pas encore prouvé leur valeur sur cette fenêtre.

---

## 📈 Patterns à surveiller cette semaine

Croisement entre les patterns les plus fiables et les tokens bien scorés du dernier report (3 mai 2026) :

| Pattern fiable | Tokens concernés (score ≥ 65) | Implication |
|---|---|---|
| **evening_star_4h** (85.7%) | LUNCUSDT (71.4), LPTUSDT (66.3), LUNAUSDT (74.1) | Signal baissier fort sur ces tokens malgré leur bon score |
| **macd_bearish_cross** (81.7%) | ALGOUSDT (75.5), JSTUSDT (72.0), SKYUSDT (69.2), SUSHIUSDT (69.4), CYBERUSDT (73.0), LTCUSDT (65.3), OPENUSDT (69.2), NEWTUSDT (67.4) | Nombreux tokens bien scorés portent ce signal |
| **double_top_90d** (61.0%) | ONDOUSDT (67.5), SUSHIUSDT (69.4), LPTUSDT (66.3) | Confirmation de retournement potentiel |
| **rsi_bearish_divergence** (66.7%) | TRXUSDT (78.2) — le #1 Etabli | Divergence sur le token le mieux scoré du tier Etabli |

---

## 🔄 Évolution depuis la semaine dernière

C'est le premier rapport avec données réelles (le précédent du 1er mai signalait l'absence des fichiers). L'évolution des poids par rapport au défaut (1.0) montre les ajustements les plus forts du système :

| Pattern | Poids | Δ vs défaut | Sens de l'ajustement |
|---|---|---|---|
| evening_star_4h | 2.429 | **+1.43** | Fortement renforcé |
| macd_bearish_cross | 2.268 | **+1.27** | Fortement renforcé |
| breakout_30d | 0.100 | **-0.90** | Quasiment neutralisé |
| support_bounce | 0.100 | **-0.90** | Quasiment neutralisé |
| rsi_bullish_divergence | 0.100 | **-0.90** | Quasiment neutralisé |
| resistance_test | 0.277 | **-0.72** | Très affaibli |
| rsi_bearish_divergence | 1.667 | **+0.67** | Renforcé |
| double_top_90d | 1.441 | **+0.44** | Renforcé |

Le système a clairement séparé les patterns en deux camps : les patterns baissiers ont été renforcés, les patterns haussiers ont été pénalisés.

---

## 📉 Patterns peu fiables (à pondérer moins)

Patterns avec hit rate < 50% et ≥ 5 observations — ceux qui prédisent mal sur cette fenêtre :

| Pattern | Direction | Poids actuel | Hit rate 14j | Nb obs. |
|---|---|---|---|---|
| breakout_30d | Bull | 0.100 | **11.4%** | 44 |
| support_bounce | Bull | 0.100 | **17.6%** | 17 |
| rsi_bullish_divergence | Bull | 0.100 | **20.0%** | 10 |
| resistance_test | Bear | 0.277 | **31.9%** | 47 |
| bullish_engulfing_4h | Bull | 0.600 | **40.0%** | 20 |
| double_bottom_90d | Bull | 0.656 | **41.4%** | 256 |
| uptrend | Bull | 0.731 | **43.3%** | 171 |
| macd_bullish_cross | Bull | 0.761 | **44.0%** | 109 |

À noter : resistance_test (bear) sous-performe aussi, malgré sa direction baissière. Les 3 patterns au plancher (poids = 0.10) sont effectivement les moins prédictifs.

---

## 📌 Synthèse

Les patterns baissiers (evening_star_4h, macd_bearish_cross, rsi_bearish_divergence, double_top_90d) sont actuellement les seuls à dépasser 50% de fiabilité sur 15 jours d'apprentissage — aucun pattern haussier n'a encore prouvé sa valeur dans les conditions de marché récentes. Le système apprend depuis **15 jours** ; la robustesse des conclusions augmentera avec le temps, en particulier lorsque le marché traversera une phase haussière.

---

*Prochain rapport : lundi 18 mai 2026.*
