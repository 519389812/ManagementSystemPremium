# Generated by Django 3.2.9 on 2022-03-30 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentStorage',
            fields=[
                ('id', models.CharField(max_length=29, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=500, verbose_name='内容')),
                ('signature', models.TextField(blank=True, max_length=150000, verbose_name='签名')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('edit_datetime', models.DateTimeField(auto_now=True, verbose_name='最新修改时间')),
            ],
            options={
                'verbose_name': '文档内容',
                'verbose_name_plural': '文档内容',
            },
        ),
        migrations.CreateModel(
            name='DocxInit',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('template_name', models.CharField(max_length=30, verbose_name='模板名')),
                ('docx_name', models.CharField(max_length=30, verbose_name='文档名')),
                ('content', models.TextField(max_length=500, verbose_name='内容')),
                ('version', models.IntegerField(default=0, verbose_name='版本号')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('edit_datetime', models.DateTimeField(auto_now=True, verbose_name='最新修改时间')),
                ('close_datetime', models.DateTimeField(blank=True, verbose_name='截止时间')),
            ],
            options={
                'verbose_name': '文档',
                'verbose_name_plural': '文档',
            },
        ),
        migrations.CreateModel(
            name='SignatureStorage',
            fields=[
                ('id', models.CharField(max_length=29, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=500, verbose_name='内容')),
                ('signature', models.TextField(blank=True, max_length=150000, verbose_name='签名')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('docx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.docxinit', verbose_name='模板')),
            ],
            options={
                'verbose_name': '签名',
                'verbose_name_plural': '签名',
            },
        ),
    ]
