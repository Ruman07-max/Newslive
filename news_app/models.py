from django.db import models

# ---------------- CATEGORY ----------------
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# ---------------- NEWS ----------------
class News(models.Model):
    title = models.CharField(max_length=255)
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


# ---------------- EPAPER ----------------
class Epaper(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='epaper/')  # PDFs saved in media/epaper/
    publish_date = models.DateField()  # manually select publish date in admin

    def __str__(self):
        return self.title
