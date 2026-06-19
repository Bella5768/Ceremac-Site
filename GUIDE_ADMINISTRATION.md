# Guide d'Administration du Site CEREMAC

## Connexion à l'interface d'administration

1. **URL de connexion:** https://ceremac-g.org/admin/
2. **Identifiants:**
   - Nom d'utilisateur: `admin`
   - Mot de passe: `admin123`

## Sections disponibles dans l'administration

### 1. Gestion des Utilisateurs (CustomUser)
- **Accès:** Auth → Users
- **Actions possibles:**
  - Créer de nouveaux utilisateurs
  - Modifier les rôles (admin/member)
  - Activer/désactiver les droits de validation
  - Gérer les informations personnelles

### 2. Gestion des Actualités (News)
- **Accès:** Main → News
- **Champs à remplir:**
  - `title`: Titre de l'actualité
  - `content`: Contenu de l'actualité
  - `image`: Image optionnelle
- **Actions:** Ajouter, modifier, supprimer des actualités

### 3. Gestion des Projets (Project)
- **Accès:** Main → Projects
- **Champs à remplir:**
  - `title`: Titre du projet
  - `description`: Description détaillée
  - `image`: Image du projet
  - `file_path`: Fichier/document associé
  - `status`: Statut (En cours/Terminé)
  - `date_start`: Date de début
  - `date_end`: Date de fin

### 4. Gestion des Publications (Publication)
- **Accès:** Main → Publications
- **Champs à remplir:**
  - `title`: Titre de la publication
  - `author`: Auteur(s)
  - `description`: Résumé
  - `file_path`: Fichier PDF
  - `publication_date`: Date de publication

### 5. Gestion des Partenaires (Partner)
- **Accès:** Main → Partners
- **Champs à remplir:**
  - `name`: Nom du partenaire
  - `logo`: Logo du partenaire
  - `website`: Site web
  - `type`: National/International
  - `description`: Description

### 6. Gestion des Départements (Department)
- **Accès:** Main → Departments
- **Champs à remplir:**
  - `name`: Nom du département
  - `order`: Ordre d'affichage (1-5)
  - `description`: Description
  - `mission`: Mission du département
  - `image`: Image du département
  - `head_of_department`: Chef de département
  - `email`: Email
  - `phone`: Téléphone

### 7. Projets par Département (DepartmentProject)
- **Accès:** Main → Department Projects
- Permet d'ajouter des projets spécifiques à chaque département

### 8. Publications par Département (DepartmentPublication)
- **Accès:** Main → Department Publications
- Permet d'ajouter des publications spécifiques à chaque département

### 9. Membres par Département (DepartmentMember)
- **Accès:** Main → Department Members
- **Champs à remplir:**
  - `department`: Département d'appartenance
  - `name`: Nom du membre
  - `position`: Poste
  - `email`: Email
  - `phone`: Téléphone
  - `photo`: Photo du membre
  - `bio`: Biographie
  - `is_head`: Est-ce le chef?

### 10. Images Hero (HeroImage)
- **Accès:** Main → Hero Images
- **Champs à remplir:**
  - `title`: Titre de l'image
  - `description`: Description affichée
  - `image`: Image (recommandé: 1920x600px)
  - `order`: Ordre d'affichage
  - `is_active`: Activer/désactiver

### 11. Messages de Contact (ContactMessage)
- **Accès:** Main → Contact Messages
- Permet de voir et gérer les messages envoyés via le formulaire de contact

### 12. Abonnés Newsletter (NewsletterSubscriber)
- **Accès:** Main → Newsletter Subscribers
- Gestion des abonnés à la newsletter

## Étapes recommandées pour compléter le site

### Étape 1: Configurer les départements
1. Allez dans Main → Departments
2. Créez les 5 départements avec leurs informations
3. Ajoutez les membres de chaque département
4. Ajoutez les projets et publications par département

### Étape 2: Ajouter du contenu principal
1. **Actualités:** Ajoutez des nouvelles et événements
2. **Projets:** Ajoutez les projets de recherche
3. **Publications:** Ajoutez les publications scientifiques
4. **Partenaires:** Ajoutez les partenaires institutionnels

### Étape 3: Configurer l'apparence
1. Allez dans Main → Hero Images
2. Ajoutez des images pour le carrousel de la page d'accueil
3. Utilisez des images de haute qualité (1920x600px)

### Étape 4: Gérer les utilisateurs
1. Allez dans Auth → Users
2. Créez des comptes pour les membres du personnel
3. Attribuez les rôles appropriés (admin/member)

## Conseils importants

- **Sauvegardez régulièrement** votre travail
- **Utilisez des images optimisées** pour le web
- **Remplissez tous les champs** pour une meilleure présentation
- **Vérifiez les permissions** des utilisateurs créés
- **Testez les modifications** sur le site public

## Dépannage

### Problème de connexion
- Vérifiez que vous utilisez les bons identifiants
- Si oublié du mot de passe, recréez l'utilisateur avec:
  ```bash
  python manage.py createsuperuser
  ```

### Images ne s'affichent pas
- Vérifiez que les fichiers sont bien uploadés
- Vérifiez les permissions sur le dossier media/

### Modifications ne s'affichent pas
- Videz le cache de votre navigateur
- Vérifiez que le champ `is_active` est coché pour les éléments concernés

## Support

Pour toute question ou problème technique, contactez l'administrateur système.
