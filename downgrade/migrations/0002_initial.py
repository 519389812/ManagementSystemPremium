# Generated by Django 3.2.9 on 2022-04-29 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('downgrade', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='downgraderecord',
            name='fill_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='downgradeRecord_fill_user', to=settings.AUTH_USER_MODEL, verbose_name='经办人'),
        ),
        migrations.AddField(
            model_name='downgraderecord',
            name='manager_verify_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='downgradeRecord_manager_verify_user', to=settings.AUTH_USER_MODEL, verbose_name='审核主任'),
        ),
        migrations.AddField(
            model_name='downgraderecord',
            name='review_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='downgradeRecord_review_user', to=settings.AUTH_USER_MODEL, verbose_name='审核人'),
        ),
        migrations.AddField(
            model_name='downgraderecord',
            name='supervisor_verify_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='downgradeRecord_supervisor_verify_user', to=settings.AUTH_USER_MODEL, verbose_name='审核值班主任'),
        ),
        migrations.AddField(
            model_name='downgraderecord',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downgradeRecord_type', to='downgrade.flighttype', verbose_name='航班类型'),
        ),
        migrations.CreateModel(
            name='DowngradeSummary',
            fields=[
            ],
            options={
                'verbose_name': '非自愿降舱统计',
                'verbose_name_plural': '非自愿降舱统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('downgrade.downgraderecord',),
        ),
    ]