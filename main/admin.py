from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    CustomUser, News, Project, Publication, Partner, ContactMessage,
    NewsletterSubscriber, Department, DepartmentProject, DepartmentPublication,
    DepartmentMember, DepartmentService, HeroImage, SiteSettings, Event, Service,
    StaticPage, Laboratory, CallForProjects, LibraryDocument, PartnershipRequest,
    ScientificAgenda, InstitutionalDocument
)


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


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'head_of_department', 'email', 'phone', 'is_active', 'date_created', 'head_photo_preview')
    list_filter = ('is_active', 'date_created', 'order')
    search_fields = ('name', 'description', 'head_of_department', 'phone')
    list_editable = ('is_active', 'head_of_department', 'phone')
    ordering = ('order',)
    fieldsets = (
        ('Informations générales', {
            'fields': ('name', 'order', 'is_active')
        }),
        ('Description', {
            'fields': ('description', 'mission')
        }),
        ('Chef de département', {
            'fields': ('head_of_department', 'head_photo')
        }),
        ('Contact', {
            'fields': ('email', 'phone')
        }),
        ('Média', {
            'fields': ('image',)
        })
    )
    
    def head_photo_preview(self, obj):
        if obj.head_photo:
            return f'<img src="{obj.head_photo.url}" style="max-height: 60px; border-radius: 4px;" />'
        return '-'
    head_photo_preview.short_description = 'Photo chef'
    head_photo_preview.allow_tags = True


@admin.register(DepartmentProject)
class DepartmentProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'status', 'date_start', 'date_created')
    list_filter = ('department', 'status', 'date_created')
    search_fields = ('title', 'description')


@admin.register(DepartmentPublication)
class DepartmentPublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'authors', 'publication_date', 'date_created')
    list_filter = ('department', 'publication_date', 'date_created')
    search_fields = ('title', 'authors', 'description')


@admin.register(DepartmentMember)
class DepartmentMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'position', 'is_head', 'is_active', 'date_created')
    list_filter = ('department', 'is_head', 'is_active', 'date_created')
    search_fields = ('name', 'position', 'email')
    list_editable = ('is_active', 'is_head')


@admin.register(DepartmentService)
class DepartmentServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'order', 'is_active', 'date_created')
    list_filter = ('department', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('order', 'is_active')


@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'date_created', 'image_preview')
    list_filter = ('is_active', 'date_created')
    search_fields = ('title', 'description')
    list_editable = ('order', 'is_active')
    ordering = ('order', '-date_created')
    
    fieldsets = (
        ('Informations', {
            'fields': ('title', 'description', 'order', 'is_active')
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 100px; border-radius: 5px;" />'
        return '-'
    image_preview.short_description = 'Aperçu'
    image_preview.allow_tags = True


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'director_name', 'date_updated', 'director_photo_preview')
    
    fieldsets = (
        ('Directeur Général', {
            'fields': ('director_photo', 'director_name', 'director_title')
        }),
        ('Citation', {
            'fields': ('director_quote',)
        }),
    )
    
    def director_photo_preview(self, obj):
        if obj.director_photo:
            return f'<img src="{obj.director_photo.url}" style="max-height: 80px; border-radius: 4px;" />'
        return '-'
    director_photo_preview.short_description = 'Aperçu photo'
    director_photo_preview.allow_tags = True


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'head_name', 'is_active', 'date_created')
    list_filter = ('department', 'is_active')
    search_fields = ('name', 'description', 'head_name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CallForProjects)
class CallForProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'is_featured', 'date_created')
    list_filter = ('status', 'is_featured', 'date_created')
    search_fields = ('title', 'description')


@admin.register(LibraryDocument)
class LibraryDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'file_type', 'department', 'year', 'download_count', 'is_public')
    list_filter = ('category', 'file_type', 'department', 'year', 'is_public')
    search_fields = ('title', 'author', 'description', 'keywords')


@admin.register(PartnershipRequest)
class PartnershipRequestAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'contact_name', 'contact_email', 'status', 'date_created')
    list_filter = ('status', 'date_created')
    search_fields = ('organization_name', 'contact_name', 'contact_email')
    readonly_fields = ('date_created', 'date_updated')


@admin.register(ScientificAgenda)
class ScientificAgendaAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'start_date', 'location', 'department', 'is_public')
    list_filter = ('event_type', 'department', 'is_public', 'start_date')
    search_fields = ('title', 'description', 'speaker', 'location')


@admin.register(InstitutionalDocument)
class InstitutionalDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'reference', 'date_issued', 'is_public')
    list_filter = ('category', 'is_public', 'date_issued')
    search_fields = ('title', 'description', 'reference')

