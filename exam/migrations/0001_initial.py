# Generated by Django 3.2.9 on 2022-03-03 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='课程名称')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40, verbose_name='试卷名')),
                ('exam_time', models.IntegerField(help_text='单位:秒，0表示不设时长限制', verbose_name='考试时长')),
                ('pass_score', models.IntegerField(verbose_name='及格分数')),
                ('login_required', models.BooleanField(default=True, verbose_name='是否要求登录')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '试卷设置',
                'verbose_name_plural': '试卷设置',
            },
        ),
        migrations.CreateModel(
            name='ExamRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('anonymous', models.CharField(blank=True, max_length=300, null=True, verbose_name='未登录用户')),
                ('answer', models.JSONField(blank=True, max_length=100000, null=True, verbose_name='答案')),
                ('times', models.IntegerField(blank=True, null=True, verbose_name='参与次数')),
                ('exam_time', models.IntegerField(blank=True, null=True, verbose_name='考试时长')),
                ('answer_time', models.IntegerField(blank=True, null=True, verbose_name='答题时长')),
                ('total_score', models.IntegerField(blank=True, null=True, verbose_name='总分')),
                ('pass_score', models.IntegerField(blank=True, null=True, verbose_name='及格分数')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name='成绩')),
                ('is_passed', models.BooleanField(blank=True, null=True, verbose_name='是否及格')),
                ('submit_datetime', models.DateTimeField(auto_now_add=True, verbose_name='提交时间')),
            ],
            options={
                'verbose_name': '成绩记录',
                'verbose_name_plural': '成绩记录',
            },
        ),
        migrations.CreateModel(
            name='ExamSummary',
            fields=[
                ('examrecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='exam.examrecord')),
            ],
            options={
                'verbose_name': '成绩统计',
                'verbose_name_plural': '成绩统计',
            },
            bases=('exam.examrecord',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=1000, verbose_name='题目')),
                ('type', models.CharField(choices=[('radio', '单选题'), ('checkbox', '多选题'), ('text', '填空题'), ('number', '算数题'), ('textarea', '简答题')], max_length=300, verbose_name='题型')),
                ('option', models.TextField(blank=True, help_text='单选、多选，选项用“ ”(空格)隔开', max_length=1000, null=True, verbose_name='选项')),
                ('answer', models.TextField(blank=True, help_text='多选、填空，答案用“ ”(空格)隔开，答案需要与选项完全相同；简答题，可以填写关键字眼，同一得分点，不同表述，用“/”(斜杠)隔开，不同得分点，用“ ”(空格)隔开，匹配与关键字眼完全相同的字符，则得分', max_length=1000, null=True, verbose_name='答案')),
                ('difficulty', models.CharField(choices=[('easy', '简单'), ('middle', '中等'), ('hard', '困难')], max_length=300, verbose_name='题目难度')),
                ('score', models.IntegerField(verbose_name='分值')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_course', to='exam.course', verbose_name='科目')),
            ],
            options={
                'verbose_name': '题库',
                'verbose_name_plural': '题库',
                'ordering': ['course'],
            },
        ),
    ]
