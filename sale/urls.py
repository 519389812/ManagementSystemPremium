from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('/', views.sales, name='sales'),
    path('add_sales/', views.add_sales, name='add_sales'),
    path('view_sales/', views.view_sales, name='view_sales'),
]
