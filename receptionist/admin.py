from django.contrib import admin
from .models import Room, Booking, Cars, Car_Rental, Collective_Room

# Register your models here.

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Cars)
admin.site.register(Car_Rental) 
admin.site.register(Collective_Room) 
