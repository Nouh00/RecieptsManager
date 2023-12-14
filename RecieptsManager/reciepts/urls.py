from django.urls import path
from . import views

app_name = 'reciepts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/', views.recieptView, name='reciept'),
]
