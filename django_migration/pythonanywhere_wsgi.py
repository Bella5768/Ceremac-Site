# Fichier WSGI pour PythonAnywhere
# À copier dans le fichier WSGI de PythonAnywhere

import os
import sys

# Chemin vers votre projet Django
path = '/home/votreusername/django_migration'
if path not in sys.path:
    sys.path.insert(0, path)

# Définir le module de settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'ceremac_site.settings'

# Charger l'application Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

