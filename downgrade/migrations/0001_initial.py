# Generated by Django 3.2.9 on 2022-03-03 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compensation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='补偿名称')),
            ],
            options={
                'verbose_name': '补偿方案设置',
                'verbose_name_plural': '补偿方案设置',
            },
        ),
        migrations.CreateModel(
            name='FlightType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='类型名称')),
            ],
            options={
                'verbose_name': '航班类型设置',
                'verbose_name_plural': '航班类型设置',
            },
        ),
        migrations.CreateModel(
            name='DowngradeRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='日期')),
                ('flight_number', models.CharField(max_length=30, verbose_name='航班号')),
                ('aircraft_id', models.CharField(max_length=30, verbose_name='飞机号')),
                ('aircraft', models.CharField(max_length=30, verbose_name='飞机型号')),
                ('passenger', models.CharField(max_length=30, verbose_name='旅客姓名')),
                ('phone', models.CharField(max_length=30, verbose_name='联系电话')),
                ('ticket', models.CharField(max_length=30, verbose_name='客票号')),
                ('release', models.CharField(max_length=30, verbose_name='免责书号')),
                ('before_class', models.CharField(max_length=30, verbose_name='原舱位')),
                ('new_class', models.CharField(max_length=30, verbose_name='新舱位')),
                ('compensation_miles', models.FloatField(verbose_name='补偿里程数')),
                ('compensation_amount', models.FloatField(verbose_name='补偿金额')),
                ('fill_datetime', models.DateTimeField(blank=True, null=True, verbose_name='填写时间')),
                ('review', models.BooleanField(default=False, verbose_name='审核状态')),
                ('review_datetime', models.DateTimeField(blank=True, null=True, verbose_name='审核时间')),
                ('supervisor_verify', models.BooleanField(default=False, verbose_name='值班主任审核状态')),
                ('supervisor_verify_datetime', models.DateTimeField(blank=True, null=True, verbose_name='值班主任审核时间')),
                ('manager_verify', models.BooleanField(default=False, verbose_name='主任审核状态')),
                ('manager_verify_datetime', models.DateTimeField(blank=True, null=True, verbose_name='主任审核时间')),
                ('compensation', models.ManyToManyField(to='downgrade.Compensation', verbose_name='补偿方案')),
            ],
            options={
                'verbose_name': '非自愿降舱记录',
                'verbose_name_plural': '非自愿降舱记录',
                'ordering': ['-fill_datetime'],
            },
        ),
    ]
