from django.db import models
from user.models import CustomUser


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='服务名称')

    class Meta:
        verbose_name = '服务名称'
        verbose_name_plural = '服务名称'

    def __str__(self):
        return self.name


class ServiceRecord(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='日期')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='serviceRecord_user', verbose_name='员工')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='serviceRecord_service', verbose_name='服务名称')
    score = models.FloatField(verbose_name='得分')
    fill_user = models.ForeignKey(CustomUser, null=True, blank=True, related_name='serviceRecord_fill_user', on_delete=models.DO_NOTHING, verbose_name='记录人')
    fill_datetime = models.DateTimeField(null=True, blank=True, verbose_name='记录时间')

    class Meta:
        verbose_name = '服务满意度得分'
        verbose_name_plural = '服务满意度得分'

    def __str__(self):
        return self.user.name


class ServiceRecordSummary(ServiceRecord):

    class Meta:
        proxy = True
        verbose_name = '服务满意度得分统计'
        verbose_name_plural = '服务满意度得分统计'
