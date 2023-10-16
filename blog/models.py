from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержание')
    picture = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='Изображение')
    view_count = models.IntegerField(default=0, verbose_name="Количество просмотров")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.title} ({self.date_created})'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
