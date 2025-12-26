# Fichier WSGI pour PythonAnywhere
# À copier dans le fichier WSGI de PythonAnywhere: /var/www/boubacar32_pythonanywhere_com_wsgi.py

import os
import sys

# Chemin vers votre projet Django
# IMPORTANT: Ajustez ce chemin selon votre structure sur PythonAnywhere
# Si vous avez cloné depuis GitHub dans /home/Boubacar32/mysite/
# et que django_migration est dans ce dossier, utilisez:
path = '/home/Boubacar32/mysite/django_migration'

# OU si vous avez directement uploadé django_migration dans /home/Boubacar32/
# path = '/home/Boubacar32/django_migration'

# OU si le projet est dans /home/Boubacar32/Ceremac-Site/django_migration/
# path = '/home/Boubacar32/Ceremac-Site/django_migration'

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

