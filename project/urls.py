from django.urls import path
from . import views

urlpatterns = [

    path('test/', views.test, name='test'),


    path('sign-up/', views.signup, name='signup'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('profile/', views.profile, name='profile'),
    path('donation-status/', views.donation_status, name='donation-status'),
    path('update-profile/', views.update_profile, name='update-profile'),

    path('donar-list/', views.donor_list, name='donor-list'),
    path('news-feed/', views.news_feed, name='news-feed'),
]
