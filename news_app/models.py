from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

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
    image = models.ImageField(upload_to='ads/')
    link_url = models.URLField(blank=True, null=True)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, default='sidebar')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.position})'
