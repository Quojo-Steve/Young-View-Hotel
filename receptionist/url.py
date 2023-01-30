from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index),
    path('emp_login', views.emp_login),
    path('emp_dashboard', views.emp_dashboard),
    path('emp_otp', views.emp_otp),
    path('emp_register', views.emp_register),
    path('logout', views.logout),
    path('emp_rooms', views.emp_rooms),
    path('emp_room/<str:pk>', views.emp_room),
    path('emp_car/<str:pk>', views.emp_car),
    path('emp_book_room', views.emp_booking),
    path('congrats', views.congrats),
    path('checked_out', views.checked_out),
    path('emp_cars', views.emp_cars),
    path('emp_qrcode', views.emp_qrcode),
    path('emp_invoice', views.emp_invoice),
    path('invoice_details/<str:pk>', views.invoice_details),
]
