from django.db import models
from user.models import CustomUser


class FlightType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='类型名称')

    class Meta:
        verbose_name = '航班类型设置'
        verbose_name_plural = '航班类型设置'

    def __str__(self):
        return self.name


class Compensation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='补偿名称')

    class Meta:
        verbose_name = '补偿方案设置'
        verbose_name_plural = '补偿方案设置'

    def __str__(self):
        return self.name


class DowngradeRecord(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='日期')
    type = models.ForeignKey(FlightType, related_name='downgradeRecord_type', on_delete=models.CASCADE, verbose_name='航班类型')
    flight_number = models.CharField(max_length=30, verbose_name='航班号')
    aircraft_id = models.CharField(max_length=30, verbose_name='飞机号')
    aircraft = models.CharField(max_length=30, verbose_name='飞机型号')
    passenger = models.CharField(max_length=30, verbose_name='旅客姓名')
    phone = models.CharField(max_length=30, verbose_name='联系电话')
    ticket = models.CharField(max_length=30, verbose_name='客票号')
    release = models.CharField(max_length=30, verbose_name='免责书号')
    before_class = models.CharField(max_length=30, verbose_name='原舱位')
    new_class = models.CharField(max_length=30, verbose_name='新舱位')
    compensation = models.ManyToManyField(Compensation, verbose_name='补偿方案')
    compensation_miles = models.FloatField(verbose_name='补偿里程数')
    compensation_amount = models.FloatField(verbose_name='补偿金额')
    fill_user = models.ForeignKey(CustomUser, null=True, blank=True, related_name='downgradeRecord_fill_user', on_delete=models.DO_NOTHING, verbose_name='经办人')
    fill_datetime = models.DateTimeField(null=True, blank=True, verbose_name='填写时间')
    review = models.BooleanField(default=False, verbose_name='审核状态')
    review_user = models.ForeignKey(CustomUser, null=True, blank=True, related_name='downgradeRecord_review_user', on_delete=models.DO_NOTHING, verbose_name='审核人')
    review_datetime = models.DateTimeField(null=True, blank=True, verbose_name='审核时间')
    supervisor_verify = models.BooleanField(default=False, verbose_name='值班主任审核状态')
    supervisor_verify_user = models.ForeignKey(CustomUser, null=True, blank=True, related_name='downgradeRecord_supervisor_verify_user', on_delete=models.DO_NOTHING, verbose_name='审核值班主任')
    supervisor_verify_datetime = models.DateTimeField(null=True, blank=True, verbose_name='值班主任审核时间')
    manager_verify = models.BooleanField(default=False, verbose_name='主任审核状态')
    manager_verify_user = models.ForeignKey(CustomUser, null=True, blank=True, related_name='downgradeRecord_manager_verify_user', on_delete=models.DO_NOTHING, verbose_name='审核主任')
    manager_verify_datetime = models.DateTimeField(null=True, blank=True, verbose_name='主任审核时间')

    class Meta:
        verbose_name = '非自愿降舱记录'
        verbose_name_plural = '非自愿降舱记录'
        ordering = ['-fill_datetime']

    def __str__(self):
        return self.id


class DowngradeSummary(DowngradeRecord):

    class Meta:
        proxy = True
        verbose_name = '非自愿降舱统计'
        verbose_name_plural = '非自愿降舱统计'
