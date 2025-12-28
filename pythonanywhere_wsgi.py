"""
WSGI config for Ceremac-Site project on PythonAnywhere.
"""

import os
import sys

# Ajouter le chemin du projet au sys.path
path = '/home/ceremacsite/Ceremac-Site'
if path not in sys.path:
    sys.path.insert(0, path)

# Définir le module de settings Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'ceremac_site.settings'

# Importer l'application WSGI de Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
