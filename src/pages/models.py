from django.db import models
from src.image_seo.models import SEO, ImageGallery


class MainPage(models.Model):
    # TODO: Дата
    active = models.BooleanField(default=True)
    phone1 = models.CharField(max_length=19)
    phone2 = models.CharField(max_length=19)
    seo_text = models.TextField()
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)


class OtherPage(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    main_image = models.ImageField
    # TODO: upload_to, MEDIA_ROOT для ImageField
    gallery = models.OneToOneField(ImageGallery, on_delete=models.PROTECT)
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)


class Contact(models.Model):
    # TODO: Активность кинотеатра
    name = models.CharField(50)
    address = models.TextField
    coords = models.CharField(20)
    logo = models.ImageField
    # TODO: upload_to, MEDIA_ROOT для ImageField


class NewsPromotionPage(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()
    main_image = models.ImageField
    # TODO: upload_to, MEDIA_ROOT для ImageField
    gallery = models.OneToOneField(ImageGallery, on_delete=models.PROTECT)
    url = models.URLField()
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
