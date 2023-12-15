from django.urls import path
from . import views

app_name = 'reciepts'

urlpatterns = [
    path('', views.index, name='index'),

    #CRUD Functionalities
    path('<str:pk>/', views.recieptView, name='reciept'),
    path('newReciept', views.newReciept, name='newReciept'),
    path('editReciept/<str:pk>/', views.editReciept, name='editReciept'),
    path('deleteReciept/<str:pk>/', views.deleteReciept, name='deleteReciept'),

    #Authentication
    path('login', views.loginUser, name='login'),
    path('register', views.registerUser, name='register'),    
    path('logout', views.logoutUser, name='logout'),

]
