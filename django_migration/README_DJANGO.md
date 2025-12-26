# Site CEREMAC - Version Django

Version Django du site web CEREMAC pour déploiement sur PythonAnywhere.

## Fonctionnalités

- ✅ Pages publiques (Accueil, À propos, Services, Publications, Partenaires, Actualités, Contact)
- ✅ Système d'authentification
- ✅ Espace membres
- ✅ Panneau d'administration
- ✅ Multilingue (FR/EN)
- ✅ Upload de fichiers
- ✅ Newsletter
- ✅ Gestion de contenu complète

## Installation Rapide

```bash
# 1. Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Configurer .env
cp .env.example .env
# Éditer .env avec vos paramètres

# 4. Migrations
python manage.py makemigrations
python manage.py migrate

# 5. Créer un superutilisateur
python manage.py createsuperuser

# 6. Lancer le serveur
python manage.py runserver
```

## Structure

- `main/`: App principale avec modèles et vues publiques
- `admin_panel/`: Vues d'administration
- `members/`: Espace membres
- `templates/`: Templates HTML (à créer depuis les fichiers PHP)
- `static/`: Fichiers CSS, JS, images
- `media/`: Fichiers uploadés

## Prochaines Étapes

1. Copier les templates HTML depuis le projet PHP et les adapter pour Django
2. Copier les fichiers statiques (CSS, JS, images)
3. Tester localement
4. Déployer sur PythonAnywhere (voir MIGRATION_GUIDE.md)

