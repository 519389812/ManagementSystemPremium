from django.db import models


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
