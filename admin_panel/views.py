from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from main.models import News, Project, Publication, Partner, ContactMessage, NewsletterSubscriber, CustomUser


@login_required
def admin_dashboard(request):
    """Dashboard admin"""
    if not request.user.is_admin():
        return redirect('members:index')
    
    stats = {
        'users': CustomUser.objects.count(),
        'news': News.objects.count(),
        'projects': Project.objects.count(),
        'publications': Publication.objects.count(),
        'partners': Partner.objects.count(),
        'messages': ContactMessage.objects.filter(is_read=False).count(),
        'subscribers': NewsletterSubscriber.objects.filter(is_active=True).count(),
    }
    
    return render(request, 'admin_panel/index.html', {'stats': stats})


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

