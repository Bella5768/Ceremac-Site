# Site Web CEREMAC Guinée - Version Django

Site web du Centre de Recherche en Océanographie, Environnement Marin et Côtier (CEREMAC) en Guinée, développé avec Django.

## 🚀 Fonctionnalités

### Pages publiques
- ✅ Accueil avec présentation du CEREMAC et statistiques
- ✅ À propos (historique, missions, organisation)
- ✅ Services et Directions (organisation scientifique)
- ✅ Publications scientifiques avec téléchargement
- ✅ Partenaires (nationaux et internationaux)
- ✅ Actualités avec articles détaillés
- ✅ Contact avec formulaire fonctionnel
- ✅ Newsletter avec inscription par email

### Administration complète
- ✅ Gestion des actualités (via Django Admin)
- ✅ Gestion des projets
- ✅ Gestion des publications
- ✅ Gestion des partenaires
- ✅ Gestion des utilisateurs avec privilèges
- ✅ Gestion des messages de contact
- ✅ Gestion des abonnés à la newsletter
- ✅ Upload d'images et documents
- ✅ Statistiques du site

### Espace membres
- ✅ Authentification sécurisée
- ✅ Dashboard personnel
- ✅ Accès aux documents réservés
- ✅ Projets internes
- ✅ Gestion du profil utilisateur

### Autres fonctionnalités
- ✅ Système multilingue (Français / Anglais)
- ✅ Design responsive (Bootstrap 5)
- ✅ Thème bleu/vert inspiré de la mer
- ✅ Intégration réseaux sociaux
- ✅ Protection CSRF
- ✅ Gestion des sessions sécurisée

## 🛠️ Technologies utilisées

- **Backend**: Django 4.2.7
- **Base de données**: SQLite (développement) / MySQL (production)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Framework CSS**: Bootstrap 5.3
- **Icônes**: Bootstrap Icons
- **Déploiement**: PythonAnywhere ready

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- MySQL (optionnel, pour la production)

## 🔧 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/votre-username/ceremac-site.git
cd ceremac-site/django_migration
```

### 2. Créer l'environnement virtuel

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configuration

Créer un fichier `.env` à partir de `.env.example`:

```bash
cp .env.example .env
```

Éditer `.env` avec vos paramètres:

```env
SECRET_KEY=votre-secret-key-ici
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Pour SQLite (développement)
DB_ENGINE=sqlite

# Pour MySQL (production)
# DB_ENGINE=mysql
# DB_NAME=ceremac_db
# DB_USER=votre_username
# DB_PASSWORD=votre_password
# DB_HOST=localhost
# DB_PORT=3306
```

### 5. Migrations de base de données

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### 7. Collecter les fichiers statiques

```bash
python manage.py collectstatic
```

### 8. Lancer le serveur de développement

```bash
python manage.py runserver
```

Le site sera accessible à: http://127.0.0.1:8000/

## 📁 Structure du projet

```
django_migration/
├── ceremac_site/          # Configuration principale Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── main/                   # App principale (pages publiques)
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── admin_panel/           # App administration
│   ├── views.py
│   └── urls.py
├── members/               # App espace membres
│   ├── views.py
│   └── urls.py
├── templates/             # Templates HTML
│   ├── base.html
│   ├── main/
│   ├── admin_panel/
│   └── members/
├── static/                # Fichiers statiques (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── media/                 # Fichiers uploadés (non versionné)
├── requirements.txt       # Dépendances Python
├── manage.py
└── README.md
```

## 🔐 Identifiants par défaut

Après la création du superutilisateur:
- **Username**: admin (ou celui que vous avez créé)
- **Password**: (celui que vous avez défini)

⚠️ **IMPORTANT**: Changez le mot de passe après la première connexion!

## 🌐 Déploiement sur PythonAnywhere

Voir le fichier `MIGRATION_GUIDE.md` pour les instructions complètes de déploiement.

### Étapes rapides:

1. Uploader le projet sur PythonAnywhere
2. Créer une base de données MySQL
3. Configurer le fichier `.env`
4. Installer les dépendances: `pip3.10 install --user -r requirements.txt`
5. Exécuter les migrations: `python3.10 manage.py migrate`
6. Configurer le fichier WSGI (voir `pythonanywhere_wsgi.py`)
7. Configurer les fichiers statiques et media
8. Reload l'application

## 📝 Commandes utiles

```bash
# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Collecter les fichiers statiques
python manage.py collectstatic

# Lancer le serveur
python manage.py runserver

# Shell Django
python manage.py shell

# Créer les traductions
python manage.py makemessages -l fr
python manage.py makemessages -l en
python manage.py compilemessages
```

## 🐛 Dépannage

### Erreur "ModuleNotFoundError: No module named 'django'"
- Assurez-vous que l'environnement virtuel est activé
- Réinstallez les dépendances: `pip install -r requirements.txt`

### Erreur de base de données
- Vérifiez que les migrations sont appliquées: `python manage.py migrate`
- Vérifiez les paramètres dans `.env`

### Fichiers statiques non chargés
- Exécutez: `python manage.py collectstatic`
- Vérifiez `STATIC_ROOT` et `STATIC_URL` dans `settings.py`

## 📄 Licence

Ce projet est propriétaire du CEREMAC Guinée.

## 👥 Contribution

Pour contribuer au projet, veuillez créer une branche et soumettre une pull request.

## 📧 Contact

Pour toute question, contactez: contact@ceremac.gn

---

**Développé avec ❤️ pour CEREMAC Guinée**

