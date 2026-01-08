#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')
django.setup()

from main.models import Department

# Mise à jour des descriptions avec les vraies informations officielles
departments_updates = {
    1: {
        'description': 'Le Departement d\'Oceanographie est charge d\'etudier les processus hydrodynamiques, hydrometeorologiques et hydrochimiques des eaux de la zone economique exclusive et des zones adjacentes.',
        'mission': 'Etudier les processus hydrodynamiques, hydrometeorologiques et hydrochimiques des eaux marines pour comprendre et preserver les ecosystemes oceaniques.',
        'head_of_department': 'Dr. Oceanologue Principal',
        'email': 'oceanographie@ceremac-gn.org'
    },
    2: {
        'description': 'La mission assignee a ce Departement est d\'elaborer et de mettre en oeuvre des programmes de recherche dans le domaine des ressources vivantes aquatiques et leurs biotopes en vue de leur valorisation rationnelle pour un developpement durable.',
        'mission': 'Elaborer et mettre en oeuvre des programmes de recherche sur les ressources vivantes aquatiques et leurs biotopes pour une valorisation rationnelle et un developpement durable.',
        'head_of_department': 'Dr. Hydrobiologiste Principal',
        'email': 'hydrobiologie@ceremac-gn.org'
    },
    3: {
        'description': 'Le Departement de Geologie-Environnement a pour mission l\'etude des formations geologiques off-shore et on shore ainsi que des produits d\'alteration des formations en rapport avec les facteurs hydrologiques.',
        'mission': 'Etudier les formations geologiques off-shore et on shore ainsi que les produits d\'alteration des formations en rapport avec les facteurs hydrologiques.',
        'head_of_department': 'Dr. Geologue-Environnementaliste',
        'email': 'geologie-environnement@ceremac-gn.org'
    },
    4: {
        'description': 'Ce departement mene la recherche dans le domaine des energies renouvelables (solaire, thermique et photovoltaique, bioenergie, energie eolienne, micro hydro electricite, etc.). Il s\'interesse aux inventaires des gaz a effet de serre, aux mesures d\'attenuation et aux strategies d\'adaptation au changement climatique.',
        'mission': 'Mener la recherche dans le domaine des energies renouvelables et developper des strategies d\'adaptation au changement climatique avec une installation de production de biogaz.',
        'head_of_department': 'Dr. Energeticien',
        'email': 'energies-transition@ceremac-gn.org'
    },
    5: {
        'description': 'Ce Departement est charge d\'identifier les ressources locales, de conduire des etudes visant a ameliorer les techniques traditionnelles de construction, ainsi que de developper des technologies de fabrication de materiaux, y compris des solutions economiquement avantageuses.',
        'mission': 'Identifier les ressources locales, ameliorer les techniques traditionnelles de construction et developper des technologies de fabrication de materiaux economiquement avantageuses.',
        'head_of_department': 'Dr. Materiaux',
        'email': 'materiaux-construction@ceremac-gn.org'
    }
}

print("Mise a jour des descriptions officielles des departements...")

for order, updates in departments_updates.items():
    try:
        department = Department.objects.get(order=order)
        department.description = updates['description']
        department.mission = updates['mission']
        department.head_of_department = updates['head_of_department']
        department.email = updates['email']
        department.save()
        print(f"Mis a jour: {department.name}")
    except Department.DoesNotExist:
        print(f"Departement avec order={order} non trouve")

print("\nMise a jour terminee!")
print(f"Total departements mis a jour: {len(departments_updates)}")
