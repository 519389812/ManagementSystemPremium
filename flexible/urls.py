from django.urls import path
from . import views

app_name = 'flexible'


urlpatterns = [
    path('view_loadsheet', views.view_loadsheet, name='view_loadsheet'),
    path('add_loadsheet', views.add_loadsheet, name='add_loadsheet'),
]
