from django.db import models


class LevelRule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="程度规则名称")
    calculation = models.CharField(max_length=100, verbose_name='计算方式')

    class Meta:
        verbose_name = '程度加成规则设置'
        verbose_name_plural = '程度加成规则设置'

    def __str__(self):
        return self.name


class RepeatRule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='重复规则名称')
    day = models.IntegerField(default=0, verbose_name='天数')
    calculation = models.CharField(max_length=100, verbose_name='计算方式')

    class Meta:
        verbose_name = '重复规则设置'
        verbose_name_plural = '重复规则设置'

    def __str__(self):
        return self.name


class SaleRule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='销量规则名称')
    require = models.CharField(max_length=100, verbose_name='要求量')
    calculation = models.CharField(max_length=100, verbose_name='计算方式')

    class Meta:
        verbose_name = '销量规则设置'
        verbose_name_plural = '销量规则设置'

    def __str__(self):
        return self.name


class PositionType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='岗位及特殊岗位类别')

    class Meta:
        verbose_name = '岗位及特殊岗位类别'
        verbose_name_plural = '岗位及特殊岗位类别'

    def __str__(self):
        return self.name


class Position(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(PositionType, on_delete=models.CASCADE, verbose_name='岗位及特殊岗位类别')
    name = models.CharField(max_length=100, verbose_name='岗位及特殊岗位名称')
    score = models.FloatField(verbose_name='岗位及特殊岗位分数')
    sale_rule = models.ForeignKey(SaleRule, null=True, blank=True, on_delete=models.CASCADE, verbose_name='销量加成规则')

    class Meta:
        verbose_name = '岗位及特殊岗位'
        verbose_name_plural = '岗位及特殊岗位'

    def __str__(self):
        return self.name


class RewardType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='奖惩类别')

    class Meta:
        verbose_name = '奖励类别'
        verbose_name_plural = '奖励类别'

    def __str__(self):
        return self.name


class Reward(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(RewardType, on_delete=models.CASCADE, verbose_name='奖励类别')
    name = models.CharField(max_length=100, verbose_name='奖励名称')
    score = models.FloatField(verbose_name='奖励分数')
    repeat_rule = models.ForeignKey(RepeatRule, null=True, blank=True, on_delete=models.CASCADE, verbose_name='重复规则')

    class Meta:
        verbose_name = '奖励'
        verbose_name_plural = '奖励'

    def __str__(self):
        return self.name


class PenaltyType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='处罚类别')

    class Meta:
        verbose_name = '处罚类别'
        verbose_name_plural = '处罚类别'

    def __str__(self):
        return self.name


class Penalty(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(RewardType, on_delete=models.CASCADE, verbose_name='处罚类别')
    name = models.CharField(max_length=100, verbose_name='处罚名称')
    score = models.FloatField(verbose_name='处罚分数')
    repeat_rule = models.ForeignKey(RepeatRule, null=True, blank=True, on_delete=models.CASCADE, verbose_name='重复规则')

    class Meta:
        verbose_name = '处罚'
        verbose_name_plural = '处罚'

    def __str__(self):
        return self.name
