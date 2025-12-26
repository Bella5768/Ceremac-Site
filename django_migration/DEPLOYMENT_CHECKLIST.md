# Checklist de Déploiement sur PythonAnywhere

## ✅ Préparation Locale

- [ ] Tester le projet localement
- [ ] Créer un superutilisateur
- [ ] Vérifier que toutes les migrations sont appliquées
- [ ] Tester l'upload de fichiers
- [ ] Tester l'authentification
- [ ] Vérifier les traductions (FR/EN)

## ✅ Configuration PythonAnywhere

- [ ] Créer un compte PythonAnywhere
- [ ] Uploader le projet (via Git ou interface web)
- [ ] Créer la base de données MySQL
- [ ] Configurer le fichier .env avec les bonnes valeurs
- [ ] Installer les dépendances (`pip3.10 install --user -r requirements.txt`)

## ✅ Base de Données

- [ ] Exécuter `python3.10 manage.py makemigrations`
- [ ] Exécuter `python3.10 manage.py migrate`
- [ ] Importer les données depuis MySQL PHP (si nécessaire)
- [ ] Créer un superutilisateur (`python3.10 manage.py createsuperuser`)

## ✅ Configuration Web

- [ ] Configurer le fichier WSGI (copier depuis pythonanywhere_wsgi.py)
- [ ] Configurer les Static Files:
  - URL: `/static/`
  - Directory: `/home/username/django_migration/staticfiles`
- [ ] Configurer les Media Files:
  - URL: `/media/`
  - Directory: `/home/username/django_migration/media`
- [ ] Exécuter `python3.10 manage.py collectstatic`

## ✅ Fichiers Statiques

- [ ] Copier les fichiers CSS depuis `assets/css/` vers `static/css/`
- [ ] Copier les fichiers JS depuis `assets/js/` vers `static/js/`
- [ ] Copier les images depuis `assets/images/` vers `static/images/`
- [ ] Vérifier que tous les chemins dans les templates utilisent `{% static %}`

## ✅ Templates

- [ ] Créer `templates/base.html` (depuis header.php + footer.php)
- [ ] Créer tous les templates nécessaires
- [ ] Adapter les templates PHP vers Django (voir TEMPLATE_EXAMPLE.md)
- [ ] Tester tous les templates

## ✅ Sécurité

- [ ] Changer `DEBUG = False` dans settings.py (ou .env)
- [ ] Générer un nouveau `SECRET_KEY`
- [ ] Vérifier `ALLOWED_HOSTS`
- [ ] Tester les formulaires avec CSRF

## ✅ Tests Finaux

- [ ] Tester toutes les pages publiques
- [ ] Tester l'authentification
- [ ] Tester l'espace membres
- [ ] Tester le panneau admin
- [ ] Tester l'upload de fichiers
- [ ] Tester le formulaire de contact
- [ ] Tester la newsletter
- [ ] Tester le changement de langue
- [ ] Tester sur mobile (responsive)

## ✅ Post-Déploiement

- [ ] Configurer un domaine personnalisé (si nécessaire)
- [ ] Configurer SSL/HTTPS (si nécessaire)
- [ ] Mettre en place des backups réguliers
- [ ] Configurer les logs
- [ ] Tester les performances

## Commandes Utiles

```bash
# Dans la console Bash de PythonAnywhere
cd ~/django_migration

# Installer les dépendances
pip3.10 install --user -r requirements.txt

# Migrations
python3.10 manage.py makemigrations
python3.10 manage.py migrate

# Collecter les fichiers statiques
python3.10 manage.py collectstatic --noinput

# Créer un superutilisateur
python3.10 manage.py createsuperuser

# Shell Django
python3.10 manage.py shell

# Vérifier la configuration
python3.10 manage.py check
```

## Support

En cas de problème:
1. Vérifier les logs dans PythonAnywhere (Web > Error log)
2. Vérifier la console Bash pour les erreurs
3. Tester localement d'abord
4. Consulter la documentation Django et PythonAnywhere

