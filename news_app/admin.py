from django.contrib import admin
from .models import Category, News, Epaper, Advertisement

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


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'position', 'is_active', 'order', 'created_at')
    list_filter = ('position', 'is_active')
    list_editable = ('is_active', 'order')
    search_fields = ('title',)
