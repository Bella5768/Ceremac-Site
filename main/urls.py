from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('publications/', views.publications, name='publications'),
    path('partners/', views.partners, name='partners'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('events/', views.events, name='events'),
    path('services/', views.services, name='services'),
    path('page/<slug:slug>/', views.static_page, name='static_page'),
]

