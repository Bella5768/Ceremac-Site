# 🔴 Guide de Résolution d'Erreur WSGI PythonAnywhere

## Erreur: `ModuleNotFoundError: No module named 'ceremac_site'`

### ✅ Solution Étape par Étape

#### Étape 1: Vérifier la Structure du Projet

Dans la **console Bash** de PythonAnywhere, exécutez:

```bash
cd ~
ls -la
```

Si vous avez cloné depuis GitHub:
```bash
cd Ceremac-Site
ls -la django_migration/
```

Vous devriez voir:
```
django_migration/
├── ceremac_site/     ← IMPORTANT: Ce dossier doit exister
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── main/
├── admin_panel/
└── members/
```

#### Étape 2: Trouver le Chemin Exact

```bash
cd ~
pwd
find . -name "manage.py" -type f 2>/dev/null | head -1
```

Notez le chemin complet, par exemple:
- `/home/Boubacar32/Ceremac-Site/django_migration/manage.py`

Le chemin du projet sera (sans `/manage.py`):
- `/home/Boubacar32/Ceremac-Site/django_migration`

#### Étape 3: Configurer le Fichier WSGI

1. Allez dans **Web** → **WSGI configuration file**
2. **Supprimez TOUT le contenu existant**
3. **Copiez-collez ce code** (remplacez le chemin si nécessaire):

```python
import os
import sys

# ⚠️ IMPORTANT: Remplacez ce chemin par le vôtre
project_path = '/home/Boubacar32/Ceremac-Site/django_migration'

# Vérifier que le chemin existe
if not os.path.exists(project_path):
    raise Exception(f"❌ ERREUR: Le chemin {project_path} n'existe pas!\nVérifiez le chemin dans la console Bash.")

# Ajouter au PYTHONPATH
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Changer le répertoire de travail
os.chdir(project_path)

# Définir le module de settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')

# Charger l'application Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### Étape 4: Vérifier que Django est Installé

Dans la **console Bash**:

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 -m pip install --user -r requirements.txt
```

#### Étape 5: Tester en Ligne de Commande

```bash
cd /home/Boubacar32/Ceremac-Site/django_migration
python3.10 manage.py check
```

Si cette commande fonctionne, le WSGI devrait aussi fonctionner.

#### Étape 6: Reload l'Application Web

1. Allez dans **Web**
2. Cliquez sur le bouton vert **Reload**
3. Attendez quelques secondes
4. Visitez votre site: `https://boubacar32.pythonanywhere.com`

### 🔍 Vérifications Supplémentaires

#### Si l'erreur persiste:

1. **Vérifier le nom d'utilisateur:**
   ```bash
   whoami
   ```
   Utilisez ce nom dans le chemin WSGI.

2. **Vérifier la structure:**
   ```bash
   cd /home/Boubacar32/Ceremac-Site/django_migration
   ls -la ceremac_site/
   ```
   Vous devriez voir `settings.py`, `urls.py`, `wsgi.py`.

3. **Vérifier les imports Python:**
   ```bash
   cd /home/Boubacar32/Ceremac-Site/django_migration
   python3.10 -c "import sys; sys.path.insert(0, '.'); import ceremac_site.settings; print('✅ OK')"
   ```

4. **Vérifier les logs d'erreur:**
   - Allez dans **Web** → **Error log**
   - Lisez les dernières lignes pour voir l'erreur exacte

### 📝 Exemple de Configuration Complète

Si votre structure est:
```
/home/Boubacar32/
└── Ceremac-Site/
    └── django_migration/
        ├── ceremac_site/
        ├── manage.py
        └── ...
```

Alors le WSGI doit être:
```python
project_path = '/home/Boubacar32/Ceremac-Site/django_migration'
```

### ⚠️ Erreurs Courantes

1. **Chemin incorrect:** Vérifiez avec `pwd` dans la console
2. **Dossier `ceremac_site` manquant:** Vérifiez la structure
3. **Django non installé:** Installez avec `pip install -r requirements.txt`
4. **Mauvais Python:** Utilisez `python3.10` sur PythonAnywhere

### 🆘 Besoin d'Aide?

Si l'erreur persiste, copiez:
1. Le contenu de votre fichier WSGI
2. Le résultat de `ls -la /home/Boubacar32/Ceremac-Site/django_migration/`
3. Les dernières lignes du **Error log**

