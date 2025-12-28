"""
Tests unitaires pour l'application main
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import News, Project, Publication, Partner

User = get_user_model()


class NewsModelTest(TestCase):
    """Tests pour le modèle News"""
    
    def test_create_news(self):
        """Test de création d'une actualité"""
        news = News.objects.create(
            title="Test News",
            content="Test content",
            is_published=True
        )
        self.assertEqual(news.title, "Test News")
        self.assertTrue(news.is_published)


class ProjectModelTest(TestCase):
    """Tests pour le modèle Project"""
    
    def test_create_project(self):
        """Test de création d'un projet"""
        project = Project.objects.create(
            title="Test Project",
            description="Test description",
            status="current"
        )
        self.assertEqual(project.title, "Test Project")
        self.assertEqual(project.status, "current")


class PublicationModelTest(TestCase):
    """Tests pour le modèle Publication"""
    
    def test_create_publication(self):
        """Test de création d'une publication"""
        publication = Publication.objects.create(
            title="Test Publication",
            authors="Test Author",
            journal="Test Journal"
        )
        self.assertEqual(publication.title, "Test Publication")


class PartnerModelTest(TestCase):
    """Tests pour le modèle Partner"""
    
    def test_create_partner(self):
        """Test de création d'un partenaire"""
        partner = Partner.objects.create(
            name="Test Partner",
            type="national"
        )
        self.assertEqual(partner.name, "Test Partner")
        self.assertEqual(partner.type, "national")

