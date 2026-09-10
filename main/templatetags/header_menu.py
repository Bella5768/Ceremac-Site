from django import template
from django.db.models import Prefetch

from main.models import HeaderMenuItem

register = template.Library()


@register.simple_tag
def get_header_menu():
    """Retourne les éléments racines actifs du menu header, avec leurs enfants actifs."""
    active_children = HeaderMenuItem.objects.filter(is_active=True).order_by('order', 'id')
    return (
        HeaderMenuItem.objects
        .filter(is_active=True, parent__isnull=True)
        .order_by('order', 'id')
        .prefetch_related(Prefetch('children', queryset=active_children, to_attr='visible_children'))
    )
