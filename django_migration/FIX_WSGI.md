# 🔧 Correction WSGI PythonAnywhere

## ⚠️ Erreur: ModuleNotFoundError: No module named 'ceremac_site'

## Solution Rapide

### 1. Trouver le Chemin Exact

Dans la console Bash de PythonAnywhere:

```bash
cd ~
find . -name "manage.py" -type f 2>/dev/null
```

Cela vous donnera le chemin exact, par exemple:
- `/home/Boubacar32/Ceremac-Site/django_migration/manage.py`

### 2. Configurer le WSGI

Allez dans **Web** → **WSGI configuration file**

**Remplacez TOUT par:**

```python
import os
import sys

# CHEMIN EXACT - Remplacez par le chemin trouvé à l'étape 1
# Enlevez "/manage.py" à la fin si présent
path = '/home/Boubacar32/Ceremac-Site/django_migration'

# Vérifier que le chemin existe
if not os.path.exists(path):
    raise Exception(f"Le chemin {path} n'existe pas! Vérifiez le chemin.")

# Ajouter au PYTHONPATH
if path not in sys.path:
    sys.path.insert(0, path)

# Ajouter le répertoire parent
parent = os.path.dirname(path)
if parent not in sys.path:
    sys.path.insert(0, parent)

# Settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')

# Application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 3. Vérifier la Structure

Le dossier `ceremac_site` doit être dans `django_migration/`:

```
django_migration/
├── ceremac_site/    ← Ce dossier doit exister
│   ├── settings.py
│   └── ...
├── manage.py
└── ...
```

### 4. Tester

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 manage.py check
```

Si ça fonctionne, le WSGI devrait aussi fonctionner.

### 5. Reload

Cliquez sur **Reload** dans la section Web.

