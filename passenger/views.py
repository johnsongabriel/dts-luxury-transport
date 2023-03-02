from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from .models import BookingDB
# Create your views here.



def homePage(request):
    if request.method == 'POST':
        service_detail = request.POST['service_details']
        pick_up_date = request.POST['pick_up_date']
        pick_up_time = request.POST['pick_up_time']
        number_of_passenger = request.POST['number_of_passenger']
        number_of_luggages = request.POST['number_of_luggages']
        pick_up_address = request.POST['pick_up_address']
        drop_off_address = request.POST['drop_off_address']

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
                drop_off_address = drop_off_address
            )
            print('Booking saved')
            return redirect('home')

    return render(request, 'passenger/index.html')



def galleryPage(request):
    return render(request, 'passenger/gallery.html')

