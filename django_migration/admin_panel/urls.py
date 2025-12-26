from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.admin_dashboard, name='dashboard'),
    path('news/', views.manage_news, name='news'),
    path('projects/', views.manage_projects, name='projects'),
    path('publications/', views.manage_publications, name='publications'),
    path('partners/', views.manage_partners, name='partners'),
    path('users/', views.manage_users, name='users'),
    path('messages/', views.manage_messages, name='messages'),
    path('subscribers/', views.manage_subscribers, name='subscribers'),
]

