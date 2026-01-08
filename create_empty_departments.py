#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')
django.setup()

from main.models import Department

print("=== CREATION DEPARTEMENTS VIDES ===")

# Suppression des départements existants
Department.objects.all().delete()
print("✓ Anciens départements supprimés")

# Création des 5 départements vides
departments = [
    {'order': 1, 'name': 'Département d\'Océanographie'},
    {'order': 2, 'name': 'Département d\'Hydrobiologie'},
    {'order': 3, 'name': 'Département de Géologie-Environnement'},
    {'order': 4, 'name': 'Département des Énergies et de la Transition énergétique'},
    {'order': 5, 'name': 'Département des Matériaux locaux de Construction et Produits Finis'}
]

# Création des départements vides
for dept_data in departments:
    department = Department.objects.create(**dept_data)
    print(f"✓ Créé: {department.name} (ID: {department.id})")

print(f"\n🎉 Total départements créés: {Department.objects.count()}")
print("\n📋 Liste des départements:")
for dept in Department.objects.all().order_by('order'):
    print(f"  - {dept.order}. {dept.name} (ID: {dept.id})")

print("\n✅ Prêt pour ajout manuel des infos depuis l'admin!")
