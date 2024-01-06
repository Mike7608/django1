from django.db import models
from django.urls import reverse
from users.models import User


class Blog(models.Model):
    heading = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=250, verbose_name='slug')
    text = models.TextField(verbose_name='Содержание')
    pict = models.ImageField(upload_to='image/', verbose_name='Изображение', blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(default=True, verbose_name='Признак публикации')
    total_view = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='автор')

    def __str__(self):
        return f"{self.heading}, дата публикации: {self.date_create}, просмотров: {self.total_view}"

    def get_absolute_url(self):
        return reverse('blog:view', kwargs={'pk': self.id})

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"


class Version(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="блог")
    version = models.PositiveSmallIntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    sign = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f"{self.blog}, версия: {self.version}, наименование: {self.name}, признак: {self.sign}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
