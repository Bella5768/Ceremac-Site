# Guide d'installation - Site CEREMAC

## Installation rapide

### 1. Prérequis
- WAMP/XAMPP installé et démarré
- PHP 7.4 ou supérieur
- MySQL/MariaDB
- Navigateur web moderne

### 2. Étapes d'installation

#### Étape 1 : Base de données
1. Ouvrir phpMyAdmin : http://localhost/phpmyadmin
2. Créer une nouvelle base de données nommée `ceremac_db`
3. Importer le fichier `database.sql` dans cette base de données
   - Cliquer sur "Importer"
   - Sélectionner le fichier `database.sql`
   - Cliquer sur "Exécuter"

#### Étape 2 : Configuration
1. Ouvrir le fichier `config/database.php`
2. Vérifier/modifier les paramètres de connexion :
   ```php
   define('DB_HOST', 'localhost');
   define('DB_NAME', 'ceremac_db');
   define('DB_USER', 'root');
   define('DB_PASS', '');  // Mettre votre mot de passe MySQL si nécessaire
   ```

3. Ouvrir le fichier `config/config.php`
4. Vérifier l'URL de base :
   ```php
   define('BASE_URL', 'http://localhost/Ceremac-Site/');
   ```
   Modifier si votre URL est différente.

#### Étape 3 : Permissions
Assurez-vous que les dossiers suivants ont les permissions d'écriture :
- `uploads/`
- `documents/`

#### Étape 4 : Accès au site
1. Ouvrir votre navigateur
2. Aller à : http://localhost/Ceremac-Site/
3. Le site devrait s'afficher correctement

### 3. Connexion à l'espace membres

**Identifiants par défaut :**
- Username : `admin`
- Password : `admin123`

⚠️ **IMPORTANT** : Changez immédiatement le mot de passe après la première connexion !

### 4. Vérification

Vérifiez que :
- ✅ Le site s'affiche correctement
- ✅ La navigation fonctionne
- ✅ Le changement de langue fonctionne
- ✅ Le formulaire de contact fonctionne
- ✅ La connexion à l'espace membres fonctionne

### 5. Personnalisation

#### Ajouter du contenu
- **Actualités** : Ajouter dans la table `news`
- **Projets** : Ajouter dans la table `projects`
- **Publications** : Ajouter dans la table `publications`
- **Partenaires** : Ajouter dans la table `partners`

#### Modifier le design
- Couleurs : `assets/css/style.css` (variables CSS)
- Logo : Remplacer dans `includes/header.php`

#### Ajouter des traductions
- Modifier `config/translations.php`

## Dépannage

### Erreur de connexion à la base de données
- Vérifier que MySQL est démarré
- Vérifier les identifiants dans `config/database.php`
- Vérifier que la base de données `ceremac_db` existe

### Pages blanches
- Activer l'affichage des erreurs PHP dans `php.ini`
- Vérifier les logs d'erreur Apache

### Images non affichées
- Vérifier que les dossiers `uploads/` et `documents/` existent
- Vérifier les permissions d'écriture

## Support

Pour toute question, consultez le fichier `README.md` ou contactez l'équipe de développement.


