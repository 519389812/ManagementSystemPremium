# Generated by Django 3.2.9 on 2022-03-03 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('performance', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workloadrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workloadRecord_user', to=settings.AUTH_USER_MODEL, verbose_name='登记人'),
        ),
        migrations.AddField(
            model_name='workloadrecord',
            name='verifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workloadRecord_verifier', to='team.customteam', verbose_name='审核组'),
        ),
        migrations.AddField(
            model_name='workloadrecord',
            name='verify_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workloadRecord_verify_user', to=settings.AUTH_USER_MODEL, verbose_name='审核人'),
        ),
        migrations.AddField(
            model_name='workloaditem',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.position', verbose_name='所属岗位'),
        ),
        migrations.AddField(
            model_name='manhourrecord',
            name='man_hour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manHourRecord_man_hour', to='performance.manhouritem', verbose_name='所属岗位'),
        ),
        migrations.AddField(
            model_name='manhourrecord',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manHourRecord_position', to='performance.position', verbose_name='岗位'),
        ),
        migrations.AddField(
            model_name='manhourrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manHourRecord_user', to=settings.AUTH_USER_MODEL, verbose_name='登记人'),
        ),
        migrations.AddField(
            model_name='manhourrecord',
            name='verifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manHourRecord_verifier', to='team.customteam', verbose_name='审核组'),
        ),
        migrations.AddField(
            model_name='manhourrecord',
            name='verify_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manHourRecord_verify_user', to=settings.AUTH_USER_MODEL, verbose_name='审核人'),
        ),
        migrations.AddField(
            model_name='manhouritem',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performance.position', verbose_name='所属岗位'),
        ),
        migrations.CreateModel(
            name='ManHourSummary',
            fields=[
            ],
            options={
                'verbose_name': '工时统计',
                'verbose_name_plural': '工时统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('performance.manhourrecord',),
        ),
        migrations.CreateModel(
            name='WorkloadSummary',
            fields=[
            ],
            options={
                'verbose_name': '工作量统计',
                'verbose_name_plural': '工作量统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('performance.workloadrecord',),
        ),
    ]
