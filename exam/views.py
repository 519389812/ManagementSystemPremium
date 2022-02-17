from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from exam.models import Exam, ExamRecord, Question
from user.views import check_authority
from django.core.paginator import Paginator
import json


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
        return render(request, 'view_exam_list.html', {'page_object_list': list(page.object_list),
                                                       'total_num': paginator.count,
                                                       'total_page_num': paginator.num_pages,
                                                       'page_num': page.number})
    else:
        return render(request, 'error_400.html', status=400)


def view_exam(request):
    if request.Method == 'POST':
        post_data = request.POST.dict()
        exam_id = post_data['exam_id']
        answer_time = post_data['answer_time']
        del(post_data['csrfmiddlewaretoken'])
        del(post_data['exam_id'])
        del(post_data['answer_time'])
        try:
            exam = Exam.objects.get(id=exam_id)
        except:
            return render(request, 'error_500.html', status=500)
        if request.user:
            user = request.user
            exam_record = ExamRecord.objects.create(user=user, exam=exam, answer_time=answer_time)
            times = ExamRecord.objects.filter(exam=exam, user=request.user).count()
        else:
            user = post_data['name']
            del (post_data['name'])
            exam_record = ExamRecord.objects.create(anonymous=user, exam=exam, answer_time=answer_time)
            times = ExamRecord.objects.filter(exam=exam, anonymous=user).count()
        score = 0
        total_score = 0
        answer_dict = {}
        for question_id, answer in post_data.items():
            try:
                question = Question.objects.get(id=question_id)
            except:
                continue
            exam_record.examRecord_question.add(question)
            answer_dict[question_id] = answer
            if question.type == 'radio' or question.type == 'number':
                if answer == question.answer:
                    score += question.score
            elif question.type == 'checkbox':
                correct_list = [i for i in question.answer.split(' ') if i != '']
                answer = [i for i in answer.split(' ') if i != '']
                if set(answer) == set(correct_list):
                    score += question.score
            elif question.type == 'text':
                correct_list = [i for i in question.answer.split(' ') if i != '']
                answer = [i for i in answer.split(' ') if i != '']
                if answer == correct_list:
                    score += question.score
            elif question.type == 'textarea':
                point = 0
                correct_list = [i.split('/') for i in question.answer.split(' ') if i != '']
                answer = [i for i in answer.split(' ') if i != '']
                for a in answer:
                    for c in correct_list:
                        if a in c:
                            point += 1
                score += round(point / len(correct_list))
            total_score += question.score
        is_passed = True if score >= exam.pass_score else False
        exam_record.update(answer=json.dumps(answer_dict), times=times, exam_time=exam.exam_time, total_score=total_score, pass_score=exam.pass_score, score=score, is_passed=is_passed)
        return render(request, 'view_exam_list.html')
    else:
        exam_id = request.GET.get('id')
        exam = Exam.objects.get(id=exam_id)
        return render(request, 'view_exam.html', {'exam': exam})


@check_authority
def review_exam_list(request):
    if request.method == 'GET':
        page_num = request.GET.get('page', '1')
        exam_record = ExamRecord.objects.filter(user=request.user).order_by('-submit_datetime')
        paginator = Paginator(exam_record, 15)
        page = paginator.get_page(int(page_num))
        return render(request, 'review_exam_list.html', {'page_object_list': list(page.object_list),
                                                         'total_num': paginator.count,
                                                         'total_page_num': paginator.num_pages,
                                                         'page_num': page.number})
    else:
        return render(request, 'error_400.html', status=400)


@check_authority
def review_exam(request):
    if request.Method == 'GET':
        exam_record_id = request.GET.get('exam_record_id', '')
        try:
            exam_record = ExamRecord.objects.get(id=exam_record_id)
            return render(request, 'review_exam.html', {'exam_record': exam_record})
        except:
            return render(request, 'error_500.html', status=500)
    else:
        return render(request, 'error_400.html', status=400)
