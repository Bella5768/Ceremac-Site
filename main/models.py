from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify


class CustomUser(AbstractUser):
    """Modèle utilisateur personnalisé"""
    email = models.EmailField(_('email address'), blank=True)
    full_name = models.CharField(_('full name'), max_length=100, blank=True)
    role = models.CharField(
        max_length=20,
        choices=[('admin', 'Admin'), ('member', 'Member')],
        default='member'
    )
    can_validate = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def is_admin(self):
        return self.role == 'admin'


class News(models.Model):
    """Modèle pour les actualités avec fonctionnalités WordPress-like"""
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('published', 'Publié'),
        ('archived', 'Archivé'),
    ]
    
    VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Privé'),
        ('members', 'Membres uniquement'),
    ]
    
    SUBTITLE_ALIGNMENT_CHOICES = [
        ('left', 'Gauche'),
        ('center', 'Centre'),
        ('right', 'Droite'),
    ]
    
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True, null=True)
    subtitle_alignment = models.CharField(max_length=10, choices=SUBTITLE_ALIGNMENT_CHOICES, default='left')
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    image_caption = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='public')
    publication_date = models.DateTimeField(blank=True, null=True)
    is_pinned = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)
    show_on_home = models.BooleanField(default=False)
    show_on_news_page = models.BooleanField(default=True)
    show_on_workshops = models.BooleanField(default=False)
    show_on_events = models.BooleanField(default=False)
    show_on_podcasts = models.BooleanField(default=False)
    show_on_deliverables = models.BooleanField(default=False)
    show_on_about = models.BooleanField(default=False)
    category = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True, help_text="Tags séparés par des virgules")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='news_articles')
    displayed_author = models.CharField(max_length=100, blank=True, null=True)
    views_count = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
        ordering = ['-is_pinned', '-publication_date', '-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})

    @property
    def is_published(self):
        return self.status == 'published'

    @property
    def is_scheduled(self):
        if self.publication_date:
            return self.publication_date > timezone.now()
        return False

    @property
    def author_display(self):
        if self.displayed_author:
            return self.displayed_author
        elif self.author:
            return f"{self.author.first_name} {self.author.last_name}".strip() or self.author.username
        return "Anonyme"

    @property
    def tags_list(self):
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []


class Project(models.Model):
    """Modèle pour les projets"""
    STATUS_CHOICES = [
        ('current', 'En cours'),
        ('past', 'Terminé'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    file_path = models.FileField(upload_to='documents/projects/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='current')
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})


class Publication(models.Model):
    """Modèle pour les publications"""
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file_path = models.FileField(upload_to='documents/publications/', blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('publication')
        verbose_name_plural = _('publications')
        ordering = ['-publication_date', '-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('publication_detail', kwargs={'pk': self.pk})


class Partner(models.Model):
    """Modèle pour les partenaires"""
    TYPE_CHOICES = [
        ('national', 'National'),
        ('international', 'International'),
    ]
    
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    website = models.URLField(blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='national')
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('partner')
        verbose_name_plural = _('partners')
        ordering = ['type', 'name']

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    """Modèle pour les messages de contact"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('contact message')
        verbose_name_plural = _('contact messages')
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.subject} - {self.name}"


class NewsletterSubscriber(models.Model):
    """Modèle pour les abonnés à la newsletter"""
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('newsletter subscriber')
        verbose_name_plural = _('newsletter subscribers')
        ordering = ['-date_subscribed']

    def __str__(self):
        return self.email


class Department(models.Model):
    """Modèle pour les départements CEREMAC"""
    DEPARTMENT_CHOICES = [
        (1, 'Département Océanographie'),
        (2, 'Département Hydrobiologie'),
        (3, 'Département Géologie-Environnement'),
        (4, 'Département des Énergies et de la Transition Énergétique'),
        (5, 'Département des Matériaux Locaux de Construction et Produits Finis'),
    ]
    
    name = models.CharField(max_length=255, unique=True)
    order = models.IntegerField(choices=DEPARTMENT_CHOICES, unique=True)
    description = models.TextField()
    mission = models.TextField()
    image = models.ImageField(upload_to='departments/', blank=True, null=True)
    head_of_department = models.CharField(max_length=255, blank=True)
    head_photo = models.ImageField(upload_to='departments/heads/', blank=True, null=True, help_text="Photo du chef de département (recommandé: portrait)")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True, help_text="Numéro de téléphone du département")
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('department_detail', kwargs={'pk': self.pk})


class DepartmentProject(models.Model):
    """Projets par département"""
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='department_projects/', blank=True, null=True)
    file_path = models.FileField(upload_to='documents/department_projects/', blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('current', 'En cours'), ('completed', 'Terminé'), ('planned', 'Planifié')],
        default='current'
    )
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('department project')
        verbose_name_plural = _('department projects')
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.department.name} - {self.title}"


class DepartmentPublication(models.Model):
    """Publications par département"""
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='publications')
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    file_path = models.FileField(upload_to='documents/department_publications/', blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    journal = models.CharField(max_length=255, blank=True)
    doi = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('department publication')
        verbose_name_plural = _('department publications')
        ordering = ['-publication_date', '-date_created']

    def __str__(self):
        return f"{self.department.name} - {self.title}"


class DepartmentMember(models.Model):
    """Membres du département"""
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='members/', blank=True, null=True)
    bio = models.TextField(blank=True)
    is_head = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('department member')
        verbose_name_plural = _('department members')
        ordering = ['-is_head', 'name']

    def __str__(self):
        return f"{self.name} - {self.department.name}"


class HeroImage(models.Model):
    """Modèle pour les images du hero et carrousel"""
    PAGE_CHOICES = [
        ('home', 'Accueil'),
        ('news', 'Actualités'),
        ('projects', 'Projets'),
        ('publications', 'Publications'),
        ('partners', 'Partenaires'),
        ('departments', 'Départements'),
        ('about', 'À propos'),
        ('contact', 'Contact'),
        ('events', 'Événements'),
        ('services', 'Services'),
    ]
    
    page = models.CharField(
        _('page'),
        max_length=20,
        choices=PAGE_CHOICES,
        default='home',
        help_text="Page sur laquelle afficher cette image"
    )
    title = models.CharField(_('title'), max_length=255, help_text="Titre de l'image")
    description = models.TextField(_('description'), blank=True, help_text="Description affichée sur l'image")
    image = models.ImageField(_('image'), upload_to='hero/', help_text="Image (recommandé: 1920x600px)")
    order = models.IntegerField(_('order'), default=0, help_text="Ordre d'affichage (0 = premier)")
    is_active = models.BooleanField(_('active'), default=True, help_text="Afficher cette image")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('hero image')
        verbose_name_plural = _('hero images')
        ordering = ['page', 'order', '-date_created']

    def __str__(self):
        return f"{self.get_page_display()} - {self.title}"


class SiteSettings(models.Model):
    """Paramètres du site CEREMAC"""
    director_photo = models.ImageField(
        _('Photo du Directeur'),
        upload_to='site/',
        blank=True,
        null=True,
        help_text="Photo du Directeur Général (recommandé: 220x280px ou portrait)"
    )
    director_name = models.CharField(
        _('Nom du Directeur'),
        max_length=255,
        default="Pr Alpha Issaga Pallé Diallo",
        blank=True
    )
    director_title = models.CharField(
        _('Titre du Directeur'),
        max_length=255,
        default="Directeur Général",
        blank=True
    )
    director_quote = models.TextField(
        _('Citation du Directeur'),
        default="La science est le langage à travers lequel nous comprenons et préservons les océans qui bordent la Guinée. Le CEREMAC engage cette responsabilité avec rigueur, ouverture et un souci constant du bien commun.",
        blank=True
    )
    about_content = models.TextField(
        _('Contenu de la page À propos'),
        default="",
        blank=True,
        help_text="Contenu principal de la page À propos (supporte HTML)"
    )
    about_history = models.TextField(
        _('Historique et Évolution'),
        default="",
        blank=True,
        help_text="Section Historique de la page À propos (supporte HTML)"
    )
    about_administration = models.TextField(
        _('Organisation Administrative'),
        default="",
        blank=True,
        help_text="Section Organisation Administrative (supporte HTML)"
    )
    about_scientific = models.TextField(
        _('Organisation Scientifique'),
        default="",
        blank=True,
        help_text="Section Organisation Scientifique (supporte HTML)"
    )
    about_research = models.TextField(
        _('Domaines de Recherche'),
        default="",
        blank=True,
        help_text="Section Domaines de Recherche (supporte HTML)"
    )
    about_missions = models.TextField(
        _('Missions'),
        default="",
        blank=True,
        help_text="Section Missions (supporte HTML)"
    )
    contact_address = models.TextField(
        _('Adresse de contact'),
        default="",
        blank=True,
        help_text="Adresse physique du CEREMAC"
    )
    contact_phone = models.CharField(
        _('Téléphone de contact'),
        max_length=50,
        default="",
        blank=True
    )
    contact_email = models.EmailField(
        _('Email de contact'),
        default="",
        blank=True
    )
    facebook_url = models.URLField(
        _('Facebook'),
        default="",
        blank=True
    )
    twitter_url = models.URLField(
        _('Twitter/X'),
        default="",
        blank=True
    )
    linkedin_url = models.URLField(
        _('LinkedIn'),
        default="",
        blank=True
    )
    instagram_url = models.URLField(
        _('Instagram'),
        default="",
        blank=True
    )
    youtube_url = models.URLField(
        _('YouTube'),
        default="",
        blank=True
    )
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Paramètre du site')
        verbose_name_plural = _('Paramètres du site')

    def __str__(self):
        return "Paramètres du site CEREMAC"

    def save(self, *args, **kwargs):
        """Empêche la création de plusieurs instances"""
        if not self.pk and SiteSettings.objects.exists():
            # Si une instance existe déjà, on met à jour celle-ci au lieu d'en créer une nouvelle
            existing = SiteSettings.objects.first()
            self.pk = existing.pk
        super().save(*args, **kwargs)


class Event(models.Model):
    """Modèle pour les événements"""
    STATUS_CHOICES = [
        ('upcoming', 'À venir'),
        ('ongoing', 'En cours'),
        ('completed', 'Terminé'),
        ('cancelled', 'Annulé'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    is_featured = models.BooleanField(default=False)
    registration_required = models.BooleanField(default=False)
    max_participants = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
        ordering = ['-start_date']

    def __str__(self):
        return self.title


class Service(models.Model):
    """Modèle pour les services"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, help_text="Classe d'icône Bootstrap (ex: bi-clipboard-data)")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')
        ordering = ['order']

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Modèle pour les témoignages"""
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True)
    organization = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.IntegerField(default=5, help_text="Note sur 5")
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('testimonial')
        verbose_name_plural = _('testimonials')
        ordering = ['-is_featured', '-date_created']

    def __str__(self):
        return f"{self.name} - {self.organization}"


class FAQ(models.Model):
    """Modèle pour les FAQ"""
    CATEGORY_CHOICES = [
        ('general', 'Général'),
        ('research', 'Recherche'),
        ('education', 'Formation'),
        ('partnership', 'Partenariat'),
        ('contact', 'Contact'),
    ]
    
    question = models.CharField(max_length=500)
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')
        ordering = ['category', 'order']

    def __str__(self):
        return self.question


class StaticPage(models.Model):
    """Modèle pour les pages statiques personnalisées"""
    title = models.CharField(max_length=200, verbose_name=_('Titre'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('Slug'))
    content = models.TextField(verbose_name=_('Contenu'))
    is_active = models.BooleanField(default=True, verbose_name=_('Actif'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date de création'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Date de mise à jour'))

    class Meta:
        verbose_name = _('Page statique')
        verbose_name_plural = _('Pages statiques')
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

