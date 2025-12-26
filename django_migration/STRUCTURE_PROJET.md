# 📁 Structure du Projet CEREMAC

## Structure Actuelle

```
django_migration/
├── ceremac_site/              # Configuration du projet
│   ├── __init__.py
│   ├── settings.py            # Configuration Django
│   ├── urls.py                # URLs principales
│   ├── wsgi.py                # Configuration WSGI
│   └── asgi.py                # Configuration ASGI
│
├── main/                      # Application principale
│   ├── __init__.py
│   ├── models.py              # Modèles de données
│   ├── views.py               # Vues
│   ├── urls.py                # URLs de l'app
│   ├── forms.py               # Formulaires
│   ├── admin.py               # Configuration admin
│   ├── apps.py                # Configuration app
│   ├── context_processors.py # Context processors
│   ├── tests.py               # Tests unitaires
│   ├── migrations/            # Migrations base de données
│   ├── templates/             # Templates HTML
│   │   └── main/
│   │       ├── base.html      # Template de base
│   │       ├── index.html
│   │       ├── about.html
│   │       ├── projects.html
│   │       └── ...
│   └── static/                # Fichiers statiques
│       └── main/
│           ├── css/
│           │   ├── style.css
│           │   └── images.css
│           ├── js/
│           │   └── main.js
│           └── images/
│               └── placeholder.svg
│
├── admin_panel/               # Application administration
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   ├── apps.py
│   └── templates/
│       └── admin_panel/
│           ├── index.html
│           ├── news.html
│           └── ...
│
├── members/                   # Application espace membres
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   ├── apps.py
│   └── templates/
│       └── members/
│           ├── login.html
│           ├── index.html
│           └── ...
│
├── manage.py                  # Script de gestion Django
├── requirements.txt           # Dépendances Python
├── db.sqlite3                  # Base de données SQLite (dev)
├── staticfiles/               # Fichiers statiques collectés
└── media/                     # Fichiers uploadés
    └── uploads/
```

## Organisation des Templates

Les templates sont organisés par application :

- **main/templates/main/** : Templates de l'application principale
- **admin_panel/templates/admin_panel/** : Templates de l'administration
- **members/templates/members/** : Templates de l'espace membres

## Organisation des Fichiers Statiques

Les fichiers statiques sont dans chaque application :

- **main/static/main/** : CSS, JS, images de l'application principale
- Les autres apps peuvent avoir leurs propres fichiers statiques si nécessaire

## Configuration Django

### Templates
- `APP_DIRS = True` : Django cherche automatiquement dans `app/templates/`
- `DIRS = []` : Pas de répertoire global (tout est dans les apps)

### Fichiers Statiques
- `STATICFILES_DIRS = [BASE_DIR / 'main' / 'static']` : Répertoire des fichiers statiques
- `STATIC_ROOT = BASE_DIR / 'staticfiles'` : Répertoire de collecte pour la production

## Utilisation

### Templates
```django
{% extends 'main/base.html' %}
```

### Fichiers Statiques
```django
{% load static %}
<link rel="stylesheet" href="{% static 'main/css/style.css' %}">
<script src="{% static 'main/js/main.js' %}"></script>
```

## Avantages de cette Structure

1. **Modularité** : Chaque app contient ses propres templates et fichiers statiques
2. **Organisation** : Structure claire et logique
3. **Réutilisabilité** : Les apps peuvent être réutilisées dans d'autres projets
4. **Convention Django** : Suit les meilleures pratiques Django

