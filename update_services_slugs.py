import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceremac_site.settings')
django.setup()

from main.models import Service
from django.utils.text import slugify

# Mettre à jour les services existants avec des slugs
services = Service.objects.all()
for service in services:
    if not service.slug:
        service.slug = slugify(service.title)
        service.save()
        print(f"✓ Service '{service.title}' mis à jour avec slug: {service.slug}")
    else:
        print(f"- Service '{service.title}' a déjà un slug: {service.slug}")

print(f"\nTotal des services mis à jour: {services.count()}")
