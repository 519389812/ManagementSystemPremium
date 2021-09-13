# Generated by Django 3.2.6 on 2021-09-13 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='成本名称')),
            ],
            options={
                'verbose_name': '成本',
                'verbose_name_plural': '成本',
            },
        ),
        migrations.CreateModel(
            name='CostType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='成本类别')),
            ],
            options={
                'verbose_name': '成本类别',
                'verbose_name_plural': '成本类别',
            },
        ),
        migrations.CreateModel(
            name='CostRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='日期')),
                ('quantity', models.FloatField(blank=True, null=True, verbose_name='金额')),
                ('remark', models.TextField(blank=True, max_length=1000, verbose_name='备注')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='登记时间')),
                ('cost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cost.cost', verbose_name='成本')),
            ],
            options={
                'verbose_name': '成本登记记录',
                'verbose_name_plural': '成本登记记录',
            },
        ),
    ]
