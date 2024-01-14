# Generated by Django 4.2 on 2024-01-14 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_alter_blog_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': [('set_published_status', 'Can publish post')], 'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
    ]
