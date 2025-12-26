# 🔧 Correction WSGI PythonAnywhere - Erreur ModuleNotFoundError

## ⚠️ Erreur Actuelle
```
ModuleNotFoundError: No module named 'ceremac_site'
```

## ✅ Solution Étape par Étape

### Étape 1: Trouver le Chemin Exact du Projet

Dans la **console Bash** de PythonAnywhere:

```bash
cd ~
find . -name "manage.py" -type f 2>/dev/null
```

Vous obtiendrez quelque chose comme:
```
./Ceremac-Site/django_migration/manage.py
```

Le chemin complet sera: `/home/Boubacar32/Ceremac-Site/django_migration`

### Étape 2: Vérifier la Structure

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
ls -la
```

Vous devez voir:
- `ceremac_site/` (dossier)
- `manage.py`
- `requirements.txt`
- etc.

### Étape 3: Configurer le Fichier WSGI

1. Allez dans **Web** → **WSGI configuration file**
2. **Supprimez TOUT le contenu existant**
3. **Copiez-collez ceci:**

```python
import os
import sys

# ============================================
# IMPORTANT: Ajustez ce chemin selon votre structure
# ============================================
# Trouvez d'abord le chemin avec: find ~ -name "manage.py"
# Enlevez "/manage.py" à la fin

# Exemple si le projet est dans ~/Ceremac-Site/django_migration/
path = '/home/Boubacar32/Ceremac-Site/django_migration'

# Si votre projet est ailleurs, changez le chemin ci-dessus
# Par exemple:
# path = '/home/Boubacar32/mysite/django_migration'
# OU
# path = '/home/Boubacar32/django_migration'

# ============================================
# Ne modifiez rien en dessous
# ============================================

# Vérifier que le chemin existe
if not os.path.exists(path):
    raise Exception(f"ERREUR: Le chemin {path} n'existe pas!\nVérifiez le chemin avec: find ~ -name 'manage.py'")

# Ajouter au PYTHONPATH
if path not in sys.path:
    sys.path.insert(0, path)

# Ajouter aussi le répertoire parent (important!)
parent_path = os.path.dirname(path)
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)

# Définir le module de settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')

# Charger l'application Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Étape 4: Tester le Chemin

Dans la console Bash:

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 manage.py check
```

Si ça fonctionne, le WSGI devrait aussi fonctionner.

### Étape 5: Installer les Dépendances

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
pip3.10 install --user -r requirements.txt
```

### Étape 6: Configurer .env

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
nano .env
```

Ajoutez:
```env
SECRET_KEY=votre-secret-key-production-changez-moi
DEBUG=False
ALLOWED_HOSTS=boubacar32.pythonanywhere.com

DB_ENGINE=mysql
DB_NAME=Boubacar32$ceremac_db
DB_USER=Boubacar32
DB_PASSWORD=votre-mot-de-passe-mysql
DB_HOST=Boubacar32.mysql.pythonanywhere-services.com
DB_PORT=3306
```

### Étape 7: Migrations

```bash
python3.10 manage.py makemigrations
python3.10 manage.py migrate
python3.10 manage.py collectstatic --noinput
```

### Étape 8: Configurer Static Files

Dans **Web** → **Static files**:

1. **URL**: `/static/`
   **Directory**: `/home/Boubacar32/Ceremac-Site/django_migration/staticfiles`

2. **URL**: `/media/`
   **Directory**: `/home/Boubacar32/Ceremac-Site/django_migration/media`

### Étape 9: Reload

Cliquez sur le bouton vert **"Reload"** dans la section Web.

## 🔍 Si ça ne fonctionne toujours pas

### Vérifier les Logs

Allez dans **Web** → **Error log** pour voir les erreurs détaillées.

### Tester l'Import Manuel

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10
```

Puis dans Python:
```python
import sys
sys.path.insert(0, '/home/Boubacar32/Ceremac-Site/django_migration')
from ceremac_site import settings
print("OK!")
```

Si ça fonctionne, le problème est dans le WSGI. Si ça ne fonctionne pas, le projet n'est pas au bon endroit.

## 📝 Checklist Finale

- [ ] Chemin trouvé avec `find ~ -name "manage.py"`
- [ ] Chemin correct dans le WSGI
- [ ] Dépendances installées
- [ ] Fichier `.env` créé
- [ ] Migrations appliquées
- [ ] Static files configurés
- [ ] Application reloadée

