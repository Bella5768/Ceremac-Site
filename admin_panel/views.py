from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.utils import timezone
from main.models import News, Project, Publication, Partner, ContactMessage, NewsletterSubscriber, CustomUser, Department, DepartmentProject, DepartmentPublication, DepartmentMember, HeroImage, SiteSettings
from main.forms import NewsForm, ProjectForm, PublicationForm, PartnerForm, DepartmentForm, DepartmentProjectForm, DepartmentPublicationForm, DepartmentMemberForm, HeroImageForm, UserForm, SiteSettingsForm


@login_required
def admin_dashboard(request):
    """Dashboard admin"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    context = {
        'news_count': News.objects.count(),
        'projects_count': Project.objects.count(),
        'publications_count': Publication.objects.count(),
        'partners_count': Partner.objects.count(),
        'departments_count': Department.objects.count(),
        'users_count': CustomUser.objects.count(),
        'messages_count': ContactMessage.objects.filter(is_read=False).count(),
        'subscribers_count': NewsletterSubscriber.objects.filter(is_active=True).count(),
    }
    
    return render(request, 'admin_panel/dashboard.html', context)


@login_required
def manage_news(request):
    """Gestion des actualités"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    news_list = News.objects.all()
    return render(request, 'admin_panel/news.html', {'news_list': news_list})


@login_required
def manage_projects(request):
    """Gestion des projets"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    projects = Project.objects.all()
    return render(request, 'admin_panel/projects.html', {'projects': projects})


@login_required
def manage_publications(request):
    """Gestion des publications"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    publications = Publication.objects.all()
    return render(request, 'admin_panel/publications.html', {'publications': publications})


@login_required
def manage_partners(request):
    """Gestion des partenaires"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    partners = Partner.objects.all()
    return render(request, 'admin_panel/partners.html', {'partners': partners})


@login_required
def manage_users(request):
    """Gestion des utilisateurs"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    users = CustomUser.objects.all()
    return render(request, 'admin_panel/users.html', {'users': users})


@login_required
def manage_messages(request):
    """Gestion des messages"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    messages_list = ContactMessage.objects.all()
    return render(request, 'admin_panel/messages.html', {'messages_list': messages_list})


@login_required
def manage_subscribers(request):
    """Gestion des abonnés"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    subscribers = NewsletterSubscriber.objects.all()
    return render(request, 'admin_panel/subscribers.html', {'subscribers': subscribers})


# CRUD pour les actualités
@login_required
def news_create(request):
    """Créer une actualité"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            
            # Gérer le statut selon le bouton cliqué
            action = request.POST.get('action', 'draft')
            if action == 'publish':
                news.status = 'published'
                if not news.publication_date:
                    news.publication_date = timezone.now()
            else:
                news.status = 'draft'
            
            news.save()
            messages.success(request, 'Actualité créée avec succès')
            return redirect('admin_panel:news')
    else:
        form = NewsForm()
    
    return render(request, 'admin_panel/news_form.html', {'form': form, 'action': 'Créer', 'icon': 'newspaper'})

@login_required
def news_edit(request, pk):
    """Modifier une actualité"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    news = get_object_or_404(News, pk=pk)
    
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            updated_news = form.save(commit=False)
            
            # Gérer le statut selon le bouton cliqué
            action = request.POST.get('action', 'draft')
            if action == 'publish':
                updated_news.status = 'published'
                if not updated_news.publication_date:
                    updated_news.publication_date = timezone.now()
            else:
                updated_news.status = 'draft'
            
            updated_news.save()
            messages.success(request, 'Actualité modifiée avec succès')
            return redirect('admin_panel:news')
    else:
        form = NewsForm(instance=news)
    
    return render(request, 'admin_panel/news_form.html', {'form': form, 'action': 'Modifier', 'icon': 'newspaper'})

@login_required
def news_delete(request, pk):
    """Supprimer une actualité"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        messages.success(request, 'Actualité supprimée avec succès')
        return redirect('admin_panel:news')
    
    return render(request, 'admin_panel/news_confirm_delete.html', {'news': news})


# CRUD pour les projets
@login_required
def project_create(request):
    """Créer un projet"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projet créé avec succès')
            return redirect('admin_panel:projects')
    else:
        form = ProjectForm()
    
    return render(request, 'admin_panel/project_form.html', {'form': form, 'action': 'Créer', 'icon': 'project-diagram'})

@login_required
def project_edit(request, pk):
    """Modifier un projet"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projet modifié avec succès')
            return redirect('admin_panel:projects')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'admin_panel/project_form.html', {'form': form, 'action': 'Modifier', 'icon': 'project-diagram'})

@login_required
def project_delete(request, pk):
    """Supprimer un projet"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Projet supprimé avec succès')
        return redirect('admin_panel:projects')
    
    return render(request, 'admin_panel/project_confirm_delete.html', {'project': project})


# CRUD pour les publications
@login_required
def publication_create(request):
    """Créer une publication"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publication créée avec succès')
            return redirect('admin_panel:publications')
    else:
        form = PublicationForm()
    
    return render(request, 'admin_panel/publication_form.html', {'form': form, 'action': 'Créer', 'icon': 'book'})

@login_required
def publication_edit(request, pk):
    """Modifier une publication"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    publication = get_object_or_404(Publication, pk=pk)
    
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES, instance=publication)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publication modifiée avec succès')
            return redirect('admin_panel:publications')
    else:
        form = PublicationForm(instance=publication)
    
    return render(request, 'admin_panel/publication_form.html', {'form': form, 'action': 'Modifier', 'icon': 'book'})

@login_required
def publication_delete(request, pk):
    """Supprimer une publication"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        publication.delete()
        messages.success(request, 'Publication supprimée avec succès')
        return redirect('admin_panel:publications')
    
    return render(request, 'admin_panel/publication_confirm_delete.html', {'publication': publication})


# CRUD pour les partenaires
@login_required
def partner_create(request):
    """Créer un partenaire"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Partenaire créé avec succès')
            return redirect('admin_panel:partners')
    else:
        form = PartnerForm()
    
    return render(request, 'admin_panel/partner_form.html', {'form': form, 'action': 'Créer', 'icon': 'handshake'})

@login_required
def partner_edit(request, pk):
    """Modifier un partenaire"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    partner = get_object_or_404(Partner, pk=pk)
    
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES, instance=partner)
        if form.is_valid():
            form.save()
            messages.success(request, 'Partenaire modifié avec succès')
            return redirect('admin_panel:partners')
    else:
        form = PartnerForm(instance=partner)
    
    return render(request, 'admin_panel/partner_form.html', {'form': form, 'action': 'Modifier', 'icon': 'handshake'})

@login_required
def partner_delete(request, pk):
    """Supprimer un partenaire"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == 'POST':
        partner.delete()
        messages.success(request, 'Partenaire supprimé avec succès')
        return redirect('admin_panel:partners')
    
    return render(request, 'admin_panel/partner_confirm_delete.html', {'partner': partner})


# CRUD pour les départements
@login_required
def departments(request):
    """Gestion des départements"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    departments = Department.objects.all()
    return render(request, 'admin_panel/departments.html', {'departments': departments})

@login_required
def department_create(request):
    """Créer un département"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Département créé avec succès')
            return redirect('admin_panel:departments')
    else:
        form = DepartmentForm()
    
    return render(request, 'admin_panel/department_form.html', {'form': form, 'action': 'Créer', 'icon': 'building'})

@login_required
def department_edit(request, pk):
    """Modifier un département"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    department = get_object_or_404(Department, pk=pk)
    
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Département modifié avec succès')
            return redirect('admin_panel:departments')
    else:
        form = DepartmentForm(instance=department)
    
    return render(request, 'admin_panel/department_form.html', {'form': form, 'action': 'Modifier', 'icon': 'building'})

@login_required
def department_delete(request, pk):
    """Supprimer un département"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        messages.success(request, 'Département supprimé avec succès')
        return redirect('admin_panel:departments')
    
    return render(request, 'admin_panel/department_confirm_delete.html', {'department': department})


# CRUD pour les membres de département
@login_required
def department_members(request, department_pk):
    """Gestion des membres d'un département"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    department = get_object_or_404(Department, pk=department_pk)
    members = department.members.all()
    return render(request, 'admin_panel/department_members.html', {'department': department, 'members': members})

@login_required
def department_member_create(request, department_pk):
    """Créer un membre de département"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    department = get_object_or_404(Department, pk=department_pk)
    
    if request.method == 'POST':
        form = DepartmentMemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.department = department
            member.save()
            messages.success(request, 'Membre créé avec succès')
            return redirect('admin_panel:department_members', department_pk=department_pk)
    else:
        form = DepartmentMemberForm(initial={'department': department})
    
    return render(request, 'admin_panel/department_member_form.html', {'form': form, 'action': 'Créer', 'icon': 'user', 'department': department})

@login_required
def department_member_edit(request, pk):
    """Modifier un membre de département"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    member = get_object_or_404(DepartmentMember, pk=pk)
    
    if request.method == 'POST':
        form = DepartmentMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membre modifié avec succès')
            return redirect('admin_panel:department_members', department_pk=member.department.pk)
    else:
        form = DepartmentMemberForm(instance=member)
    
    return render(request, 'admin_panel/department_member_form.html', {'form': form, 'action': 'Modifier', 'icon': 'user', 'department': member.department})

@login_required
def department_member_delete(request, pk):
    """Supprimer un membre de département"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    member = get_object_or_404(DepartmentMember, pk=pk)
    department_pk = member.department.pk
    if request.method == 'POST':
        member.delete()
        messages.success(request, 'Membre supprimé avec succès')
        return redirect('admin_panel:department_members', department_pk=department_pk)
    
    return render(request, 'admin_panel/department_member_confirm_delete.html', {'member': member})


# CRUD pour les images hero
@login_required
def hero_images(request):
    """Gestion des images hero"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    hero_images = HeroImage.objects.all()
    return render(request, 'admin_panel/hero_images.html', {'hero_images': hero_images})

@login_required
def hero_image_create(request):
    """Créer une image hero"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    if request.method == 'POST':
        form = HeroImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image hero créée avec succès')
            return redirect('admin_panel:hero_images')
    else:
        form = HeroImageForm()
    
    return render(request, 'admin_panel/hero_image_form.html', {'form': form, 'action': 'Créer', 'icon': 'images'})

@login_required
def hero_image_edit(request, pk):
    """Modifier une image hero"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    hero_image = get_object_or_404(HeroImage, pk=pk)
    
    if request.method == 'POST':
        form = HeroImageForm(request.POST, request.FILES, instance=hero_image)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image hero modifiée avec succès')
            return redirect('admin_panel:hero_images')
    else:
        form = HeroImageForm(instance=hero_image)
    
    return render(request, 'admin_panel/hero_image_form.html', {'form': form, 'action': 'Modifier', 'icon': 'images'})

@login_required
def hero_image_delete(request, pk):
    """Supprimer une image hero"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    hero_image = get_object_or_404(HeroImage, pk=pk)
    if request.method == 'POST':
        hero_image.delete()
        messages.success(request, 'Image hero supprimée avec succès')
        return redirect('admin_panel:hero_images')
    
    return render(request, 'admin_panel/hero_image_confirm_delete.html', {'hero_image': hero_image})


# CRUD pour les utilisateurs
@login_required
def user_create(request):
    """Créer un utilisateur"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.is_staff = True
            user.save()
            messages.success(request, 'Utilisateur créé avec succès')
            return redirect('admin_panel:users')
    else:
        form = UserForm()
    
    return render(request, 'admin_panel/user_form.html', {'form': form, 'action': 'Créer', 'icon': 'user'})

@login_required
def user_edit(request, pk):
    """Modifier un utilisateur"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    user = get_object_or_404(CustomUser, pk=pk)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            messages.success(request, 'Utilisateur modifié avec succès')
            return redirect('admin_panel:users')
    else:
        form = UserForm(instance=user)
    
    return render(request, 'admin_panel/user_form.html', {'form': form, 'action': 'Modifier', 'icon': 'user'})

@login_required
def user_delete(request, pk):
    """Supprimer un utilisateur"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Utilisateur supprimé avec succès')
        return redirect('admin_panel:users')
    
    return render(request, 'admin_panel/user_confirm_delete.html', {'user': user})


@login_required
def site_settings_edit(request):
    """Modifier les paramètres du site"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    settings_obj, created = SiteSettings.objects.get_or_create(pk=1)
    
    if request.method == 'POST':
        form = SiteSettingsForm(request.POST, request.FILES, instance=settings_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paramètres du site mis à jour avec succès')
            return redirect('admin_panel:dashboard')
    else:
        form = SiteSettingsForm(instance=settings_obj)
    
    return render(request, 'admin_panel/site_settings_form.html', {'form': form, 'action': 'Modifier', 'icon': 'gear'})

