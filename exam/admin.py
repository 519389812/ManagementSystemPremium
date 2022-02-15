from django.contrib import admin
from exam.models import Course, QuestionBank

admin.site.register([Academy, Major, Course, Student, QuestionBank, TestPaper, Record])
