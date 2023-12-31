# Generated by Django 4.2.7 on 2023-12-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=250, verbose_name='slug')),
                ('text', models.TextField(verbose_name='Содержание')),
                ('pict', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Изображение')),
                ('date_create', models.DateTimeField(verbose_name='Дата создания')),
                ('published', models.BooleanField(verbose_name='Признак публикации')),
                ('total_view', models.IntegerField(verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
    ]
