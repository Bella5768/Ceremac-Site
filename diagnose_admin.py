#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')
django.setup()

print("=== DIAGNOSTIC ADMIN DJANGO ===")

# Vérification des modèles
try:
    from main.models import Department, DepartmentProject, DepartmentPublication, DepartmentMember
    print("✓ Modèles importés avec succès")
    print(f"  - Department: {Department._meta.verbose_name_plural}")
    print(f"  - DepartmentProject: {DepartmentProject._meta.verbose_name_plural}")
    print(f"  - DepartmentPublication: {DepartmentPublication._meta.verbose_name_plural}")
    print(f"  - DepartmentMember: {DepartmentMember._meta.verbose_name_plural}")
except ImportError as e:
    print(f"✗ Erreur import modèles: {e}")

# Vérification admin
try:
    from django.contrib import admin
    from main.admin import DepartmentAdmin, DepartmentProjectAdmin, DepartmentPublicationAdmin, DepartmentMemberAdmin
    print("✓ Classes admin importées")
except ImportError as e:
    print(f"✗ Erreur import admin: {e}")

# Vérification enregistrement admin
try:
    from main.models import Department
    print(f"✓ Department enregistré dans admin: {admin.site.is_registered(Department)}")
    if not admin.site.is_registered(Department):
        # Forcer l'enregistrement
        from main.admin import DepartmentAdmin
        admin.site.register(Department, DepartmentAdmin)
        print("✓ Department enregistré manuellement")
except Exception as e:
    print(f"✗ Erreur vérification admin: {e}")

# Vérification départements existants
try:
    from main.models import Department
    count = Department.objects.count()
    print(f"✓ Départements dans la base: {count}")
    if count > 0:
        for dept in Department.objects.all():
            print(f"  - {dept.order}. {dept.name}")
except Exception as e:
    print(f"✗ Erreur base de données: {e}")

print("\n=== FIN DIAGNOSTIC ===")
