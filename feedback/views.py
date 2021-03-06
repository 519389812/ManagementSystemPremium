from django.shortcuts import render
from feedback.models import Feedback
from ManagementSystemPremium.views import check_post_validate, check_fullname_validate, check_email_validate


def feedback(request):
    if request.method == 'GET':
        return render(request, 'feedback.html')
    else:
        content = request.POST.get('content', '')
        contact = request.POST.get('email', '')
        if content == '':
            return render(request, 'error_custom.html', {'msg': '反馈内容不能为空'})
        if request.user:
            Feedback.objects.create(user=request.user, content=content, contact=content)
        else:
            anonymous = request.POST.get('fullname', '')
            if anonymous == '':
                Feedback.objects.create(content=content, contact=contact)
            else:
                Feedback.objects.create(anonymous=anonymous, content=content, contact=contact)
        return render(request, 'feedback.html', {'msg': '提交成功！'})
