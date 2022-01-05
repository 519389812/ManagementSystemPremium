from django.shortcuts import render
import os
import base64
from urllib import parse
from django.shortcuts import render
from django.http import *
from django.utils.datastructures import MultiValueDictKeyError
import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def home(request):
    return render(request, "home.html")


def error_404(request, exception='', template_name='templates/error_404.html'):
    return render(request, "error_404.html")


def error_400(request, exception='', template_name='templates/error_400.html'):
    return render(request, "error_400.html")


def error_403(request, exception='', template_name='templates/error_403.html'):
    return render(request, "error_403.html")


def error_500(request):
    return render(request, "error_500.html")


def error_not_accessible(request):
    return render(request, "error_not_accessible.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


# 解析url中的参数
def parse_url_param(url):
    url_content = parse.urlparse(url)
    query_dict = parse.parse_qs(url_content.query)
    return query_dict


def check_username_validate(request, username_tag):
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
    return HttpResponse('')


def check_password_validate(request, password_tag):
    if request.method == 'GET':
        password = request.GET.get(password_tag)
    else:
        password = request.POST.get(password_tag)
    if password == '':
        return HttpResponse('密码不能为空')
    if len(password) < 6 or len(password) > 16:
        return HttpResponse('密码不能少于6个字符或超过16个字符')
    if not re.search(r'^\S+$', password):
        return HttpResponse('密码包含非法字符(‘ ’)')
    return HttpResponse('')


def check_name_validate(request, name_tag):
    if request.method == 'GET':
        name = request.GET.get(name_tag)
    else:
        name = request.POST.get(name_tag)
    if name == '':
        return HttpResponse('姓氏不能为空')
    if len(name) > 50:
        return HttpResponse('姓氏不能超过50个字符')
    if not re.search(r'^[_a-zA-Z0-9\u4e00-\u9fa5]+$', name):
        return HttpResponse('姓氏包含非法字符(!,@,#,$,%...)')
    return HttpResponse('')


def check_question_validate(request, question_tag):
    if request.method == 'GET':
        question = request.GET.get(question_tag)
    else:
        question = request.POST.get(question_tag)
    if question == '':
        return HttpResponse('密保问题不能为空')
    if len(question) < 3 or len(question) > 50:
        return HttpResponse('密保问题不能少于3个字符或者超过50个字符')
    if not re.search(r'^[_a-zA-Z0-9\u4e00-\u9fa5\?\uff1f]+$', question):
        return HttpResponse('密保问题包含非法字符(!,@,#,$,%...)')
    return HttpResponse('')


def check_answer_validate(request, answer_tag):
    if request.method == 'GET':
        answer = request.GET.get(answer_tag)
    else:
        answer = request.POST.get(answer_tag)
    if answer == '':
        return HttpResponse('密保答案不能为空')
    if len(answer) < 2 or len(answer) > 16:
        return HttpResponse('密保答案不能少于2个字符或者超过16个字符')
    if not re.search(r'^[_a-zA-Z0-9\u4e00-\u9fa5]+$', answer):
        return HttpResponse('密保答案包含非法字符(!,@,#,$,%...)')
    return HttpResponse('')


def check_email_validate(request, email_tag):
    if request.method == 'GET':
        email = request.GET.get(email_tag)
    else:
        email = request.POST.get(email_tag)
    try:
        validate_email(email)
    except ValidationError:
        return HttpResponse('请输入正确的邮箱格式')
    return HttpResponse('')


def check_fullname_validate(request, fullname_tag):
    if request.method == 'GET':
        fullname = request.GET.get(fullname_tag)
    else:
        fullname = request.POST.get(fullname_tag)
    if fullname == '':
        return HttpResponse('姓名不能为空 A name is required')
    if len(fullname) < 2:
        return HttpResponse('姓名格式不正确 Fullname is not valid')
    if not re.search(r'^[_a-zA-Z0-9\x20\u4e00-\u9fa5]+$', fullname):
        return HttpResponse('姓名格式不正确 Fullname is not valid')
    return HttpResponse('')


def check_flight_validate(request, flight_tag):
    if request.method == 'GET':
        flight = request.GET.get(flight_tag)
    else:
        flight = request.POST.get(flight_tag)
    if flight == '':
        return HttpResponse('航班号不能为空 A flight number is required')
    if len(flight) < 5 or len(flight) > 6:
        return HttpResponse('航班号格式不正确 Flight number is not valid')
    if not re.search(r'^\w{2}\d{3,4}$', flight):
        return HttpResponse('航班号格式不正确 Flight number is not valid')
    return HttpResponse('')


def check_airport_code_validate(request, airport_code_tag):
    if request.method == 'GET':
        departure = request.GET.get(airport_code_tag)
    else:
        departure = request.POST.get(airport_code_tag)
    if departure == '':
        return HttpResponse('始发地不能为空 A departure city is required')
    if len(departure) < 2:
        return HttpResponse('始发地格式不正确 Departure city is not valid')
    if not re.search(r'^[_a-zA-Z0-9\x20\u4e00-\u9fa5]+$', departure):
        return HttpResponse('始发地格式不正确 Departure city is not valid')
    return HttpResponse('')


def check_seat_validate(request, seat_tag):
    if request.method == 'GET':
        seat = request.GET.get(seat_tag)
    else:
        seat = request.POST.get(seat_tag)
    if seat == '':
        return HttpResponse('座位号不能为空 A seat number city is required')
    if len(seat) < 2 or len(seat) > 3:
        return HttpResponse('座位号格式不正确 Seat number is not valid')
    if not re.search(r'^\d{1,2}\w$', seat):
        return HttpResponse('座位号格式不正确 Arrival city is not valid')
    return HttpResponse('')


def check_baggage_validate(request, baggage_tag):
    if request.method == 'GET':
        baggage = request.GET.get(baggage_tag)
    else:
        baggage = request.POST.get(baggage_tag)
    if baggage == '':
        return HttpResponse('托运行李件数不能为空 Number of checked baggage is required')
    if not re.search(r'^\d{1,2}$', baggage):
        return HttpResponse('托运行李件数格式不正确 Number of checked baggage is not valid')
    if int(baggage) < 0 or int(baggage) > 50:
        return HttpResponse('托运行李件数不正确 Number of checked baggage is not valid')
    return HttpResponse('')


def check_id_type_validate(request, id_type_tag):
    if request.method == 'GET':
        id_type = request.GET.get(id_type_tag)
    else:
        id_type = request.POST.get(id_type_tag)
    if id_type == '':
        return HttpResponse('证件类别不能为空 An id type is required')
    if len(id_type) < 2 or len(id_type) > 10:
        return HttpResponse('证件类别格式不正确 Id type is not valid')
    if not re.search(r'^[_a-zA-Z0-9\x20\u4e00-\u9fa5]+$', id_type):
        return HttpResponse('证件类别格式不正确 Id type is not valid')
    return HttpResponse('')


def check_id_number_validate(request):
    if request.method == 'GET':
        id_type = request.GET.get('idType')
        id_number = request.GET.get('idNumber')
    else:
        id_type = request.POST.get('idType')
        id_number = request.POST.get('idNumber')
    if id_type == '':
        return HttpResponse('请选择证件类别 An id type is required')
    if id_number == '':
        return HttpResponse('证件号不能为空 An id number city is required')
    if id_type == '身份证':
        if len(id_number) != 15 and len(id_number) != 18:
            return HttpResponse('证件号格式不正确 Id number is not valid')
        if not re.search(r'(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)', id_number):
            return HttpResponse('证件号格式不正确 Id number is not valid')
    if id_type == '护照':
        if len(id_number) < 5 or len(id_number) > 12:
            return HttpResponse('证件号格式不正确 Id number is not valid')
        if not re.search(r'^\w{5,12}$', id_number):
            return HttpResponse('证件号格式不正确 Id number is not valid')
    return HttpResponse('')


def check_ticket_validate(request, ticket_tag):
    if request.method == 'GET':
        ticket = request.GET.get(ticket_tag)
    else:
        ticket = request.POST.get(ticket_tag)
    if ticket == '':
        return HttpResponse('票号不能位空 A ticket number is required')
    if len(ticket) != 13:
        return HttpResponse('票号格式不正确 Ticket number is not valid')
    if not re.search(r'^\d{15}$', ticket):
        return HttpResponse('票号格式不正确 Ticket number is not valid')
    return HttpResponse('')


def check_amount_validate(request, amount_tag):
    if request.method == 'GET':
        ticket = request.GET.get(amount_tag)
    else:
        ticket = request.POST.get(amount_tag)
    if ticket == '':
        return HttpResponse('数额不能位空 A number is required')
    if len(ticket) > 12:
        return HttpResponse('数额格式不正确 Number is not valid')
    if not re.search(r'^\d{12}$', ticket):
        return HttpResponse('数额格式不正确 Number is not valid')
    return HttpResponse('')


def check_dialling_code_validate(request, dialling_code_tag):
    if request.method == 'GET':
        dialling_code = request.GET.get(dialling_code_tag)
    else:
        dialling_code = request.POST.get(dialling_code_tag)
    if dialling_code == '':
        return HttpResponse('电话区号不能为空 A dialling code city is required')
    if len(dialling_code) < 2 or len(dialling_code) > 5:
        return HttpResponse('电话区号格式不正确 Dialling code is not valid')
    if not re.search(r'^\d{2,5}$', dialling_code):
        return HttpResponse('电话区号格式不正确 Dialling code is not valid')
    return HttpResponse('')


def check_telephone_validate(request, telephone_tag):
    if request.method == 'GET':
        telephone = request.GET.get(telephone_tag)
    else:
        telephone = request.POST.get(telephone_tag)
    if telephone == '':
        return HttpResponse('联系电话不能为空 A telephone number is required')
    if len(telephone) < 5 or len(telephone) > 20:
        return HttpResponse('联系电话格式不正确 Telephone number is not valid')
    if not re.search(r'^\d{5,20}$', telephone):
        return HttpResponse('联系电话格式不正确 Telephone number is not valid')
    return HttpResponse('')


def check_country_validate(request, country_tag):
    if request.method == 'GET':
        inbound_country = request.GET.get(country_tag)
    else:
        inbound_country = request.POST.get(country_tag)
    if inbound_country == '':
        return HttpResponse('入境国家不能为空 An inbound country is required')
    if len(inbound_country) < 2 or len(inbound_country) > 30:
        return HttpResponse('入境国家格式不正确 Inbound country is not valid')
    if not re.search(r'^[a-zA-Z0-9\x20\u4e00-\u9fa5]+$', inbound_country):
        return HttpResponse('入境国家格式不正确 Inbound country is not valid')
    return HttpResponse('')


def check_date_validate(request, date_tag):
    if request.method == 'GET':
        inbound_date = request.GET.get(date_tag)
    else:
        inbound_date = request.POST.get(date_tag)
    if inbound_date == '':
        return HttpResponse('日期不能为空 Inbound date is required')
    return HttpResponse('')


def check_body_temperature_validate(request, body_temperature_tag):
    if request.method == 'GET':
        body_temperature = request.GET.get(body_temperature_tag)
    else:
        body_temperature = request.POST.get(body_temperature_tag)
    if body_temperature == '':
        return HttpResponse('体温不能为空 A body temperature is required')
    if not re.search(r'^\d{2}\.?\d{0,2}?$', body_temperature):
        return HttpResponse('体温格式不正确 Body temperature is not valid')
    if float(body_temperature) < 30 or float(body_temperature) > 43:
        return HttpResponse('体温格式不正确 Body temperature is not valid')
    return HttpResponse('')


def check_healthy_code_validate(request, healthy_code_tag):
    if request.method == 'GET':
        healthy_code = request.GET.get(healthy_code_tag)
    else:
        healthy_code = request.POST.get(healthy_code_tag)
    if healthy_code == '':
        return HttpResponse('健康码不能为空 A healthy code is required')
    if len(healthy_code) < 2 or len(healthy_code) > 10:
        return HttpResponse('健康码格式不正确 Healthy code is not valid')
    if not re.search(r'^[a-zA-Z0-9\x20\u4e00-\u9fa5]+$', healthy_code):
        return HttpResponse('健康码格式不正确 Healthy code is not valid')
    return HttpResponse('')


def check_address_validate(request, address_tag):
    if request.method == 'GET':
        address = request.GET.get(address_tag)
    else:
        address = request.POST.get(address_tag)
    if address == '':
        return HttpResponse('目的地住址不能为空 A destination address is required')
    if len(address) < 10 or len(address) > 200:
        return HttpResponse('目的地住址格式不正确 Destination address is not valid')
    if not re.search(r'^[a-zA-Z0-9\x20\u4e00-\u9fa5]+$', address):
        return HttpResponse('目的地住址格式不正确 Destination address is not valid')
    return HttpResponse('')


def check_code_validate(request, code):
    if request.method == 'GET':
        code = request.GET.get(code)
    else:
        code = request.POST.get(code)
    if code == '':
        return HttpResponse('验证码不能为空 A verification code is required')
    if len(code) != 4:
        return HttpResponse('验证码格式不正确 Verification code is not valid')
    if not re.search(r'^\d{4}$', code):
        return HttpResponse('验证码格式不正确 Verification code is not valid')
    return HttpResponse('')


def check_post_validate(request, *args):
    check_method = args[:-1]
    args = args[-1]
    for i in range(len(check_method)):
        if check_method[i](request, args[i]).content != b'':
            return False
    return True
