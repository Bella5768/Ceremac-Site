from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from main.models import Project, Publication, CustomUser


@login_required
def member_dashboard(request):
    """Dashboard membre"""
    try:
        user_obj = CustomUser.objects.get(pk=request.user.pk)
    except CustomUser.DoesNotExist:
        user_obj = request.user
    return render(request, 'members/index.html', {'user': user_obj})


@login_required
def member_documents(request):
    """Documents réservés"""
    publications = Publication.objects.all()
    return render(request, 'members/documents.html', {'publications': publications})


@login_required
def member_projects(request):
    """Projets internes"""
    projects = Project.objects.all()
    return render(request, 'members/projects.html', {'projects': projects})


@login_required
def member_profile(request):
    """Profil utilisateur"""
    try:
        user_obj = CustomUser.objects.get(pk=request.user.pk)
    except CustomUser.DoesNotExist:
        user_obj = request.user
    return render(request, 'members/profile.html', {'user': user_obj})

