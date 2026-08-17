#!/bin/bash
# Script de déploiement pour PythonAnywhere
# Usage: bash deploy.sh

set -e

USER_HOME="$HOME"
PROJECT_DIR="$USER_HOME/Ceremac-Site"
VENV_DIR="$USER_HOME/.virtualenvs/ceremac-env"
REPO_URL="https://github.com/Bella5768/Ceremac-Site.git"

echo "========================================"
echo "Déploiement CEREMAC sur PythonAnywhere"
echo "Utilisateur: $(whoami)"
echo "Home: $USER_HOME"
echo "========================================"

# 1. Cloner ou mettre à jour le projet
if [ -d "$PROJECT_DIR/.git" ]; then
    echo "[1/6] Mise à jour du dépôt existant..."
    cd "$PROJECT_DIR"
    git pull origin main
else
    echo "[1/6] Clonage du dépôt..."
    cd "$USER_HOME"
    git clone "$REPO_URL" Ceremac-Site
    cd "$PROJECT_DIR"
fi

# 2. Virtualenv
if [ -d "$VENV_DIR" ]; then
    echo "[2/6] Activation du virtualenv..."
    source "$VENV_DIR/bin/activate"
else
    echo "[2/6] Virtualenv non trouvé à $VENV_DIR"
    echo "      Création d'un nouveau virtualenv..."
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
fi

# 3. Dépendances
if [ -f "requirements.txt" ]; then
    echo "[3/6] Installation des dépendances..."
    pip install -r requirements.txt
else
    echo "[3/6] requirements.txt introuvable, étape ignorée."
fi

# 4. Migrations
echo "[4/6] Exécution des migrations..."
python manage.py migrate

# 5. Static files
echo "[5/6] Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

# 6. Permissions (optionnel)
echo "[6/6] Vérification des permissions..."
chmod -R 755 "$PROJECT_DIR"

echo "========================================"
echo "Déploiement terminé."
echo "Pensez à recharger l'application web dans l'onglet Web → Reload."
echo "========================================"
