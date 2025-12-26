# Fichier WSGI pour PythonAnywhere
# À copier dans le fichier WSGI de PythonAnywhere: /var/www/boubacar32_pythonanywhere_com_wsgi.py

import os
import sys

# Chemin vers votre projet Django sur PythonAnywhere
# IMPORTANT: Ajustez ce chemin selon votre structure sur PythonAnywhere
project_path = '/home/Boubacar32/Ceremac-Site/django_migration'

# Ajouter le chemin du projet au PYTHONPATH
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Changer le répertoire de travail vers le projet
os.chdir(project_path)

# Définir le module de settings AVANT d'importer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')

# Charger l'application Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

