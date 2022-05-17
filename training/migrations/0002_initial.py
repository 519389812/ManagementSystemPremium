# Generated by Django 3.2.9 on 2022-04-29 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('training', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingrecord',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='trainingRecord_user', to=settings.AUTH_USER_MODEL, verbose_name='培训对象'),
        ),
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.coursetype', verbose_name='课程类别'),
        ),
        migrations.CreateModel(
            name='TrainingRecordSummary',
            fields=[
            ],
            options={
                'verbose_name': '培训统计',
                'verbose_name_plural': '培训统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('training.trainingrecord',),
        ),
    ]
