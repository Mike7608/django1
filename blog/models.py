import datetime

from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    heading = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=250, verbose_name='slug')
    text = models.TextField(verbose_name='Содержание')
    pict = models.ImageField(upload_to='image/', verbose_name='Изображение', **NULLABLE)
    date_create = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата создания')
    published = models.BooleanField(default=True, verbose_name='Признак публикации')
    total_view = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f"{self.heading}, дата публикации: {self.date_create}, просмотров: {self.total_view}"

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
