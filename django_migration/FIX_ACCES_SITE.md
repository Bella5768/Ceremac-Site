# 🔴 Problème: Pas d'accès au vrai site sur PythonAnywhere

## Symptôme
- Seule une page simple avec "Bienvenue sur le site Ceremac!" s'affiche
- Le site complet avec navigation, design, etc. ne s'affiche pas

## ✅ Solutions

### 1. Vérifier que le WSGI charge correctement Django

Dans le fichier WSGI de PythonAnywhere, vous devez avoir:

```python
import os
import sys

project_path = '/home/Boubacar32/Ceremac-Site/django_migration'

if not os.path.exists(project_path):
    raise Exception(f"❌ ERREUR: Le chemin {project_path} n'existe pas!")

if project_path not in sys.path:
    sys.path.insert(0, project_path)

os.chdir(project_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 2. Vérifier la Structure du Projet

Dans la console Bash de PythonAnywhere:

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
ls -la
```

Vous devriez voir:
- `ceremac_site/` (dossier)
- `main/` (dossier)
- `templates/` (dossier)
- `static/` (dossier)
- `manage.py` (fichier)

### 3. Vérifier que Django fonctionne

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 manage.py check
```

Si cette commande échoue, installez Django:
```bash
pip3.10 install --user -r requirements.txt
```

### 4. Exécuter les Migrations

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 manage.py migrate
```

### 5. Collecter les Fichiers Statiques

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 manage.py collectstatic --noinput
```

### 6. Configurer les Fichiers Statiques sur PythonAnywhere

1. Allez dans **Web** → **Static files**
2. Ajoutez ces mappings:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/Boubacar32/Ceremac-Site/django_migration/staticfiles/` |
| `/media/` | `/home/Boubacar32/Ceremac-Site/django_migration/media/` |

### 7. Vérifier ALLOWED_HOSTS

Dans `django_migration/ceremac_site/settings.py`, assurez-vous que:

```python
ALLOWED_HOSTS = ['boubacar32.pythonanywhere.com', 'localhost', '127.0.0.1']
```

Ou créez un fichier `.env` dans `django_migration/`:

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
nano .env
```

Ajoutez:
```
ALLOWED_HOSTS=boubacar32.pythonanywhere.com,localhost,127.0.0.1
DEBUG=False
SECRET_KEY=votre-secret-key-ici
```

### 8. Vérifier les Logs d'Erreur

1. Allez dans **Web** → **Error log**
2. Lisez les dernières lignes pour voir les erreurs exactes

### 9. Tester l'Application en Ligne de Commande

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 manage.py runserver 0.0.0.0:8000
```

Si ça fonctionne, le problème est dans la configuration WSGI.

### 10. Vérifier les URLs

Assurez-vous que l'URL racine pointe vers Django. Dans PythonAnywhere:
- L'URL racine (`/`) doit être gérée par Django
- Pas de fichier `index.html` dans le répertoire web qui pourrait intercepter

### 11. Reload l'Application

Après chaque modification:
1. Allez dans **Web**
2. Cliquez sur **Reload**
3. Attendez 10-15 secondes
4. Rafraîchissez votre navigateur (Ctrl+F5)

## 🔍 Diagnostic Rapide

Exécutez ces commandes dans la console Bash:

```bash
# 1. Vérifier la structure
cd /home/Boubacar32/Ceremac-Site/django_migration
ls -la

# 2. Vérifier Django
python3.10 -c "import django; print(django.get_version())"

# 3. Vérifier les imports
python3.10 -c "import sys; sys.path.insert(0, '.'); import ceremac_site.settings; print('✅ OK')"

# 4. Vérifier les migrations
python3.10 manage.py showmigrations

# 5. Vérifier les templates
ls -la templates/main/

# 6. Vérifier les fichiers statiques
ls -la staticfiles/
```

## ⚠️ Problèmes Courants

### Problème: "TemplateDoesNotExist"
**Solution:** Vérifiez que `TEMPLATES['DIRS']` dans `settings.py` contient `BASE_DIR / 'templates'`

### Problème: "Static files not found"
**Solution:** 
1. Exécutez `python3.10 manage.py collectstatic`
2. Configurez les mappings statiques dans PythonAnywhere Web

### Problème: "No module named 'ceremac_site'"
**Solution:** Vérifiez le chemin dans le fichier WSGI

### Problème: Page blanche ou erreur 500
**Solution:** Consultez les logs d'erreur dans PythonAnywhere Web → Error log

## 📝 Checklist Complète

- [ ] Le fichier WSGI est correctement configuré
- [ ] Le chemin dans WSGI correspond à la structure réelle
- [ ] Django est installé (`pip3.10 install --user -r requirements.txt`)
- [ ] Les migrations sont exécutées (`python3.10 manage.py migrate`)
- [ ] Les fichiers statiques sont collectés (`python3.10 manage.py collectstatic`)
- [ ] Les mappings statiques sont configurés dans PythonAnywhere Web
- [ ] `ALLOWED_HOSTS` contient votre domaine PythonAnywhere
- [ ] Le fichier `.env` existe et est correctement configuré (si utilisé)
- [ ] L'application a été rechargée après les modifications
- [ ] Les logs d'erreur ont été consultés

## 🆘 Si Rien ne Fonctionne

1. **Copiez les logs d'erreur** depuis PythonAnywhere Web → Error log
2. **Vérifiez la structure** avec `find ~ -name "manage.py"`
3. **Testez en local** d'abord pour vérifier que le code fonctionne
4. **Vérifiez la version Python** sur PythonAnywhere (doit être 3.10)

