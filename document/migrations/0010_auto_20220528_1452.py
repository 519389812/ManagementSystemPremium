# Generated by Django 3.2.9 on 2022-05-28 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0009_alter_contentstorage_signature_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentstorage',
            name='content_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='内容名'),
        ),
        migrations.AlterField(
            model_name='contentstorage',
            name='content',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='contentstorage',
            name='content_id',
            field=models.CharField(max_length=30, unique=True, verbose_name='填写id'),
        ),
        migrations.AlterField(
            model_name='contentstorage',
            name='is_confirm',
            field=models.BooleanField(default=False, verbose_name='远程确认签字'),
        ),
    ]
