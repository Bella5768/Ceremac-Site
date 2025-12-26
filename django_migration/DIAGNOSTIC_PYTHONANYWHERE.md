# 🔍 Diagnostic et Correction - Accès au Site sur PythonAnywhere

## Problème Actuel
Vous voyez seulement "Bienvenue sur le site Ceremac!" au lieu du site complet.

## ✅ Solution Étape par Étape

### Étape 1: Vérifier la Structure du Projet

Dans la **console Bash** de PythonAnywhere:

```bash
cd ~
ls -la
```

Si vous avez cloné depuis GitHub:
```bash
cd Ceremac-Site/django_migration
ls -la
```

Vous devriez voir:
- `ceremac_site/` (dossier avec settings.py)
- `main/` (dossier)
- `templates/` (dossier)
- `static/` (dossier)
- `manage.py` (fichier)

### Étape 2: Installer les Dépendances

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
pip3.10 install --user -r requirements.txt
```

### Étape 3: Configurer la Base de Données

**Option A: SQLite (plus simple pour commencer)**

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 manage.py migrate
```

**Option B: MySQL (si vous avez une base de données MySQL)**

1. Créez un fichier `.env`:
```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
nano .env
```

2. Ajoutez:
```
DB_ENGINE=mysql
DB_NAME=votre_nom_base
DB_USER=votre_utilisateur
DB_PASSWORD=votre_mot_de_passe
DB_HOST=localhost
DB_PORT=3306
ALLOWED_HOSTS=boubacar32.pythonanywhere.com
DEBUG=False
SECRET_KEY=votre-secret-key-tres-long-et-aleatoire
```

3. Exécutez les migrations:
```bash
python3.10 manage.py migrate
```

### Étape 4: Créer un Superutilisateur

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 manage.py createsuperuser
```

### Étape 5: Collecter les Fichiers Statiques

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 manage.py collectstatic --noinput
```

### Étape 6: Configurer les Fichiers Statiques sur PythonAnywhere

1. Allez dans **Web** → **Static files**
2. **Supprimez** tous les mappings existants
3. **Ajoutez** ces nouveaux mappings:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/Boubacar32/Ceremac-Site/django_migration/staticfiles/` |
| `/media/` | `/home/Boubacar32/Ceremac-Site/django_migration/media/` |

### Étape 7: Vérifier le Fichier WSGI

1. Allez dans **Web** → **WSGI configuration file**
2. **Remplacez TOUT** par:

```python
import os
import sys

# ⚠️ IMPORTANT: Vérifiez ce chemin avec: find ~ -name "manage.py"
project_path = '/home/Boubacar32/Ceremac-Site/django_migration'

# Vérifier que le chemin existe
if not os.path.exists(project_path):
    raise Exception(f"❌ ERREUR: Le chemin {project_path} n'existe pas!\nVérifiez avec: find ~ -name 'manage.py'")

# Ajouter au PYTHONPATH
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Changer le répertoire de travail
os.chdir(project_path)

# Définir le module de settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')

# Charger l'application Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Étape 8: Vérifier ALLOWED_HOSTS

Créez ou modifiez le fichier `.env`:

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
nano .env
```

Ajoutez (remplacez `boubacar32` par votre nom d'utilisateur si différent):
```
ALLOWED_HOSTS=boubacar32.pythonanywhere.com
DEBUG=False
SECRET_KEY=django-insecure-change-this-in-production-avec-une-cle-longue-et-aleatoire
```

### Étape 9: Tester en Ligne de Commande

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 manage.py check
python3.10 manage.py runserver 0.0.0.0:8000
```

Si ces commandes fonctionnent, Django est correctement configuré.

### Étape 10: Reload l'Application Web

1. Allez dans **Web**
2. Cliquez sur le bouton vert **Reload**
3. **Attendez 15-20 secondes** (important!)
4. Visitez: `https://boubacar32.pythonanywhere.com`
5. Vous devriez être redirigé vers: `https://boubacar32.pythonanywhere.com/fr/`

### Étape 11: Vérifier les Logs

Si ça ne fonctionne toujours pas:

1. Allez dans **Web** → **Error log**
2. Copiez les dernières lignes d'erreur
3. Analysez les erreurs pour identifier le problème

## 🔍 Commandes de Diagnostic

Exécutez ces commandes pour diagnostiquer:

```bash
# 1. Trouver le chemin exact
find ~ -name "manage.py" -type f

# 2. Vérifier la structure
cd /home/Boubacar32/Ceremac-Site/django_migration
ls -la
ls -la ceremac_site/
ls -la templates/
ls -la staticfiles/

# 3. Vérifier Django
python3.10 -c "import django; print('Django version:', django.get_version())"

# 4. Vérifier les imports
python3.10 -c "import sys; sys.path.insert(0, '/home/Boubacar32/Ceremac-Site/django_migration'); import ceremac_site.settings; print('✅ Settings OK')"

# 5. Vérifier les migrations
python3.10 manage.py showmigrations

# 6. Vérifier les templates
python3.10 manage.py check --deploy

# 7. Tester les URLs
python3.10 manage.py shell
>>> from django.urls import reverse
>>> reverse('main:index')
'/fr/'
```

## ⚠️ Problèmes Courants et Solutions

### Problème: "TemplateDoesNotExist"
**Solution:**
```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
ls -la templates/main/index.html  # Vérifier que le fichier existe
python3.10 manage.py collectstatic --noinput
```

### Problème: "Static files not found (404)"
**Solution:**
1. Vérifiez les mappings statiques dans PythonAnywhere Web
2. Exécutez `python3.10 manage.py collectstatic --noinput`
3. Vérifiez que `staticfiles/` contient les fichiers

### Problème: "DisallowedHost"
**Solution:**
Ajoutez votre domaine dans `.env`:
```
ALLOWED_HOSTS=boubacar32.pythonanywhere.com
```

### Problème: Page blanche
**Solution:**
1. Consultez les logs d'erreur
2. Vérifiez que `DEBUG=False` dans `.env` (mais les erreurs seront moins visibles)
3. Testez avec `DEBUG=True` temporairement pour voir les erreurs

### Problème: Redirection infinie
**Solution:**
Vérifiez que les URLs dans `ceremac_site/urls.py` sont correctes et qu'il n'y a pas de boucle.

## 📋 Checklist Finale

- [ ] Structure du projet correcte
- [ ] Dépendances installées (`pip3.10 install --user -r requirements.txt`)
- [ ] Migrations exécutées (`python3.10 manage.py migrate`)
- [ ] Superutilisateur créé (`python3.10 manage.py createsuperuser`)
- [ ] Fichiers statiques collectés (`python3.10 manage.py collectstatic`)
- [ ] Mappings statiques configurés dans PythonAnywhere Web
- [ ] Fichier WSGI correctement configuré
- [ ] Fichier `.env` créé avec `ALLOWED_HOSTS`
- [ ] `python3.10 manage.py check` fonctionne sans erreur
- [ ] Application rechargée sur PythonAnywhere
- [ ] Site accessible sur `https://boubacar32.pythonanywhere.com/fr/`

## 🆘 Si Rien ne Fonctionne

1. **Copiez les logs d'erreur** complets depuis PythonAnywhere
2. **Vérifiez la version Python**: `python3.10 --version` (doit être 3.10)
3. **Testez en local** d'abord pour vérifier que le code fonctionne
4. **Vérifiez les permissions**: `chmod -R 755 /home/Boubacar32/Ceremac-Site/django_migration`

