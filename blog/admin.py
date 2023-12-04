from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'slug', 'published', 'total_view')
    list_filter = ('published',)
    search_fields = ('heading', 'text')
    prepopulated_fields = {'slug': ('heading',)}
    readonly_fields = ('total_view',)