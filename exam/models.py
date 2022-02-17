import json

from django.db import models
from user.models import CustomUser
import random


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='课程名称')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'

    def __str__(self):
        return self.name


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, related_name='question_course', on_delete=models.CASCADE, verbose_name='科目')
    title = models.TextField(max_length=1000, verbose_name='题目')
    type = models.CharField(max_length=300, choices=(('radio', '单选题'), ('checkbox', '多选题'), ('text', '填空题'), ('number', '算数题'), ('textarea', '简答题')), verbose_name='题型')
    option = models.TextField(max_length=1000, null=True, blank=True, help_text='单选、多选，选项用“ ”(空格)隔开', verbose_name='选项')
    answer = models.TextField(max_length=1000, null=True, blank=True, help_text='多选、填空，答案用“ ”(空格)隔开，答案需要与选项完全相同；简答题，可以填写关键字眼，同一得分点，不同表述，用“/”(斜杠)隔开，不同得分点，用“ ”(空格)隔开，匹配与关键字眼完全相同的字符，则得分', verbose_name='答案')
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

    def template_option_split(self):
        return [i for i in random.shuffle(self.option.split(' ')) if i != '']


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
    question = models.ManyToManyField(Question, null=True, blank=True, related_name='examRecord_question', verbose_name='题目')
    answer = models.JSONField(max_length=100000, null=True, blank=True, verbose_name='答案')
    times = models.IntegerField(null=True, blank=True, verbose_name='参与次数')
    exam_time = models.IntegerField(null=True, blank=True, verbose_name='考试时长')
    answer_time = models.IntegerField(null=True, blank=True, verbose_name='答题时长')
    total_score = models.IntegerField(null=True, blank=True, verbose_name='总分')
    pass_score = models.IntegerField(null=True, blank=True, verbose_name='及格分数')
    score = models.IntegerField(null=True, blank=True, verbose_name='成绩')
    is_passed = models.BooleanField(null=True, blank=True, verbose_name='是否及格')
    submit_datetime = models.DateTimeField(auto_now_add=True, verbose_name='提交时间')

    class Meta:
        verbose_name = '学生成绩'
        verbose_name_plural = '学生成绩'

    def __str__(self):
        return '<%s:%s>' % (self.user.name, self.score)

    def template_load_answer_as_dict(self):
        return json.loads(self.answer)
