from django.db import models
from user.models import CustomUser


class TrainingType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="培训类别")

    class Meta:
        verbose_name = '培训类别'
        verbose_name_plural = '培训类别'

    def __str__(self):
        return self.name


class Training(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(TrainingType, on_delete=models.CASCADE, verbose_name="培训类别")
    name = models.CharField(max_length=100, verbose_name="培训名称")
    student = models.ManyToManyField(CustomUser, related_name='training_user', blank=True, verbose_name='培训对象')
    training_date = models.DateField(verbose_name='培训日期')
    expiration_date = models.DateField(verbose_name='到期日期')
    remind_retraining = models.BooleanField(default=False, verbose_name='是否提醒复训')
    retraining_period = models.IntegerField(default=0, verbose_name='提示周期天数')

    class Meta:
        verbose_name = '培训'
        verbose_name_plural = '培训'

    def __str__(self):
        return self.name
