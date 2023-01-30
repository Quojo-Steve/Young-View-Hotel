from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from .models import Room, Booking, Cars, Car_Rental
import random
import string
from datetime import date, timedelta
# Create your views here.

def index(request):
    all_rooms = Room.objects.all()
    today = date.today()

    
    for each_room in all_rooms:
        check = Booking.objects.filter(room_name=each_room.name).first()
        
        if check is not None and check.active is True: 
            print( each_room.name + str(daterange(check.arrival, check.departure)))
            dates = daterange(check.arrival, check.departure)
            
            for datey in dates:
                if datey == today:
                    each_room.availability = False
                    each_room.save()
                    print('done')
                    break 
                else:
                    each_room.availability = True
                    each_room.save()
    return render(request, 'index.html')

def emp_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('./emp_dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('./emp_login')
                
    return render(request, 'emp_login.html')


    return render(request, "emp_change_password.html")

def emp_otp(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        if User.objects.filter(username = otp).exists():
            fake = User.objects.filter(username = otp).first()
            fake.delete()
            return redirect('./emp_register')
        else:
            messages.info(request, 'No such OTP')
            return redirect('./emp_otp')
    return render(request, 'emp_otp.html')


def emp_register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username taken')
                return redirect('./emp_register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email taken')
                return redirect('./emp_register')
            else:
                User.objects.create_user(username= username, password= password, email=email, last_name= lname, first_name= fname)
                User.save
                return redirect('./emp_login')
        else:
            messages.info(request, "Passwords don't match")
            return redirect('./emp_register')
                
    return render(request, 'emp_register.html')

@login_required(login_url = './emp_login')
def emp_dashboard(request):
    all_rooms = Room.objects.all()
    today = date.today()

    
    for each_room in all_rooms:
        check = Booking.objects.filter(room_name=each_room.name).first()
        
        if check is not None and check.active is True: 
            print( each_room.name + str(daterange(check.arrival, check.departure)))
            dates = daterange(check.arrival, check.departure)
            last_date = dates[len(dates) -1]
            print(last_date)
            
            for datey in dates:
                if datey == today:
                    each_room.availability = False
                    each_room.save()
                    print('done')
                    break 
                else:
                    each_room.availability = True
                    each_room.save()
                if last_date < today:
                    each_room.availability = True
                    each_room.save()
                    check.active = False
                    check.save()
    return render(request, 'emp_dashboard.html')

@login_required(login_url = './emp_login')
def logout(request):
    auth.logout(request)
    return redirect('./')

def daterange(start, end):
    return [start + timedelta(n) for n in range(int((end - start).days))]

@login_required(login_url = './emp_login')
def emp_rooms(request):
    all_rooms = Room.objects.all()
    today = date.today()

    for each_room in all_rooms:
        check = Booking.objects.filter(room_name=each_room.name).first()
        
        if check is not None and check.active is True: 
            print( each_room.name + str(daterange(check.arrival, check.departure)))
            dates = daterange(check.arrival, check.departure)
            
            for datey in dates:
                if datey == today:
                    each_room.availability = False
                    each_room.save()
                    print('done')
                    break 
                else:
                    each_room.availability = True
                    each_room.save()
               
    return render(request, 'emp_rooms.html', {'all_rooms': all_rooms})

@login_required(login_url = './emp_login')
def emp_room(request, pk):
    room = Room.objects.get(name= pk)
    room_name = room.name
    booker = Booking.objects.filter(room_name=room_name).first()
    
    if request.method == 'POST':
        booker.active = False
        room.availability = True
        
        booker.save()
        room.save()
        
        return redirect('../emp_rooms') 
    
    return render(request, 'emp_room.html', {'room': room, 'booker':booker})

@login_required(login_url = './emp_login')
def emp_qrcode(request):
    return render(request, 'emp_qrcode.html')

@login_required(login_url = './emp_login')
def emp_booking(request):

    all_rooms = Room.objects.all()
    today = date.today()

    
    for each_room in all_rooms:
        check = Booking.objects.filter(room_name=each_room.name).first()
        
        if check is not None and check.active is True: 
            dates = daterange(check.arrival, check.departure)
            
            for datey in dates:
                if datey == today:
                    each_room.availability = False
                    each_room.save()
                    print('done')
                    break 
                else:
                    each_room.availability = True
                    each_room.save()
    
    if request.method == 'POST':
        guest_name = request.POST['gname']
        room_name = request.POST['rname']
        guest_no = request.POST['guest_no']
        adate = request.POST['adate']
        ddate = request.POST['ddate']
        pnum = request.POST['pnum']
        cards = request.POST['cards']
        idnum = request.POST['idnum']
        # paid = request.POST['paid']
        price = request.POST['price']
        booking_id = ''.join(random.choice(string.ascii_letters) for i in range(10))
        
        room_name = room_name.upper()
        
        if Room.objects.filter(name=room_name).exists():
            room = Room.objects.filter(name=room_name).first()
        else:
            messages.info(request, "no such room")
            return redirect('./emp_book_room')
        
        if room.availability is False:
            messages.info(request, "This room is taken")
            return redirect('./emp_book_room')
        
        
        room.availability = False
        room.next_booked_date = adate
        room.next_free_date = ddate
        room.save()
        
        booked = Booking.objects.create(room_name=room, booking_id=booking_id, guest_name=guest_name, no_of_guests= guest_no, arrival= adate, departure= ddate, phone_number= pnum, id_type= cards, id_number= idnum, price= price, expired=False)
        booked.save
        return redirect('./congrats')
    
    return render(request, 'emp_book_room.html')
    
@login_required(login_url = './emp_login')
def congrats(request):
    return render(request, 'emp_booking_sucess.html')
        
@login_required(login_url = './emp_login')
def checked_out(request):
    return render(request, 'emp_dashboard.html')

@login_required(login_url = './emp_login')
def emp_cars(request):
    cars = Cars.objects.all()
    
    return render(request, 'emp_cars.html', {'cars': cars})

@login_required(login_url = './emp_login')
def emp_car(request, pk):
    cars = Cars.objects.get(name= pk)
    return render(request, "emp_car.html", {"cars":cars})

@login_required(login_url = './emp_login')
def emp_invoice(request):
    all_bookings = Booking.objects.all()
    all_booking = []
    search_booking = []
    today = date.today()
    
    if request.method == 'POST':
        searched = request.POST['search']
        
        if Booking.objects.filter(booking_id=searched).exists():
            result = Booking.objects.filter(booking_id=searched).first()
        
            if result.active is True:
                
                dates = daterange(result.arrival, result.departure) 
            
                for datey in dates:
                    if datey == today:
                        search_booking.append(result)
                        
                        return render(request, 'emp_invoice.html', {"search_booking":search_booking})
        else:
            messages.info(request, 'Invalid ID')
            return redirect('./emp_invoice')

    for each in all_bookings:
        if each.active is True:
            
            dates = daterange(each.arrival, each.departure) 
        
            for datey in dates:
                if datey == today:
                    all_booking.append(each) 
    
    
    return render(request, 'emp_invoice.html', {"all_booking":all_booking})

def invoice_details(request, pk):
    booking = Booking.objects.get(booking_id=pk)
    return render(request, 'emp_invoice_details.html', {'booking':booking})
    