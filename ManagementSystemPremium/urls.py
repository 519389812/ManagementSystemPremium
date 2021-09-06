"""ManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views as main_views
from user import views as user_views
from performance import views as performance_views
from django.shortcuts import render
from ManagementSystemPremium.views import error_404, error_400, error_403, error_500


handler404 = error_404
handler400 = error_400
handler403 = error_403
handler500 = error_500


urlpatterns = [
    # main
    path('admin/', admin.site.urls),
    path('', main_views.home, name="home"),
    path('error_404/', main_views.error_404, name="error_404"),
    path('error_400/', main_views.error_400, name="error_400"),
    path('error_not_accessible/', main_views.error_not_accessible, name="error_not_accessible"),
    path('contact/', main_views.contact, name="contact"),
    path('about/', main_views.about, name="about"),

    # user
    path('login/', user_views.login, name="login"),
    path('logout/', user_views.logout, name="logout"),
    path('register/', user_views.register, name="register"),
    path('user_setting/', user_views.user_setting, name="user_setting"),
    path('change_password/', user_views.change_password, name="change_password"),

    path('check_username_validate/', user_views.check_username_validate, name="check_username_validate"),
    path('check_password_validate/', user_views.check_password_validate, name="check_password_validate"),
    path('check_old_password_validate/', user_views.check_old_password_validate, name="check_old_password_validate"),
    path('check_password_repeat_validate/', user_views.check_password_repeat_validate, name="check_password_repeat_validate"),
    path('check_lastname_validate/', user_views.check_lastname_validate, name="check_lastname_validate"),
    path('check_firstname_validate/', user_views.check_firstname_validate, name="check_firstname_validate"),
    path('check_email_validate/', user_views.check_email_validate, name="check_email_validate"),
    path('check_question_validate/', user_views.check_question_validate, name="check_question_validate"),
    path('check_answer_validate/', user_views.check_answer_validate, name="check_answer_validate"),
    path('check_post_validate/', user_views.check_post_validate, name="check_post_validate"),

    path(r'set_email_verify/', user_views.set_email_verify, name="set_email_verify"),
    path(r'send_verify_email/', user_views.send_verify_email, name="send_verify_email"),
    re_path(r'check_verify_email/(.*)/$', user_views.check_verify_email, name="check_verify_email"),

    path(r'pre_reset_password/', user_views.pre_reset_password, name="pre_reset_password"),

    path(r'pre_reset_password_by_question/', user_views.pre_reset_password_by_question, name="pre_reset_password_by_question"),
    path(r'show_reset_password_question/', user_views.show_reset_password_question, name="show_reset_password_question"),
    path(r'check_reset_password_answer/', user_views.check_reset_password_answer, name="check_reset_password_answer"),
    re_path(r'reset_password_by_question/(.*)/$', user_views.reset_password_by_question, name="reset_password_by_question"),

    path(r'pre_reset_password_by_email/', user_views.pre_reset_password_by_email, name="pre_reset_password_by_email"),
    path(r'send_reset_password_email/', user_views.send_reset_password_email, name="send_reset_password_email"),
    re_path(r'reset_password_by_email/(.*)/$', user_views.reset_password_by_email, name="reset_password_by_email"),

    # performance
    path('performance/', performance_views.performance, name="performance"),
    path('performance/reward_charts', performance_views.reward_charts, name="reward_charts"),
    path('performance/add_workload/', performance_views.add_workload, name="add_workload"),
    path('performance/view_workload/', performance_views.view_workload, name="view_workload"),
    path('performance/workload_summary_export/', performance_views.workload_summary_export, name="workload_summary_export"),
]
