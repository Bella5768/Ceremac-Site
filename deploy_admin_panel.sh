#!/bin/bash
# Script de déploiement du panneau d'administration sur PythonAnywhere

echo "Déploiement du panneau d'administration CEREMAC..."

# Se connecter au serveur et exécuter les commandes
ssh ceremacsite@ssh.pythonanywhere.com << 'ENDSSH'
cd ~/Ceremac-Site
source venv/bin/activate

# Arrêter l'application temporairement
echo "Arrêt de l'application..."
touch /var/www/ceremacsite_pythonanywhere_com_wsgi.py.restart

# Mettre à jour le code (si git)
# git pull origin main

# Installer les dépendances
echo "Installation des dépendances..."
pip install -r requirements.txt

# Appliquer les migrations
echo "Application des migrations..."
python manage.py migrate

# Collecter les fichiers statiques
echo "Collection des fichiers statiques..."
python manage.py collectstatic --noinput

# Redémarrer l'application
echo "Redémarrage de l'application..."
touch /var/www/ceremacsite_pythonanywhere_com_wsgi.py.restart

echo "Déploiement terminé!"
ENDSSH

echo "Le panneau d'administration a été déployé avec succès."
echo "Accédez à: https://ceremac.edu.gn/fr/admin-panel/"
