from django.urls import path
from . import views

app_name = 'asset'

urlpatterns = [
    path('', views.asset, name='asset'),
    path('warehousing/', views.warehousing, name='warehousing'),
]
