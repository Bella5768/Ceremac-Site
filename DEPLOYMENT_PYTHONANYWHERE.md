# Déploiement sur PythonAnywhere

## Configuration WSGI

Sur PythonAnywhere, dans l'onglet **Web**, configurez le fichier WSGI avec ce contenu:

```python
import os
import sys

# Ajouter le chemin du projet
path = '/home/ceremacsite/Ceremac-Site'
if path not in sys.path:
    sys.path.insert(0, path)

# Configuration Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'ceremac_site.settings'

# Application WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## Variables d'environnement

Créez un fichier `.env` dans `/home/ceremacsite/Ceremac-Site/`:

```env
SECRET_KEY=votre-cle-secrete-unique
DEBUG=False
ALLOWED_HOSTS=ceremacsite.pythonanywhere.com
DB_ENGINE=mysql
DB_NAME=ceremacsite$ceremac_db
DB_USER=ceremacsite
DB_PASSWORD=votre-mot-de-passe
DB_HOST=ceremacsite.mysql.pythonanywhere-services.com
```

## Installation

```bash
cd ~/Ceremac-Site
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

## Fichiers statiques

Dans l'onglet **Web** de PythonAnywhere:
- **Static files URL**: `/static/`
- **Static files directory**: `/home/ceremacsite/Ceremac-Site/staticfiles/`

- **Media files URL**: `/media/`
- **Media files directory**: `/home/ceremacsite/Ceremac-Site/media/`

## Recharger l'application

Après chaque modification, cliquez sur le bouton **Reload** dans l'onglet Web.
