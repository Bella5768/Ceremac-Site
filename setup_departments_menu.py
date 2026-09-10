import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')
django.setup()

from main.models import HeaderMenuItem

# Supprimer les éléments de menu existants liés aux départements/services
HeaderMenuItem.objects.filter(title__in=['Départements', 'Services']).delete()

# Créer l'élément parent "Départements"
departments_parent = HeaderMenuItem.objects.create(
    title='Départements',
    url='',
    icon='bi-building',
    order=3,
    is_active=True,
    parent=None
)

# Créer le sous-élément "Départements" qui pointe vers la page des départements
departments_child = HeaderMenuItem.objects.create(
    title='Départements',
    url='main:projects',
    icon='bi-building',
    order=1,
    is_active=True,
    parent=departments_parent
)

# Créer le sous-élément "Services" qui pointe vers la page des services
services_child = HeaderMenuItem.objects.create(
    title='Services',
    url='main:services',
    icon='bi-gear',
    order=2,
    is_active=True,
    parent=departments_parent
)

print("✓ Menu des départements créé avec succès")
print(f"  - Élément parent: {departments_parent.title}")
print(f"  - Sous-élément 1: {departments_child.title} -> {departments_child.url}")
print(f"  - Sous-élément 2: {services_child.title} -> {services_child.url}")
