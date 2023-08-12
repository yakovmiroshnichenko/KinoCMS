from django.db import models
from src.image_seo.models import ImageGallery, SEO


class Cinema(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    conditions = models.TextField()
    logo = models.ImageField
    banner_image = models.ImageField
    # TODO: upload_to, MEDIA_ROOT для ImageField
    gallery = models.OneToOneField(ImageGallery, on_delete=models.PROTECT)
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)


class Film(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    release = models.DateField(null=False)
    main_image = models.ImageField
    # TODO: upload_to, MEDIA_ROOT для ImageField
    gallery = models.OneToOneField(ImageGallery, on_delete=models.PROTECT)
    trailer_url = models.URLField(blank=True)
    type_2D = models.BooleanField()
    type_3D = models.BooleanField()
    type_IMAX = models.BooleanField()
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)


class Hall(models.Model):
    # TODO: upload_to, MEDIA_ROOT для ImageField
    cinema = models.ForeignKey(Cinema, on_delete=models.PROTECT)
    number = models.SmallIntegerField()
    description = models.TextField()
    scheme_image = models.ImageField
    banner_image = models.ImageField
    gallery = models.OneToOneField(ImageGallery, on_delete=models.PROTECT)
    seo = models.OneToOneField(SEO, on_delete=models.PROTECT)


class MovieSession(models.Model):
    # TODO: ???on_delete для Film и Hall???
    film = models.ForeignKey(Film, on_delete=models.PROTECT)
    hall = models.ForeignKey(Hall, on_delete=models.PROTECT)
    price = models.SmallIntegerField()
    time = models.DateTimeField()
    type_3D = models.BooleanField()
    type_DBOX = models.BooleanField()
    VIP = models.BooleanField()
