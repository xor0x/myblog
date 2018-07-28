from django.contrib import admin

from .models import BlogNews, Post, Category, SiteSettings

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class AdmSiteSettings(admin.ModelAdmin):
    fields = ['site_title', 'site_email']

    def has_add_permission(self, request):
        return False


    def has_delete_permission(self, request, obj=None):
        return False


class AdmNews(admin.ModelAdmin):
    fields = ('title','image','text','link')

    def has_add_permission(self, request):
        return False


admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogNews, AdmNews)
admin.site.register(Post)
admin.site.register(SiteSettings, AdmSiteSettings)
