from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('logout', views.logout),
    path('signup', views.signup),
    path('booking/<str:pk>', views.booking),
    path('ordinary', views.ordinaryRoomBooking),
    path('executive', views.executiveRoomBooking),
    path('standard', views.standardRoomBooking),
    path('generate', views.generate),
]