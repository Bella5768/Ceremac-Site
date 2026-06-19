import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')
django.setup()

from main.models import CustomUser, News, Project, Publication, Partner, Department, HeroImage
from django.utils import timezone

# Créer un utilisateur administrateur
print("Création d'un utilisateur administrateur...")
# Vérifier si l'utilisateur existe déjà
if CustomUser.objects.filter(username='admin').exists():
    admin_user = CustomUser.objects.get(username='admin')
    admin_user.email = 'admin@ceremac.org'
    admin_user.full_name = 'Administrateur CEREMAC'
    admin_user.role = 'admin'
    admin_user.can_validate = True
    admin_user.set_password('admin123')
    admin_user.save()
    print(f"Utilisateur admin mis à jour: {admin_user.username}")
else:
    admin_user = CustomUser.objects.create_superuser(
        username='admin',
        email='admin@ceremac.org',
        password='admin123',
        full_name='Administrateur CEREMAC',
        role='admin',
        can_validate=True
    )
    print(f"Utilisateur admin créé: {admin_user.username}")

# Créer quelques actualités
print("\nCréation d'actualités...")
news_items = [
    {
        'title': 'Nouveau projet de recherche sur l\'océanographie',
        'content': 'Le CEREMAC lance un nouveau projet ambitieux visant à étudier les courants marins de la côte guinéenne. Ce projet permettra de mieux comprendre les écosystèmes marins et de contribuer à la préservation de la biodiversité marine.',
    },
    {
        'title': 'Conférence internationale sur les énergies renouvelables',
        'content': 'Le CEREMAC organise une conférence internationale sur les énergies renouvelables qui se tiendra à Conakry le mois prochain. Des experts du monde entier seront présents pour partager leurs connaissances et expériences.',
    },
    {
        'title': 'Publication des résultats du département Hydrobiologie',
        'content': 'Le département d\'Hydrobiologie publie ses derniers résultats de recherche sur la qualité des eaux douces en Guinée. Ces données sont cruciales pour la gestion des ressources en eau.',
    },
]

for news_data in news_items:
    news, created = News.objects.get_or_create(
        title=news_data['title'],
        defaults=news_data
    )
    if created:
        print(f"Actualité créée: {news.title}")
    else:
        print(f"Actualité existe déjà: {news.title}")

# Créer des projets
print("\nCréation de projets...")
projects = [
    {
        'title': 'Étude des écosystèmes marins guinéens',
        'description': 'Projet de recherche sur la biodiversité marine et les écosystèmes côtiers de la Guinée.',
        'status': 'current',
    },
    {
        'title': 'Développement de matériaux locaux',
        'description': 'Recherche sur l\'utilisation de matériaux locaux pour la construction durable.',
        'status': 'current',
    },
    {
        'title': 'Cartographie géologique',
        'description': 'Projet terminé de cartographie géologique de la région de Kindia.',
        'status': 'past',
    },
]

for project_data in projects:
    project, created = Project.objects.get_or_create(
        title=project_data['title'],
        defaults=project_data
    )
    if created:
        print(f"Projet créé: {project.title}")
    else:
        print(f"Projet existe déjà: {project.title}")

# Créer des publications
print("\nCréation de publications...")
publications = [
    {
        'title': 'Analyse des courants marins en Guinée',
        'author': 'Dr. Mamadou Diallo',
        'description': 'Étude détaillée des courants marins et de leur impact sur l\'écosystème côtier.',
        'publication_date': timezone.now().date(),
    },
    {
        'title': 'Propriétés des matériaux de construction locaux',
        'author': 'Pr. Aïcha Koné',
        'description': 'Analyse physico-chimique des matériaux locaux pour la construction.',
        'publication_date': timezone.now().date(),
    },
]

for pub_data in publications:
    pub, created = Publication.objects.get_or_create(
        title=pub_data['title'],
        defaults=pub_data
    )
    if created:
        print(f"Publication créée: {pub.title}")
    else:
        print(f"Publication existe déjà: {pub.title}")

# Créer des partenaires
print("\nCréation de partenaires...")
partners = [
    {
        'name': 'Université de Conakry',
        'type': 'national',
        'website': 'https://univ-conakry.org',
        'description': 'Partenaire académique majeur pour les projets de recherche.',
    },
    {
        'name': 'UNESCO',
        'type': 'international',
        'website': 'https://unesco.org',
        'description': 'Organisation internationale soutenant nos projets de recherche.',
    },
    {
        'name': 'Ministère de l\'Enseignement Supérieur',
        'type': 'national',
        'description': 'Partenaire institutionnel pour le développement de la recherche.',
    },
]

for partner_data in partners:
    partner, created = Partner.objects.get_or_create(
        name=partner_data['name'],
        defaults=partner_data
    )
    if created:
        print(f"Partenaire créé: {partner.name}")
    else:
        print(f"Partenaire existe déjà: {partner.name}")

# Créer une image hero
print("\nCréation d'une image hero...")
hero, created = HeroImage.objects.get_or_create(
    title='Bienvenue au CEREMAC',
    defaults={
        'description': 'Centre d\'Études et de Recherche en Environnement, Matériaux et Chimie',
        'order': 0,
        'is_active': True
    }
)
if created:
    print(f"Image hero créée: {hero.title}")
else:
    print(f"Image hero existe déjà: {hero.title}")

print("\n" + "="*50)
print("Création terminée avec succès!")
print("="*50)
print(f"\nUtilisateur admin:")
print(f"  Nom d'utilisateur: admin")
print(f"  Mot de passe: admin123")
print(f"\nVous pouvez maintenant vous connecter à:")
print(f"  - Interface d'administration: http://localhost:8000/admin/")
print(f"  - Page de connexion: http://localhost:8000/login/")
