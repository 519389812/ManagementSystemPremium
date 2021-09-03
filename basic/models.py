from django.db import models


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
    name = models.CharField(max_length=300, verbose_name='岗位及特殊岗位名称')
    score = models.FloatField(verbose_name='岗位及特殊岗位分数')

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

    class Meta:
        verbose_name = '奖励'
        verbose_name_plural = '奖励'

    def __str__(self):
        return self.name


class PenaltyType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='惩罚类别')

    class Meta:
        verbose_name = '惩罚类别'
        verbose_name_plural = '惩罚类别'

    def __str__(self):
        return self.name


class Penalty(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(RewardType, on_delete=models.CASCADE, verbose_name='惩罚类别')
    name = models.CharField(max_length=100, verbose_name='惩罚名称')
    score = models.FloatField(verbose_name='惩罚分数')

    class Meta:
        verbose_name = '惩罚'
        verbose_name_plural = '惩罚'

    def __str__(self):
        return self.name
