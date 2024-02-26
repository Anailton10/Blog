from django.contrib import admin

from .models import BlogPost, Category, Language


# Register your models here.
@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "created_at")
    search_fields = ("title", "author", "category")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
