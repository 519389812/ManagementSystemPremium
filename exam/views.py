from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from exam.models import Exam, ExamRecord
from user.views import check_authority
from django.core.paginator import Paginator


def exam(request):
    return render(request, 'exam.html')


@check_authority
def view_exam_list(request):
    if request.method == 'GET':
        page_num = request.GET.get('page', '1')
        exams = Exam.objects.all()
        exam_list = list(exams.values('id', 'course', 'title', 'exam_time', 'update_datetime'))
        for i in range(len(exams)):
            if ExamRecord.objects.filter(exam=exams[i], user=request.user, is_passed=True).count() > 0:
                exam_list[i].append(('is_passed', True))
            else:
                exam_list[i].append(('is_passed', False))
        paginator = Paginator(exam_list, 30)
        page = paginator.get_page(int(page_num))
        return render(request, 'view_exam_list.html', {'page_exam_list': list(page.object_list),
                                                       'total_exam': paginator.count,
                                                       'total_page_num': paginator.num_pages,
                                                       'page_num': page.number})
    else:
        return render(request, 'error_400.html', status=400)


@check_authority
def view_exam(request):
    if request.Method == 'POST':
        pass
    else:
        exam_id = request.GET.get('id')
        exam = Exam.objects.get(id=exam_id)
        return render(request, 'view_exam.html', {'exam': exam})


def examinfo(request):
    if request.session.get('is_login', None):  # 若session认证为真
        username = request.session.get('username', None)
        student = models.Student.objects.get(sid=username)
        # 查询成绩信息
        grade = models.Record.objects.filter(sid=student.sid)
        return render(request, 'examinfo.html', {'student': student, 'grade': grade})
    else:
        return render(request, 'examinfo.html')


# 计算考试成绩
def calculateGrade(request):
    if request.method == 'POST':
        sid = request.POST.get('sid')
        subject1 = request.POST.get('subject')
        student = models.Student.objects.get(sid=sid)
        paper = models.TestPaper.objects.filter(major=student.major)
        grade = models.Record.objects.filter(sid=student.sid)
        course = models.Course.objects.filter(course_name=subject1).first()
        now = datetime.now()
        # 计算考试成绩
        questions = models.TestPaper.objects.filter(course__course_name=subject1). \
            values('pid').values('pid__id', 'pid__answer', 'pid__score')

        stu_grade = 0  # 初始化一个成绩
        for p in questions:
            qid = str(p['pid__id'])
            stu_ans = request.POST.get(qid)
            cor_ans = p['pid__answer']
            if stu_ans == cor_ans:
                stu_grade += p['pid__score']
        models.Record.objects.create(sid_id=sid, course_id=course.id, grade=stu_grade, rtime=now)
        context = {
            'student': student,
            'paper': paper,
            'grade': grade
        }
        return render(request, 'index.html', context=context)
