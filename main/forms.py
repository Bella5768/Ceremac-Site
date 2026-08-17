from django import forms
from django.core.validators import EmailValidator
from .models import (
    CustomUser, News, Project, Publication, Partner, Department,
    DepartmentProject, DepartmentPublication, DepartmentMember, DepartmentService,
    HeroImage, SiteSettings, Event, Service, StaticPage, Laboratory,
    CallForProjects, LibraryDocument, PartnershipRequest, ScientificAgenda,
    InstitutionalDocument
)


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Votre nom',
            'required': True,
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Votre email',
            'required': True,
        })
    )
    subject = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Sujet',
            'required': True,
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Votre message',
            'required': True,
        })
    )


class NewsletterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Votre email',
            'required': True,
        })
    )


# Formulaires pour l'administration du site

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title', 'subtitle', 'subtitle_alignment', 'content',
            'image', 'image_caption', 'image_url',
            'status', 'visibility', 'publication_date',
            'is_pinned', 'allow_comments',
            'show_on_home', 'show_on_news_page', 'show_on_workshops',
            'show_on_events', 'show_on_podcasts', 'show_on_deliverables', 'show_on_about',
            'category', 'tags', 'displayed_author',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'article'}),
            'subtitle': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Sous-titre...'}),
            'subtitle_alignment': forms.RadioSelect(),
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'id_content', 'rows': 20, 'placeholder': 'Contenu de l\'article...'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'image_caption': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Légende de l\'image...'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'visibility': forms.Select(attrs={'class': 'form-control'}),
            'publication_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'is_pinned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'allow_comments': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_on_home': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_on_news_page': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_on_workshops': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_on_events': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_on_podcasts': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_on_deliverables': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_on_about': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rubrique...'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tags séparés par virgules...'}),
            'displayed_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Auteur affiché...'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'file_path', 'status', 'date_start', 'date_end']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du projet'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Description du projet'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'file_path': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'date_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'author', 'description', 'file_path', 'publication_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de la publication'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Auteur(s)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Description'}),
            'file_path': forms.FileInput(attrs={'class': 'form-control'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'logo', 'website', 'type', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du partenaire'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Site web'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'order', 'description', 'mission', 'image', 'head_of_department', 'head_photo', 'email', 'phone', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du département'}),
            'order': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Description'}),
            'mission': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Mission'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'head_of_department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Chef de département'}),
            'head_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class DepartmentProjectForm(forms.ModelForm):
    class Meta:
        model = DepartmentProject
        fields = ['department', 'title', 'description', 'image', 'file_path', 'status', 'date_start', 'date_end']
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du projet'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Description'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'file_path': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'date_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class DepartmentPublicationForm(forms.ModelForm):
    class Meta:
        model = DepartmentPublication
        fields = ['department', 'title', 'authors', 'description', 'file_path', 'publication_date', 'journal', 'doi']
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'authors': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Auteurs'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'file_path': forms.FileInput(attrs={'class': 'form-control'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'journal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Journal'}),
            'doi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DOI'}),
        }


class DepartmentMemberForm(forms.ModelForm):
    class Meta:
        model = DepartmentMember
        fields = ['department', 'name', 'position', 'email', 'phone', 'photo', 'bio', 'is_head', 'is_active']
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Poste'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Biographie'}),
            'is_head': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class DepartmentServiceForm(forms.ModelForm):
    class Meta:
        model = DepartmentService
        fields = ['department', 'title', 'description', 'icon', 'image', 'order', 'is_active']
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du service'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Description du service'}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Icône Bootstrap (ex: bi-clipboard-data)'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ordre d\'affichage'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class HeroImageForm(forms.ModelForm):
    class Meta:
        model = HeroImage
        fields = ['page', 'title', 'description', 'image', 'order', 'is_active']
        widgets = {
            'page': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Description'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ordre'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = ['director_photo', 'director_name', 'director_title', 'director_quote', 'about_content', 'about_history', 'about_administration', 'about_scientific', 'about_research', 'about_missions', 'contact_address', 'contact_phone', 'contact_email', 'facebook_url', 'twitter_url', 'linkedin_url', 'instagram_url', 'youtube_url']
        widgets = {
            'director_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'director_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du Directeur'}),
            'director_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du Directeur'}),
            'director_quote': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Citation du Directeur'}),
            'about_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Contenu principal de la page À propos (HTML autorisé)'}),
            'about_history': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Section Historique (HTML autorisé)'}),
            'about_administration': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Section Organisation Administrative (HTML autorisé)'}),
            'about_scientific': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Section Organisation Scientifique (HTML autorisé)'}),
            'about_research': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Section Domaines de Recherche (HTML autorisé)'}),
            'about_missions': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Section Missions (HTML autorisé)'}),
            'contact_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adresse physique'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://facebook.com/...'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://twitter.com/...'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/...'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://instagram.com/...'}),
            'youtube_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://youtube.com/...'}),
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}), required=False)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'full_name', 'role', 'can_validate', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'can_validate': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'location', 'image', 'status', 'is_featured', 'registration_required', 'max_participants']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'événement'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Description'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lieu'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'registration_required': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'max_participants': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre maximum de participants'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'icon', 'image', 'order', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du service'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Description'}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Icône Bootstrap (ex: bi-clipboard-data)'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ordre d\'affichage'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class StaticPageForm(forms.ModelForm):
    class Meta:
        model = StaticPage
        fields = ['title', 'slug', 'content', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de la page'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'slug-de-la-page'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Contenu de la page (HTML autorisé)'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class PartnershipRequestForm(forms.ModelForm):
    class Meta:
        model = PartnershipRequest
        fields = [
            'organization_name', 'organization_type', 'country',
            'contact_name', 'contact_email', 'contact_phone',
            'website', 'partnership_type', 'description'
        ]
        widgets = {
            'organization_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom de l'organisation"}),
            'organization_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Type (Université, ONG, Entreprise...)"}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pays'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemple.com'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+224 XXX XX XX XX'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
            'partnership_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recherche, Formation, Échange...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Décrivez votre projet de partenariat...'}),
        }


class LaboratoryForm(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = ['department', 'name', 'description', 'scientific_description', 'equipment', 'results', 'image', 'head_name', 'head_photo', 'email', 'phone', 'is_active']
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du laboratoire'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Description'}),
            'scientific_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Description scientifique détaillée'}),
            'equipment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Équipements disponibles'}),
            'results': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Résultats marquants'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'head_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Responsable'}),
            'head_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CallForProjectsForm(forms.ModelForm):
    class Meta:
        model = CallForProjects
        fields = ['title', 'description', 'deadline', 'status', 'file_path', 'external_link', 'image', 'is_featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Titre de l'appel"}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Description'}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'file_path': forms.FileInput(attrs={'class': 'form-control'}),
            'external_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class LibraryDocumentForm(forms.ModelForm):
    class Meta:
        model = LibraryDocument
        fields = ['title', 'author', 'description', 'category', 'file_type', 'file_path', 'department', 'year', 'keywords', 'is_public']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du document'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Auteur(s)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'file_type': forms.Select(attrs={'class': 'form-control'}),
            'file_path': forms.FileInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2025'}),
            'keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mots-clés séparés par virgules'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ScientificAgendaForm(forms.ModelForm):
    class Meta:
        model = ScientificAgenda
        fields = ['title', 'event_type', 'description', 'start_date', 'end_date', 'location', 'speaker', 'department', 'is_public', 'registration_link', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Titre de l'événement"}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Description'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lieu'}),
            'speaker': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Intervenant(s)'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'registration_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class InstitutionalDocumentForm(forms.ModelForm):
    class Meta:
        model = InstitutionalDocument
        fields = ['title', 'category', 'description', 'file_path', 'reference', 'date_issued', 'is_public']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du document'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'file_path': forms.FileInput(attrs={'class': 'form-control'}),
            'reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Référence (ex: Décret 0134)'}),
            'date_issued': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

