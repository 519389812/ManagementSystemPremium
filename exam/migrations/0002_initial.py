# Generated by Django 3.2.9 on 2022-04-29 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_update_user', to=settings.AUTH_USER_MODEL, verbose_name='更新用户'),
        ),
        migrations.AddField(
            model_name='examrecord',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examRecord_exam', to='exam.exam', verbose_name='试卷'),
        ),
        migrations.AddField(
            model_name='examrecord',
            name='question',
            field=models.ManyToManyField(blank=True, related_name='examRecord_question', to='exam.Question', verbose_name='题目'),
        ),
        migrations.AddField(
            model_name='examrecord',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='examRecord_user', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='exam',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_course', to='exam.course', verbose_name='科目'),
        ),
        migrations.AddField(
            model_name='exam',
            name='question',
            field=models.ManyToManyField(limit_choices_to={'Question__course__name': None}, to='exam.Question', verbose_name='题目'),
        ),
        migrations.AddField(
            model_name='exam',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_update_user', to=settings.AUTH_USER_MODEL, verbose_name='更新用户'),
        ),
    ]
