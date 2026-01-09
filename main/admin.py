from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, News, Project, Publication, Partner, ContactMessage, NewsletterSubscriber, Department, DepartmentProject, DepartmentPublication, DepartmentMember, HeroImage


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
    list_display = ('name', 'order', 'head_of_department', 'email', 'phone', 'is_active', 'date_created')
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
        ('Contact', {
            'fields': ('head_of_department', 'email', 'phone')
        }),
        ('Média', {
            'fields': ('image',)
        })
    )


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

