from django.contrib import admin
from exam.models import Course, Question, Exam, ExamRecord

admin.site.register([Course, Question, Exam, ExamRecord])
