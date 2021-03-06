from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from user.models import CustomUser, EmailVerifyRecord, QuestionVerifyRecord
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import login as login_admin
from django.contrib.auth import logout as logout_admin
from django.contrib.auth import authenticate
from django.utils.datastructures import MultiValueDictKeyError
import re
from django.utils import timezone
import datetime
from django.core.mail import send_mail
from ManagementSystemPremium.settings import EMAIL_FROM
from ManagementSystemPremium.views import *
import random
from user_agents import parse
import json
# from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
# from django.utils import timezone
from document.models import SignatureRemoteStorage


def check_datetime_opened(close_timezone, now_timezone):
    return True if close_timezone > now_timezone else False


def check_authority(func):
    def wrapper(*args, **kwargs):
        if not args[0].user.is_authenticated:
            # if "X-Requested_With" in args[0].headers:
            #     return JsonResponse('请先登录', safe=False, json_dumps_params={'ensure_ascii': False})
            if args[0].META['QUERY_STRING']:
                return redirect('/user/login/?next=%s?%s' % (args[0].path, args[0].META['QUERY_STRING']))
            return redirect('/user/login/?next=%s' % args[0].path)
        return func(*args, **kwargs)
    return wrapper


def check_is_superuser(func):
    def wrapper(*args, **kwargs):
        if not args[0].user.is_superuser:
            if "X-Requested_With" in args[0].headers:
                return JsonResponse('无权限访问', safe=False, json_dumps_params={'ensure_ascii': False})
            return redirect(reverse('error_not_accessible'))
        return func(*args, **kwargs)
    return wrapper


def check_is_touch_capable(func):
    def wrapper(*args, **kwargs):
        user_agent = parse(args[0].META.get('HTTP_USER_AGENT'))
        if not user_agent.is_touch_capable:
            if args[0].META.get('HTTP_REFERER'):
                return redirect(args[0].META.get('HTTP_REFERER')+'请使用触屏设备签名')
            else:
                return redirect('/')
        return func(*args, **kwargs)
    return wrapper


# 仅适用于嵌套在第一个参数是requests,第二个参数是object_id的函数上
def check_accessible(model_object, field_name):
    def func_wrapper(func):
        def args_wrapper(*args, **kwargs):
            try:
                model = model_object
                obj = eval('model.objects.get(%s=args[1])' % field_name)
            except Exception as e:
                return redirect('/error_404')
            if args[0].user.is_superuser:
                return func(*args, **kwargs)
            accessible_team_id = list(obj.team.all().values_list('id', flat=True))
            if len(accessible_team_id) == 0:
                return func(*args, **kwargs)
            else:
                if not args[0].user.team:
                    return render(args[0], 'user_setting.html', {'msg': '您还未有分组，请先进行分组设置！'})
                else:
                    for team_id in accessible_team_id:
                        if team_id in json.loads(args[0].user.team.related_parent):
                            return func(*args, **kwargs)
            return redirect(reverse('error_not_accessible'))
        return args_wrapper
    return func_wrapper


def check_grouping(func):
    def wrapper(*args, **kwargs):
        if not args[0].user.team:
            return render(args[0], 'user_setting.html', {'msg': '您尚未有分组，请联系管理员进行分组设置！'})
        return func(*args, **kwargs)
    return wrapper


def home(request):
    return render(request, 'home.html')


@check_authority
def user_setting(request):
    is_sign = True if SignatureRemoteStorage.objects.filter(user=request.user).count() > 0 else False
    return render(request, 'user_setting.html', {"is_sign": is_sign})


def register(request):
    if request.method == 'POST':
        if not check_post_validate(request, check_register_username_validate, check_password_validate, check_name_validate,
                                   check_name_validate, check_email_validate, check_question_validate,
                                   check_answer_validate, ['username', 'password', 'lastname', 'firstname', 'email', 'question', 'answer']):
            return render(request, 'register.html', {'msg': '用户名已存在，或存在未按规定要求填写的字段！'})
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        last_name = request.POST.get('lastname', '')
        first_name = request.POST.get('firstname', '')
        email = request.POST.get('email', '')
        question = request.POST.get('question', '')
        answer = request.POST.get('answer', '')
        try:
            CustomUser.objects.create(username=username, password=make_password(password), last_name=last_name,
                                      first_name=first_name, email=email, question=question,
                                      answer=make_password(answer), is_active=False)
            return render(request, 'register.html', {'msg': '注册成功，请等待管理员审核！'})
        except:
            return render(request, 'register.html', {'msg': '注册失败，出现未知错误，请联系管理员！'})
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login_admin(request, user)
            next_url = request.GET.get('next', '')
            if next_url != '':
                return redirect(next_url)
            else:
                return redirect('/')
        else:
            try:
                user = CustomUser.objects.get(username=username)
                if check_password(password, user.password):
                    if user.is_active:
                        return render(request, 'login.html', {'msg': '登录出错，请管理员！'})
                    else:
                        return render(request, 'login.html', {'msg': '用户未认证，请联系管理员审核！'})
                else:
                    return render(request, 'login.html', {'msg': '用户名或密码错误！'})
            except:
                return render(request, 'login.html', {'msg': '用户名或密码错误！'})
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            next_url = request.GET.get('next', '')
            return render(request, 'login.html', {'next': next_url})


def random_str(str_length=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    for i in range(str_length):
        str += chars[random.randint(0, length)]
    return str


@check_authority
def set_email_verify(request):
    return render(request, 'email_verify.html')


@check_authority
def send_verify_email(request):
    if request.method == 'POST':
        if not check_post_validate(request, check_username_validate, check_email_validate, ['username', 'email']):
            return render(request, 'email_verify.html', {'msg': '存在未按格式输入的字段!'})
        user = request.user
        code = random_str(16)
        EmailVerifyRecord.objects.create(user=user, email=user.email, code=code, type='register', close_datetime=timezone.localtime(timezone.now()) + datetime.timedelta(minutes=5))
        email_title = '管理系统 - 验证邮箱'
        email_body = '请点击下面的链接验证邮箱，有效期为5分钟: https://%s/check_verify_email/%s' % (request.get_host(), code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [user.email])
        if send_status:
            return render(request, 'email_verify.html', {'msg': '邮件已发送，请登录邮箱查收'})
        else:
            return render(request, 'email_verify.html', {'msg': '邮件发送失败，请检查邮箱地址或者检查邮箱接收设置'})
    else:
        return render(request, 'error_400.html', status=400)


@check_authority
def check_verify_email(request, code):
    records = EmailVerifyRecord.objects.filter(code=code)
    if len(records) > 0:
        for record in records:
            if check_datetime_opened(timezone.localtime(record.close_datetime), timezone.localtime(timezone.now())):
                user = CustomUser.objects.get(id=record.user.id)
                user.email = record.email
                user.email_verify = True
                user.save()
                return render(request, 'user_setting.html', {'msg': '邮箱验证成功'})
        return render(request, 'email_verify.html', {'msg': '验证码已过期'})
    else:
        return render(request, 'email_verify.html', {'msg': '验证失败，验证码错误'})


def pre_reset_password(request):
    return render(request, 'pre_reset_password.html')


def pre_reset_password_by_question(request):
    return render(request, 'pre_reset_password_by_question.html')


def show_reset_password_question(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        if username == '':
            return render(request, 'pre_reset_password_by_question.html', {'msg': '用户名为空'})
        try:
            user = CustomUser.objects.get(username=username)
            return render(request, 'reset_password_by_question_answer.html', {'user_id': user.id, 'question': user.question})
        except:
            return render(request, 'pre_reset_password_by_question.html', {'msg': '用户名不存在'})
    else:
        return render(request, 'error_400.html', status=400)


def check_reset_password_answer(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id', '')
        answer = request.POST.get('answer', '')
        if user_id == '' or answer == '':
            return render(request, 'reset_password_by_question_answer.html', {'msg': '输入为空'})
        try:
            user = CustomUser.objects.get(id=user_id)
            if check_password(answer, user.answer):
                code = random_str(16)
                QuestionVerifyRecord.objects.create(user=user, code=code, close_datetime=timezone.localtime(timezone.now()) + datetime.timedelta(minutes=5))
                return render(request, 'reset_password_by_question.html', {'code': code, 'msg': '验证成功，请输入新密码'})
            else:
                return render(request, 'pre_reset_password_by_question.html', {'msg': '答案不匹配，请检查'})
        except:
            return render(request, 'pre_reset_password_by_question.html', {'msg': '用户不存在'})
    else:
        return render(request, 'error_400.html', status=400)


def reset_password_by_question(request, code):
    if request.method == 'POST':
        records = QuestionVerifyRecord.objects.filter(code=code)
        if len(records) > 0:
            for record in records:
                if check_datetime_opened(timezone.localtime(record.close_datetime), timezone.localtime(timezone.now())):
                    if not check_post_validate(request, check_password_validate, check_password_validate, ['password', 'password_repeat']):
                        return render(request, 'reset_password_by_question.html', {'msg': '存在未按格式输入的字段!'})
                    password = request.POST.get('password', '')
                    password_repeat = request.POST.get('password_repeat', '')
                    if password == '' or password_repeat == '':
                        return render(request, 'reset_password_by_question.html', {'msg': '密码为空', 'code': code})
                    if password != password_repeat:
                        return render(request, 'reset_password_by_question.html', {'msg': '两次输入的密码不一致', 'code': code})
                    user = CustomUser.objects.get(id=record.user.id)
                    user.password = make_password(password)
                    user.save()
                    return render(request, 'login.html', {'msg': '密码修改成功'})
            return render(request, 'reset_password_by_question_answer.html', {'msg': '验证码已过期'})
    else:
        return render(request, 'error_400.html', status=400)


def pre_reset_password_by_email(request):
    return render(request, 'pre_reset_password_by_email.html')


def send_reset_password_email(request):
    if request.method == 'POST':
        if not check_post_validate(request, check_username_validate, check_email_validate, ['username', 'email']):
            return render(request, 'pre_reset_password_email.html', {'msg': '存在未按格式输入的字段!'})
        username = request.POST.get('username', '')
        try:
            user = CustomUser.objects.get(username=username)
        except:
            return render(request, 'pre_reset_password_by_email.html', {'msg': '用户名不存在'})
        email = request.POST.get('email', '')
        if not user.email == email:
            return render(request, 'pre_reset_password_by_email.html', {'msg': '邮箱不匹配'})
        code = random_str(16)
        EmailVerifyRecord.objects.create(user=user, email=email, code=code, type='reset', close_datetime=timezone.localtime(timezone.now()) + datetime.timedelta(minutes=5))
        email_title = '管理系统 - 找回密码'
        email_body = '请点击下面的链接重设密码，有效期为5分钟: https://%s/reset_password/%s' % (request.get_host(), code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            return render(request, 'pre_reset_password_by_email.html', {'msg': '邮件已发送，请登录邮箱查收'})
        else:
            return render(request, 'pre_reset_password_by_email.html', {'msg': '邮件发送失败，请检查邮箱地址或者检查邮箱接收设置'})
    else:
        return render(request, 'error_400.html', status=400)


def reset_password_by_email(request, code):
    records = EmailVerifyRecord.objects.filter(code=code)
    if len(records) > 0:
        for record in records:
            if check_datetime_opened(timezone.localtime(record.close_datetime), timezone.localtime(timezone.now())):
                if request.method == 'GET':
                    record.close_datetime = timezone.localtime(timezone.now()) + datetime.timedelta(minutes=5)
                    record.save()
                    return render(request, 'reset_password_by_email.html', {'msg': '验证成功，请于5分钟内重设密码', 'code': code})
                elif request.method == 'POST':
                    if not check_post_validate(request, check_password_validate, check_password_validate, ['password', 'password_repeat']):
                        return render(request, 'reset_password_by_email.html', {'msg': '存在未按格式输入的字段!'})
                    password = request.POST.get('password', '')
                    password_repeat = request.POST.get('password_repeat', '')
                    if password == '' or password_repeat == '':
                        return render(request, 'reset_password_by_email.html', {'msg': '密码为空', 'code': code})
                    if password != password_repeat:
                        return render(request, 'reset_password_by_email.html', {'msg': '两次输入的密码不一致', 'code': code})
                    user = CustomUser.objects.get(id=record.user.id)
                    user.password = make_password(password)
                    user.save()
                    return render(request, 'login.html', {'msg': '密码修改成功'})
        return render(request, 'pre_reset_password_by_email.html', {'msg': '验证码已过期'})
    else:
        return render(request, 'pre_reset_password_by_email.html', {'msg': '重设密码失败，验证码错误'})


@check_authority
def change_password(request):
    if request.method == 'GET':
        return render(request, 'change_password.html')
    else:
        if not check_post_validate(request, check_password_validate, check_password_validate, ['password', 'password_repeat']):
            return render(request, 'change_password.html', {'msg': '存在未按格式输入的字段!'})
        old_password = request.POST.get('old_password', '')
        if check_password(old_password, request.user.password):
            password = request.POST.get('password', '')
            password_repeat = request.POST.get('password_repeat', '')
            if password == '' or password_repeat == '':
                return render(request, 'change_password.html', {'msg': '密码为空'})
            if password != password_repeat:
                return render(request, 'change_password.html', {'msg': '两次输入的密码不一致'})
            user = CustomUser.objects.get(id=request.user.id)
            user.password = make_password(password)
            user.save()
            return render(request, 'login.html', {'msg': '密码修改成功，请重新登录'})
        else:
            return render(request, 'change_password.html', {'msg': '旧密码不正确!'})


def logout(request):
    logout_admin(request)
    return redirect(reverse('home'))


def check_register_username_validate(request, username_tag):
    if request.method == 'GET':
        username = request.GET.get(username_tag)
    else:
        username = request.POST.get(username_tag)
    if username == '':
        return HttpResponse('用户名不能为空')
    if len(username) < 4 or len(username) > 16:
        return HttpResponse('用户名不能少于4个字符或超过16个字符')
    if not re.search(r'^[_a-zA-Z0-9]+$', username):
        return HttpResponse('用户名包含非法字符(!,@,#,$,%...)')
    if CustomUser.objects.filter(username=username).count() != 0:
        return HttpResponse('用户名已存在')
    return HttpResponse('')
