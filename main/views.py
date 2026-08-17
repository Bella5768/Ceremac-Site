from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from django.utils.translation import get_language
from django.http import JsonResponse
from django.utils import timezone
import json
from .models import (
    News, Project, Publication, Partner, ContactMessage, NewsletterSubscriber,
    CustomUser, Department, DepartmentProject, DepartmentPublication, DepartmentMember,
    DepartmentService, HeroImage, SiteSettings, Event, Service, StaticPage,
    Laboratory, CallForProjects, LibraryDocument, PartnershipRequest,
    ScientificAgenda, InstitutionalDocument
)
from .forms import ContactForm, NewsletterForm, PartnershipRequestForm


def index(request):
    """Page d'accueil"""
    latest_news = News.objects.filter(status='published')[:3]
    hero_images = HeroImage.objects.filter(is_active=True, page='home').exclude(image='').order_by('order')
    
    # Paramètres du site (photo du directeur, citation, etc.)
    site_settings = SiteSettings.objects.first()
    
    # Chiffres clés institutionnels
    members_count = DepartmentMember.objects.filter(is_active=True).count()
    departments_count = Department.objects.filter(is_active=True).count()
    publications_count = Publication.objects.count()
    partners_count = Partner.objects.count()
    
    stats = {
        'members': members_count if members_count > 0 else 109,
        'departments': departments_count if departments_count > 0 else 5,
        'publications': publications_count if publications_count > 0 else 13,
        'partners': partners_count if partners_count > 0 else 20,
    }
    
    # Projets mis en avant
    featured_projects = Project.objects.filter(is_featured=True, status='current')[:3]
    if not featured_projects.exists():
        featured_projects = Project.objects.filter(status='current')[:3]
    
    # Publications récentes
    recent_publications = Publication.objects.all()[:4]
    
    # Partenaires pour la frise défilante
    all_partners = Partner.objects.all()
    
    # Appels à projets
    open_calls = CallForProjects.objects.filter(status='open')[:3]
    
    # Agenda scientifique
    upcoming_agenda = ScientificAgenda.objects.filter(
        start_date__gte=timezone.now(), is_public=True
    )[:5]
    
    return render(request, 'main/index.html', {
        'latest_news': latest_news,
        'hero_images': hero_images,
        'stats': stats,
        'site_settings': site_settings,
        'featured_projects': featured_projects,
        'recent_publications': recent_publications,
        'all_partners': all_partners,
        'open_calls': open_calls,
        'upcoming_agenda': upcoming_agenda,
    })


def about(request):
    """Page À propos"""
    site_settings = SiteSettings.objects.first()
    hero_images = HeroImage.objects.filter(is_active=True, page='about').order_by('order')
    departments = Department.objects.filter(is_active=True).order_by('order')
    institutional_docs = InstitutionalDocument.objects.filter(is_public=True)
    
    return render(request, 'main/about.html', {
        'site_settings': site_settings,
        'hero_images': hero_images,
        'departments': departments,
        'institutional_docs': institutional_docs,
    })


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
    laboratories = department.laboratories.filter(is_active=True)
    services = department.services.filter(is_active=True).order_by('order')
    
    return render(request, 'main/department_detail.html', {
        'department': department,
        'projects': projects,
        'publications': publications,
        'members': members,
        'laboratories': laboratories,
        'services': services,
    })


def laboratory_detail(request, slug):
    """Détail d'un laboratoire"""
    laboratory = get_object_or_404(Laboratory, slug=slug, is_active=True)
    return render(request, 'main/laboratory_detail.html', {
        'laboratory': laboratory,
    })


def project_detail(request, pk):
    """Détail d'un projet"""
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'main/project_detail.html', {'project': project})


def research(request):
    """Page Recherche et Innovation"""
    hero_images = HeroImage.objects.filter(is_active=True, page='projects').order_by('order')
    
    # Projets avec coordonnées pour la carte Leaflet
    all_projects = Project.objects.all()
    projects_with_coords = Project.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True)
    
    # Publications filtrables
    publications_list = Publication.objects.all()
    
    # Filtres
    year = request.GET.get('year')
    department_id = request.GET.get('department')
    pub_type = request.GET.get('type')
    author = request.GET.get('author')
    
    if year:
        publications_list = publications_list.filter(publication_date__year=year)
    if department_id:
        publications_list = publications_list.filter(department_id=department_id)
    if pub_type:
        publications_list = publications_list.filter(publication_type=pub_type)
    if author:
        publications_list = publications_list.filter(author__icontains=author)
    
    # Données pour les filtres
    years = Publication.objects.exclude(
        publication_date__isnull=True
    ).values_list('publication_date__year', flat=True).distinct().order_by('-publication_date__year')
    departments = Department.objects.filter(is_active=True)
    
    # Données JSON pour la carte
    projects_json = []
    for p in projects_with_coords:
        projects_json.append({
            'id': p.pk,
            'title': p.title,
            'description': p.description[:150],
            'lat': p.latitude,
            'lng': p.longitude,
            'status': p.get_status_display(),
        })
    
    return render(request, 'main/research.html', {
        'hero_images': hero_images,
        'all_projects': all_projects,
        'publications': publications_list,
        'years': years,
        'departments': departments,
        'selected_year': year,
        'selected_department': department_id,
        'selected_type': pub_type,
        'selected_author': author,
        'projects_json': json.dumps(projects_json),
    })


def publications(request):
    """Page Publications"""
    publications_list = Publication.objects.all()
    hero_images = HeroImage.objects.filter(is_active=True, page='publications').order_by('order')
    
    # Filtrage
    year = request.GET.get('year')
    department_id = request.GET.get('department')
    pub_type = request.GET.get('type')
    author = request.GET.get('author')
    
    if year:
        publications_list = publications_list.filter(publication_date__year=year)
    if department_id:
        publications_list = publications_list.filter(department_id=department_id)
    if pub_type:
        publications_list = publications_list.filter(publication_type=pub_type)
    if author:
        publications_list = publications_list.filter(author__icontains=author)
    
    # Liste des années disponibles
    years = Publication.objects.exclude(
        publication_date__isnull=True
    ).values_list('publication_date__year', flat=True).distinct().order_by('-publication_date__year')
    
    departments = Department.objects.filter(is_active=True)
    
    return render(request, 'main/publications.html', {
        'publications': publications_list,
        'years': years,
        'departments': departments,
        'selected_year': year,
        'selected_department': department_id,
        'selected_type': pub_type,
        'selected_author': author,
        'hero_images': hero_images,
    })


def library(request):
    """Bibliothèque numérique"""
    documents = LibraryDocument.objects.filter(is_public=True)
    
    # Filtres
    category = request.GET.get('category')
    file_type = request.GET.get('file_type')
    year = request.GET.get('year')
    search_query = request.GET.get('q')
    
    if category:
        documents = documents.filter(category=category)
    if file_type:
        documents = documents.filter(file_type=file_type)
    if year:
        documents = documents.filter(year=year)
    if search_query:
        documents = documents.filter(
            Q(title__icontains=search_query) |
            Q(author__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(keywords__icontains=search_query)
        )
    
    years = LibraryDocument.objects.exclude(
        year__isnull=True
    ).values_list('year', flat=True).distinct().order_by('-year')
    
    return render(request, 'main/library.html', {
        'documents': documents,
        'years': years,
        'selected_category': category,
        'selected_file_type': file_type,
        'selected_year': year,
        'search_query': search_query,
    })


def partners(request):
    """Page Partenaires"""
    national_partners = Partner.objects.filter(type='national')
    international_partners = Partner.objects.filter(type='international')
    hero_images = HeroImage.objects.filter(is_active=True, page='partners').order_by('order')
    conventions = InstitutionalDocument.objects.filter(category__in=['convention', 'protocol'], is_public=True)
    
    # Formulaire de demande de partenariat
    if request.method == 'POST':
        partnership_form = PartnershipRequestForm(request.POST)
        if partnership_form.is_valid():
            partnership_form.save()
            messages.success(request, 'Votre demande de partenariat a été envoyée avec succès!')
            return redirect('main:partners')
    else:
        partnership_form = PartnershipRequestForm()
    
    return render(request, 'main/partners.html', {
        'national_partners': national_partners,
        'international_partners': international_partners,
        'hero_images': hero_images,
        'conventions': conventions,
        'partnership_form': partnership_form,
    })


def news_list(request):
    """Liste des actualités"""
    news_items = News.objects.filter(status='published')
    hero_images = HeroImage.objects.filter(is_active=True, page='news').order_by('order')
    return render(request, 'main/news_list.html', {'news_list': news_items, 'hero_images': hero_images})


def news_detail(request, pk):
    """Détail d'une actualité"""
    try:
        news = News.objects.get(pk=pk)
        news.views_count += 1
        news.save(update_fields=['views_count'])
        return render(request, 'main/news_detail.html', {'news': news})
    except News.DoesNotExist:
        messages.error(request, "Cet article n'existe pas ou a été supprimé.")
        return redirect('main:news_list')


def contact(request):
    """Page Contact"""
    site_settings = SiteSettings.objects.first()
    
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
    departments = Department.objects.filter(is_active=True).order_by('order')
    
    return render(request, 'main/contact.html', {
        'form': form,
        'hero_images': hero_images,
        'site_settings': site_settings,
        'departments': departments,
    })


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
    """Page Événements et Agenda"""
    events_list = Event.objects.filter(status__in=['upcoming', 'ongoing']).order_by('-start_date')
    hero_images = HeroImage.objects.filter(is_active=True, page='events').order_by('order')
    
    return render(request, 'main/events.html', {
        'events_list': events_list,
        'hero_images': hero_images,
    })


def scientific_agenda(request):
    """Agenda scientifique avec vue calendrier"""
    agenda_events = ScientificAgenda.objects.filter(is_public=True)
    
    # Filtres
    event_type = request.GET.get('type')
    department_id = request.GET.get('department')
    
    if event_type:
        agenda_events = agenda_events.filter(event_type=event_type)
    if department_id:
        agenda_events = agenda_events.filter(department_id=department_id)
    
    departments = Department.objects.filter(is_active=True)
    
    # Données JSON pour le calendrier
    events_json = []
    for event in agenda_events:
        events_json.append({
            'id': event.pk,
            'title': event.title,
            'start': event.start_date.isoformat(),
            'end': event.end_date.isoformat() if event.end_date else None,
            'type': event.get_event_type_display(),
            'location': event.location,
            'speaker': event.speaker,
            'description': event.description[:200],
        })
    
    return render(request, 'main/scientific_agenda.html', {
        'agenda_events': agenda_events,
        'departments': departments,
        'selected_type': event_type,
        'selected_department': department_id,
        'events_json': json.dumps(events_json),
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


