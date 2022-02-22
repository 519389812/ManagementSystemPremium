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
from django.urls import path, include
from . import views as main_views
from user import views as user_views
from performance import views as performance_views
from sale import views as sales_views
from exam import views as exam_views
from django.shortcuts import render
from ManagementSystemPremium.views import error_404, error_400, error_403, error_500
import notifications.urls


handler404 = error_404
handler400 = error_400
handler403 = error_403
handler500 = error_500


urlpatterns = [
    # main
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('error_404/', main_views.error_404, name='error_404'),
    path('error_400/', main_views.error_400, name='error_400'),
    path('error_not_accessible/', main_views.error_not_accessible, name='error_not_accessible'),
    path('contact/', main_views.contact, name='contact'),
    path('about/', main_views.about, name='about'),

    # notifications
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('notice/', include('notice.urls', namespace='notice')),

    # user
    path('user/', include('user.urls', namespace='user')),

    # announcement
    path('announcement/', include('announcement.urls', namespace='announcement')),

    # bbs
    path('bbs/', include('bbs.urls', namespace='bbs')),

    # document
    path('document/', include('document.urls', namespace='document')),

    # exam
    path('exam/', include('exam.urls', namespace='exam')),

    # feedback
    path('feedback/', include('feedback.urls', namespace='feedback')),

    # performance
    path('performance/', include('performance.urls', namespace='performance')),

    # sale
    path('sale/', include('sale.urls', namespace='sale')),
]
