# Generated by Django 3.2.7 on 2021-09-11 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
        ('performance', '0001_initial'),
        ('rule', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workloadRecord_team', to='team.customteam', verbose_name='审核组'),
        ),
        migrations.AddField(
            model_name='workloadrecord',
            name='verify_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workloadRecord_verify_user', to=settings.AUTH_USER_MODEL, verbose_name='审核人'),
        ),
        migrations.AddField(
            model_name='rewardrecord',
            name='create_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='登记人'),
        ),
        migrations.AddField(
            model_name='rewardrecord',
            name='level_rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rule.levelrule', verbose_name='程度加成规则'),
        ),
        migrations.AddField(
            model_name='rewardrecord',
            name='reward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rule.reward', verbose_name='奖励项'),
        ),
        migrations.AddField(
            model_name='rewardrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewardRecord_user', to=settings.AUTH_USER_MODEL, verbose_name='奖励人'),
        ),
        migrations.AddField(
            model_name='penaltyrecord',
            name='create_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='登记人'),
        ),
        migrations.AddField(
            model_name='penaltyrecord',
            name='level_rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rule.levelrule', verbose_name='程度加成规则'),
        ),
        migrations.AddField(
            model_name='penaltyrecord',
            name='penalty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rule.penalty', verbose_name='处罚项'),
        ),
        migrations.AddField(
            model_name='penaltyrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penaltyRecord_user', to=settings.AUTH_USER_MODEL, verbose_name='责任人'),
        ),
        migrations.CreateModel(
            name='PenaltySummary',
            fields=[
            ],
            options={
                'verbose_name': '处罚统计',
                'verbose_name_plural': '处罚统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('performance.penaltyrecord',),
        ),
        migrations.CreateModel(
            name='RewardSummary',
            fields=[
            ],
            options={
                'verbose_name': '奖惩统计',
                'verbose_name_plural': '奖励统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('performance.rewardrecord',),
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
