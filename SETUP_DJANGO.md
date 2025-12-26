# Configuration Django - CEREMAC Site

## Structure Actuelle

```
Ceremac-Site/
├── assets/              # Fichiers statiques (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── django_migration/    # Projet Django complet
│   ├── main/           # App principale
│   ├── admin_panel/    # App administration
│   ├── members/         # App espace membres
│   └── ...
├── database.sql         # Structure de base de données
├── documents/           # Documents uploadés
└── uploads/            # Images uploadées
```

## Prochaines Étapes

### 1. Copier les fichiers statiques vers Django

```bash
cd django_migration

# Créer les dossiers statiques
mkdir -p static/css static/js static/images

# Copier les fichiers
cp -r ../assets/css/* static/css/
cp -r ../assets/js/* static/js/
cp -r ../assets/images/* static/images/
```

### 2. Créer les templates Django

Les templates doivent être créés dans `django_migration/templates/` en adaptant vos fichiers HTML existants.

Structure à créer :
```
templates/
├── base.html           # Template de base (header + footer)
├── main/
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   ├── publications.html
│   ├── partners.html
│   ├── news_list.html
│   ├── news_detail.html
│   └── contact.html
├── admin_panel/
│   └── ...
└── members/
    └── ...
```

### 3. Installation et Configuration

```bash
cd django_migration

# Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer .env
cp .env.example .env
# Éditer .env avec vos paramètres

# Migrations
python manage.py makemigrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Collecter les fichiers statiques
python manage.py collectstatic

# Lancer le serveur
python manage.py runserver
```

## Fichiers Conservés

✅ **Conservés** :
- `assets/` - CSS, JS, images (à copier vers Django)
- `database.sql` - Structure de base de données
- `django_migration/` - Projet Django complet
- `documents/` - Documents existants
- `uploads/` - Images existantes
- Documentation (.md)

❌ **Supprimés** :
- Tous les fichiers `.php`
- Tous les fichiers `.bat`
- Dossiers `config/`, `admin/`, `includes/`, `members/` (PHP)

## Migration des Données

Si vous avez des données existantes dans MySQL :

1. Exporter depuis MySQL :
```bash
mysqldump -u root ceremac_db > backup.sql
```

2. Importer dans Django (après migrations) :
```bash
mysql -u username -p ceremac_db < backup.sql
```

## Ressources

- `django_migration/QUICK_START.md` - Guide de démarrage rapide
- `django_migration/MIGRATION_GUIDE.md` - Guide de migration complet
- `django_migration/TEMPLATE_EXAMPLE.md` - Exemples de templates
- `django_migration/DEPLOYMENT_CHECKLIST.md` - Checklist de déploiement

