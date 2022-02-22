from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('', views.exam, name='exam'),
    path('view_exam_list/', views.view_exam_list, name='view_exam_list'),
    path('view_exam/', views.view_exam, name='view_exam'),
    path('review_exam_list/', views.review_exam_list, name='review_exam_list'),
    path('review_exam/', views.review_exam, name='review_exam'),
]
