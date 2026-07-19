from django.shortcuts import render # ye abhi hua hai
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from .models import News, Category, Epaper, Advertisement
from django.http import JsonResponse
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
        data = {
            "city": "Delhi",
            "temperature": "32°C",
            "condition": "Sunny"
        }
        return JsonResponse(data)

# ---------------- HOME PAGE ----------------
def home(request):
    return render(request, 'index.html')
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
