from django.db import migrations


DEFAULT_MENU = [
    {'title': 'Accueil', 'url': 'main:index', 'icon': 'bi-house-door', 'order': 1, 'children': []},
    {'title': 'À propos', 'url': 'main:about', 'icon': 'bi-info-circle', 'order': 2, 'children': []},
    {'title': 'Départements', 'url': 'main:projects', 'icon': 'bi-building', 'order': 3, 'children': []},
    {'title': 'Recherche', 'url': '', 'icon': 'bi-lightbulb', 'order': 4, 'children': [
        {'title': 'Projets & Innovation', 'url': 'main:research', 'order': 1},
        {'title': 'Publications', 'url': 'main:publications', 'order': 2},
        {'title': 'Bibliothèque numérique', 'url': 'main:library', 'order': 3},
    ]},
    {'title': 'Actualités', 'url': '', 'icon': 'bi-newspaper', 'order': 5, 'children': [
        {'title': 'Articles & Communiqués', 'url': 'main:news_list', 'order': 1},
        {'title': 'Événements', 'url': 'main:events', 'order': 2},
        {'title': 'Agenda scientifique', 'url': 'main:scientific_agenda', 'order': 3},
    ]},
    {'title': 'Partenariats', 'url': 'main:partners', 'icon': 'bi-handshake', 'order': 6, 'children': []},
    {'title': 'Contact', 'url': 'main:contact', 'icon': 'bi-envelope', 'order': 7, 'children': []},
]


def seed_header_menu(apps, schema_editor):
    HeaderMenuItem = apps.get_model('main', 'HeaderMenuItem')
    if HeaderMenuItem.objects.exists():
        return

    for entry in DEFAULT_MENU:
        parent = HeaderMenuItem.objects.create(
            title=entry['title'],
            url=entry['url'],
            icon=entry['icon'],
            order=entry['order'],
            is_active=True,
        )
        for child in entry['children']:
            HeaderMenuItem.objects.create(
                title=child['title'],
                url=child['url'],
                icon='',
                order=child['order'],
                is_active=True,
                parent=parent,
            )


def unseed_header_menu(apps, schema_editor):
    HeaderMenuItem = apps.get_model('main', 'HeaderMenuItem')
    HeaderMenuItem.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_headermenuitem_options_headermenuitem_icon_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_header_menu, unseed_header_menu),
    ]
