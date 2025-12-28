from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('publications/', views.publications, name='publications'),
    path('partners/', views.partners, name='partners'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter_subscribe, name='newsletter_subscribe'),
]

