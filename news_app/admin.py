from django.contrib import admin
from .models import Category, News, Epaper

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'reporter', 'date')
    list_filter = ('category',)
    search_fields = ('title', 'reporter')


@admin.register(Epaper)
class EpaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish_date')
