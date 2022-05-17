# Generated by Django 3.2.9 on 2022-04-29 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sale', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='salesrecord',
            name='issue_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesRecord_issue_user', to=settings.AUTH_USER_MODEL, verbose_name='开票人'),
        ),
        migrations.AddField(
            model_name='salesrecord',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesRecord_product', to='sale.product', verbose_name='产品名称'),
        ),
        migrations.AddField(
            model_name='salesrecord',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesRecord_user', to=settings.AUTH_USER_MODEL, verbose_name='经办人'),
        ),
        migrations.CreateModel(
            name='SalesSummary',
            fields=[
            ],
            options={
                'verbose_name': '销售统计',
                'verbose_name_plural': '销售统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sale.salesrecord',),
        ),
    ]
