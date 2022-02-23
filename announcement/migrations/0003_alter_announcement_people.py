# Generated by Django 3.2.9 on 2022-02-23 03:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('announcement', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='people',
            field=models.ManyToManyField(blank=True, related_name='announcement_people', to=settings.AUTH_USER_MODEL, verbose_name='目标用户'),
        ),
    ]
