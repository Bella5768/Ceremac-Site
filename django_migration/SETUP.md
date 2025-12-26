# Guide de Configuration Rapide

## Installation Locale

```bash
# 1. Cloner le repository
git clone https://github.com/votre-username/ceremac-site.git
cd ceremac-site/django_migration

# 2. Créer et activer l'environnement virtuel
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Créer le fichier .env
cp .env.example .env
# Éditer .env avec vos paramètres

# 5. Migrations
python manage.py makemigrations
python manage.py migrate

# 6. Créer un superutilisateur
python manage.py createsuperuser

# 7. Collecter les fichiers statiques
python manage.py collectstatic --noinput

# 8. Lancer le serveur
python manage.py runserver
```

## Accès

- Site: http://localhost:8000/
- Admin: http://localhost:8000/admin/

## Identifiants

Créez votre superutilisateur avec la commande `createsuperuser`.

