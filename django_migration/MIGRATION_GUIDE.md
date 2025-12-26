# Guide de Migration vers Django pour PythonAnywhere

Ce guide vous aidera à migrer votre site PHP vers Django et à le déployer sur PythonAnywhere.

## Structure du Projet Django

```
django_migration/
├── ceremac_site/          # Configuration principale Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── main/                   # App principale (pages publiques)
│   ├── models.py          # Modèles de données
│   ├── views.py           # Vues publiques
│   ├── forms.py           # Formulaires
│   └── urls.py
├── admin_panel/           # App administration
│   ├── views.py
│   └── urls.py
├── members/               # App espace membres
│   ├── views.py
│   └── urls.py
├── templates/             # Templates HTML (à créer)
├── static/                # Fichiers statiques (CSS, JS, images)
├── media/                 # Fichiers uploadés
├── requirements.txt
├── manage.py
└── .env.example
```

## Installation Locale

### 1. Prérequis
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configuration
```bash
# Copier le fichier .env.example
cp .env.example .env

# Éditer .env avec vos paramètres locaux
# Pour développement local:
SECRET_KEY=django-insecure-dev-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=ceremac_db
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

### 3. Migrations de base de données
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Copier les fichiers statiques
```bash
# Copier les fichiers CSS, JS et images depuis le projet PHP
cp -r ../Ceremac-Site/assets/css static/
cp -r ../Ceremac-Site/assets/js static/
cp -r ../Ceremac-Site/assets/images static/
```

### 5. Lancer le serveur
```bash
python manage.py runserver
```

## Déploiement sur PythonAnywhere

### 1. Créer un compte PythonAnywhere
- Aller sur https://www.pythonanywhere.com
- Créer un compte gratuit ou payant

### 2. Uploader le projet
```bash
# Via Git (recommandé)
git clone votre-repo
cd django_migration

# Ou via l'interface web de PythonAnywhere
# Files > Upload a file
```

### 3. Configurer la base de données MySQL
- Dans PythonAnywhere, aller dans "Databases"
- Créer une base de données MySQL
- Noter les informations de connexion:
  - Host: username.mysql.pythonanywhere-services.com
  - Username: username
  - Password: (celui que vous avez défini)
  - Database name: username$ceremac_db

### 4. Configuration .env pour PythonAnywhere
```bash
# Dans le fichier .env sur PythonAnywhere
SECRET_KEY=votre-secret-key-production
DEBUG=False
ALLOWED_HOSTS=votreusername.pythonanywhere.com

DB_NAME=votreusername$ceremac_db
DB_USER=votreusername
DB_PASSWORD=votre-mot-de-passe-mysql
DB_HOST=votreusername.mysql.pythonanywhere-services.com
DB_PORT=3306
```

### 5. Installer les dépendances
```bash
# Dans la console Bash de PythonAnywhere
cd ~/django_migration
pip3.10 install --user -r requirements.txt
```

### 6. Migrations
```bash
python3.10 manage.py makemigrations
python3.10 manage.py migrate
python3.10 manage.py collectstatic
python3.10 manage.py createsuperuser
```

### 7. Configuration WSGI
- Aller dans "Web" > "WSGI configuration file"
- Remplacer le contenu par:

```python
import os
import sys

path = '/home/votreusername/django_migration'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ceremac_site.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 8. Configuration Static Files
Dans "Web" > "Static files":
- URL: `/static/`
- Directory: `/home/votreusername/django_migration/staticfiles`

Pour les media files:
- URL: `/media/`
- Directory: `/home/votreusername/django_migration/media`

### 9. Reload l'application
- Cliquer sur le bouton vert "Reload" dans la section Web

## Migration des Données

### Option 1: Via SQL
```bash
# Exporter depuis MySQL PHP
mysqldump -u root ceremac_db > ceremac_backup.sql

# Importer dans PythonAnywhere MySQL
mysql -u votreusername -p votreusername$ceremac_db < ceremac_backup.sql
```

### Option 2: Via Django Management Command
Créer un script de migration personnalisé pour importer les données.

## Templates à Créer

Les templates HTML doivent être adaptés depuis les fichiers PHP:
- `templates/base.html` (header + footer)
- `templates/main/index.html`
- `templates/main/about.html`
- `templates/main/projects.html`
- `templates/main/publications.html`
- `templates/main/partners.html`
- `templates/main/news_list.html`
- `templates/main/contact.html`
- `templates/admin_panel/*.html`
- `templates/members/*.html`

## Adaptations Nécessaires

1. **Templates**: Remplacer `<?php echo ... ?>` par `{{ variable }}` et `{% tag %}`
2. **URLs**: Utiliser `{% url 'name' %}` au lieu de `BASE_URL`
3. **Forms**: Utiliser les formulaires Django au lieu de formulaires HTML bruts
4. **Static Files**: Utiliser `{% load static %}` et `{% static 'path' %}`
5. **Multilingue**: Utiliser le système i18n de Django

## Commandes Utiles

```bash
# Créer un superutilisateur
python manage.py createsuperuser

# Collecter les fichiers statiques
python manage.py collectstatic

# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Shell Django
python manage.py shell

# Créer les traductions
python manage.py makemessages -l fr
python manage.py makemessages -l en
python manage.py compilemessages
```

## Support

Pour toute question, consultez:
- Documentation Django: https://docs.djangoproject.com/
- PythonAnywhere Help: https://help.pythonanywhere.com/

