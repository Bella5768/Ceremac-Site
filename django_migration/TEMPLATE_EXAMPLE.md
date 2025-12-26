# Exemple d'Adaptation des Templates PHP vers Django

## Template de Base (base.html)

Voici comment adapter votre `includes/header.php` et `includes/footer.php` en Django:

```django
{% load static %}
{% load i18n %}
<!DOCTYPE html>
<html lang="{{ LANGUAGE_CODE }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="CEREMAC Guinée - Centre de Recherche en Océanographie, Environnement Marin et Côtier">
    <title>{% block title %}{% endblock %} - CEREMAC Guinée</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <link rel="stylesheet" href="{% static 'css/images.css' %}">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top" style="background: linear-gradient(135deg, #003366 0%, #0066cc 50%, #00a896 100%) !important;">
        <div class="container">
            <a class="navbar-brand" href="{% url 'main:index' %}">
                <i class="bi bi-water"></i> CEREMAC
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'main:index' %}">
                            <i class="bi bi-house-door"></i> {% trans "Accueil" %}
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'main:about' %}">
                            <i class="bi bi-info-circle"></i> {% trans "À propos" %}
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'main:projects' %}">
                            <i class="bi bi-folder"></i> {% trans "Services et Directions" %}
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'main:publications' %}">
                            <i class="bi bi-journal-text"></i> {% trans "Publications" %}
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'main:partners' %}">
                            <i class="bi bi-handshake"></i> {% trans "Partenaires" %}
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'main:news_list' %}">
                            <i class="bi bi-newspaper"></i> {% trans "Actualités" %}
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'main:contact' %}">
                            <i class="bi bi-envelope"></i> {% trans "Contact" %}
                        </a>
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <!-- Sélecteur de langue -->
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="langDropdown" role="button" data-bs-toggle="dropdown">
                            <i class="bi bi-globe"></i> {{ LANGUAGE_CODE|upper }}
                        </a>
                        <ul class="dropdown-menu">
                            {% get_current_language as CURRENT_LANGUAGE %}
                            {% get_available_languages as LANGUAGES %}
                            {% for lang_code, lang_name in LANGUAGES %}
                                <li>
                                    <a class="dropdown-item" href="/{{ lang_code }}{{ request.get_full_path|slice:'3:' }}">
                                        {{ lang_name }}
                                    </a>
                                </li>
                            {% endfor %}
                        </ul>
                    </li>
                    
                    {% if user.is_authenticated %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'members:index' %}" style="background: rgba(255, 255, 255, 0.2); border-radius: 25px; padding: 10px 25px; margin: 0 5px; font-weight: 600; border: 1px solid rgba(255, 255, 255, 0.3);">
                                <i class="bi bi-person-circle-fill"></i> <strong>{% trans "Espace Membres" %}</strong>
                            </a>
                        </li>
                        {% if user.is_admin %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'admin_panel:dashboard' %}" style="color: #ffd700 !important; font-weight: 700; background: rgba(255, 215, 0, 0.25); border-radius: 25px; padding: 10px 25px; margin: 0 5px; border: 1px solid rgba(255, 215, 0, 0.4);">
                                <i class="bi bi-shield-lock-fill"></i> <strong>{% trans "Administration" %}</strong>
                            </a>
                        </li>
                        {% endif %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'members:logout' %}" style="padding: 10px 20px;">
                                <i class="bi bi-box-arrow-right"></i> {% trans "Déconnexion" %}
                            </a>
                        </li>
                    {% else %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'members:login' %}" style="background: rgba(255, 255, 255, 0.2); border-radius: 25px; padding: 10px 25px; margin: 0 5px; font-weight: 600; border: 1px solid rgba(255, 255, 255, 0.3);">
                                <i class="bi bi-box-arrow-in-right"></i> <strong>{% trans "Connexion" %}</strong>
                            </a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <!-- Messages Django -->
    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                {{ message }}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        {% endfor %}
    {% endif %}

    <!-- Contenu principal -->
    {% block content %}
    {% endblock %}

    <!-- Footer -->
    <footer class="bg-dark text-light py-5 mt-5">
        <div class="container">
            <div class="row">
                <div class="col-md-4 mb-4">
                    <h5><i class="bi bi-water"></i> CEREMAC</h5>
                    <p>Centre de Recherche en Océanographie, Environnement Marin et Côtier</p>
                    <p>Guinée</p>
                </div>
                <div class="col-md-4 mb-4">
                    <h5>{% trans "Actualités" %}</h5>
                    <p>{% trans "Newsletter" %}</p>
                    <form class="newsletter-form" method="POST" action="{% url 'main:newsletter_subscribe' %}">
                        {% csrf_token %}
                        <div class="input-group mb-3">
                            <input type="email" class="form-control" name="email" placeholder="{% trans 'Votre email' %}" required>
                            <button class="btn btn-primary" type="submit">{% trans "S'abonner" %}</button>
                        </div>
                    </form>
                </div>
                <div class="col-md-4 mb-4">
                    <h5>{% trans "Contact" %}</h5>
                    <p><i class="bi bi-envelope"></i> contact@ceremac.gn</p>
                    <p><i class="bi bi-telephone"></i> +224 XXX XXX XXX</p>
                    <div class="social-links mt-3">
                        <a href="#" class="text-light me-3"><i class="bi bi-facebook"></i></a>
                        <a href="#" class="text-light me-3"><i class="bi bi-twitter"></i></a>
                        <a href="#" class="text-light me-3"><i class="bi bi-linkedin"></i></a>
                        <a href="#" class="text-light"><i class="bi bi-instagram"></i></a>
                    </div>
                </div>
            </div>
            <hr class="my-4">
            <div class="row">
                <div class="col-md-12 text-center">
                    <p>&copy; {% now "Y" %} CEREMAC Guinée. {% trans "Tous droits réservés." %}</p>
                </div>
            </div>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Custom JS -->
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>
```

## Exemple de Page (index.html)

```django
{% extends 'base.html' %}
{% load static %}
{% load i18n %}

{% block title %}{% trans "Accueil" %}{% endblock %}

{% block content %}
<!-- Hero Section -->
<section class="hero-section" style="background-image: url('https://images.unsplash.com/photo-1559827260-dc66d52bef19?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80');">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-10 mx-auto text-center">
                <h1 class="fade-in-up">{% trans "CEREMAC Guinée" %}</h1>
                <p class="lead fade-in-up">{% trans "Centre de Recherche en Océanographie, Environnement Marin et Côtier" %}</p>
            </div>
        </div>
    </div>
</section>

<!-- Statistiques -->
<section class="stats-section">
    <div class="container">
        <div class="row">
            <div class="col-md-3 col-sm-6 mb-4">
                <div class="stat-item fade-in">
                    <div class="stat-number">{{ stats.projects }}+</div>
                    <div class="stat-label">{% trans "Projets Actifs" %}</div>
                </div>
            </div>
            <!-- ... autres stats ... -->
        </div>
    </div>
</section>

<!-- Dernières Actualités -->
{% if latest_news %}
<section class="py-5 section-alt">
    <div class="container">
        <h2 class="section-title">{% trans "Dernières Actualités" %}</h2>
        <div class="row">
            {% for news in latest_news %}
            <div class="col-md-4 mb-4">
                <div class="card news-card fade-in">
                    {% if news.image %}
                    <img src="{{ news.image.url }}" class="card-img-top" alt="{{ news.title }}">
                    {% endif %}
                    <div class="card-body">
                        <span class="badge badge-custom">{{ news.date_created|date:"d/m/Y" }}</span>
                        <h5 class="card-title mt-3">{{ news.title }}</h5>
                        <p class="card-text">{{ news.content|truncatewords:20 }}</p>
                        <a href="{% url 'main:news_detail' news.pk %}" class="btn btn-primary btn-sm">
                            {% trans "Lire la suite" %} <i class="bi bi-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
{% endif %}
{% endblock %}
```

## Conversions Principales

| PHP | Django |
|-----|--------|
| `<?php echo $var; ?>` | `{{ var }}` |
| `<?php include 'file.php'; ?>` | `{% include 'file.html' %}` |
| `<?php if ($condition): ?>` | `{% if condition %}` |
| `<?php foreach ($items as $item): ?>` | `{% for item in items %}` |
| `BASE_URL . 'path'` | `{% url 'app:name' %}` |
| `<?php echo t('key'); ?>` | `{% trans "key" %}` |
| `<img src="<?php echo BASE_URL; ?>uploads/image.jpg">` | `<img src="{{ object.image.url }}">` |
| `<?php echo htmlspecialchars($text); ?>` | `{{ text }}` (automatique) |

## Notes Importantes

1. **Sécurité CSRF**: Tous les formulaires doivent inclure `{% csrf_token %}`
2. **Static Files**: Utiliser `{% load static %}` et `{% static 'path' %}`
3. **URLs**: Utiliser `{% url 'app:name' %}` au lieu de chemins hardcodés
4. **Multilingue**: Utiliser `{% trans %}` et `{% blocktrans %}`
5. **Images**: Utiliser `.url` pour les champs ImageField/FileField

