from django.urls import path
from . import views

app_name = 'flexible'


urlpatterns = [
    path('view_loadsheet', views.view_loadsheet, name='view_loadsheet'),
    path('add_loadsheet', views.add_loadsheet, name='add_loadsheet'),
    path('view_loadsheet_list', views.view_loadsheet_list, name='view_loadsheet_list'),
]
