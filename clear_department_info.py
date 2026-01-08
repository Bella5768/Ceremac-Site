#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')
django.setup()

from main.models import Department, DepartmentProject, DepartmentPublication, DepartmentMember

print("=== VIDAGE DES INFORMATIONS DES DEPARTEMENTS ===")

# Vider les informations des départements (garder la structure)
try:
    departments = Department.objects.all()
    dept_count = 0
    for dept in departments:
        if dept.description or dept.mission or dept.head_of_department or dept.email:
            dept.description = ""
            dept.mission = ""
            dept.head_of_department = ""
            dept.email = ""
            dept.save()
            dept_count += 1
            print(f"✓ Informations vidées pour: {dept.name}")
    
    print(f"\n✓ {dept_count} départements vidés (structure conservée)")
except Exception as e:
    print(f"✗ Erreur vidage départements: {e}")

# Vider les projets de département
try:
    projects = DepartmentProject.objects.all()
    project_count = projects.count()
    if project_count > 0:
        projects.delete()
        print(f"✓ {project_count} projets de département supprimés")
except Exception as e:
    print(f"✗ Erreur suppression projets: {e}")

# Vider les publications de département
try:
    publications = DepartmentPublication.objects.all()
    pub_count = publications.count()
    if pub_count > 0:
        publications.delete()
        print(f"✓ {pub_count} publications de département supprimées")
except Exception as e:
    print(f"✗ Erreur suppression publications: {e}")

# Vider les membres de département
try:
    members = DepartmentMember.objects.all()
    member_count = members.count()
    if member_count > 0:
        members.delete()
        print(f"✓ {member_count} membres de département supprimés")
except Exception as e:
    print(f"✗ Erreur suppression membres: {e}")

print("\n=== VERIFICATION ===")
try:
    departments = Department.objects.all()
    print(f"Départements conservés: {departments.count()}")
    for dept in departments:
        print(f"  - {dept.order}. {dept.name} (ID: {dept.id})")
        print(f"    Description: '{dept.description}'")
        print(f"    Mission: '{dept.mission}'")
    print("\n✅ Structure conservée - informations vidées!")
    print("🎯 Prêt pour ajout manuel des infos depuis l'admin!")
except Exception as e:
    print(f"✗ Erreur vérification: {e}")

print("\n=== FIN VIDAGE ===")
