from django.urls import path
from . import views

urlpatterns = [

    path('test/', views.Test, name='test'),


    path('sign-up/', views.SignUp, name='signup'),

    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),

    path('donar-list/', views.DonorList, name='donor-list'),
]
