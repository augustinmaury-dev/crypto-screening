# Rapport hebdomadaire — Performance des patterns techniques

**Date :** 1er mai 2026 (vendredi)

---

## Statut : Apprentissage en cours — pas encore assez de données

Les fichiers requis pour produire ce rapport n'existent pas encore :

- `data/learning/pattern_weights.json` — **absent**
- `data/learning/outcomes.csv` — **absent**

Le dossier `data/learning/` n'a pas encore été créé, ce qui indique que le pipeline d'apprentissage adaptatif (collecte des outcomes et mise à jour des poids) n'a pas encore été exécuté.

### Ce qu'il faut pour que ce rapport fonctionne

1. **Créer le dossier** `data/learning/` dans le projet crypto-screening
2. **Mettre en place un script** qui, après chaque run du pipeline quotidien :
   - Enregistre les patterns détectés et leur résultat (return à J+14) dans `outcomes.csv`
   - Calcule et met à jour les poids adaptatifs dans `pattern_weights.json`
3. **Attendre au minimum 5 jours de run quotidien** pour avoir assez d'observations

Une fois ces fichiers alimentés, ce rapport hebdomadaire pourra produire les tableaux de fiabilité des patterns, les évolutions de poids, et la synthèse.

---

*Ce rapport est purement informatif sur des indicateurs passés. Ce n'est pas un conseil financier.*
