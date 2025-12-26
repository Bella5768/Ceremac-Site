# Site Web CEREMAC Guinée

Site web du Centre de Recherche en Océanographie, Environnement Marin et Côtier (CEREMAC) en Guinée.

## 📦 Versions

Ce repository contient deux versions du site:

1. **Version Django** (actuelle) - `django_migration/`
   - Framework: Django 4.2.7
   - Base de données: SQLite/MySQL
   - Prêt pour déploiement sur PythonAnywhere

2. **Version PHP** (ancienne) - Fichiers supprimés
   - Les fichiers PHP ont été supprimés lors de la migration vers Django

## 🚀 Démarrage Rapide

### Version Django

Voir le README dans `django_migration/README.md` pour les instructions complètes.

```bash
cd django_migration
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 📁 Structure

```
Ceremac-Site/
├── django_migration/      # Projet Django (version actuelle)
│   ├── ceremac_site/     # Configuration Django
│   ├── main/             # App principale
│   ├── admin_panel/      # App administration
│   ├── members/          # App espace membres
│   ├── templates/        # Templates HTML
│   ├── static/           # Fichiers statiques
│   └── requirements.txt  # Dépendances
├── assets/               # Fichiers statiques (CSS, JS, images)
├── database.sql          # Structure de base de données
└── README.md            # Ce fichier
```

## 🌐 Déploiement

### PythonAnywhere

Le projet est configuré pour être déployé sur PythonAnywhere. Voir `django_migration/MIGRATION_GUIDE.md` pour les instructions.

## 📝 Documentation

- `django_migration/README.md` - Documentation complète Django
- `django_migration/MIGRATION_GUIDE.md` - Guide de migration vers PythonAnywhere
- `django_migration/QUICK_START.md` - Démarrage rapide
- `django_migration/TEMPLATE_EXAMPLE.md` - Exemples de templates

## 🔐 Sécurité

⚠️ **IMPORTANT**: 
- Ne commitez JAMAIS le fichier `.env` contenant les secrets
- Changez le `SECRET_KEY` en production
- Utilisez `DEBUG=False` en production

## 📧 Contact

CEREMAC Guinée
Email: contact@ceremac.gn

---

**Développé pour CEREMAC Guinée**
