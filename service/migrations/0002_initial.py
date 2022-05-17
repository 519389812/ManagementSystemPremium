# Generated by Django 3.2.9 on 2022-04-29 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerecord',
            name='fill_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='serviceRecord_fill_user', to=settings.AUTH_USER_MODEL, verbose_name='记录人'),
        ),
        migrations.AddField(
            model_name='servicerecord',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serviceRecord_service', to='service.service', verbose_name='服务名称'),
        ),
        migrations.AddField(
            model_name='servicerecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serviceRecord_user', to=settings.AUTH_USER_MODEL, verbose_name='员工'),
        ),
        migrations.CreateModel(
            name='ServiceRecordSummary',
            fields=[
            ],
            options={
                'verbose_name': '服务满意度得分统计',
                'verbose_name_plural': '服务满意度得分统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('service.servicerecord',),
        ),
    ]
