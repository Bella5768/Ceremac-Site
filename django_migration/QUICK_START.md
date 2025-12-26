# Guide de Démarrage Rapide - Django CEREMAC

## 🚀 Installation en 5 minutes

### 1. Préparer l'environnement
```bash
cd django_migration
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configurer
```bash
cp .env.example .env
# Éditer .env avec vos paramètres de base de données
```

### 3. Base de données
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Copier les fichiers statiques
```bash
# Depuis le projet PHP
mkdir -p static/css static/js static/images
cp ../Ceremac-Site/assets/css/* static/css/
cp ../Ceremac-Site/assets/js/* static/js/
cp ../Ceremac-Site/assets/images/* static/images/
```

### 5. Lancer
```bash
python manage.py runserver
```

Visitez http://127.0.0.1:8000/

## 📁 Structure des Templates à Créer

Créez ces fichiers dans `templates/`:

```
templates/
├── base.html              # Template de base (header + footer)
├── main/
│   ├── index.html         # Page d'accueil
│   ├── about.html         # À propos
│   ├── projects.html      # Services et Directions
│   ├── project_detail.html
│   ├── publications.html
│   ├── partners.html
│   ├── news_list.html
│   ├── news_detail.html
│   └── contact.html
├── admin_panel/
│   ├── index.html
│   ├── news.html
│   ├── projects.html
│   ├── publications.html
│   ├── partners.html
│   ├── users.html
│   ├── messages.html
│   └── subscribers.html
└── members/
    ├── login.html
    ├── index.html
    ├── documents.html
    ├── projects.html
    └── profile.html
```

## 🔄 Conversion PHP → Django

### Variables
```php
<?php echo $variable; ?>
```
```django
{{ variable }}
```

### Boucles
```php
<?php foreach ($items as $item): ?>
    <?php echo $item; ?>
<?php endforeach; ?>
```
```django
{% for item in items %}
    {{ item }}
{% endfor %}
```

### Conditions
```php
<?php if ($condition): ?>
    ...
<?php endif; ?>
```
```django
{% if condition %}
    ...
{% endif %}
```

### URLs
```php
<a href="<?php echo BASE_URL; ?>page.php">
```
```django
<a href="{% url 'main:page' %}">
```

### Images
```php
<img src="<?php echo BASE_URL; ?>uploads/image.jpg">
```
```django
<img src="{{ object.image.url }}">
```

### Formulaires
```php
<form method="POST" action="handler.php">
```
```django
<form method="POST" action="{% url 'main:action' %}">
    {% csrf_token %}
    ...
</form>
```

## 📝 Prochaines Étapes

1. **Créer les templates** - Adapter les fichiers PHP en templates Django
2. **Tester localement** - Vérifier que tout fonctionne
3. **Déployer** - Suivre MIGRATION_GUIDE.md pour PythonAnywhere

## ⚠️ Points Importants

- Tous les formulaires doivent avoir `{% csrf_token %}`
- Utiliser `{% load static %}` pour les fichiers statiques
- Utiliser `{% url 'app:name' %}` pour les liens
- Les images uploadées utilisent `.url` (ex: `{{ image.url }}`)
- Le multilingue utilise `{% trans %}` et `{% blocktrans %}`

## 🆘 Besoin d'aide?

- Consultez `TEMPLATE_EXAMPLE.md` pour des exemples complets
- Consultez `MIGRATION_GUIDE.md` pour le déploiement
- Documentation Django: https://docs.djangoproject.com/

