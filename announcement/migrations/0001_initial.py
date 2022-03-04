# Generated by Django 3.2.9 on 2022-03-04 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(max_length=800, verbose_name='内容')),
                ('require_upload', models.BooleanField(default=False, verbose_name='需要上传')),
                ('issue_datetime', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('edit_datetime', models.DateTimeField(auto_now=True, verbose_name='最新修改时间')),
                ('close_datetime', models.DateTimeField(blank=True, verbose_name='截止时间')),
                ('repeat', models.TextField(blank=True, choices=[('', '无'), ('every day', '每天'), ('every week', '每周'), ('every month', '每月'), ('every year', '每年'), ('custom', '自定义/天')], max_length=300, null=True, verbose_name='重复规则')),
                ('repeat_number', models.IntegerField(blank=True, null=True, verbose_name='重复天数')),
                ('period_close_datetime', models.DateTimeField(blank=True, null=True, verbose_name='子阶段截止时间')),
                ('parent_id', models.IntegerField(blank=True, null=True, verbose_name='父id')),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告',
            },
        ),
        migrations.CreateModel(
            name='AnnouncementRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('read_datetime', models.DateTimeField(auto_now=True, verbose_name='确认时间')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcementRecord_announcement', to='announcement.announcement', verbose_name='通知')),
            ],
            options={
                'verbose_name': '公告确认明细',
                'verbose_name_plural': '公告确认明细',
            },
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='files', verbose_name='上传文件')),
                ('announcement_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcement_team', to='announcement.announcementrecord', verbose_name='通知')),
            ],
            options={
                'verbose_name': '上传文件明细',
                'verbose_name_plural': '上传文件明细',
            },
        ),
    ]
