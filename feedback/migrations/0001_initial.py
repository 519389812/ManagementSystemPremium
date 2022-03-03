# Generated by Django 3.2.9 on 2022-03-03 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('anonymous', models.CharField(blank=True, max_length=300, null=True, verbose_name='未登录用户')),
                ('submit_datetime', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
                ('content', models.TextField(max_length=100000, verbose_name='内容')),
                ('contact', models.TextField(blank=True, max_length=1000, null=True, verbose_name='联系方式')),
            ],
            options={
                'verbose_name': '留言',
                'verbose_name_plural': '留言',
            },
        ),
    ]
