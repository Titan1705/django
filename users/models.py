from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.CharField(unique= True, verbose_name="Email")

    phone = models.CharField(max_length=35, verbose_name="Телефон", blank=True,
        null=True , help_text="Введите номер телефона")
    Country = models.CharField(max_length=20, verbose_name="Страна", blank=True,
        null=True , help_text="Страна проживания")
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name="Страна", blank=True,
        null=True , help_text="Загрузите фото")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email