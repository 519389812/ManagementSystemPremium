from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from training.models import TrainingRecord


class NoticeListView(LoginRequiredMixin, ListView):
    """通知列表"""
    # 上下文的名称
    context_object_name = 'notices'
    # 模板位置
    template_name = 'notice_list.html'
    # 登录重定向
    login_url = '/login/'

    # 未读通知的查询集
    def get_queryset(self):
        return self.request.user.notifications.unread()


class MarkTrainingNoticeAsReadView(View):
    """更新通知状态"""
    # 处理 get 请求
    def get(self, request):
        # 获取未读消息
        notice_id = request.GET.get('notice_id')
        # 更新单条通知
        if notice_id:
            training_record_id = request.GET.get('training_record_id')
            try:
                training_record = TrainingRecord.objects.get(id=training_record_id)
                request.user.notifications.get(id=notice_id).mark_as_read()
                return redirect(training_record)
            except:
                return redirect('notice:show_notice')
        # 更新全部通知
        else:
            request.user.notifications.mark_all_as_read()
            return redirect('notice:show_notice')
