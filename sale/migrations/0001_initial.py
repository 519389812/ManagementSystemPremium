# Generated by Django 3.2.9 on 2022-04-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='产品名称')),
            ],
            options={
                'verbose_name': '产品设置',
                'verbose_name_plural': '产品设置',
            },
        ),
        migrations.CreateModel(
            name='SalesRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='日期')),
                ('flight_number', models.CharField(max_length=30, verbose_name='航班号')),
                ('passenger', models.CharField(max_length=30, verbose_name='旅客姓名')),
                ('ticket', models.CharField(max_length=30, verbose_name='客票号')),
                ('emd', models.CharField(max_length=30, verbose_name='emd号')),
                ('destination', models.CharField(max_length=30, verbose_name='目的地')),
                ('amount', models.FloatField(verbose_name='销售金额')),
                ('miles', models.FloatField(verbose_name='销售里程')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='登记时间')),
            ],
            options={
                'verbose_name': '销售记录',
                'verbose_name_plural': '产品记录',
            },
        ),
        migrations.CreateModel(
            name='SalesRule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='销量规则名称')),
                ('require', models.CharField(max_length=100, verbose_name='要求量')),
                ('calculation', models.CharField(max_length=100, verbose_name='计算方式')),
            ],
            options={
                'verbose_name': '销量规则设置',
                'verbose_name_plural': '销量规则设置',
            },
        ),
    ]
