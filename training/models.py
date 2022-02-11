from django.db import models
from user.models import CustomUser


class CourseType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="课程类别名称")

    class Meta:
        verbose_name = '课程类别'
        verbose_name_plural = '课程类别'

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(CourseType, on_delete=models.CASCADE, verbose_name="课程类别")
    name = models.CharField(max_length=100, verbose_name="课程名称")

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'

    def __str__(self):
        return self.name


class TrainingRecord(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="培训名称")
    date = models.DateField(verbose_name='培训日期')
    user = models.ManyToManyField(CustomUser, related_name='trainingRecord_user', blank=True, verbose_name='培训对象')
    expiration_date = models.DateField(verbose_name='到期日期')
    remind_retraining = models.BooleanField(default=False, verbose_name='是否提醒复训')

    class Meta:
        verbose_name = '培训记录'
        verbose_name_plural = '培训记录'

    def __str__(self):
        return self.course.name


class TrainingRecordSummary(TrainingRecord):

    class Meta:
        proxy = True
        verbose_name = '培训统计'
        verbose_name_plural = '培训统计'
