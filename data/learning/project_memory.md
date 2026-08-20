# Mémoire du Projet Crypto Screening
*Dernière mise à jour : 20 août 2026*

---

## Qui je suis

Je suis un système de screening automatique qui analyse chaque matin les marchés crypto.
Je collecte des données de prix, volume et indicateurs techniques sur plusieurs centaines de tokens.
Je détecte des patterns chartistes (golden_cross, bear_flag, squeeze_breakout, etc.)
et calcule pour chaque token un `score` = probabilité estimée de hausse sur 7 jours (`bull_prob_7d`).
J'apprends chaque jour en mesurant si mes prédictions passées étaient correctes.

---

## Mon auto-évaluation

**Régime de marché (BTC bull_prob) :** 🟢 Haussier — 64%

**Signaux haussiers fiables (>50%) :** aucun ❌
  → Meilleur signal haussier actuel : `rsi_bullish_divergence` à 36.5%
**Signaux baissiers fiables (>50%) :** 11 / 11

### ❌ Mes signaux d'ACHAT ne sont PAS encore fiables.
N'agis pas sur mes recommandations d'achat sans vérification supplémentaire.

---

## Ce que j'ai appris sur les patterns

### Signaux baissiers (>50% = le signal prédit correctement la baisse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `bear_flag` | 82.1% | 324 | 📉 |
| `double_top_90d` | 74.7% | 2492 | → |
| `rsi_bearish_divergence` | 74.6% | 493 | → |
| `shooting_star_4h` | 73.7% | 179 | → |
| `downtrend` | 68.8% | 12325 | → |
| `bearish_engulfing_4h` | 65.5% | 583 | → |
| `evening_star_4h` | 63.4% | 554 | → |
| `macd_bearish_cross` | 61.7% | 4757 | → |
| `breakdown_30d` | 61.4% | 88 | → |
| `death_cross` | 59.6% | 265 | → |
| `resistance_test` | 54.9% | 1135 | → |

### Signaux haussiers (>50% = le signal prédit correctement la hausse)

| Pattern | Hit rate | Échantillons | Tendance |
|---------|----------|--------------|---------|
| `rsi_bullish_divergence` | 36.5% | 2039 | → |
| `support_bounce` | 32.1% | 1789 | → |
| `bullish_engulfing_4h` | 31.8% | 746 | → |
| `golden_cross` | 29.9% | 321 | → |
| `hammer_4h` | 29.6% | 162 | → |
| `bull_flag` | 29.1% | 110 | → |
| `double_bottom_90d` | 28.9% | 1638 | → |
| `uptrend` | 27.3% | 6172 | → |
| `morning_star_4h` | 26.3% | 627 | → |
| `squeeze_breakout` | 26.1% | 134 | → |
| `macd_bullish_cross` | 23.9% | 5552 | → |
| `breakout_30d` | 15.9% | 201 | → |

---

## Mes prédictions passées et leurs résultats

*Aucune prédiction mesurée pour l'instant (14 jours de recul nécessaires).*

**19 prédictions en attente de résultat (< 14 jours) :**

| Date | Token | Score | Prix |
|------|-------|-------|------|
| 20 août 2026 | **PLUME** | 75% | 0.01261 |
| 20 août 2026 | **TRUMP** | 74% | 1.642 |
| 20 août 2026 | **XEC** | 73% | 6.95e-06 |
| 20 août 2026 | **MET** | 70% | 0.219 |
| 20 août 2026 | **ACE** | 70% | 0.1884 |
| 20 août 2026 | **EURI** | 70% | 1.1693 |
| 19 août 2026 | **GNO** | 74% | 114.45 |
| 19 août 2026 | **ACE** | 71% | 0.2266 |
| 19 août 2026 | **GPS** | 70% | 0.01236 |
| 19 août 2026 | **ALPINE** | 70% | 0.337 |
| 19 août 2026 | **ACM** | 70% | 0.288 |
| 19 août 2026 | **USDE** | 76% | 1.0005 |
| 19 août 2026 | **EURI** | 74% | 1.1601 |
| 19 août 2026 | **XUSD** | 70% | 1.0009 |
| 18 août 2026 | **ACE** | 77% | 0.1958 |

---

## Le score composite est-il utile ?

J'ai analysé **24093 paires (date, token)** pour mesurer si mon score composite prédit les returns à 14j.

| Sous-score | Corrélation avec return 14j |
|------------|---------------------------|
| solidity | 0.0002 |
| momentum | 0.0000 |
| risk | 0.0000 |
| antiscam | 0.0000 |
| signal | 0.0000 |

**Verdict : corrélations toutes proches de zéro. Le score composite ne prédit PAS les returns.**
C'est pourquoi j'utilise `bull_prob_7d` comme score principal.

---

## Aujourd'hui — 20 août 2026

**Régime :** 🟢 Haussier (BTC bull_prob = 64%)

**Top tokens aujourd'hui (score ≥ 70%) :**

| Token | Score | Alpha vs BTC | Exit risk | Catalyseurs |
|-------|-------|--------------|-----------|-------------|
| **PLUME** | 75% | +17pp | 0 | ⚡ Volume ×27.8 vs médiane |
| **TRUMP** | 74% | +16pp | 0 | ⚡ Volume ×3.1 vs médiane |
| **XEC** | 73% | +15pp | 0 | ⚡ Volume ×3.9 vs médiane |
| **MET** | 70% | +12pp | ⚠️ 4 | ⚡ Volume ×5.9 vs médiane |
| **ACE** | 70% | +12pp | 0 | ⚡ Volume ×3.2 vs médiane |
| **EURI** | 70% | +12pp | ⚠️ 4 | ⚡ Volume ×5.6 vs médiane |
