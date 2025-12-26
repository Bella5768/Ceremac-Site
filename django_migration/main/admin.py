from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, News, Project, Publication, Partner, ContactMessage, NewsletterSubscriber


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'full_name', 'role', 'can_validate', 'date_created')
    list_filter = ('role', 'can_validate', 'date_created')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('full_name', 'role', 'can_validate')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('full_name', 'role', 'can_validate')}),
    )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_updated')
    list_filter = ('date_created',)
    search_fields = ('title', 'content')
    prepopulated_fields = {}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_start', 'date_created')
    list_filter = ('status', 'date_created')
    search_fields = ('title', 'description')


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'date_created')
    list_filter = ('publication_date', 'date_created')
    search_fields = ('title', 'author', 'description')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'website', 'date_created')
    list_filter = ('type', 'date_created')
    search_fields = ('name', 'description')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'date_created')
    list_filter = ('is_read', 'date_created')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('date_created',)


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'date_subscribed')
    list_filter = ('is_active', 'date_subscribed')
    search_fields = ('email',)

