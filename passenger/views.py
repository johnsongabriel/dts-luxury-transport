from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.conf import settings
from .models import BookingDB
# Create your views here.



def homePage(request):
    if request.method == 'POST':
        service_detail = request.POST['service_details']
        pick_up_date = request.POST['pick_up_date']
        pick_up_time = request.POST['pick_up_time']
        number_of_passenger = request.POST['number_of_passenger']
        number_of_luggages = request.POST['number_of_luggages']
        pick_up_address = request.POST['google_address_a']
        drop_off_address = request.POST['google_address_b']


        way_point_1 = request.POST['google_address_c']
        way_point_2 = request.POST['google_address_d']

        airline = request.POST["airline"]
        flight_number = request.POST["flight_number"]

        if BookingDB.objects.filter(pick_up_date=pick_up_date).exists() and BookingDB.objects.filter(pick_up_time=pick_up_time).exists():
            messages.info(request, 'This Time has already been booked')
            return redirect('home')

        else:
            bookingForm = BookingDB.objects.get_or_create(
                service_detail = service_detail, 
                pick_up_date = pick_up_date,
                pick_up_time = pick_up_time, 
                number_of_passenger = number_of_passenger, 
                number_of_luggages = number_of_luggages,
                pick_up_address = pick_up_address, 
                drop_off_address = drop_off_address,
                airline = airline,
                flight_number = flight_number,


                way_point_1 = way_point_1,
                way_point_2 = way_point_2,
            )
            messages.info(request, "let's proceed")
            print('Booking saved')
            return redirect('home')
    context = {
	    "google_api_key": settings.GOOGLE_API_KEY,
        "base_country": settings.BASE_COUNTRY
        }

    return render(request, 'passenger/index.html', context)



def galleryPage(request):
    return render(request, 'passenger/gallery.html')

def car_selection(request):
    return render(request, 'passenger/select.html')

def complete_booking(request):
    return render(request, 'passenger/user_details.html')
