from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news_app.views import home, privacy_policy, news_detail
from django.contrib.sitemaps.views import sitemap
from news_app.sitemaps import NewsSitemap, CategorySitemap

sitemaps = {
    'news': NewsSitemap,
    'categories': CategorySitemap,
}

urlpatterns = [
    path('', home),
    path('privacy-policy/', privacy_policy),
    path('admin/', admin.site.urls),
    path('news/<int:news_id>/<str:slug>/', news_detail, name='news_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('api/', include('news_app.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




