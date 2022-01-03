from django.db import models
from user.models import CustomUser
from django.contrib import admin
from django.utils import timezone


def get_weight_column(self, column_name, model_name, model_column):
    return_column = eval('self.%s.%s' % (model_column, column_name))
    if eval('self.%s.repeat_rule' % model_column):
        end_date = self.date
        day_delta = eval('self.%s.repeat_rule.day' % model_column)
        start_date = end_date - timezone.timedelta(day_delta)
        count = eval('%s.objects.filter(user=self.user, %s=self.%s, date__gte=start_date, date__lte=end_date, create_datetime__lt=self.create_datetime).count()' % (model_name, model_column, model_column))
        if count > 0:
            string = 'self.%s.repeat_rule.calculation' % model_column
            try:
                return_column = eval('%s %s' % (return_column, eval(string))) if eval(string) else return_column
            except:
                pass
    if self.level_rule:
        string = 'self.level_rule.calculation'
        try:
            return_column = eval('%s %s' % (return_column, eval(string))) if eval(string) else return_column
        except:
            pass
    return return_column


class LevelRule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="程度规则名称")
    calculation = models.CharField(max_length=100, verbose_name='计算方式')

    class Meta:
        verbose_name = '程度加成规则设置'
        verbose_name_plural = '程度加成规则设置'

    def __str__(self):
        return self.name


class RepeatRule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='重复规则名称')
    day = models.IntegerField(default=0, verbose_name='天数')
    calculation = models.CharField(max_length=100, verbose_name='计算方式')

    class Meta:
        verbose_name = '重复规则设置'
        verbose_name_plural = '重复规则设置'

    def __str__(self):
        return self.name


class RewardPenaltyType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='奖惩类别')

    class Meta:
        verbose_name = '奖励类别'
        verbose_name_plural = '奖励类别'

    def __str__(self):
        return self.name


class RewardPenalty(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(RewardPenaltyType, on_delete=models.CASCADE, verbose_name='奖励类别')
    name = models.CharField(max_length=100, verbose_name='奖惩名称')
    score = models.FloatField(verbose_name='奖惩分数')
    repeat_rule = models.ForeignKey(RepeatRule, null=True, blank=True, on_delete=models.CASCADE, verbose_name='重复规则')

    class Meta:
        verbose_name = '奖励'
        verbose_name_plural = '奖励'

    def __str__(self):
        return self.name


class RewardPenaltyRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='rewardPenaltyRecord_user', on_delete=models.CASCADE, verbose_name='奖励人')
    date = models.DateField(verbose_name='日期')
    reward_penalty = models.ForeignKey(RewardPenalty, on_delete=models.CASCADE, verbose_name='奖惩项')
    level_rule = models.ForeignKey(LevelRule, null=True, blank=True, on_delete=models.CASCADE, verbose_name='程度加成规则')
    score = models.FloatField(null=True, blank=True, verbose_name='加成后奖惩分数')
    title = models.CharField(max_length=500, verbose_name='简述')
    content = models.TextField(max_length=1000, blank=True, verbose_name='详细情况')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='登记时间')
    create_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='登记人')

    class Meta:
        verbose_name = '奖惩记录'
        verbose_name_plural = '奖惩记录'

    def __str__(self):
        return str(self.id)


class RewardPenaltySummary(RewardPenaltyRecord):

    @property
    @admin.display(description='加成后分数')
    def weight_score(self):
        return get_weight_column(self, 'score', 'RewardPenaltyRecord', 'reward_penalty')

    class Meta:
        proxy = True
        verbose_name = '奖惩统计'
        verbose_name_plural = '奖励统计'
