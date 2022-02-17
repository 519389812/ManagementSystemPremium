from django.shortcuts import render, redirect
from django.urls import reverse
from user.models import CustomUser
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import login as login_admin
import os
from announcement.models import Announcement, AnnouncementRecord, Feedback
from django.http import HttpResponse
from PIL import Image
from announcement.models import file_path
from ManagementSystemPremium import settings
from django.views.decorators.csrf import csrf_exempt
import re
from user.views import check_authority
from django.core.paginator import Paginator
from django.utils import timezone


@check_authority
def announcement(request):
    return render(request, 'announcement.html')


@check_authority
def view_announcement_list(request):
    if request.method == 'GET':
        page_num = request.GET.get('page', '1')
        announcement = Announcement.objects.all()
        paginator = Paginator(announcement, 20)
        page = paginator.get_page(int(page_num))
        return render(request, 'view_announcement_list.html', {'page_object_list': list(page.object_list),
                                                               'total_num': paginator.count,
                                                               'total_page_num': paginator.num_pages,
                                                               'page_num': page.number})
    else:
        return render(request, 'error_400.html', status=400)


@check_authority
def view_announcement(request):
    if request.Method == 'GET':
        announcement_id = request.GET.get('announcement_id', '')
    else:
        return render(request, 'error_400.html', status=400)
    try:
        announcement = Announcement.objects.get(id=announcement_id)
    except:
        return render(request, 'error_500.html', status=500)
    if request.user.team not in announcement.team:
        return render(request, 'error_custom.html', {'msg': '您不在该通知的可见用户范围内'}, status=200)
    read_times = AnnouncementRecord.objects.filter(announcement=announcement, user=request.user).count()
    is_read = True if read_times > 0 else False
    target_team_name = announcement.team.all().values_list('name', flat=True)
    target_user = list(announcement.people.all().values_list('full_name', flat=True))
    target_team_member_dict = {}
    for team in target_team_name:
        user = list(CustomUser.objects.filter(team__name=team).values_list('full_name', flat=True))
        target_user = list(set(target_user).difference(set(user)))
        target_team_member_dict[team] = user
    read_user_list = AnnouncementRecord.objects.filter(announcement=announcement).values_list('user__full_name', flat=True)
    for _, user_list in target_team_member_dict.items():
        for i in range(len(user_list)):
            read_status = True if user_list[i] in read_user_list else False
            user_list[i] = (user_list[i], read_status)
    return render(request, 'view_announcement.html', {'announcement': announcement, 'target_team_member_dict': target_team_member_dict, 'is_read': is_read})


@check_authority
def confirm_announcement(request):
    if request.Method == 'POST':
        announcement_id = request.POST.get('announcement_id', '')
        try:
            announcement = Announcement.objects.get(id=announcement_id)
        except:
            return render(request, 'error_500.html', status=500)
        if AnnouncementRecord.objects.filter(announcement=announcement, user=request.user).count() > 0:
            return render(request, 'error_custom.html', {'msg': '请勿重复提交'}, status=200)
        else:
            if announcement.require_upload == "True":
                image_list = request.FILES.getlist('file', [])
                transform_image_list = []
                if len(image_list) > 0:
                    for image in image_list:
                        image_name = image.name.lower()
                        if image_name.endswith("jpg") or image_name.endswith("jpeg") or image_name.endswith("png"):
                            try:
                                image_type = image_name.split(".")[-1]
                                image = Image.open(image)
                                x, y = image.size
                                if x > y:
                                    image = image.rotate(90, expand=True)
                                image = image.resize((392, 700))
                                transform_image_list.append((image, image_type))
                            except:
                                return render(request, 'error_custom.html', {'msg': '图片格式错误，请更换图片重新上传！'}, status=200)
                        else:
                            return render(request, 'error_custom.html', {'msg': '图片格式错误，请更换图片重新上传！'}, status=200)
                    for image, image_type in transform_image_list:
                        timestamp = timezone.now().timestamp()
                        image.save(os.path.join(file_path, (request.user.id + '_' + announcement_id + '_' + timestamp + '.' + image_type)))
                        AnnouncementRecord.objects.create(aid=id, reader=user.full_name, image=os.path.join(image_path, (
                                id + '_' + user.full_name + '.' + img_type)), team_id=user.team_id)
                    return redirect(request.META['HTTP_REFERER'])
                else:
                    return render(request, 'error_500.html', status=500)
            else:
                AnnouncementRecord.objects.create(aid=id, reader=user.full_name, team_id=user.team_id)
                return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'error_400.html', status=400)


@check_authority
def feedback_confirm(request, id):
    # 对应action中 <form action = "{% url 'feedback_confirm' id %}" method = "post"> 的 {% url 'feedback_confirm' id %} 方法，
    # confirm指向urls.py中name=confirm的url
    user = request.session.get("login_user", "")
    user = User.objects.get(username=user)
    comment = request.POST.get("feedback")
    if len(Feedback.objects.filter(aid=id, sender=user.full_name)) > 3:
        return HttpResponse("您的评论次数过多，已经限制评论，请勿刷屏！")
    else:
        Feedback.objects.create(aid=id, sender=user.full_name, comment=comment, team_id=user.team_id)
        return redirect(request.META['HTTP_REFERER'])


@csrf_exempt
def show_upload(request, id, names=None):
    if request.method == "POST":
        if names is not None:
            values = AnnouncementRecord.objects.filter(aid=id)
            if len(values) != 0:
                try:
                    values = {"reader_upload": {values.get(reader=name).reader: values.get(reader=name).image
                                                for name in values.values_list("reader", flat=True) if name in names},
                              "media_url": MEDIA_URL}
                    return render(request, "show-upload.html", values)
                except:
                    return HttpResponse("请求错误！请从公告阅读界面访问该页。")
            else:
                return HttpResponse("没有公告确认记录！")
        else:
            return HttpResponse("请求错误！请从公告阅读界面访问该页。")
    else:
        return HttpResponse("请求错误！请从公告阅读界面访问该页。")


# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")
#
#
# @register_job(scheduler, "interval", hours=1, id="clean_expired_data")
# def clean_expired_data():
#     data = Announcement.objects.filter(deadline__lte=timezone.now(), active=True)
#     if len(data) > 0:
#         data_id = list(set(data.values_list("id", flat=True)))
#         data.update(content="已过期", active=False)
#         data_id = [str(i) for i in data_id]
#         dir = os.path.join(settings.MEDIA_ROOT, image_path)
#         for file in os.listdir(dir):
#             if file.startswith(tuple(data_id)):
#                 os.remove(os.path.join(dir, file))
#
#
# register_events(scheduler)
# scheduler.start()
