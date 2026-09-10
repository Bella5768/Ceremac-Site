#!/bin/bash

# Script de déploiement complet - Local + PythonAnywhere
# Ce script doit être exécuté localement

echo "=========================================="
echo "Déploiement complet CEREMAC"
echo "=========================================="

# 1. Commit et push vers GitHub
echo "1. Commit et push vers GitHub..."
git add .
git commit -m "Mise à jour automatique - $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main

if [ $? -ne 0 ]; then
    echo "Erreur lors du push vers GitHub"
    exit 1
fi

echo "✓ Code poussé sur GitHub avec succès"

# 2. Déploiement sur PythonAnywhere (nécessite SSH)
echo ""
echo "2. Déploiement sur PythonAnywhere..."
echo "Veuillez vous assurer d'avoir accès SSH à PythonAnywhere"
echo ""

# Demander si l'utilisateur veut déployer sur PythonAnywhere
read -p "Voulez-vous déployer sur PythonAnywhere maintenant ? (o/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Oo]$ ]]; then
    echo "Connexion à PythonAnywhere..."
    # Remplacez votre_username par votre nom d'utilisateur PythonAnywhere
    ssh votre_username@ssh.pythonanywhere.com 'cd ~/Ceremac-Site && git pull && source .venv/bin/activate && python manage.py migrate && python manage.py collectstatic --noinput && python setup_departments_menu.py && python update_services_slugs.py'
    
    if [ $? -eq 0 ]; then
        echo "✓ Déploiement sur PythonAnywhere réussi"
        echo "⚠ N'oubliez pas de redémarrer l'application via l'interface web PythonAnywhere"
    else
        echo "✗ Erreur lors du déploiement sur PythonAnywhere"
        echo "Veuillez vérifier votre connexion SSH et vos identifiants"
    fi
else
    echo "Déploiement sur PythonAnywhere annulé"
    echo "Vous pourrez le faire manuellement plus tard"
fi

echo ""
echo "=========================================="
echo "Déploiement terminé !"
echo "=========================================="
