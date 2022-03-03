from django.db import models
from user.models import CustomUser


class SalesRule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='销量规则名称')
    require = models.CharField(max_length=100, verbose_name='要求量')
    calculation = models.CharField(max_length=100, verbose_name='计算方式')

    class Meta:
        verbose_name = '销量规则设置'
        verbose_name_plural = '销量规则设置'

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='产品名称')

    class Meta:
        verbose_name = '产品设置'
        verbose_name_plural = '产品设置'

    def __str__(self):
        return self.name


class SalesRecord(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='日期')
    product = models.ForeignKey(Product, related_name='salesRecord_product', on_delete=models.CASCADE, verbose_name='产品名称')
    flight_number = models.CharField(max_length=30, verbose_name='航班号')
    passenger = models.CharField(max_length=30, verbose_name='旅客姓名')
    ticket = models.CharField(max_length=30, verbose_name='客票号')
    emd = models.CharField(max_length=30, verbose_name='emd号')
    destination = models.CharField(max_length=30, verbose_name='目的地')
    issue_user = models.ForeignKey(CustomUser, related_name='salesRecord_issue_user', on_delete=models.CASCADE, verbose_name='开票人')
    amount = models.FloatField(verbose_name='销售金额')
    miles = models.FloatField(verbose_name='销售里程')
    user = models.ForeignKey(CustomUser, null=True, blank=True, related_name='salesRecord_user', on_delete=models.CASCADE, verbose_name='经办人')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='登记时间')

    class Meta:
        verbose_name = '销售记录'
        verbose_name_plural = '产品记录'

    def __str__(self):
        return self.flight_number


class SalesSummary(SalesRecord):

    class Meta:
        proxy = True
        verbose_name = '销售统计'
        verbose_name_plural = '销售统计'
