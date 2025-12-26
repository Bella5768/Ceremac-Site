# 🚀 Guide de Déploiement sur PythonAnywhere

## ⚠️ Erreur Actuelle: ModuleNotFoundError: No module named 'ceremac_site'

Cette erreur signifie que Python ne trouve pas le module `ceremac_site`. Voici comment corriger:

## 📋 Étapes de Correction

### 1. Vérifier la Structure sur PythonAnywhere

Connectez-vous à PythonAnywhere et vérifiez où se trouve votre projet:

```bash
# Dans la console Bash de PythonAnywhere
cd ~
ls -la
# Trouvez où est votre projet Django
```

### 2. Structure Attendue

Votre projet doit être dans un de ces emplacements:
- `/home/Boubacar32/mysite/django_migration/`
- `/home/Boubacar32/django_migration/`
- `/home/Boubacar32/Ceremac-Site/django_migration/`

### 3. Cloner depuis GitHub (si pas déjà fait)

```bash
cd ~
git clone https://github.com/Bella5768/Ceremac-Site.git
cd Ceremac-Site/django_migration
```

### 4. Configurer le Fichier WSGI

Allez dans **Web** → **WSGI configuration file** sur PythonAnywhere.

**Remplacez TOUT le contenu par:**

```python
import os
import sys

# IMPORTANT: Ajustez ce chemin selon votre structure réelle
# Vérifiez d'abord où se trouve votre projet avec: ls -la ~
path = '/home/Boubacar32/Ceremac-Site/django_migration'

# Si votre projet est ailleurs, changez le chemin ci-dessus
# Par exemple:
# path = '/home/Boubacar32/mysite/django_migration'
# OU
# path = '/home/Boubacar32/django_migration'

if path not in sys.path:
    sys.path.insert(0, path)

# Ajouter le répertoire parent
parent_path = os.path.dirname(path)
if parent_path not in sys.path:
    sys.path.insert(0, parent_path)

# Définir le module de settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'ceremac_site.settings'

# Charger l'application Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 5. Vérifier le Chemin

**Dans la console Bash**, testez:

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 manage.py shell
```

Si ça fonctionne, le chemin est correct. Sinon, trouvez le bon chemin avec:

```bash
find ~ -name "manage.py" -type f
```

### 6. Installer les Dépendances

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
pip3.10 install --user -r requirements.txt
```

### 7. Configurer la Base de Données

```bash
# Créer le fichier .env
nano .env
```

Ajoutez:
```env
SECRET_KEY=votre-secret-key-production
DEBUG=False
ALLOWED_HOSTS=boubacar32.pythonanywhere.com

DB_ENGINE=mysql
DB_NAME=Boubacar32$ceremac_db
DB_USER=Boubacar32
DB_PASSWORD=votre-mot-de-passe-mysql
DB_HOST=Boubacar32.mysql.pythonanywhere-services.com
DB_PORT=3306
```

### 8. Migrations

```bash
python3.10 manage.py makemigrations
python3.10 manage.py migrate
python3.10 manage.py collectstatic --noinput
```

### 9. Créer un Superutilisateur

```bash
python3.10 manage.py createsuperuser
```

### 10. Configurer les Fichiers Statiques

Dans **Web** → **Static files**:

- **URL**: `/static/`
- **Directory**: `/home/Boubacar32/Ceremac-Site/django_migration/staticfiles`

- **URL**: `/media/`
- **Directory**: `/home/Boubacar32/Ceremac-Site/django_migration/media`

### 11. Reload l'Application

Cliquez sur le bouton vert **"Reload"** dans la section Web.

## 🔍 Débogage

### Vérifier le Chemin du Projet

```bash
# Dans la console Bash
find ~ -name "ceremac_site" -type d
find ~ -name "manage.py" -type f
```

### Tester l'Import

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 -c "import sys; sys.path.insert(0, '.'); from ceremac_site import settings; print('OK')"
```

### Vérifier les Logs

Allez dans **Web** → **Error log** pour voir les erreurs détaillées.

## ✅ Checklist

- [ ] Projet cloné depuis GitHub
- [ ] Chemin dans WSGI correct
- [ ] Dépendances installées (`pip3.10 install --user -r requirements.txt`)
- [ ] Fichier `.env` créé avec les bonnes valeurs
- [ ] Migrations appliquées
- [ ] Fichiers statiques configurés
- [ ] Application reloadée

## 📝 Commandes Utiles

```bash
# Vérifier où est le projet
pwd
ls -la

# Tester Django
python3.10 manage.py check

# Voir les erreurs
tail -f /var/log/boubacar32.pythonanywhere.com.error.log
```

