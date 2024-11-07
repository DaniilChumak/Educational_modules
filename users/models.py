from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name="Имя",
        **NULLABLE
    )
    last_name = models.CharField(
        max_length=200,
        verbose_name="Фамилия",
        **NULLABLE
    )
    country = models.CharField(
        max_length=150,
        verbose_name="Страна",
        **NULLABLE
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/",
        verbose_name="Аватар",
        **NULLABLE
    )
    last_login = models.DateTimeField(
        verbose_name="Дата последнего входа",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("email",)
