"""
URL configuration for ceremac_site project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.shortcuts import redirect

def redirect_to_language(request):
    """Redirige vers la langue par défaut"""
    return redirect('/fr/')

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', redirect_to_language, name='root'),  # Redirection explicite vers /fr/
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('admin-panel/', include('admin_panel.urls')),
    path('', include('members.urls')),  # login, logout, et routes members
)

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
