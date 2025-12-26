# Fichier WSGI pour PythonAnywhere
# À copier dans le fichier WSGI de PythonAnywhere: /var/www/boubacar32_pythonanywhere_com_wsgi.py

import os
import sys

# Chemin vers votre projet Django sur PythonAnywhere
path = '/home/Boubacar32/Ceremac-Site/django_migration'

if path not in sys.path:
    sys.path.insert(0, path)

# Ajouter aussi le répertoire parent au PYTHONPATH
parent_path = os.path.dirname(path)
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)

# Définir le module de settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'ceremac_site.settings'

# Charger l'application Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

