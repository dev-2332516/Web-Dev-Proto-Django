from django.contrib import admin
from .models import Todo
from .models import Category

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