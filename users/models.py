from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Почта", unique=True)
    first_name = models.CharField(
        verbose_name="Имя пользователя", max_length=75, **NULLABLE
    )
    last_name = models.CharField(
        verbose_name="Фамилия пользователя", max_length=75, **NULLABLE
    )
    phone = models.CharField(verbose_name="Номер телефона", max_length=30, **NULLABLE)
    image = models.ImageField(verbose_name="Аватар", upload_to="users/", **NULLABLE)
    token = models.CharField(verbose_name="Токен", max_length=10, default="-")

    USER_ROLE = "user"
    ADMIN_ROLE = "admin"

    ROLE_CHOICES = [
        (USER_ROLE, "User"),
        (ADMIN_ROLE, "Admin"),
    ]

    role = models.CharField(
        verbose_name="Роль", max_length=10, choices=ROLE_CHOICES, default=USER_ROLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
