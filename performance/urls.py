from django.urls import path
from . import views

app_name = 'performance'

urlpatterns = [
    path('', views.performance, name='performance'),
    path('reward_charts', views.reward_penalty_charts, name='reward_penalty_charts'),
    path('add_workload/', views.add_workload, name='add_workload'),
    path('view_workload/', views.view_workload, name='view_workload'),
    path('add_man_hour/', views.add_man_hour, name='add_man_hour'),
    path('view_man_hour/', views.view_man_hour, name='view_man_hour'),
    path('workload_summary_export/', views.workload_summary_export, name='workload_summary_export'),
    path('get_workload_item/', views.get_workload_item, name='get_workload_item'),
    path('get_man_hour_item/', views.get_man_hour_item, name='get_man_hour_item'),
]
