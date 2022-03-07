from django.db import models
from user.models import CustomUser


class LoadSheet(models.Model):
    id = models.AutoField(primary_key=True)
    flight = models.CharField(max_length=30, verbose_name='航班号')
    date = models.DateField(verbose_name='日期')
    destination = models.CharField(max_length=30, verbose_name='目的地')

    class Meta:
        verbose_name = '舱单'
        verbose_name_plural = '舱单'

    def __str__(self):
        return '%s %s' % (self.flight, self.date)


class LoadSheetContent(models.Model):
    id = models.AutoField(primary_key=True)
    load_sheet = models.ForeignKey(LoadSheet, related_name='loadSheet_load_sheet', on_delete=models.CASCADE, verbose_name='舱单')
    destination = models.CharField(max_length=30, null=True, blank=True, verbose_name='目的地')
    project = models.CharField(max_length=30, choices=(('旅客', '旅客'), ('行李', '行李'), ('其他', '其他')), verbose_name='项目')
    number = models.IntegerField(verbose_name='数量')
    type = models.CharField(max_length=30, null=True, blank=True, choices=(('', '无'), ('成人', '成人'), ('儿童', '儿童'), ('婴儿', '婴儿'), ('机组', '机组'), ('货', '货'), ('邮', '邮'), ('压舱物', '压舱物')), verbose_name='类型')
    _class = models.CharField(max_length=30, null=True, blank=True, choices=(('', '无'), ('Y', 'Y'), ('W', 'W'), ('C', 'C'), ('F', 'F')), verbose_name='舱位')
    location = models.CharField(max_length=30, null=True, blank=True, verbose_name='位置')
    weight = models.IntegerField(verbose_name='重量')

    class Meta:
        verbose_name = '舱单内容'
        verbose_name_plural = '舱单内容'

    def __str__(self):
        return '%s %s' % (self.load_sheet.flight, self.load_sheet.date)


class LoadSheetRecord(models.Model):
    id = models.AutoField('序号', primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='loadSheetRecord_user', null=True, on_delete=models.CASCADE, verbose_name='用户')
    anonymous = models.CharField(max_length=300, null=True, blank=True, verbose_name='未登录用户')
    load_sheet = models.ForeignKey(LoadSheet, related_name='loadSheetRecord_load_sheet', on_delete=models.CASCADE, verbose_name='舱单')
    times = models.IntegerField(null=True, blank=True, verbose_name='参与次数')
    answer_time = models.IntegerField(null=True, blank=True, verbose_name='答题时长')
    score = models.IntegerField(null=True, blank=True, verbose_name='成绩')
    submit_datetime = models.DateTimeField(auto_now_add=True, verbose_name='提交时间')

    class Meta:
        verbose_name = '成绩记录'
        verbose_name_plural = '成绩记录'

    def __str__(self):
        return '%s %s' % (self.user.name, self.score)
