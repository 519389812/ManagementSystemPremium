from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from user.models import User, EmailVerifyRecord, QuestionVerifySource, QuestionVerifyRecord
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import login as login_admin
from django.contrib.auth import logout as logout_admin
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.datastructures import MultiValueDictKeyError
import re
from django.utils import timezone
import datetime
from django.core.mail import send_mail
from ManagementSystem.settings import EMAIL_FROM
import random
from user_agents import parse
import json
from urllib.parse import urlparse
import uuid
# from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
# from django.utils import timezone
from django.http import Http404


def check_datetime_opened(close_timezone, now_timezone):
    return True if close_timezone > now_timezone else False


def check_authority(func):
    def wrapper(*args, **kwargs):
        if not args[0].user.is_authenticated:
            return redirect("/login/?next=%s" % args[0].path)
        return func(*args, **kwargs)
    return wrapper


def check_is_touch_capable(func):
    def wrapper(*args, **kwargs):
        user_agent = parse(args[0].META.get('HTTP_USER_AGENT'))
        if not user_agent.is_touch_capable:
            if args[0].META.get("HTTP_REFERER"):
                return redirect(args[0].META.get("HTTP_REFERER")+"请使用触屏设备签名")
            else:
                return redirect("/")
        return func(*args, **kwargs)
    return wrapper


# 仅适用于嵌套在第一个参数是requests,第二个参数是object_id的函数上
def check_accessible(model_object):
    def func_wrapper(func):
        def args_wrapper(*args, **kwargs):
            try:
                obj = model_object.objects.get(id=args[1])
            except:
                return redirect('/error_404')
            if args[0].user.is_superuser:
                return func(*args, **kwargs)
            accessible_team_id = list(obj.team.all().values_list("id", flat=True))
            if len(accessible_team_id) == 0:
                return func(*args, **kwargs)
            else:
                if not args[0].user.team:
                    return render(args[0], "user_setting.html", {'msg': '您还未有分组，请先进行分组设置！'})
                else:
                    for team_id in accessible_team_id:
                        if team_id in json.loads(args[0].user.team.related_parent):
                            return func(*args, **kwargs)
            return redirect('/error_not_accessible')
        return args_wrapper
    return func_wrapper


def check_grouping(func):
    def wrapper(*args, **kwargs):
        if not args[0].user.team:
            return render(args[0], "user_setting.html", {'msg': '您还未有分组，请先进行分组设置！'})
        return func(*args, **kwargs)
    return wrapper


def home(request):
    return render(request, "home.html")


@check_authority
def user_setting(request):
    return render(request, "user_setting.html")


def register(request):
    if request.method == "POST":
        if not check_post_valudate(request, check_username_validate, check_password_validate, check_lastname_validate,
                                       check_firstname_validate):
            return render(request, "register.html", {"msg": "存在未按规定要求的字段！"})
        username = request.POST.get("username")
        password = request.POST.get("password")
        last_name = request.POST.get("lastname")
        first_name = request.POST.get("firstname")
        try:
            User.objects.create(username=username, password=make_password(password), last_name=last_name,
                                first_name=first_name, is_active=False)
            return render(request, "register.html", {"msg": "注册成功，请等待管理员审核！"})
        except:
            return render(request, "register.html", {"msg": "注册失败，出现未知错误，请联系管理员！"})
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login_admin(request, user)
            next_url = request.GET.get('next', '')
            if next_url != "":
                return redirect(next_url)
            else:
                return redirect('/')
        else:
            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    if user.is_active:
                        return render(request, "login.html", {"msg": "登录出错，请管理员！"})
                    else:
                        return render(request, "login.html", {"msg": "用户未认证，请联系管理员审核！"})
                else:
                    return render(request, "login.html", {"msg": "用户名或密码错误！"})
            except:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            next_url = request.GET.get('next', '')
            return render(request, "login.html", {'next': next_url})


def random_str(str_length=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    for i in range(str_length):
        str += chars[random.randint(0, length)]
    return str


@check_authority
def set_question_verify(request):
    return render(request, "set_question_verify.html")


@check_authority
def save_question_verify(request):
    if request.method == "POST":
        question = request.POST.get("question", "")
        answer = request.POST.get("answer", "")
        if not check_post_valudate(request, check_question_validate, check_answer_validate):
            return render(request, "set_question_verify.html", {"msg": "请输入正确的格式！"})
        if QuestionVerifySource.objects.filter(user=request.user).count() > 2:
            return render(request, "user_setting.html", {"msg": "设置失败，已经超过最大问题数量！"})
        QuestionVerifySource.objects.create(user=request.user, question=question, answer=make_password(answer))
        return render(request, "user_setting.html", {"msg": "设置成功！"})
    else:
        return render(request, "error_400.html", status=400)


@check_authority
def set_email_verify(request):
    return render(request, "set_email_verify.html")


@check_authority
def send_set_user_verify_email(request):
    if request.method == "POST":
        email_address = request.POST.get("email_address", "")
        if not check_post_valudate(request, check_email_validate):
            return render(request, "set_email_verify.html", {"msg": "请输入正确的邮箱格式!"})
        code = random_str(16)
        EmailVerifyRecord.objects.create(user=request.user, email=email_address, code=code, type="register", close_datetime=timezone.localtime(timezone.now()) + datetime.timedelta(minutes=5))
        email_title = "管理系统 - 邮箱激活链接"
        email_body = "请点击下面的链接激活你的账号，有效期为5分钟: http://%s/check_set_user_verify_email/%s" % (request.get_host(), code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email_address])
        if send_status:
            return render(request, "set_email_verify.html", {"msg": "邮件已发送，请登录邮箱查收"})
        else:
            return render(request, "set_email_verify.html", {"msg": "邮件发送失败，请检查邮箱地址或者检查邮箱接收设置"})
    else:
        return render(request, "error_400.html", status=400)


@check_authority
def check_set_user_verify_email(request, code):
    records = EmailVerifyRecord.objects.filter(code=code)
    if len(records) > 0:
        for record in records:
            if check_datetime_opened(timezone.localtime(record.close_datetime), timezone.localtime(timezone.now())):
                user = User.objects.get(id=record.user.id)
                user.email = record.email
                user.save()
                return render(request, 'user_setting.html', {"msg": "邮箱验证成功"})
        return render(request, 'set_email_verify.html', {"msg": "验证码已过期"})
    else:
        return render(request, 'set_email_verify.html', {"msg": "验证失败，验证码错误"})


def pre_reset_password(request):
    return render(request, "pre_reset_password.html")


def pre_reset_password_by_question(request):
    return render(request, "pre_reset_password_by_question.html")


def pre_reset_password_by_email(request):
    return render(request, "pre_reset_password_by_email.html")


def select_reset_password_by_question(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        if username == "":
            return render(request, "pre_reset_password_by_question.html", {"msg": "用户名为空"})
        try:
            user = User.objects.get(username=username)
            question_list = QuestionVerifySource.objects.filter(user=user).values('id', 'question')
            return render(request, "select_reset_password_by_question.html", {"question_list": question_list})
        except:
            return render(request, "pre_reset_password_by_question.html", {"msg": "用户名不存在"})
    else:
        return render(request, "error_400.html", status=400)


def check_reset_password_question(request):
    if request.method == "POST":
        question_id = request.POST.get("question_id", "")
        answer = request.POST.get("answer", "")
        if question_id == "" or answer == "":
            return render(request, "select_reset_password_by_question.html", {"msg": "输入为空"})
        try:
            question = QuestionVerifySource.objects.get(id=int(question_id))
            print(answer, make_password(answer))
            if check_password(answer, question.answer):
                code = random_str(16)
                QuestionVerifyRecord.objects.create(user=question.user, code=code, close_datetime=timezone.localtime(timezone.now()) + datetime.timedelta(minutes=5))
                return render(request, "reset_password_by_question.html", {'code': code})
            else:
                return render(request, "pre_reset_password_by_question.html", {"msg": "答案不匹配，请检查"})
        except:
            return render(request, "pre_reset_password_by_question.html", {"msg": "问题不存在"})
    else:
        return render(request, "error_400.html", status=400)


def reset_password_by_question(request, code):
    if request.method == 'POST':
        records = QuestionVerifyRecord.objects.filter(code=code)
        if len(records) > 0:
            for record in records:
                if check_datetime_opened(timezone.localtime(record.close_datetime), timezone.localtime(timezone.now())):
                    if not check_post_valudate(request, check_passwords_validate):
                        return render(request, "reset_password_by_question.html", {"msg": "存在未按格式输入的字段!"})
                    password = request.POST.get("password", "")
                    password_repeat = request.POST.get("password_repeat", "")
                    if password == "" or password_repeat == "":
                        return render(request, 'reset_password_by_question.html', {"msg": "密码为空", "code": code})
                    if password != password_repeat:
                        return render(request, 'reset_password_by_question.html', {"msg": "两次输入的密码不一致", "code": code})
                    user = User.objects.get(id=record.user.id)
                    user.password = make_password(password)
                    user.save()
                    return render(request, 'login.html', {"msg": "密码修改成功"})
            return render(request, 'reset_password_by_question.html', {"msg": "验证码已过期"})
    else:
        return render(request, "error_400.html", status=400)


def send_reset_password_email(request):
    if request.method == "POST":
        if not check_post_valudate(request, check_email_validate):
            return render(request, "reset_password_email.html", {"msg": "存在未按格式输入的字段!"})
        username = request.POST.get("username", "")
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, "pre_reset_password_by_email.html", {"msg": "用户名不存在"})
        email_address = request.POST.get("email_address", "")
        if not user.email == email_address:
            return render(request, "pre_reset_password_by_email.html", {"msg": "邮箱不匹配"})
        code = random_str(16)
        EmailVerifyRecord.objects.create(user=user, code=code, type="reset", close_datetime=timezone.localtime(timezone.now()) + datetime.timedelta(minutes=5))
        email_title = "管理系统 - 找回密码"
        email_body = "请点击下面的链接找回你的密码，有效期为5分钟: https://%s/reset_password/%s" % (request.get_host(), code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email_address])
        if send_status:
            return render(request, "reset_password_by_email.html", {"msg": "邮件已发送，请登录邮箱查收"})
        else:
            return render(request, "pre_reset_password_by_email.html", {"msg": "邮件发送失败，请检查邮箱地址或者检查邮箱接收设置"})
    else:
        return render(request, "error_400.html", status=400)


def reset_password_by_email(request, code):
    records = EmailVerifyRecord.objects.filter(code=code)
    if len(records) > 0:
        for record in records:
            if check_datetime_opened(timezone.localtime(record.close_datetime), timezone.localtime(timezone.now())):
                if request.method == "GET":
                    record.close_datetime = timezone.localtime(timezone.now()) + datetime.timedelta(minutes=5)
                    record.save()
                    return render(request, 'reset_password_by_email.html', {"msg": "验证成功，请于5分钟内重设密码", "code": code})
                else:
                    if not check_post_valudate(request, check_passwords_validate):
                        return render(request, "reset_password_by_email.html", {"msg": "存在未按格式输入的字段!"})
                    password = request.POST.get("password", "")
                    password_repeat = request.POST.get("password_repeat", "")
                    if password == "" or password_repeat == "":
                        return render(request, 'reset_password_by_email.html', {"msg": "密码为空", "code": code})
                    if password != password_repeat:
                        return render(request, 'reset_password_by_email.html', {"msg": "两次输入的密码不一致", "code": code})
                    user = User.objects.get(id=record.user.id)
                    user.password = make_password(password)
                    user.save()
                    return render(request, 'login.html', {"msg": "密码修改成功"})
        return render(request, 'reset_password_by_email.html', {"msg": "验证码已过期"})
    else:
        return render(request, 'reset_password_by_email.html', {"msg": "重设密码失败，验证码错误"})


@check_authority
def change_password(request):
    if request.method == "GET":
        return render(request, 'change_password.html')
    else:
        if not check_post_valudate(request, check_passwords_validate):
            return render(request, "change_password.html", {"msg": "存在未按格式输入的字段!"})
        old_password = request.POST.get("old_password", "")
        if check_password(old_password, request.user.password):
            password = request.POST.get("password", "")
            password_repeat = request.POST.get("password_repeat", "")
            if password == "" or password_repeat == "":
                return render(request, 'change_password.html', {"msg": "密码为空"})
            if password != password_repeat:
                return render(request, 'change_password.html', {"msg": "两次输入的密码不一致"})
            user = User.objects.get(id=request.user.id)
            user.password = make_password(password)
            user.save()
            return render(request, 'login.html', {"msg": "密码修改成功，请重新登录"})
        else:
            return render(request, "change_password.html", {"msg": "旧密码不正确!"})


def logout(request):
    logout_admin(request)
    return redirect(reverse("home"))


def check_username_validate(request):
    try:
        username = request.GET["username"]
    except MultiValueDictKeyError:
        username = request.POST.get("username")
    if username == "":
        return HttpResponse('用户名不能为空')
    if len(username) < 4 or len(username) > 16:
        return HttpResponse('用户名不能少于4个字符或超过16个字符')
    if not re.search(r'^[_a-zA-Z0-9]+$', username):
        return HttpResponse("用户名包含非法字符(!,@,#,$,%...)")
    if User.objects.filter(username=username).count() != 0:
        return HttpResponse('用户名已存在')
    return HttpResponse('')


def check_password_validate(request):
    try:
        password = request.GET["password"]
    except MultiValueDictKeyError:
        password = request.POST.get("password")
    if password == "":
        return HttpResponse('密码不能为空')
    if len(password) < 6 or len(password) > 16:
        return HttpResponse('密码不能少于6个字符或超过16个字符')
    if not re.search(r'^\S+$', password):
        return HttpResponse("密码包含非法字符(‘ ’)")
    return HttpResponse('')


def check_old_password_validate(request):
    try:
        password = request.GET["old_password"]
    except MultiValueDictKeyError:
        password = request.POST.get("old_password")
    if password == "":
        return HttpResponse('密码不能为空')
    if len(password) < 6 or len(password) > 16:
        return HttpResponse('密码不能少于6个字符或超过16个字符')
    if not re.search(r'^\S+$', password):
        return HttpResponse("密码包含非法字符(‘ ’)")
    return HttpResponse('')


def check_password_repeat_validate(request):
    try:
        password = request.GET["password_repeat"]
    except MultiValueDictKeyError:
        password = request.POST.get("password_repeat")
    if password == "":
        return HttpResponse('密码不能为空')
    if len(password) < 6 or len(password) > 16:
        return HttpResponse('密码不能少于6个字符或超过16个字符')
    if not re.search(r'^\S+$', password):
        return HttpResponse("密码包含非法字符(‘ ’)")
    return HttpResponse('')


def check_passwords_validate(request):
    try:
        params = request.GET.dict()
    except MultiValueDictKeyError:
        params = request.POST.dict()
    for key, value in params.items():
        if "password" in key:
            if key == "":
                return HttpResponse('密码不能为空')
            if len(key) < 6 or len(key) > 16:
                return HttpResponse('密码不能少于6个字符或超过16个字符')
            if not re.search(r'^\S+$', key):
                return HttpResponse("密码包含非法字符(‘ ’)")
    return HttpResponse('')


def check_lastname_validate(request):
    try:
        lastname = request.GET["lastname"]
    except MultiValueDictKeyError:
        lastname = request.POST.get("lastname")
    if lastname == "":
        return HttpResponse('姓氏不能为空')
    if len(lastname) > 50:
        return HttpResponse('姓氏不能超过50个字符')
    if not re.search(r'^[_a-zA-Z0-9\u4e00-\u9fa5]+$', lastname):
        return HttpResponse("姓氏包含非法字符(!,@,#,$,%...)")
    return HttpResponse('')


def check_firstname_validate(request):
    try:
        firstname = request.GET["firstname"]
    except MultiValueDictKeyError:
        firstname = request.POST.get("firstname")
    if firstname == "":
        return HttpResponse('名字不能为空')
    if len(firstname) > 50:
        return HttpResponse('名字不能超过50个字符')
    if not re.search(r'^[_a-zA-Z0-9\u4e00-\u9fa5]+$', firstname):
        return HttpResponse("名字包含非法字符(!,@,#,$,%...)")
    return HttpResponse('')


def check_question_validate(request):
    try:
        question = request.GET["question"]
    except MultiValueDictKeyError:
        question = request.POST.get("question")
    if question == "":
        return HttpResponse('密保问题不能为空')
    if len(question) < 6 or len(question) > 50:
        return HttpResponse('密保问题不能少于6个字符或者超过50个字符')
    if not re.search(r'^[_a-zA-Z0-9\u4e00-\u9fa5\?\uff1f]+$', question):
        return HttpResponse("密保问题包含非法字符(!,@,#,$,%...)")
    return HttpResponse('')


def check_answer_validate(request):
    try:
        answer = request.GET["answer"]
    except MultiValueDictKeyError:
        answer = request.POST.get("answer")
    if answer == "":
        return HttpResponse('密保答案不能为空')
    if len(answer) < 2 or len(answer) > 16:
        return HttpResponse('密保答案不能少于2个字符或者超过16个字符')
    if not re.search(r'^[_a-zA-Z0-9\u4e00-\u9fa5]+$', answer):
        return HttpResponse("密保答案包含非法字符(!,@,#,$,%...)")
    return HttpResponse('')


def check_email_validate(request):
    try:
        email_address = request.GET["email_address"]
    except MultiValueDictKeyError:
        email_address = request.POST.get("email_address")
    try:
        validate_email(email_address)
    except ValidationError:
        return HttpResponse("请输入正确的邮箱格式")
    return HttpResponse('')


def check_post_valudate(request, *args):
    check_method = args
    for method in check_method:
        if method(request).content != b'':
            return False
    return True
