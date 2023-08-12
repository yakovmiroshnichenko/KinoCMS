from django.db import models
from src.image_seo.models import ImageGallery

Rotation_Speed_CHOISES = [('5000', '5s'),
                          ('10000', '10s'),
                          ('15000', '15s'),
                          ('20000', '20s'),
                          ('30000', '30s'),
                          ('45000', '45s'),
                          ('60000', '1m'),
                          ]


class BackgroundBanner(models.Model):
    image = models.ImageField
    # TODO: upload_to, MEDIA_ROOT для ImageField
    color = models.CharField(max_length=7)
    is_image = models.BooleanField()


class BannerNews(models.Model):
    rotation_speed = models.CharField(max_length=10, choices=Rotation_Speed_CHOISES, default='5000')
    url = models.URLField()
    active = models.BooleanField()
    gallery = models.OneToOneField(ImageGallery, on_delete=models.PROTECT)


class Banner(models.Model):
    text = models.CharField(max_length=50)
    rotation_speed = models.CharField(max_length=10, choices=Rotation_Speed_CHOISES, default='5000')
    url = models.URLField()
    active = models.BooleanField()
    gallery = models.OneToOneField(ImageGallery, on_delete=models.PROTECT)
