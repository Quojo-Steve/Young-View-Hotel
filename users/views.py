from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from receptionist.models import Collective_Room, Room, Booking
from receptionist.views import daterange
from datetime import date
import datetime
import random
import string

# Create your views here.
def index(request):
    rooms = Collective_Room.objects.all()
    return render(request, 'user_main.html', {'rooms':rooms})

def login(request):        
    if request.method == 'POST':
        email2 = request.POST['email2']
        password2 = request.POST['pswd2']
        
        if User.objects.filter(email=email2).exists():
            logger = User.objects.filter(email=email2).first()
            username2 = logger.username
            user = auth.authenticate(username = username2, password = password2)
    
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('/login')
            
    return render(request, 'user_login.html')

@login_required(login_url='./login')
def logout(request):
    auth.logout(request)
    return redirect('/login')

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = fname+' '+lname
        password = request.POST['pswd']
        password2 = request.POST['pswd2']
        if password != password2:
            messages.info(request, 'Passwords don\'t match')
            return redirect('/signup')
        elif User.objects.filter(username = username).exists():
            messages.info(request, 'Username taken')
            return redirect('/signup')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'Email taken')
            return redirect('/signup')
        else:
            User.objects.create_user(username= username, password= password, email=email, last_name= lname, first_name= fname)
            User.save
            messages.info(request, 'Now login please')
            return redirect('/login')
    return render(request, 'user_signup.html')

def booking(request, pk):
    if pk == 'Ordinary':
        return redirect('/ordinary')
    if pk == 'Executive':
        return redirect('/executive')
    if pk == 'Standard':
        return redirect('/standard')
    return render(request, 'user_book_room.html')

@login_required(login_url='./login')
def standardRoomBooking(request):
    
    if request.method == 'POST':
        arrival = request.POST['arrival']
        departure = request.POST['dep']
        guest = request.POST['guest']
        number = request.POST['num']
        price = request.POST['price']
        room_chosen = request.POST['rooms']
        
        books = Booking.objects.filter(room_name=room_chosen, expired=False)
        room = Room.objects.get(name=room_chosen)
        
        arrival_date = arrival.split('-')
        departure_date = departure.split('-')
            
        a_date = datetime.date(int(arrival_date[0]), int(arrival_date[1]), int(arrival_date[2]))
        d_date = datetime.date(int(departure_date[0]), int(departure_date[1]), int(departure_date[2]))
        
        if len(books) > 0:
            for book in books:
                dates = daterange(book.arrival, book.departure)
                
                new_dates = daterange(a_date, d_date)
                print(new_dates)
                i=1
                stop = False
                while i == 1:    
                    for dat in dates:
                        for new_date in new_dates:
                            if dat == new_date:
                                print('bad')
                                i=0
                                messages.info(request, str(room_chosen) +' is not available on the selected dates')
                                return redirect('/standard')
                            else:
                                i=10
                                stop = True
                        if i == 0:
                            break
                        
                if dates is None:
                    print('ohno')
                    stop = True
                
                if stop:
                    booking_id = ''.join(random.choice(string.ascii_letters) for i in range(10))
                    print(booking_id)
                    new_booking = Booking.objects.create(room_name=room, guest_name=request.user, arrival=arrival, departure=departure, price=price, expired=False, no_of_guests=guest, booking_id=booking_id, phone_number=number)
                    new_booking.save
                    return render(request, 'user_generate_qr.html', {'name':new_booking})
        else:
            booking_id = ''.join(random.choice(string.ascii_letters) for i in range(10))
            print(booking_id)
            new_booking = Booking.objects.create(room_name=room, guest_name=request.user, arrival=arrival, departure=departure, price=price, expired=False, no_of_guests=guest, booking_id=booking_id, phone_number=number)
            new_booking.save
            return render(request, 'user_generate_qr.html', {'name':new_booking})
        
    return render(request, 'user_book_room_stan.html')

@login_required(login_url='./login')
def ordinaryRoomBooking(request):
    # rooms = Room.objects.filter(grade='Ordinary')
    if request.method == 'POST':
        arrival = request.POST['arrival']
        departure = request.POST['dep']
        guest = request.POST['guest']
        number = request.POST['num']
        price = request.POST['price']
        room_chosen = request.POST['rooms']
        
        books = Booking.objects.filter(room_name=room_chosen, expired=False)
        room = Room.objects.get(name=room_chosen)
        
        arrival_date = arrival.split('-')
        departure_date = departure.split('-')
            
        a_date = datetime.date(int(arrival_date[0]), int(arrival_date[1]), int(arrival_date[2]))
        d_date = datetime.date(int(departure_date[0]), int(departure_date[1]), int(departure_date[2]))
        
        if len(books) > 0:
            for book in books:
                dates = daterange(book.arrival, book.departure)
                
                new_dates = daterange(a_date, d_date)
                print(new_dates)
                i=1
                stop = False
                while i == 1:    
                    for dat in dates:
                        for new_date in new_dates:
                            if dat == new_date:
                                print('bad')
                                i=0
                                messages.info(request, str(room_chosen) +' is not available on the selected dates')
                                return redirect('/ordinary')
                            else:
                                i=10
                                stop = True
                        if i == 0:
                            break
                        
                if dates is None:
                    print('ohno')
                    stop = True
                
                if stop:
                    booking_id = ''.join(random.choice(string.ascii_letters) for i in range(10))
                    print(booking_id)
                    new_booking = Booking.objects.create(room_name=room, guest_name=request.user, arrival=arrival, departure=departure, price=price, expired=False, no_of_guests=guest, booking_id=booking_id, phone_number=number)
                    new_booking.save
                    return render(request, 'user_generate_qr.html', {'name':new_booking})                
        else:
            booking_id = ''.join(random.choice(string.ascii_letters) for i in range(10))
            print(booking_id)
            new_booking = Booking.objects.create(room_name=room, guest_name=request.user, arrival=arrival, departure=departure, price=price, expired=False, no_of_guests=guest, booking_id=booking_id, phone_number=number)
            new_booking.save
            return render(request, 'user_generate_qr.html', {'name':new_booking})
        
    return render(request, 'user_book_room_ord.html')

@login_required(login_url='./login')
def executiveRoomBooking(request):
    if request.method == 'POST':
        arrival = request.POST['arrival']
        departure = request.POST['dep']
        guest = request.POST['guest']
        number = request.POST['num']
        price = request.POST['price']
        room_chosen = request.POST['rooms']
        
        books = Booking.objects.filter(room_name=room_chosen, expired=False)
        room = Room.objects.get(name=room_chosen)
        
        arrival_date = arrival.split('-')
        departure_date = departure.split('-')
            
        a_date = datetime.date(int(arrival_date[0]), int(arrival_date[1]), int(arrival_date[2]))
        d_date = datetime.date(int(departure_date[0]), int(departure_date[1]), int(departure_date[2]))
        
        if len(books) > 0:
            for book in books:
                dates = daterange(book.arrival, book.departure)
                
                new_dates = daterange(a_date, d_date)
                print(new_dates)
                i=1
                stop = False
                while i == 1:    
                    for dat in dates:
                        for new_date in new_dates:
                            if dat == new_date:
                                print('bad')
                                i=0
                                messages.info(request, str(room_chosen) +' is not available on the selected dates')
                                return redirect('/executive')
                            else:
                                i=10
                                stop = True
                        if i == 0:
                            break
                        
                if dates is None:
                    print('ohno')
                    stop = True
                
                if stop:
                    booking_id = ''.join(random.choice(string.ascii_letters) for i in range(10))
                    print(booking_id)
                    new_booking = Booking.objects.create(room_name=room, guest_name=request.user, arrival=arrival, departure=departure, price=price, expired=False, no_of_guests=guest, booking_id=booking_id, phone_number=number)
                    new_booking.save
                    return render(request, 'user_generate_qr.html', {'name':new_booking})
                
        else:
            booking_id = ''.join(random.choice(string.ascii_letters) for i in range(10))
            print(booking_id)
            new_booking = Booking.objects.create(room_name=room, guest_name=request.user, arrival=arrival, departure=departure, price=price, expired=False, no_of_guests=guest, booking_id=booking_id, phone_number=number)
            new_booking.save
            return render(request, 'user_generate_qr.html', {'name':new_booking})
        
    return render(request, 'user_book_room_exec.html')

def generate(request):
    return render(request, 'user_generate_qr.html')