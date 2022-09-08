from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """clase para generar mi modelo personalizado de Users"""

    GENDER_CHOICES = (("1", "hombre"), ("2", "mujer"),)

    username = models.CharField("nombre de usuario", max_length=50, unique=True)
    full_name = models.CharField("nombre completo", max_length=150)
    gender = models.CharField("género", max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    age = models.PositiveIntegerField("edad", blank=True, null=True)
    email = models.EmailField("correo electrónico", max_length=254, unique=True)

    USERNAME_FIELD = "username"

    objects = UserManager()
