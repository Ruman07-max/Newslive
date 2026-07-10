from django.urls import path
from .views import NewsList, CategoryList, EpaperList, WeatherAPI


urlpatterns = [
    path('news/', NewsList.as_view(), name='news_list'),
    path('categories/', CategoryList.as_view(), name='categories_list'),
    path('epaper/', EpaperList.as_view(), name='epaper_list'),
    path('weather/', WeatherAPI.as_view(), name='weather_api'),  # ✅ ADD
]
