from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


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
    """Modèle pour les actualités"""
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})


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

