from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news_app.views import home, privacy_policy

urlpatterns = [
    path('', home),
    path('privacy-policy/', privacy_policy),
    path('admin/', admin.site.urls),
    path('api/', include('news_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)