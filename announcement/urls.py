from django.urls import path
from . import views

app_name = 'announcement'

urlpatterns = [
    path('', views.announcement, name='announcement'),
    path('view_announcement_list', views.view_announcement_list, name='view_announcement_list'),
    path('view_sub_announcement_list', views.view_sub_announcement_list, name='view_sub_announcement_list'),
    path('view_announcement', views.view_announcement, name='view_announcement'),
    path('confirm_announcement', views.confirm_announcement, name='confirm_announcement'),
]
