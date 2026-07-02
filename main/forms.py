from django import forms
from django.core.validators import EmailValidator
from .models import CustomUser, News, Project, Publication, Partner, Department, DepartmentProject, DepartmentPublication, DepartmentMember, HeroImage, SiteSettings


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


class HeroImageForm(forms.ModelForm):
    class Meta:
        model = HeroImage
        fields = ['title', 'description', 'image', 'order', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Description'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ordre'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = ['director_photo', 'director_name', 'director_title', 'director_quote']
        widgets = {
            'director_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'director_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du Directeur'}),
            'director_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du Directeur'}),
            'director_quote': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Citation du Directeur'}),
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

