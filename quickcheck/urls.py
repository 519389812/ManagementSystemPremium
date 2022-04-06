from django.urls import path
from . import views

app_name = 'quickcheck'

urlpatterns = [
    path('', views.quickcheck, name='quickcheck'),
]
