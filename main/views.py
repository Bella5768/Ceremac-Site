from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from django.utils.translation import get_language
from .models import News, Project, Publication, Partner, ContactMessage, NewsletterSubscriber, CustomUser
from .forms import ContactForm, NewsletterForm


def index(request):
    """Page d'accueil"""
    latest_news = News.objects.all()[:3]
    
    stats = {
        'projects': Project.objects.filter(status='current').count(),
        'publications': Publication.objects.count(),
        'partners': Partner.objects.count(),
        'news': News.objects.count(),
    }
    
    return render(request, 'main/index.html', {
        'latest_news': latest_news,
        'stats': stats,
    })


def about(request):
    """Page À propos"""
    return render(request, 'main/about.html')


def projects(request):
    """Page Services et Directions"""
    current_projects = Project.objects.filter(status='current')
    past_projects = Project.objects.filter(status='past')
    
    return render(request, 'main/projects.html', {
        'current_projects': current_projects,
        'past_projects': past_projects,
    })


def project_detail(request, pk):
    """Détail d'un projet"""
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'main/project_detail.html', {'project': project})


def publications(request):
    """Page Publications"""
    publications_list = Publication.objects.all()
    
    # Filtrage par année si demandé
    year = request.GET.get('year')
    if year:
        publications_list = publications_list.filter(publication_date__year=year)
    
    # Liste des années disponibles
    years = Publication.objects.exclude(
        publication_date__isnull=True
    ).values_list('publication_date__year', flat=True).distinct().order_by('-publication_date__year')
    
    return render(request, 'main/publications.html', {
        'publications': publications_list,
        'years': years,
        'selected_year': year,
    })


def partners(request):
    """Page Partenaires"""
    national_partners = Partner.objects.filter(type='national')
    international_partners = Partner.objects.filter(type='international')
    
    return render(request, 'main/partners.html', {
        'national_partners': national_partners,
        'international_partners': international_partners,
    })


def news_list(request):
    """Liste des actualités"""
    news_list = News.objects.all()
    return render(request, 'main/news_list.html', {'news_list': news_list})


def news_detail(request, pk):
    """Détail d'une actualité"""
    news = get_object_or_404(News, pk=pk)
    return render(request, 'main/news_detail.html', {'news': news})


def contact(request):
    """Page Contact"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})


def newsletter_subscribe(request):
    """Inscription à la newsletter"""
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subscriber, created = NewsletterSubscriber.objects.get_or_create(
                email=email,
                defaults={'is_active': True}
            )
            if not created:
                subscriber.is_active = True
                subscriber.save()
            
            messages.success(request, 'Inscription réussie!')
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = NewsletterForm()
    
    return render(request, 'main/newsletter.html', {'form': form})

