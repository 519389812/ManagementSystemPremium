from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    path('', views.bbs, name='bbs'),
    path('view_post/', views.view_post, name='view_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_comment/', views.add_comment, name='add_comment'),
]