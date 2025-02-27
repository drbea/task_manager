from django.contrib import admin
from .models import Task
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('title', 'status', 'author', 'created', 'updated')
    list_filter = ('status', 'author')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'created'
    ordering = ('-created',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'status', 'author')
        }),
        ('Dates', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created', 'updated')
    