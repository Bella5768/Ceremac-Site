#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')
django.setup()

from main.models import Department

# Suppression des départements existants
Department.objects.all().delete()
print("Anciens départements supprimés")

# Création des 5 départements avec vos textes exacts
departments_data = [
    {
        'order': 1,
        'name': 'Département d\'Océanographie',
        'description': "Le Département d'Océanographie est chargé d'étudier des processus hydrodynamiques, hydrométéorologiques et hydrochimiques des eaux de la zone économique exclusive et des zones adjacentes.\n\nIl est composé de deux laboratoires :\n- Le laboratoire de recherche en hydrochimie et photochimie marine ;\n- Le Laboratoire de recherche en physique des océans et en Hydrométéorologie",
        'mission': 'Étudier les processus hydrodynamiques, hydrométéorologiques et hydrochimiques des eaux marines pour comprendre et préserver les écosystèmes océaniques.',
        'head_of_department': 'Dr. Océanologue Principal',
        'email': 'oceanographie@ceremac-gn.org',
        'is_active': True
    },
    {
        'order': 2,
        'name': 'Département d\'Hydrobiologie',
        'description': "La mission assignée à ce Département est d'élaborer et de mettre en œuvre des programmes de recherche dans le domaine des ressources vivantes aquatiques et leurs biotopes en vue de leur valorisation rationnelle pour un développement durable. Il pourrait s'intéresser à d'autres ressources vivantes ayant des interactions avec le milieu et les ressources aquatiques\n\nIl comprend :\n- Le laboratoire de recherche en Planctons\n- Le Laboratoire de recherche en Ichtyologie-Parasitologie, Aquaculture et Benthos",
        'mission': 'Élaborer et mettre en œuvre des programmes de recherche sur les ressources vivantes aquatiques et leurs biotopes pour une valorisation durable.',
        'head_of_department': 'Dr. Hydrobiologiste Principal',
        'email': 'hydrobiologie@ceremac-gn.org',
        'is_active': True
    },
    {
        'order': 3,
        'name': 'Département de Géologie-Environnement',
        'description': "Le Département de Géologie-Environnement a pour mission l'étude des formations géologiques off-shore et on shore ainsi que des produits d'altération des formations en rapport avec les facteurs hydrologiques. Il comprend :\n- Le laboratoire de recherche en Géologie marine, géochimie et minéralogie des sédiments ;\n- Le laboratoire de recherche en Analyses Environnementales et en Systèmes dynamiques ;\n- Le laboratoire de recherche en Géomatique appliquée, Photo-interprétation et Analyses spatiales",
        'mission': 'Étudier les formations géologiques off-shore et on shore ainsi que les produits d\'altération en rapport avec les facteurs hydrologiques.',
        'head_of_department': 'Dr. Géologue-Environnementaliste',
        'email': 'geologie-environnement@ceremac-gn.org',
        'is_active': True
    },
    {
        'order': 4,
        'name': 'Département des Énergies et de la Transition énergétique',
        'description': "Ce département mène la recherche dans le domaine des énergies renouvelables (solaire, thermique et photovoltaïque, bioénergie, énergie éolienne, micro hydro électricité, etc.). Il s'intéresse aux inventaires des gaz à effet de serre, aux mesures d'atténuation et aux stratégies d'adaptation au changement climatique et dispose d'une installation de production de biogaz.\n\nIl comprend :\n- Le laboratoire de recherche en Mesures thermiques et optiques\n- Le laboratoire de recherche en Énergies vertes et Efficacité Énergétique",
        'mission': 'Mener la recherche dans le domaine des énergies renouvelables et développer des stratégies d\'adaptation au changement climatique.',
        'head_of_department': 'Dr. Énergéticien',
        'email': 'energies-transition@ceremac-gn.org',
        'is_active': True
    },
    {
        'order': 5,
        'name': 'Département des Matériaux locaux de Construction et Produits Finis',
        'description': "Ce Département est chargé d'identifier les ressources locales, de conduire des études visant à améliorer les techniques traditionnelles de construction, ainsi que de développer des technologies de fabrication de matériaux, y compris des solutions économiquement avantageuses.\n\nCe département est composé de deux laboratoires :\n- Le laboratoire de recherche en Matériaux Locaux ;\n- Le laboratoire de recherche en Technologies des Matériaux",
        'mission': 'Identifier les ressources locales, améliorer les techniques traditionnelles de construction et développer des technologies de matériaux avantageuses.',
        'head_of_department': 'Dr. Matériaux',
        'email': 'materiaux-construction@ceremac-gn.org',
        'is_active': True
    }
]

# Création des départements
for dept_data in departments_data:
    department = Department.objects.create(**dept_data)
    print(f"✓ Créé: {department.name} (ID: {department.id})")

print(f"\n🎉 Total départements créés: {Department.objects.count()}")
print("📋 Liste des départements:")
for dept in Department.objects.all().order_by('order'):
    print(f"  - {dept.order}. {dept.name} (ID: {dept.id})")
