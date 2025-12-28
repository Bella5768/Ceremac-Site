# Site Web CEREMAC Guinée

Site web du Centre de Recherche en Océanographie, Environnement Marin et Côtier (CEREMAC) en Guinée.

## 🛠️ Technologies

- **Framework**: Django 4.2.7
- **Base de données**: SQLite (dev) / MySQL (prod)
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Fichiers statiques**: WhiteNoise

## 🚀 Démarrage Rapide

```bash
# Cloner le repository
git clone https://github.com/votre-username/Ceremac-Site.git
cd Ceremac-Site

# Créer l'environnement virtuel
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

Le site sera accessible sur http://127.0.0.1:8000/

## 📁 Structure

```
Ceremac-Site/
├── manage.py              # Point d'entrée Django
├── ceremac_site/          # Configuration du projet
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                  # App principale (pages publiques)
├── admin_panel/           # App administration personnalisée
├── members/               # App espace membres
├── media/                 # Fichiers uploadés
├── staticfiles/           # Fichiers statiques collectés
├── requirements.txt       # Dépendances Python
└── README.md
```

## 🔐 Configuration

Créez un fichier `.env` à la racine:

```env
SECRET_KEY=votre-cle-secrete
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=sqlite
```

## 🌐 Déploiement

### PythonAnywhere

1. Cloner le repo sur PythonAnywhere
2. Créer un virtualenv et installer les dépendances
3. Configurer le fichier WSGI
4. Configurer les fichiers statiques

## 📧 Contact

CEREMAC Guinée  
Email: contact@ceremac.gn

---

**Développé pour CEREMAC Guinée**
