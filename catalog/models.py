from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    pict = models.ImageField(upload_to='image/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')
    date_create = models.DateTimeField(verbose_name='Дата создания')
    date_edit = models.DateTimeField(verbose_name='Дата изменения')

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

