# 📝 Commandes Git pour GitHub

## 🚀 Initialisation Complète

### Option 1: Utiliser le script automatique

```bash
# Exécuter le script batch
init-git.bat
```

### Option 2: Commandes manuelles

```bash
# 1. Aller dans le dossier du projet
cd C:\wamp64\www\Ceremac-Site

# 2. Initialiser Git
git init

# 3. Vérifier ce qui sera commité
git status

# 4. Ajouter tous les fichiers
git add .

# 5. Vérifier à nouveau (important!)
git status

# 6. Premier commit
git commit -m "Initial commit: Site CEREMAC Django"

# 7. Créer le repository sur GitHub, puis:
git remote add origin https://github.com/VOTRE-USERNAME/ceremac-site.git
git branch -M main
git push -u origin main
```

## ✅ Vérifications Importantes

### Avant le commit, vérifiez que ces fichiers NE sont PAS listés:

```bash
git status
```

**DOIVENT être ignorés:**
- `django_migration/.env`
- `django_migration/db.sqlite3`
- `django_migration/venv/`
- `django_migration/__pycache__/`
- `django_migration/staticfiles/`

Si un de ces fichiers apparaît, vérifiez le `.gitignore`.

## 🔄 Commandes Utiles

```bash
# Voir les fichiers ignorés
git status --ignored

# Voir les différences
git diff

# Annuler un fichier ajouté par erreur
git reset HEAD fichier.py

# Voir l'historique
git log --oneline

# Changer le message du dernier commit
git commit --amend -m "Nouveau message"
```

## 📤 Push sur GitHub

```bash
# Ajouter le remote (remplacer VOTRE-USERNAME)
git remote add origin https://github.com/VOTRE-USERNAME/ceremac-site.git

# Vérifier le remote
git remote -v

# Push vers GitHub
git branch -M main
git push -u origin main
```

## 🔐 Sécurité

**NE JAMAIS COMMITER:**
- `.env` (contient SECRET_KEY)
- `db.sqlite3` (base de données)
- `venv/` (environnement virtuel)

**UTILISER:**
- `.env.example` comme template
- Documentation pour la configuration

