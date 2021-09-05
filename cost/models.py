from django.db import models
from user.models import CustomUser
from team.models import CustomTeam


class CostType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='成本类别')

    class Meta:
        verbose_name = '成本类别'
        verbose_name_plural = '成本类别'

    def __str__(self):
        return self.name


class Cost(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(CostType, on_delete=models.CASCADE, verbose_name='成本')
    name = models.CharField(max_length=100, verbose_name='成本')

    class Meta:
        verbose_name = '成本类别'
        verbose_name_plural = '成本类别'

    def __str__(self):
        return self.name


class CostRecord(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='日期')
    team = models.ForeignKey(CustomTeam, related_name='cost_team', on_delete=models.CASCADE, verbose_name='团队')
    cost = models.ForeignKey(Cost, related_name='cost_name', on_delete=models.CASCADE, verbose_name='成本')
    quantity = models.FloatField(null=True, blank=True, verbose_name='金额')
    remark = models.TextField(max_length=1000, blank=True, verbose_name='备注')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='登记时间')
    create_user = models.ForeignKey(CustomUser, related_name='cost_user', on_delete=models.CASCADE, verbose_name='登记人')

    class Meta:
        verbose_name = '奖惩记录'
        verbose_name_plural = '奖惩记录'

    def __str__(self):
        return str(self.id)
