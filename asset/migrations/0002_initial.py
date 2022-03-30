# Generated by Django 3.2.9 on 2022-03-30 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentrecord',
            name='operating_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currentRecord_operating_user', to=settings.AUTH_USER_MODEL, verbose_name='操作人'),
        ),
        migrations.AddField(
            model_name='currentrecord',
            name='rack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currentRecord_rack', to='asset.rack', verbose_name='位置'),
        ),
        migrations.AddField(
            model_name='current',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_type', to='asset.currenttype', verbose_name='类型'),
        ),
    ]
