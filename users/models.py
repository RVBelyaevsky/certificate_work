from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=50, verbose_name="номер", **NULLABLE)
    first_name = models.CharField(max_length=20, verbose_name="имя")
    last_name = models.CharField(max_length=50, verbose_name="фамилия")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
