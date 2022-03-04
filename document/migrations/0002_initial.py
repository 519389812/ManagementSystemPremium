# Generated by Django 3.2.9 on 2022-03-04 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('document', '0001_initial'),
        ('team', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='signaturestorage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='填写人'),
        ),
        migrations.AddField(
            model_name='docxinit',
            name='team',
            field=models.ManyToManyField(blank=True, to='team.CustomTeam', verbose_name='目标组'),
        ),
        migrations.AddField(
            model_name='docxinit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='contentstorage',
            name='docx',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.docxinit', verbose_name='模板'),
        ),
        migrations.AddField(
            model_name='contentstorage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='填写人'),
        ),
    ]
