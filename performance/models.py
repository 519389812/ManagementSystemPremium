from django.db import models
import django.utils.timezone as timezone
from user.models import CustomUser
from team.models import CustomTeam
from django.contrib import admin
from django.apps import apps
from basic.models import Position


class RewardRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='reward_user', on_delete=models.CASCADE, verbose_name='责任人')
    date = models.DateField(verbose_name='日期')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, verbose_name='奖惩')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True, verbose_name='程度')
    score = models.FloatField(null=True, blank=True, verbose_name='分数')
    workload = models.FloatField(null=True, blank=True, verbose_name='工作量')
    bonus = models.FloatField(null=True, blank=True, verbose_name='奖金')
    title = models.CharField(max_length=500, verbose_name='简述')
    content = models.TextField(max_length=1000, blank=True, verbose_name='详细情况')
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='登记时间')
    created_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='登记人')

    class Meta:
        verbose_name = '奖惩记录'
        verbose_name_plural = '奖惩记录'

    def __str__(self):
        return str(self.id)


class RewardSummary(RewardRecord):

    class Meta:
        proxy = True
        verbose_name = '奖惩统计'
        verbose_name_plural = '奖惩统计'


class WorkloadRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='workload_user', on_delete=models.CASCADE, verbose_name='登记人')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='岗位')
    number_people = models.IntegerField(null=True, blank=True, verbose_name='办理人数')
    number_baggage = models.IntegerField(null=True, blank=True, verbose_name='办理行李')
    sales = models.FloatField(null=True, blank=True, verbose_name='销售额')
    verifier = models.ForeignKey(CustomTeam, related_name='workload_assigned_team', on_delete=models.CASCADE, verbose_name='审核人')
    remark = models.TextField(max_length=1000, blank=True, verbose_name='备注')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='登记时间')
    validation = models.BooleanField(default=False, verbose_name='审核状态')
    verified_user = models.ForeignKey(CustomUser, null=True, blank=True, related_name='workload_verified_user', on_delete=models.CASCADE, verbose_name='审核人')
    verified_datetime = models.DateTimeField(null=True, blank=True, verbose_name='审核时间')

    class Meta:
        verbose_name = '工作安排记录'
        verbose_name_plural = '工作安排记录'
        ordering = ['-created_datetime']

    def __str__(self):
        return str(self.id)


class WorkloadSummary(WorkloadRecord):

    class Meta:
        proxy = True
        verbose_name = '工作安排统计'
        verbose_name_plural = '工作安排统计'


class OutputType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='产出类别名称')
    team = models.ManyToManyField(CustomTeam, blank=True, verbose_name='目标组')

    class Meta:
        verbose_name = '产出类别'
        verbose_name_plural = '产出类别'

    def __str__(self):
        return self.name


class Output(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(OutputType, on_delete=models.CASCADE, verbose_name='产出类别')
    name = models.CharField(max_length=100, verbose_name='产出名称')
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, null=True, blank=True, verbose_name='规则')
    team = models.ManyToManyField(CustomTeam, blank=True, verbose_name='目标组')

    class Meta:
        verbose_name = '产出'
        verbose_name_plural = '产出'

    def __str__(self):
        return self.name


class OutputRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='output_user', on_delete=models.CASCADE, verbose_name='登记人')
    date = models.DateField(verbose_name='日期')
    output = models.ForeignKey(Output, on_delete=models.CASCADE, verbose_name='产出')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True, verbose_name='程度')
    quantity = models.FloatField(verbose_name='数量')
    weight_quantity = models.FloatField(null=True, blank=True, verbose_name='加权后数量')
    assigned_team = models.ForeignKey(CustomTeam, related_name='output_assigned_team', on_delete=models.CASCADE, verbose_name='审核对象')
    remark = models.TextField(max_length=1000, blank=True, verbose_name='备注')
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='登记时间')
    verified = models.BooleanField(default=False, verbose_name='审核状态')
    verified_user = models.ForeignKey(CustomUser, null=True, blank=True, related_name='output_verified_user', on_delete=models.CASCADE, verbose_name='审核人')
    verified_datetime = models.DateTimeField(null=True, blank=True, verbose_name='审核时间')

    class Meta:
        verbose_name = '产出记录'
        verbose_name_plural = '产出记录'
        ordering = ['-created_datetime']

    def __str__(self):
        return str(self.id)


class OutputSummary(OutputRecord):

    class Meta:
        proxy = True
        verbose_name = '产出统计'
        verbose_name_plural = '产出统计'
