from django.db import models
import django.utils.timezone as timezone
from user.models import CustomUser
from team.models import CustomTeam
from django.contrib import admin
from django.apps import apps


class Position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='岗位名称')

    class Meta:
        verbose_name = '岗位'
        verbose_name_plural = '岗位'

    def __str__(self):
        return self.name


class WorkloadItem(models.Model):
    id = models.AutoField(primary_key=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='所属岗位')
    name = models.CharField(max_length=100, verbose_name='项目')
    weight = models.FloatField(verbose_name='每单位折算产出')

    class Meta:
        verbose_name = '工作量项目'
        verbose_name_plural = '工作量项目'

    def __str__(self):
        return self.name


class WorkloadRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='workloadRecord_user', on_delete=models.CASCADE, verbose_name='登记人')
    date = models.DateField(verbose_name='日期')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='岗位')
    workload = models.JSONField(max_length=1000, blank=True, verbose_name='项目')
    verifier = models.ForeignKey(CustomTeam, related_name='workloadRecord_verifier', on_delete=models.CASCADE, verbose_name='审核组')
    remark = models.TextField(max_length=1000, blank=True, verbose_name='备注')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='登记时间')
    verify = models.BooleanField(default=False, verbose_name='审核状态')
    verify_user = models.ForeignKey(CustomUser, null=True, blank=True, related_name='workloadRecord_verify_user', on_delete=models.CASCADE, verbose_name='审核人')
    verify_datetime = models.DateTimeField(null=True, blank=True, verbose_name='审核时间')

    class Meta:
        verbose_name = '工作量登记记录'
        verbose_name_plural = '工作量登记记录'
        ordering = ['-create_datetime']

    def __str__(self):
        return self.id


class WorkloadSummary(WorkloadRecord):

    class Meta:
        proxy = True
        verbose_name = '工作量统计'
        verbose_name_plural = '工作量统计'


class ManHourItem(models.Model):
    id = models.AutoField(primary_key=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='所属岗位')
    name = models.CharField(max_length=100, verbose_name='项目')
    weight = models.FloatField(verbose_name='每单位折算产出')

    class Meta:
        verbose_name = '工时项目'
        verbose_name_plural = '工时项目'

    def __str__(self):
        return self.name


class ManHourRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='manHourRecord_user', on_delete=models.CASCADE, verbose_name="登记人")
    position = models.ForeignKey(Position, related_name='manHourRecord_position', on_delete=models.CASCADE, verbose_name="岗位")
    man_hour = models.ForeignKey(ManHourItem, related_name='manHourRecord_man_hour', on_delete=models.CASCADE, verbose_name='所属岗位')
    start_datetime = models.DateTimeField(verbose_name="开始时间")
    end_datetime = models.DateTimeField(verbose_name="结束时间")
    verifier = models.ForeignKey(CustomTeam, related_name='manHourRecord_verifier', on_delete=models.CASCADE, verbose_name='审核组')
    remark = models.TextField(max_length=1000, blank=True, verbose_name='备注')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='登记时间')
    verify = models.BooleanField(default=False, verbose_name='审核状态')
    verify_user = models.ForeignKey(CustomUser, null=True, blank=True, related_name='manHourRecord_verify_user', on_delete=models.CASCADE, verbose_name='审核人')
    verify_datetime = models.DateTimeField(null=True, blank=True, verbose_name='审核时间')

    class Meta:
        verbose_name = '工时登记记录'
        verbose_name_plural = '工时登记记录'
        ordering = ["-create_datetime"]

    def __str__(self):
        return self.id


class ManHourSummary(ManHourRecord):

    class Meta:
        proxy = True
        verbose_name = '工时统计'
        verbose_name_plural = '工时统计'
