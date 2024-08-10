from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name="Почта", unique=True
    )
    phone_number = models.CharField(
        verbose_name="Номер телефона", max_length=30, **NULLABLE
    )
    avatar = models.ImageField(
        verbose_name="Аватар", upload_to="users/", **NULLABLE
    )
    city = models.CharField(
        verbose_name="Город", max_length=100, **NULLABLE
    )
    tg_id = models.CharField(
        verbose_name="ID в телегераме", max_length=50, **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
