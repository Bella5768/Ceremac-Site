# PythonAnywhere Deployment Guide

## Étapes pour déployer votre site Django sur PythonAnywhere

### 1. Préparation du projet

1. Clonez votre projet sur PythonAnywhere:
```bash
git clone https://github.com/Bella5768/Ceremac-Site.git
```

2. Installez les dépendances:
```bash
pip install -r requirements.txt
```

### 2. Configuration des variables d'environnement

1. Copiez le fichier `.env.pythonanywhere` vers `.env`:
```bash
cp .env.pythonanywhere .env
```

2. Modifiez le `SECRET_KEY` avec une vraie clé secrète

### 3. Configuration de la base de données

**Option 1: SQLite (recommandé pour commencer)**
- Aucune configuration supplémentaire nécessaire
- Le fichier `db.sqlite3` sera créé automatiquement

**Option 2: MySQL**
1. Activez MySQL sur PythonAnywhere
2. Modifiez les variables DB_* dans le fichier `.env`
3. Appliquez les migrations:
```bash
python manage.py migrate
```

### 4. Fichiers statiques

1. Collectez les fichiers statiques:
```bash
python manage.py collectstatic
```

2. Configurez les fichiers statiques dans l'interface PythonAnywhere:
   - Allez dans Web tab → Static files
   - Ajoutez: `/static/` → `/home/Boubacar32/Ceremac-Site/django_migration/staticfiles`

### 5. Configuration WSGI

1. Copiez le contenu de `WSGI_PYTHONANYWHERE.py` dans votre fichier WSGI PythonAnywhere
2. Le chemin est déjà configuré pour: `/home/Boubacar32/Ceremac-Site/django_migration`

### 6. Dépannage

Si vous avez une "Unhandled Exception":

1. **Vérifiez les logs**:
   - Error log: `/var/log/boubacar32.pythonanywhere.com.error.log`
   - Server log: `/var/log/boubacar32.pythonanywhere.com.server.log`

2. **Problèmes courants**:
   - Import manquant: Installez les dépendances avec `pip install -r requirements.txt`
   - Chemin incorrect: Vérifiez que le projet est bien dans `/home/Boubacar32/Ceremac-Site/`
   - Variables d'environnement: Assurez-vous que `.env` existe et est configuré

3. **Commandes utiles**:
```bash
# Vérifier l'installation
python manage.py check

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Vérifier les fichiers statiques
python manage.py collectstatic --noinput
```

### 7. Redémarrage

Après chaque modification, redémarrez votre application web dans l'interface PythonAnywhere (Web tab → Reload).
