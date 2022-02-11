from django.db import models
from performance.models import WorkloadRecord
from user.models import CustomUser


class SkillType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='类型名称')

    class Meta:
        verbose_name = '技能类型设置'
        verbose_name_plural = '技能类型设置'

    def __str__(self):
        return self.name


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(SkillType, related_name='skill_type', on_delete=models.CASCADE, verbose_name='技能')
    name = models.CharField(max_length=50, verbose_name='类型名称')

    class Meta:
        verbose_name = '技能设置'
        verbose_name_plural = '技能设置'
        ordering = ['type__name', 'name']

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, related_name='employee_user', on_delete=models.CASCADE, verbose_name='员工')
    skill = models.ManyToManyField(Skill, related_name='employee_skill', verbose_name='掌握技能')

    class Meta:
        verbose_name = '个人技能掌握'
        verbose_name_plural = '个人技能掌握'

    def __str__(self):
        return self.id


class EmployeeSummary(WorkloadRecord):

    class Meta:
        proxy = True
        verbose_name = '个人技能统计'
        verbose_name_plural = '个人技能统计'
