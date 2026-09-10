#!/bin/bash

# Script de déploiement pour PythonAnywhere
# Ce script doit être exécuté sur le serveur PythonAnywhere

echo "=========================================="
echo "Déploiement CEREMAC sur PythonAnywhere"
echo "=========================================="

# Aller dans le répertoire du projet
cd ~/Ceremac-Site || exit 1

echo "1. Mise à jour du code depuis GitHub..."
git pull origin main

echo "2. Activation de l'environnement virtuel..."
source .venv/bin/activate

echo "3. Installation des dépendances..."
pip install -r requirements.txt

echo "4. Application des migrations..."
python manage.py migrate

echo "5. Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

echo "6. Configuration du menu des départements..."
python setup_departments_menu.py

echo "7. Mise à jour des slugs des services..."
python update_services_slugs.py

echo "=========================================="
echo "Déploiement terminé avec succès !"
echo "=========================================="
echo ""
echo "N'oubliez pas de redémarrer l'application via l'interface web PythonAnywhere :"
echo "https://www.pythonanywhere.com/webapp/"
