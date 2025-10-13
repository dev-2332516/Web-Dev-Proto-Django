from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from .models import UserProfile, Todo, Category

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'isDone')
    list_filter = ('category', 'isDone')
    search_fields = ('name', 'category')
    list_editable = ('name', 'category', 'description', 'isDone')
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'description', 'isDone')
        }),
    )
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')
    search_fields = ('name', 'color')
    list_editable = ('name', 'color')
    fieldsets = (
        (None, {
            'fields': ('name', 'color')
        }),
    )

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)

# Unregister the original User admin
admin.site.unregister(User)

# Register the new User admin with Profile inline
admin.site.register(User, CustomUserAdmin)

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_image_tag']
    readonly_fields = ['profile_image_tag']

    def profile_image_tag(self, obj):
        if obj.picture:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.picture.url)
        return "No Image"

    profile_image_tag.short_description = 'Profile Picture'