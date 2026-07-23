import requests
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.conf import settings
from .models import News, Category, Epaper, Advertisement
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView

# ---------------- NEWS LIST ----------------
class NewsList(View):
    def get(self, request):
        news_qs = News.objects.all().order_by('-date')
        news_list = []
        for n in news_qs:
            news_list.append({
                'id': n.id,
                'title': n.title,
                'description': n.description,
                'category': n.category.name if n.category else None,
                'reporter': n.reporter,
                'image': request.build_absolute_uri(n.image.url) if n.image else None,
                'date': n.date,
            })
        return JsonResponse(news_list, safe=False)

# ---------------- CATEGORY LIST ----------------
class CategoryList(View):
    def get(self, request):
        categories_qs = Category.objects.all()
        categories = [{'id': c.id, 'name': c.name} for c in categories_qs]
        return JsonResponse(categories, safe=False)

# ---------------- EPAPER LIST ----------------
class EpaperList(View):
    def get(self, request):
        epapers_qs = Epaper.objects.all().order_by('-publish_date')
        epapers_list = []
        for e in epapers_qs:
            pdf_url = e.pdf.url if e.pdf else None
            epapers_list.append({
                'id': e.id,
                'title': e.title,
                'publish_date': e.publish_date,
                'pdf': pdf_url
            })
        return JsonResponse(epapers_list, safe=False)

# ---------------- WEATHER API ----------------
class WeatherAPI(APIView):
    def get(self, request):
        weather_descriptions = {
            0: 'Clear Sky', 1: 'Clear', 2: 'Partly Sunny', 3: 'Cloudy',
            45: 'Foggy', 48: 'Foggy', 51: 'Light Drizzle', 53: 'Drizzle',
            55: 'Heavy Drizzle', 61: 'Light Rain', 63: 'Rain', 65: 'Heavy Rain',
            80: 'Light Showers', 81: 'Showers', 82: 'Heavy Showers', 95: 'Thunderstorm'
        }
        weather_icons = {
            0: 'fa-sun', 1: 'fa-sun', 2: 'fa-cloud-sun', 3: 'fa-cloud',
            45: 'fa-smog', 48: 'fa-smog', 51: 'fa-cloud-rain', 53: 'fa-cloud-rain',
            55: 'fa-cloud-rain', 61: 'fa-cloud-showers-heavy', 63: 'fa-cloud-showers-heavy', 65: 'fa-cloud-showers-heavy',
            80: 'fa-cloud-showers-heavy', 81: 'fa-cloud-showers-heavy', 82: 'fa-cloud-showers-heavy', 95: 'fa-bolt'
        }
        try:
            url = (
                "https://api.open-meteo.com/v1/forecast"
                "?latitude=23.3441&longitude=85.3096"
                "&current=temperature_2m,weather_code,relative_humidity_2m,wind_speed_10m,precipitation_probability"
                "&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max"
                "&timezone=Asia%2FKolkata&forecast_days=6"
            )
            response = requests.get(url, timeout=5)
            w = response.json()
            cur = w['current']
            code = cur['weather_code']

            daily = w['daily']
            import datetime
            forecast = []
            for i in range(1, 6):
                date_obj = datetime.datetime.strptime(daily['time'][i], '%Y-%m-%d')
                day_label = date_obj.strftime('%a')
                forecast.append({
                    'day': day_label,
                    'max_temp': round(daily['temperature_2m_max'][i]),
                    'min_temp': round(daily['temperature_2m_min'][i]),
                    'description': weather_descriptions.get(daily['weather_code'][i], 'Normal'),
                    'icon': weather_icons.get(daily['weather_code'][i], 'fa-cloud'),
                    'rain_chance': daily['precipitation_probability_max'][i],
                })

            data = {
                "city": "Ranchi",
                "temperature": round(cur['temperature_2m']),
                "description": weather_descriptions.get(code, 'Normal'),
                "icon": weather_icons.get(code, 'fa-cloud'),
                "humidity": cur['relative_humidity_2m'],
                "wind_speed": round(cur['wind_speed_10m']),
                "rain_chance": cur.get('precipitation_probability', 0),
                "forecast": forecast,
            }
        except Exception:
            data = {
                "city": "Ranchi",
                "temperature": 32,
                "description": "Partly Sunny",
                "icon": "fa-cloud-sun",
                "humidity": 60,
                "wind_speed": 10,
                "rain_chance": 0,
                "forecast": []
            }
        return JsonResponse(data)

# ---------------- HOME PAGE ----------------
def home(request):
    return render(request, 'index.html')

# ---------------- NEWS DETAIL ----------------
def news_detail(request, news_id, slug):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news_detail.html', {'news': news})
# ---------------- ADVERTISEMENT LIST ----------------
class AdvertisementList(View):
    def get(self, request):
        position = request.GET.get('position')
        ads_qs = Advertisement.objects.filter(is_active=True).order_by('order')
        if position:
            ads_qs = ads_qs.filter(position=position)
        ads_list = []
        for a in ads_qs:
            ads_list.append({
                'id': a.id,
                'title': a.title,
                'image': request.build_absolute_uri(a.image.url) if a.image else None,
                'video': request.build_absolute_uri(a.video.url) if a.video else None,
                'link_url': a.link_url,
                'position': a.position,
            })
        return JsonResponse(ads_list, safe=False)

# ---------------- PRIVACY POLICY ----------------
def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def robots_txt(request):
    content = "User-agent: *\nAllow: /\n\nSitemap: https://rahnumamanzil.com/sitemap.xml\n"
    return HttpResponse(content, content_type="text/plain")
