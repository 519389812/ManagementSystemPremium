from django.db import models
from user.models import CustomUser


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='课程名称')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'

    def __str__(self):
        return self.name


class QuestionDifficulty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, verbose_name='困难度')

    class Meta:
        verbose_name = '困难度设置'
        verbose_name_plural = '困难度设置'

    def __str__(self):
        return self.name


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, related_name='question_course', on_delete=models.CASCADE, verbose_name='科目')
    title = models.TextField(max_length=1000, verbose_name='题目')
    type = models.CharField(max_length=300, choices=(('select', '单选'), ('checkbox', '多选'), ('text', '填空'), ('number', '数字'), ('textarea', '简答')), verbose_name='题型')
    option = models.TextField(max_length=1000, null=True, blank=True, help_text='单选、多选，选项用/隔开', verbose_name='选项')
    answer = models.TextField(max_length=1000, null=True, blank=True, verbose_name='答案')
    difficulty = models.CharField(max_length=300, choices=(('easy', '简单'), ('middle', '中等'), ('hard', '困难')), verbose_name='题目难度')
    score = models.IntegerField(verbose_name='分值')
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    update_user = models.ForeignKey(CustomUser, related_name='question_update_user', on_delete=models.CASCADE, verbose_name='更新用户')

    class Meta:
        verbose_name = '题库'
        verbose_name_plural = '题库'
        ordering = ['course']

    def __str__(self):
        return '<%s-%s:%s-%s>' % (self.course, self.type.name, self.title, self.difficulty)


# 试卷表
class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, related_name='exam_course', on_delete=models.CASCADE, verbose_name='科目')
    title = models.CharField(max_length=40, verbose_name='试卷名')
    question = models.ManyToManyField(Question, limit_choices_to={'Question__course__name': course.name}, verbose_name='题目')
    exam_time = models.IntegerField(help_text='单位:秒，0表示不设时长限制', verbose_name='考试时长')
    pass_score = models.IntegerField(verbose_name='及格分数')
    login_required = models.BooleanField(default=True, verbose_name='是否要求登录')
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    update_user = models.ForeignKey(CustomUser, related_name='exam_update_user', on_delete=models.CASCADE, verbose_name='更新用户')

    class Meta:
        verbose_name = '试卷设置'
        verbose_name_plural = '试卷设置'

    def __str__(self):
        return '<%s:%s>' % (self.course.name, self.title)


# 学生成绩表
class ExamRecord(models.Model):
    id = models.AutoField('序号', primary_key=True)
    user = models.ForeignKey(CustomUser, related_name='examRecord_user', null=True, on_delete=models.CASCADE, verbose_name='用户')
    anonymous = models.CharField(max_length=300, null=True, blank=True, verbose_name='未登录用户')
    exam = models.ForeignKey(Exam, related_name='examRecord_exam', on_delete=models.CASCADE, verbose_name='试卷')
    times = models.IntegerField(verbose_name='参与次数')
    exam_time = models.IntegerField(verbose_name='考试时长')
    answer_time = models.IntegerField(verbose_name='答题时长')
    pass_score = models.IntegerField(verbose_name='及格分数')
    score = models.IntegerField(verbose_name='成绩')
    is_passed = models.BooleanField(verbose_name='是否及格')
    submit_datetime = models.DateTimeField(verbose_name='提交时间')

    class Meta:
        verbose_name = '学生成绩'
        verbose_name_plural = '学生成绩'

    def __str__(self):
        return '<%s:%s>' % (self.user.name, self.score)
