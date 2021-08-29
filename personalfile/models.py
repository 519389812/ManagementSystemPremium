from django.db import models
from team.models import Team


class SkillType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="技能类别")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")

    class Meta:
        verbose_name = '技能类别'
        verbose_name_plural = "     技能类别"

    def __str__(self):
        return self.name


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(SkillType, on_delete=models.CASCADE, verbose_name="技能类别")
    name = models.CharField(max_length=100, verbose_name="技能名称")
    score = models.FloatField(verbose_name="技能基础分数")
    workload = models.FloatField(verbose_name="技能基础工作量")
    bonus = models.FloatField(verbose_name="技能基础奖金")
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, null=True, blank=True, verbose_name="规则")
    team = models.ManyToManyField(Team, blank=True, verbose_name="目标组")

    class Meta:
        verbose_name = '技能'
        verbose_name_plural = "      技能"

    def __str__(self):
        return self.name
