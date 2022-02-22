from django.urls import path
from . import views

app_name = 'sale'

urlpatterns = [
    path('', views.sales, name='sale'),
    path('add_sale/', views.add_sales, name='add_sale'),
    path('view_sale/', views.view_sales, name='view_sale'),
]
