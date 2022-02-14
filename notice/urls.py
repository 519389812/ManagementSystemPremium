from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    # 通知列表
    path('show_notice/', views.NoticeListView.as_view(), name='show_notice'),
    # 更新通知状态
    path('mark_training_notice_as_read/', views.MarkTrainingNoticeAsReadView.as_view(), name='mark_training_notice_as_read'),
]