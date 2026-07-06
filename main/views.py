from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from django.utils.translation import get_language
from .models import News, Project, Publication, Partner, ContactMessage, NewsletterSubscriber, CustomUser, Department, DepartmentProject, DepartmentPublication, DepartmentMember, HeroImage, SiteSettings, Event, Service, StaticPage
from .forms import ContactForm, NewsletterForm


def index(request):
    """Page d'accueil"""
    latest_news = News.objects.all()[:3]
    hero_images = HeroImage.objects.filter(is_active=True, page='home').order_by('order')
    
    # Paramètres du site (photo du directeur, citation, etc.)
    site_settings = SiteSettings.objects.first()
    
    # Statistiques avec valeurs par défaut si la base est vide
    projects_count = Project.objects.filter(status='current').count()
    publications_count = Publication.objects.count()
    partners_count = Partner.objects.count()
    news_count = News.objects.count()
    
    stats = {
        'projects': projects_count if projects_count > 0 else 15,
        'publications': publications_count if publications_count > 0 else 50,
        'partners': partners_count if partners_count > 0 else 20,
        'news': news_count if news_count > 0 else 30,
    }
    
    return render(request, 'main/index.html', {
        'latest_news': latest_news,
        'hero_images': hero_images,
        'stats': stats,
        'site_settings': site_settings,
    })


def about(request):
    """Page À propos"""
    site_settings = SiteSettings.objects.first()
    hero_images = HeroImage.objects.filter(is_active=True, page='about').order_by('order')
    return render(request, 'main/about.html', {'site_settings': site_settings, 'hero_images': hero_images})


def projects(request):
    """Page Départements et Services"""
    departments = Department.objects.filter(is_active=True).order_by('order')
    hero_images = HeroImage.objects.filter(is_active=True, page='projects').order_by('order')
    
    return render(request, 'main/projects.html', {
        'departments': departments,
        'hero_images': hero_images,
    })


def department_detail(request, pk):
    """Détail d'un département"""
    department = get_object_or_404(Department, pk=pk, is_active=True)
    projects = department.projects.all()
    publications = department.publications.all()
    members = department.members.filter(is_active=True)
    
    return render(request, 'main/department_detail.html', {
        'department': department,
        'projects': projects,
        'publications': publications,
        'members': members,
    })


def project_detail(request, pk):
    """Détail d'un projet"""
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'main/project_detail.html', {'project': project})


def publications(request):
    """Page Publications"""
    publications_list = Publication.objects.all()
    hero_images = HeroImage.objects.filter(is_active=True, page='publications').order_by('order')
    
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
        'hero_images': hero_images,
    })


def partners(request):
    """Page Partenaires"""
    national_partners = Partner.objects.filter(type='national')
    international_partners = Partner.objects.filter(type='international')
    hero_images = HeroImage.objects.filter(is_active=True, page='partners').order_by('order')
    
    return render(request, 'main/partners.html', {
        'national_partners': national_partners,
        'international_partners': international_partners,
        'hero_images': hero_images,
    })


def news_list(request):
    """Liste des actualités"""
    news_list = News.objects.all()
    hero_images = HeroImage.objects.filter(is_active=True, page='news').order_by('order')
    return render(request, 'main/news_list.html', {'news_list': news_list, 'hero_images': hero_images})


def news_detail(request, pk):
    """Détail d'une actualité"""
    try:
        news = News.objects.get(pk=pk)
        return render(request, 'main/news_detail.html', {'news': news})
    except News.DoesNotExist:
        messages.error(request, "Cet article n'existe pas ou a été supprimé.")
        return redirect('main:news_list')


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
            return redirect('main:contact')
    else:
        form = ContactForm()
    
    hero_images = HeroImage.objects.filter(is_active=True, page='contact').order_by('order')
    return render(request, 'main/contact.html', {'form': form, 'hero_images': hero_images})


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
            if created:
                messages.success(request, 'Merci pour votre inscription à la newsletter!')
            else:
                messages.info(request, 'Vous êtes déjà inscrit à la newsletter.')
            return redirect('main:index')
    else:
        form = NewsletterForm()
    
    return render(request, 'main/index.html', {'form': form})


def events(request):
    """Page Événements"""
    events_list = Event.objects.filter(is_active=True).order_by('-start_date')
    hero_images = HeroImage.objects.filter(is_active=True, page='events').order_by('order')
    
    return render(request, 'main/events.html', {
        'events_list': events_list,
        'hero_images': hero_images,
    })


def services(request):
    """Page Services"""
    services_list = Service.objects.filter(is_active=True).order_by('order')
    hero_images = HeroImage.objects.filter(is_active=True, page='services').order_by('order')
    
    return render(request, 'main/services.html', {
        'services_list': services_list,
        'hero_images': hero_images,
    })


def static_page(request, slug):
    """Afficher une page statique par slug"""
    page = get_object_or_404(StaticPage, slug=slug, is_active=True)
    return render(request, 'main/static_page.html', {'page': page})


