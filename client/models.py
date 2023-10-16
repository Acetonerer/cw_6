import pytz

from django.db import models

from config import settings


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    name = models.CharField(max_length=250, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Почта', unique=True)
    message = models.TextField(verbose_name='Комментарий')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
