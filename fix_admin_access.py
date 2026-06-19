import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')
django.setup()

from main.models import CustomUser

# Lister tous les utilisateurs
print("Liste des utilisateurs dans la base de données:")
print("="*50)
users = CustomUser.objects.all()
for user in users:
    print(f"Username: {user.username}")
    print(f"  Email: {user.email}")
    print(f"  Superuser: {user.is_superuser}")
    print(f"  Staff: {user.is_staff}")
    print(f"  Active: {user.is_active}")
    print(f"  Role: {user.role}")
    print(f"  Can validate: {user.can_validate}")
    print("-"*30)

# Demander quel utilisateur corriger
username = input("\nEntrez le nom d'utilisateur à corriger (ou appuyez sur Entrée pour créer 'admin'): ").strip()

if not username:
    username = 'admin'

# Vérifier si l'utilisateur existe
try:
    user = CustomUser.objects.get(username=username)
    print(f"\nUtilisateur '{username}' trouvé.")
    
    # Activer les droits admin
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.role = 'admin'
    user.can_validate = True
    user.save()
    
    print(f"\n✓ Utilisateur '{username}' configuré comme administrateur")
    print(f"  - is_superuser: {user.is_superuser}")
    print(f"  - is_staff: {user.is_staff}")
    print(f"  - is_active: {user.is_active}")
    print(f"  - role: {user.role}")
    
except CustomUser.DoesNotExist:
    print(f"\nUtilisateur '{username}' non trouvé.")
    create = input("Voulez-vous créer cet utilisateur? (o/n): ").strip().lower()
    
    if create == 'o':
        email = input("Email: ").strip()
        password = input("Mot de passe: ").strip()
        
        user = CustomUser.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            full_name='Administrateur CEREMAC',
            role='admin',
            can_validate=True
        )
        
        print(f"\n✓ Utilisateur '{username}' créé avec succès")
        print(f"  - is_superuser: {user.is_superuser}")
        print(f"  - is_staff: {user.is_staff}")
        print(f"  - is_active: {user.is_active}")

print("\n" + "="*50)
print("URLs d'accès:")
print(f"  - Admin: https://ceremac.edu.gn/fr/admin/")
print(f"  - Login: https://ceremac.edu.gn/fr/login/")
print("="*50)
