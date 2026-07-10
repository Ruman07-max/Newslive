from rest_framework import serializers
from .models import News, Category, Epaper  # Reporter class remove kiya, News me string field hai

# ---------------- CATEGORY ----------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # slug field remove, tumhare model me nahi tha

# ---------------- NEWS ----------------
class NewsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'description',
            'image',
            'date',
            'category',
            'category_name'
        ]

# ---------------- EPAPER ----------------
class EpaperSerializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Epaper
        fields = ['id', 'title', 'pdf', 'publish_date', 'pdf_url']

    def get_pdf_url(self, obj):
        request = self.context.get('request')
        if obj.pdf:
            return request.build_absolute_uri(obj.pdf.url) if request else obj.pdf.url
        return None
