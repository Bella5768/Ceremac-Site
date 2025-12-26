from django.conf import settings


def base_context(request):
    """Context processor pour les variables globales"""
    return {
        'BASE_URL': request.build_absolute_uri('/'),
        'MEDIA_URL': settings.MEDIA_URL,
        'STATIC_URL': settings.STATIC_URL,
    }

