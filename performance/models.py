from django.db import models
import django.utils.timezone as timezone
from user.models import CustomUser
from team.models import CustomTeam
from django.contrib import admin
from django.apps import apps
from rule.models import Position, Reward, Penalty


class RewardRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='rewardRecord_user', on_delete=models.CASCADE, verbose_name='奖励人')
    date = models.DateField(verbose_name='日期')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, verbose_name='奖励项')
    score = models.FloatField(null=True, blank=True, verbose_name='奖励分数')
    title = models.CharField(max_length=500, verbose_name='简述')
    content = models.TextField(max_length=1000, blank=True, verbose_name='详细情况')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='登记时间')
    create_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='登记人')

    class Meta:
        verbose_name = '奖励记录'
        verbose_name_plural = '奖励记录'

    def __str__(self):
        return str(self.id)


class RewardSummary(RewardRecord):

    class Meta:
        proxy = True
        verbose_name = '奖惩统计'
        verbose_name_plural = '奖惩统计'


class PenaltyRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='penaltyRecord_user', on_delete=models.CASCADE, verbose_name='责任人')
    date = models.DateField(verbose_name='日期')
    penalty = models.ForeignKey(Penalty, on_delete=models.CASCADE, verbose_name='处罚项')
    score = models.FloatField(null=True, blank=True, verbose_name='处罚分数')
    title = models.CharField(max_length=500, verbose_name='简述')
    content = models.TextField(max_length=1000, blank=True, verbose_name='详细情况')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='登记时间')
    create_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='登记人')

    class Meta:
        verbose_name = '处罚记录'
        verbose_name_plural = '处罚记录'

    def __str__(self):
        return str(self.id)


class PenaltySummary(RewardRecord):

    class Meta:
        proxy = True
        verbose_name = '处罚统计'
        verbose_name_plural = '处罚统计'


class WorkloadRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='workloadRecord_user', on_delete=models.CASCADE, verbose_name='登记人')
    date = models.DateField(verbose_name='日期')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='岗位')
    number_people = models.IntegerField(null=True, blank=True, verbose_name='办理人数')
    number_baggage = models.IntegerField(null=True, blank=True, verbose_name='办理行李')
    sale = models.FloatField(null=True, blank=True, verbose_name='销售额')
    verifier = models.ForeignKey(CustomTeam, related_name='workloadRecord_team', on_delete=models.CASCADE, verbose_name='审核组')
    remark = models.TextField(max_length=1000, blank=True, verbose_name='备注')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='登记时间')
    verify = models.BooleanField(default=False, verbose_name='审核状态')
    verify_user = models.ForeignKey(CustomUser, null=True, blank=True, related_name='workloadRecord_verify_user', on_delete=models.CASCADE, verbose_name='审核人')
    verify_datetime = models.DateTimeField(null=True, blank=True, verbose_name='审核时间')

    class Meta:
        verbose_name = '工作量登记记录'
        verbose_name_plural = '工作量登记记录'
        ordering = ['-created_datetime']

    def __str__(self):
        return str(self.id)


class WorkloadSummary(WorkloadRecord):

    class Meta:
        proxy = True
        verbose_name = '工作量统计'
        verbose_name_plural = '工作量统计'
