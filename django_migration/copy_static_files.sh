#!/bin/bash
# Script pour copier les fichiers statiques vers Django

# Créer les dossiers
mkdir -p static/css static/js static/images

# Copier les fichiers CSS
if [ -d "../assets/css" ]; then
    cp -r ../assets/css/* static/css/
    echo "✓ Fichiers CSS copiés"
fi

# Copier les fichiers JS
if [ -d "../assets/js" ]; then
    cp -r ../assets/js/* static/js/
    echo "✓ Fichiers JS copiés"
fi

# Copier les images
if [ -d "../assets/images" ]; then
    cp -r ../assets/images/* static/images/
    echo "✓ Images copiées"
fi

echo "✅ Tous les fichiers statiques ont été copiés vers static/"

