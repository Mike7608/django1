from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'slug', 'text', 'date_create', 'published', 'total_view')
    list_filter = ('heading', 'date_create', 'published')
    search_fields = ('heading', 'text')
