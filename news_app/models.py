from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage, VideoMediaCloudinaryStorage

# ---------------- CATEGORY ----------------
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# ---------------- NEWS ----------------
class News(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='news'
    )
    reporter = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        from django.utils.text import slugify
        import re
        slug = self.title.lower()
        slug = re.sub(r'[^\u0900-\u097F\u0600-\u06FFa-z0-9\s-]', '', slug)
        slug = slug.strip()
        slug = re.sub(r'\s+', '-', slug)
        return f'/news/{self.id}/{slug}/'

class Epaper(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(
        upload_to='epaper/',
        storage=RawMediaCloudinaryStorage()
    )  # PDFs saved in Cloudinary as raw files
    publish_date = models.DateField()  # manually select publish date in admin
    def __str__(self):
        return self.title

# ---------------- ADVERTISEMENT ----------------
class Advertisement(models.Model):
    POSITION_CHOICES = [
        ('header', 'Header ke neeche'),
        ('sidebar', 'Sidebar'),
        ('footer', 'Footer'),
        ('in_feed', 'News ke beech me'),
    ]
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/', blank=True, null=True)
    video = models.FileField(upload_to='ads_videos/', blank=True, null=True, storage=VideoMediaCloudinaryStorage(), help_text='MP4 video (image ya vidio dono me se aik koi )')
    link_url = models.URLField(blank=True, null=True)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, default='sidebar')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.position})'