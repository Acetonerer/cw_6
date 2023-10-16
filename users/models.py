from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    is_active = models.BooleanField(default=False)

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', null=True, blank=True)
    phone = models.CharField(max_length=50, verbose_name='Номер телефона', null=True, blank=True)
    verif_code = models.CharField(max_length=100, verbose_name='Код для верификации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
