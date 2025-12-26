# Guide de Configuration pour GitHub

## ✅ Fichiers Créés pour GitHub

- ✅ `.gitignore` - Ignore les fichiers sensibles et temporaires
- ✅ `README.md` - Documentation complète du projet
- ✅ `requirements.txt` - Dépendances Python
- ✅ `.env.example` - Exemple de configuration (sans secrets)

## 📋 Avant de Push sur GitHub

### 1. Vérifier que les fichiers sensibles sont ignorés

```bash
# Vérifier que .env n'est pas tracké
git status
```

Les fichiers suivants NE DOIVENT PAS être commités:
- ❌ `.env` (contient les secrets)
- ❌ `db.sqlite3` (base de données locale)
- ❌ `venv/` (environnement virtuel)
- ❌ `__pycache__/` (fichiers Python compilés)
- ❌ `staticfiles/` (fichiers statiques compilés)
- ❌ `*.pyc` (fichiers compilés)

### 2. Initialiser Git (si pas déjà fait)

```bash
cd django_migration
git init
```

### 3. Ajouter les fichiers

```bash
git add .
git status  # Vérifier ce qui sera commité
```

### 4. Premier commit

```bash
git commit -m "Initial commit: Site CEREMAC Django"
```

### 5. Créer le repository sur GitHub

1. Aller sur https://github.com
2. Créer un nouveau repository
3. Ne PAS initialiser avec README (on en a déjà un)

### 6. Lier et push

```bash
git remote add origin https://github.com/votre-username/ceremac-site.git
git branch -M main
git push -u origin main
```

## 🔒 Sécurité

⚠️ **IMPORTANT**: 
- Ne JAMAIS commiter le fichier `.env`
- Ne JAMAIS commiter les mots de passe ou clés secrètes
- Utiliser `.env.example` comme template
- Vérifier `git status` avant chaque commit

## 📁 Structure Recommandée sur GitHub

```
ceremac-site/
├── django_migration/      # Projet Django principal
│   ├── ceremac_site/
│   ├── main/
│   ├── admin_panel/
│   ├── members/
│   ├── templates/
│   ├── static/
│   ├── requirements.txt
│   ├── manage.py
│   ├── README.md
│   └── .gitignore
├── assets/               # Fichiers statiques originaux
├── database.sql          # Structure de base de données
└── README.md            # README principal
```

## 🚀 Après le Push

1. Ajouter une description au repository GitHub
2. Ajouter des tags si nécessaire
3. Configurer les secrets dans GitHub Actions (si CI/CD)
4. Ajouter un fichier LICENSE si nécessaire

## 📝 Commandes Git Utiles

```bash
# Voir les fichiers ignorés
git status --ignored

# Voir ce qui sera commité
git status

# Ajouter un fichier spécifique
git add fichier.py

# Voir les différences
git diff

# Annuler un fichier ajouté par erreur
git reset HEAD fichier.py
```

