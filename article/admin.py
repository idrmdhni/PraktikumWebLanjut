# Register your models here.

from django.contrib import admin
from article.models import Category, BlogArticle

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "created_by"]
    search_fields = ["name"]

class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ["category", "title", "created_at", "created_by", "status"]
    search_fields = ["category__name", "title"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogArticle, BlogArticleAdmin)