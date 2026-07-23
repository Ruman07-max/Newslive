from django.contrib.sitemaps import Sitemap
from .models import News, Category


class NewsSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return obj.get_absolute_url()


class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return f'/?category={obj.name}'
