from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'members'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('members/', views.member_dashboard, name='index'),
    path('members/documents/', views.member_documents, name='documents'),
    path('members/projects/', views.member_projects, name='projects'),
    path('members/profile/', views.member_profile, name='profile'),
]

