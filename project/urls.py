from django.urls import path
from . import views

urlpatterns = [

    path('test/', views.test, name='test'),


    path('sign-up/', views.signup, name='signup'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('donar-list/', views.donor_list, name='donor-list'),
]
