# 🚀 Préparation pour GitHub - Checklist

## ✅ Vérifications Avant Push

### Fichiers à Vérifier

- [x] `.gitignore` créé et configuré
- [x] `README.md` créé avec documentation complète
- [x] `requirements.txt` à jour
- [x] `.env.example` créé (sans secrets)
- [ ] `.env` N'EST PAS dans le repository (vérifier avec `git status`)

### Fichiers qui DOIVENT être ignorés

- [ ] `django_migration/.env`
- [ ] `django_migration/db.sqlite3`
- [ ] `django_migration/venv/`
- [ ] `django_migration/__pycache__/`
- [ ] `django_migration/*/__pycache__/`
- [ ] `django_migration/staticfiles/`
- [ ] `django_migration/media/`

## 📝 Commandes pour Initialiser Git

```bash
# 1. Aller dans le dossier du projet
cd C:\wamp64\www\Ceremac-Site

# 2. Initialiser Git (si pas déjà fait)
git init

# 3. Vérifier ce qui sera commité
git status

# 4. Ajouter tous les fichiers (sauf ceux dans .gitignore)
git add .

# 5. Vérifier à nouveau
git status

# 6. Premier commit
git commit -m "Initial commit: Site CEREMAC Django - Migration complète vers Django"

# 7. Créer le repository sur GitHub, puis:
git remote add origin https://github.com/VOTRE-USERNAME/ceremac-site.git
git branch -M main
git push -u origin main
```

## ⚠️ AVANT DE COMMITER

Vérifiez que ces fichiers NE SONT PAS dans le commit:
- `.env` (contient SECRET_KEY et mots de passe)
- `db.sqlite3` (base de données locale)
- `venv/` (environnement virtuel - trop volumineux)

## 📦 Structure Finale sur GitHub

Le repository contiendra:
- ✅ Code source Django
- ✅ Templates HTML
- ✅ Fichiers statiques (CSS, JS, images)
- ✅ Documentation complète
- ✅ Configuration d'exemple (.env.example)
- ❌ PAS de fichiers sensibles
- ❌ PAS de base de données
- ❌ PAS d'environnement virtuel

## 🔐 Sécurité

**NE JAMAIS COMMITER:**
- Fichiers `.env` avec les vraies valeurs
- Mots de passe
- Clés secrètes
- Base de données locale

**UTILISER:**
- `.env.example` comme template
- Variables d'environnement pour les secrets
- Documentation claire pour la configuration

