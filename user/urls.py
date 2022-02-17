from django.urls import path, re_path
from . import views

app_name = 'exam'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('user_setting/', views.user_setting, name='user_setting'),
    path('change_password/', views.change_password, name='change_password'),

    path('check_username_validate/', views.check_username_validate, name='check_username_validate'),
    path('check_password_validate/', views.check_password_validate, name='check_password_validate'),
    path('check_name_validate/', views.check_name_validate, name='check_name_validate'),
    path('check_email_validate/', views.check_email_validate, name='check_email_validate'),
    path('check_question_validate/', views.check_question_validate, name='check_question_validate'),
    path('check_answer_validate/', views.check_answer_validate, name='check_answer_validate'),
    path('check_post_validate/', views.check_post_validate, name='check_post_validate'),

    path('set_email_verify/', views.set_email_verify, name='set_email_verify'),
    path('send_verify_email/', views.send_verify_email, name='send_verify_email'),
    re_path(r'check_verify_email/(.*)/$', views.check_verify_email, name='check_verify_email'),

    path(r'pre_reset_password/', views.pre_reset_password, name='pre_reset_password'),

    path('pre_reset_password_by_question/', views.pre_reset_password_by_question, name='pre_reset_password_by_question'),
    path('show_reset_password_question/', views.show_reset_password_question, name='show_reset_password_question'),
    path('check_reset_password_answer/', views.check_reset_password_answer, name='check_reset_password_answer'),
    re_path(r'reset_password_by_question/(.*)/$', views.reset_password_by_question, name='reset_password_by_question'),

    path('pre_reset_password_by_email/', views.pre_reset_password_by_email, name='pre_reset_password_by_email'),
    path('send_reset_password_email/', views.send_reset_password_email, name='send_reset_password_email'),
    re_path(r'reset_password_by_email/(.*)/$', views.reset_password_by_email, name='reset_password_by_email'),
]