from django.db import models


class ImageGallery(models.Model):
    class Meta:
        verbose_name = 'Gallery'


class Image(models.Model):
    image = models.ImageField
    gallery = models.ForeignKey(ImageGallery, on_delete=models.PROTECT, blank=True)


class SEO(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200)
    description = models.TextField()
