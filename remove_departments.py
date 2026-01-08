#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')
django.setup()

from main.models import Department, DepartmentProject, DepartmentPublication, DepartmentMember

print("=== SUPPRESSION COMPLETE DES DEPARTEMENTS ===")

# Suppression des membres de département
try:
    member_count = DepartmentMember.objects.count()
    DepartmentMember.objects.all().delete()
    print(f"✓ {member_count} membres de département supprimés")
except Exception as e:
    print(f"✗ Erreur suppression membres: {e}")

# Suppression des publications de département
try:
    pub_count = DepartmentPublication.objects.count()
    DepartmentPublication.objects.all().delete()
    print(f"✓ {pub_count} publications de département supprimées")
except Exception as e:
    print(f"✗ Erreur suppression publications: {e}")

# Suppression des projets de département
try:
    project_count = DepartmentProject.objects.count()
    DepartmentProject.objects.all().delete()
    print(f"✓ {project_count} projets de département supprimés")
except Exception as e:
    print(f"✗ Erreur suppression projets: {e}")

# Suppression des départements
try:
    dept_count = Department.objects.count()
    Department.objects.all().delete()
    print(f"✓ {dept_count} départements supprimés")
except Exception as e:
    print(f"✗ Erreur suppression départements: {e}")

print("\n=== VERIFICATION ===")
try:
    remaining = Department.objects.count()
    print(f"Départements restants: {remaining}")
    if remaining == 0:
        print("✅ TOUS LES DEPARTEMENTS SUPPRIMES!")
        print("🎯 Prêt pour création manuelle depuis l'admin!")
    else:
        print("⚠️ Certains départements n'ont pas été supprimés")
except Exception as e:
    print(f"✗ Erreur vérification: {e}")

print("\n=== FIN SUPPRESSION ===")
