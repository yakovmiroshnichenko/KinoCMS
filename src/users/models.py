from django.db import models
from django.contrib.auth.models import AbstractUser
from src.cinema.models import MovieSession


class User(AbstractUser):
    # TODO: Абстрактный пользователь?
    CHOISES_language = [('uk', 'Українська'), ('ru', 'Русский')]
    CHOISES_gender = [('Male', 'Male'), ('Female', 'Female')]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=150)
    password = models.CharField(max_length=40)
    card_number = models.CharField(max_length=19)
    gender = models.CharField(max_length=10, choices=CHOISES_gender)
    language = models.CharField(max_length=10, choices=CHOISES_language)
    phone = models.CharField(max_length=19, unique=True)
    birth_date = models.DateField(null=True)
    city = models.CharField(max_length=50)


class Ticket(models.Model):
    session = models.ForeignKey(MovieSession, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    seat = models.CharField(max_length=5)
    reservation = models.BooleanField()
