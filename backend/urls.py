# from django.contrib import admin
# from django.urls import path, include
# from django.http import HttpResponse

# from django.conf import settings
# from django.conf.urls.static import static

# def home(request):
#     return HttpResponse("Backend is working!")

# urlpatterns = [
#     path('', home),                      # http://127.0.0.1:8000/
#     path('admin/', admin.site.urls),     # admin panel
#     path('api/', include('news_app.urls')),  # API endpoints
    

# ]

# # 🔥 MEDIA (IMAGE / PDF) serve karne ke liye
# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news_app.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('news_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)