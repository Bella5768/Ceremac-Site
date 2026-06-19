from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.admin_dashboard, name='dashboard'),
    
    # Actualités
    path('news/', views.manage_news, name='news'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/<int:pk>/edit/', views.news_edit, name='news_edit'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),
    
    # Projets
    path('projects/', views.manage_projects, name='projects'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    
    # Publications
    path('publications/', views.manage_publications, name='publications'),
    path('publications/create/', views.publication_create, name='publication_create'),
    path('publications/<int:pk>/edit/', views.publication_edit, name='publication_edit'),
    path('publications/<int:pk>/delete/', views.publication_delete, name='publication_delete'),
    
    # Partenaires
    path('partners/', views.manage_partners, name='partners'),
    path('partners/create/', views.partner_create, name='partner_create'),
    path('partners/<int:pk>/edit/', views.partner_edit, name='partner_edit'),
    path('partners/<int:pk>/delete/', views.partner_delete, name='partner_delete'),
    
    # Départements
    path('departments/', views.departments, name='departments'),
    path('departments/create/', views.department_create, name='department_create'),
    path('departments/<int:pk>/edit/', views.department_edit, name='department_edit'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department_delete'),
    path('departments/<int:department_pk>/members/', views.department_members, name='department_members'),
    path('departments/<int:department_pk>/members/create/', views.department_member_create, name='department_member_create'),
    path('department-members/<int:pk>/edit/', views.department_member_edit, name='department_member_edit'),
    path('department-members/<int:pk>/delete/', views.department_member_delete, name='department_member_delete'),
    
    # Images Hero
    path('hero-images/', views.hero_images, name='hero_images'),
    path('hero-images/create/', views.hero_image_create, name='hero_image_create'),
    path('hero-images/<int:pk>/edit/', views.hero_image_edit, name='hero_image_edit'),
    path('hero-images/<int:pk>/delete/', views.hero_image_delete, name='hero_image_delete'),
    
    # Utilisateurs
    path('users/', views.manage_users, name='users'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
    
    # Messages et abonnés
    path('messages/', views.manage_messages, name='messages'),
    path('subscribers/', views.manage_subscribers, name='subscribers'),
]

