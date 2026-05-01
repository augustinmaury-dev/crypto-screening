# Mise en ligne — Pipeline autonome + Dashboard web

## Ce que ça fait une fois en place

- Le pipeline tourne **tous les jours à 9h (Paris)** dans le cloud GitHub, sans que ton PC soit allumé
- Le dashboard est accessible via une **URL permanente** (ex: `https://tonpseudo.github.io/crypto-screening/`)
- Tu ouvres juste le site — les données sont déjà là, mises à jour automatiquement

---

## Étapes (une seule fois)

### 1. Créer un compte GitHub (si pas encore fait)
→ https://github.com/signup (gratuit)

### 2. Créer un dépôt (repository)

1. Va sur https://github.com/new
2. Nom : `crypto-screening` (ou ce que tu veux)
3. Visibilité : **Public** (nécessaire pour GitHub Pages gratuit)
4. Ne coche rien d'autre → clique **Create repository**

### 3. Envoyer les fichiers

Ouvre un terminal (cmd ou PowerShell) dans le dossier `crypto-screening` et tape :

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/TONPSEUDO/crypto-screening.git
git push -u origin main
```

> Remplace `TONPSEUDO` par ton nom d'utilisateur GitHub.

### 4. Activer GitHub Pages (le site web)

1. Va sur ton dépôt GitHub → **Settings** → **Pages**
2. Source : `Deploy from a branch`
3. Branch : `main` / `/ (root)`
4. Clique **Save**

Après 1-2 minutes, ton dashboard est en ligne à :
```
https://TONPSEUDO.github.io/crypto-screening/dashboard.html
```

### 5. Vérifier que le pipeline automatique est actif

1. Va sur ton dépôt → onglet **Actions**
2. Tu dois voir le workflow `Crypto Screening Pipeline`
3. Clique **Run workflow** pour tester manuellement une première fois
4. Si tout est vert ✅ → le pipeline tournera tout seul chaque matin

---

## Fonctionnement quotidien

```
Chaque jour à 9h (Paris) :
  GitHub Actions démarre automatiquement
    → Télécharge les données Binance + CoinGecko
    → Calcule les scores (434 tokens)
    → Met à jour scores.csv, report.md, data/history/
    → S'améliore via le système d'apprentissage (08_learn.py)
    → Commit et push dans le repo

Toi, quand tu veux :
  → Ouvre dashboard.html (URL GitHub Pages)
  → Les données du jour se chargent automatiquement
  → Clique ↻ Rafraîchir si tu veux forcer le rechargement
```

---

## Résolution de problèmes

**Le pipeline échoue (croix rouge dans Actions) :**
- Clique sur le run → lis les logs → c'est souvent un rate limit API temporaire
- Relance manuellement le lendemain

**Les données ont plus d'un jour :**
- Va dans Actions → lance manuellement `Run workflow`

**Le dashboard charge mais est vide :**
- Vérifie que `data/computed/scores.csv` existe dans le repo
- Attends la fin du premier run manuel
