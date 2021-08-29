from django.db import models
import django.utils.timezone as timezone
from user.models import User
from team.models import Team
from django.contrib import admin
from django.apps import apps


class Rule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="名称")
    effect = models.CharField(max_length=100, verbose_name="作用于")
    date_condition = models.CharField(max_length=100, null=True, blank=True, verbose_name="时间条件")
    condition = models.CharField(max_length=100, null=True, blank=True, verbose_name="数量条件")
    score = models.CharField(max_length=100, null=True, blank=True, verbose_name="分数权重")
    workload = models.CharField(max_length=100, null=True, blank=True, verbose_name="工作量权重")
    bonus = models.CharField(max_length=100, null=True, blank=True, verbose_name="奖金权重")
    man_hours = models.CharField(max_length=100, null=True, blank=True, verbose_name="工时权重")
    quantity = models.CharField(max_length=100, null=True, blank=True, verbose_name="产出权重")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")

    def __init__(self, *args, **kwargs):
        super(Rule, self).__init__(*args, **kwargs)
        rule_choices = []
        for model in list(apps.get_app_config('performance').get_models()):
            try:
                model._meta.get_field('rule')
                rule_choices.append((model._meta.model_name, model._meta.verbose_name))
            except:
                pass
        self._meta.get_field('effect').choices = rule_choices

    class Meta:
        verbose_name = '规则'
        verbose_name_plural = " 规则"

    def get_name_weight(self):
        date_condition = '时间：%s ' % self.date_condition if self.date_condition else ''
        condition = '次数：%s ' % self.condition if self.condition else ''
        score = '分数：%s ' % self.score if self.score else ''
        workload = '工作量：%s ' % self.workload if self.workload else ''
        bonus = '奖金：%s ' % self.bonus if self.bonus else ''
        man_hours = '计算工时：%s ' % self.man_hours if self.man_hours else ''
        quantity = '产出：%s ' % self.quantity if self.quantity else ''
        get_name_weight = self.name + ' ' + date_condition + condition + score + workload + bonus + man_hours + quantity
        return get_name_weight

    def __str__(self):
        return self.get_name_weight()


class LevelType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="程度类别名称")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")

    def __init__(self, *args, **kwargs):
        super(LevelType, self).__init__(*args, **kwargs)
        level_type_choices = []
        for model in list(apps.get_app_config('performance').get_models()):
            try:
                model._meta.get_field('level')
                level_type_choices.append((model._meta.model_name, model._meta.verbose_name))
            except:
                pass
        self._meta.get_field('name').choices = level_type_choices

    class Meta:
        verbose_name = '程度类别'
        verbose_name_plural = "  程度类别"

    def __str__(self):
        return self.name


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(LevelType, on_delete=models.CASCADE, verbose_name="程度类别")
    name = models.CharField(max_length=100, verbose_name="程度名称")
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, verbose_name="规则")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")

    class Meta:
        verbose_name = '程度'
        verbose_name_plural = "  程度"

    def __str__(self):
        return self.name


class PositionType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="岗位类别")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")

    class Meta:
        verbose_name = '岗位类别'
        verbose_name_plural = "   岗位类别"

    def __str__(self):
        return self.name


class Position(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(PositionType, on_delete=models.CASCADE, verbose_name="岗位类别")
    name = models.CharField(max_length=300, verbose_name="岗位名称")
    score = models.FloatField(verbose_name="岗位基础分数")
    workload = models.FloatField(verbose_name="岗位基础工作量")
    bonus = models.FloatField(verbose_name="岗位基础奖金")
    man_hours = models.BooleanField(verbose_name="是否计算工时")
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, null=True, blank=True, verbose_name="规则")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")

    class Meta:
        verbose_name = '岗位'
        verbose_name_plural = "    岗位"

    def __str__(self):
        return self.name


class RewardType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="奖惩类别")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")

    class Meta:
        verbose_name = '奖惩类别'
        verbose_name_plural = "       奖惩类别"

    def __str__(self):
        return self.name


class Reward(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(RewardType, on_delete=models.CASCADE, verbose_name="奖惩类别")
    name = models.CharField(max_length=100, verbose_name="奖惩名称")
    score = models.FloatField(verbose_name="奖惩基础分数")
    workload = models.FloatField(verbose_name="奖惩基础工作量")
    bonus = models.FloatField(verbose_name="奖惩基础奖金")
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, null=True, blank=True, verbose_name="规则")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")

    class Meta:
        verbose_name = '奖惩'
        verbose_name_plural = "        奖惩"

    def __str__(self):
        return self.name


class Shift(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="班次")
    score = models.FloatField(verbose_name="班次基础分数")
    workload = models.FloatField(verbose_name="班次基础工作量")
    bonus = models.FloatField(verbose_name="班次基础奖金")
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, null=True, blank=True, verbose_name="规则")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")

    class Meta:
        verbose_name = '班次'
        verbose_name_plural = "          班次"

    def __str__(self):
        return self.name


class RewardRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='reward_user', on_delete=models.CASCADE, verbose_name="责任人")
    date = models.DateField(verbose_name="日期")
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, verbose_name="奖惩")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True, verbose_name="程度")
    score = models.FloatField(null=True, blank=True, verbose_name="分数")
    workload = models.FloatField(null=True, blank=True, verbose_name="工作量")
    bonus = models.FloatField(null=True, blank=True, verbose_name="奖金")
    title = models.CharField(max_length=500, verbose_name="简述")
    content = models.TextField(max_length=1000, blank=True, verbose_name="详细情况")
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="登记时间")
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="登记人")

    class Meta:
        verbose_name = '奖惩记录'
        verbose_name_plural = "             奖惩记录"

    def __str__(self):
        return str(self.id)


class RewardSummary(RewardRecord):

    class Meta:
        proxy = True
        verbose_name = '奖惩统计'
        verbose_name_plural = "             奖惩统计"


class WorkloadRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='workload_user', on_delete=models.CASCADE, verbose_name="登记人")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="岗位")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True, verbose_name="程度")
    start_datetime = models.DateTimeField(verbose_name="开始时间")
    end_datetime = models.DateTimeField(verbose_name="结束时间")
    working_time = models.FloatField(verbose_name="工作时长")
    score = models.FloatField(null=True, blank=True, verbose_name="分数")
    workload = models.FloatField(null=True, blank=True, verbose_name="工作量")
    bonus = models.FloatField(null=True, blank=True, verbose_name="奖金")
    man_hours = models.FloatField(null=True, blank=True, verbose_name="工时")
    assigned_team = models.ForeignKey(Team, related_name='workload_assigned_team', on_delete=models.CASCADE, verbose_name="指派")
    remark = models.TextField(max_length=1000, blank=True, verbose_name="备注")
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="登记时间")
    verified = models.BooleanField(default=False, verbose_name="审核状态")
    verified_user = models.ForeignKey(User, null=True, blank=True, related_name='workload_verified_user', on_delete=models.CASCADE, verbose_name="审核人")
    verified_datetime = models.DateTimeField(null=True, blank=True, verbose_name="审核时间")

    class Meta:
        verbose_name = '工作安排记录'
        verbose_name_plural = "              工作安排记录"
        ordering = ["-created_datetime"]

    def __str__(self):
        return str(self.id)


class WorkloadSummary(WorkloadRecord):

    class Meta:
        proxy = True
        verbose_name = '工作安排统计'
        verbose_name_plural = "              工作安排统计"


class OutputType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="产出类别名称")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")

    class Meta:
        verbose_name = '产出类别'
        verbose_name_plural = "          产出类别"

    def __str__(self):
        return self.name


class Output(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(OutputType, on_delete=models.CASCADE, verbose_name="产出类别")
    name = models.CharField(max_length=100, verbose_name="产出名称")
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, null=True, blank=True, verbose_name="规则")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")

    class Meta:
        verbose_name = '产出'
        verbose_name_plural = "          产出"

    def __str__(self):
        return self.name


class OutputRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='output_user', on_delete=models.CASCADE, verbose_name="登记人")
    date = models.DateField(verbose_name="日期")
    output = models.ForeignKey(Output, on_delete=models.CASCADE, verbose_name="产出")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True, verbose_name="程度")
    quantity = models.FloatField(verbose_name="数量")
    weight_quantity = models.FloatField(null=True, blank=True, verbose_name="加权后数量")
    assigned_team = models.ForeignKey(Team, related_name='output_assigned_team', on_delete=models.CASCADE, verbose_name="审核对象")
    remark = models.TextField(max_length=1000, blank=True, verbose_name="备注")
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="登记时间")
    verified = models.BooleanField(default=False, verbose_name="审核状态")
    verified_user = models.ForeignKey(User, null=True, blank=True, related_name='output_verified_user', on_delete=models.CASCADE, verbose_name="审核人")
    verified_datetime = models.DateTimeField(null=True, blank=True, verbose_name="审核时间")

    class Meta:
        verbose_name = '产出记录'
        verbose_name_plural = "                 产出记录"
        ordering = ["-created_datetime"]

    def __str__(self):
        return str(self.id)


class OutputSummary(OutputRecord):

    class Meta:
        proxy = True
        verbose_name = '产出统计'
        verbose_name_plural = "                  产出统计"
