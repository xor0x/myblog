from django.contrib import admin

from .models import BlogNews, Post, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(Category, CategoryAdmin)


admin.site.register(BlogNews)
admin.site.register(Post)
