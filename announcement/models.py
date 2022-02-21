from django.db import models
from team.models import CustomTeam
from user.models import CustomUser
from django.utils import timezone
from ManagementSystemPremium.settings import BASE_DIR
import os
from django.contrib import admin


file_dir = 'files'
file_path = os.path.join(BASE_DIR, 'announcement', file_dir)


class Announcement(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='announcement_user', on_delete=models.CASCADE, verbose_name='作者')
    title = models.TextField(max_length=100, verbose_name='标题')
    content = models.TextField(max_length=800, verbose_name='内容')
    team = models.ManyToManyField(CustomTeam, related_name='announcement_team', null=True, blank=True, verbose_name='目标组')
    people = models.ManyToManyField(CustomTeam, related_name='announcement_people', null=True, blank=True, verbose_name='目标用户')
    require_upload = models.BooleanField(default=False, verbose_name='需要上传')
    issue_datetime = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    edit_datetime = models.DateTimeField(auto_now=True, verbose_name='最新修改时间')
    close_datetime = models.DateTimeField(blank=True, verbose_name='截止时间')
    repeat = models.TextField(max_length=300, null=True, blank=True, choices=(('', '无'), ('every day', '每天'), ('every week', '每周'), ('every month', '每月'), ('every year', '每年'), ('custom', '自定义/天')), verbose_name='重复规则')

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = '公告'

    def __str__(self):
        return self.title

    def template_announcement_is_active(self):
        return True if self.close_datetime <= timezone.now() else False

    def template_content_preview(self):
        return self.content[:20]


class AnnouncementRecord(models.Model):
    id = models.AutoField(primary_key=True)
    announcement = models.ForeignKey(Announcement, related_name='announcementRecord_announcement', on_delete=models.CASCADE, verbose_name='通知')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='阅读人')
    read_datetime = models.DateTimeField(auto_now=True, verbose_name='确认时间')

    class Meta:
        verbose_name = '公告确认明细'
        verbose_name_plural = '公告确认明细'

    def __str__(self):
        return self.id


class AnnouncementRecordSummary(AnnouncementRecord):

    class Meta:
        proxy = True
        verbose_name = '确认统计'
        verbose_name_plural = '确认统计'


class UploadFile(models.Model):
    id = models.AutoField(primary_key=True)
    announcement_record = models.ForeignKey(AnnouncementRecord, related_name='announcement_team', on_delete=models.CASCADE, verbose_name='通知')
    file = models.FileField(upload_to=file_dir, verbose_name='上传文件')

    class Meta:
        verbose_name = '上传文件明细'
        verbose_name_plural = '上传文件明细'

    def __str__(self):
        return self.id
