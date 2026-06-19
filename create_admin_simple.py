import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')
django.setup()

from main.models import CustomUser

# Créer ou mettre à jour l'utilisateur admin
try:
    admin = CustomUser.objects.get(username='admin')
    admin.is_superuser = True
    admin.is_staff = True
    admin.is_active = True
    admin.role = 'admin'
    admin.can_validate = True
    admin.set_password('admin123')
    admin.save()
    print("Utilisateur admin mis à jour avec succès")
except CustomUser.DoesNotExist:
    admin = CustomUser.objects.create_superuser(
        username='admin',
        email='admin@ceremac.edu.gn',
        password='admin123',
        full_name='Administrateur CEREMAC',
        role='admin',
        can_validate=True
    )
    print("Utilisateur admin créé avec succès")

print("\nIdentifiants de connexion:")
print("Nom d'utilisateur: admin")
print("Mot de passe: admin123")
print("\nURL d'administration: https://ceremac.edu.gn/fr/admin/")
