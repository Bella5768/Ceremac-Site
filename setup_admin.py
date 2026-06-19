import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')
django.setup()
from main.models import CustomUser
try:
    admin = CustomUser.objects.get(username='admin')
    admin.is_superuser = True
    admin.is_staff = True
    admin.is_active = True
    admin.role = 'admin'
    admin.can_validate = True
    admin.set_password('admin123')
    admin.save()
    print('Admin updated')
except:
    admin = CustomUser.objects.create_superuser(username='admin', email='admin@ceremac.edu.gn', password='admin123', full_name='Admin CEREMAC', role='admin', can_validate=True)
    print('Admin created')
print('Done. Login: admin/admin123 at https://ceremac.edu.gn/fr/admin/')
