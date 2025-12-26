# 🚀 Initialiser Git et Push sur GitHub

## 📋 Étapes pour Mettre le Projet sur GitHub

### 1. Initialiser Git

```bash
cd C:\wamp64\www\Ceremac-Site
git init
```

### 2. Vérifier les Fichiers à Ignorer

```bash
git status
```

Vérifiez que ces fichiers/dossiers NE sont PAS listés:
- ❌ `django_migration/.env`
- ❌ `django_migration/db.sqlite3`
- ❌ `django_migration/venv/`
- ❌ `django_migration/__pycache__/`
- ❌ `django_migration/staticfiles/`

### 3. Ajouter les Fichiers

```bash
git add .
```

### 4. Vérifier à Nouveau

```bash
git status
```

### 5. Premier Commit

```bash
git commit -m "Initial commit: Site CEREMAC Django - Migration complète vers Django 4.2.7"
```

### 6. Créer le Repository sur GitHub

1. Aller sur https://github.com
2. Cliquer sur "New repository"
3. Nom: `ceremac-site` (ou votre choix)
4. Description: "Site web CEREMAC Guinée - Django"
5. **Ne PAS** cocher "Initialize with README" (on en a déjà un)
6. Cliquer sur "Create repository"

### 7. Lier et Push

```bash
# Remplacer VOTRE-USERNAME par votre nom d'utilisateur GitHub
git remote add origin https://github.com/VOTRE-USERNAME/ceremac-site.git
git branch -M main
git push -u origin main
```

## ✅ Fichiers Créés pour GitHub

- ✅ `.gitignore` - Ignore les fichiers sensibles
- ✅ `README.md` - Documentation complète
- ✅ `django_migration/README.md` - Documentation Django
- ✅ `requirements.txt` - Dépendances
- ✅ `.env.example` - Template de configuration

## 🔒 Sécurité

⚠️ **IMPORTANT**: 
- Le fichier `.env` est dans `.gitignore` - il ne sera PAS commité
- Seul `.env.example` sera sur GitHub (sans secrets)
- Vérifiez `git status` avant chaque commit

## 📦 Structure sur GitHub

Le repository contiendra:
- ✅ Code source Django complet
- ✅ Tous les templates HTML
- ✅ Fichiers statiques (CSS, JS, images)
- ✅ Documentation complète
- ✅ Configuration d'exemple
- ❌ PAS de fichiers sensibles (.env, db.sqlite3)
- ❌ PAS d'environnement virtuel (venv/)

## 🎯 Après le Push

1. Vérifier que tout est bien sur GitHub
2. Ajouter une description au repository
3. Configurer les secrets dans GitHub (si CI/CD)
4. Partager le lien du repository

