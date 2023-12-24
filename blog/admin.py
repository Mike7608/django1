from django.contrib import admin

from blog.models import Blog, Version


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'slug', 'published', 'total_view')
    list_filter = ('published',)
    search_fields = ('heading', 'text')
    prepopulated_fields = {'slug': ('heading',)}
    readonly_fields = ('total_view',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'version', 'name', 'sign')
    list_filter = ('sign', 'name')
    search_fields = ('version', 'name')
