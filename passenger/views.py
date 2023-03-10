from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import BookingDB, Subcriber #, PersonalInfoBooking

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.



def homePage(request):
    if request.method == 'POST':
        # if request.POST.get("form_type") == 'home_form_add':
        service_detail = request.POST['service_details']
        pick_up_date = request.POST['pick_up_date']
        pick_up_time_hour = request.POST['hour']
        pick_up_time_mins = request.POST['mins']
        number_of_passenger = request.POST['number_of_passenger']
        number_of_luggages = request.POST['number_of_luggages']
        pick_up_address = request.POST['google_address_a']
        drop_off_address = request.POST['google_address_b']
        work_hour = request.POST['work_hour']


        way_point_1 = request.POST['google_address_c']
        way_point_2 = request.POST['google_address_d']

        work_hour = request.POST['work_hour']

        airline = request.POST["airline"]
        flight_number = request.POST["flight_number"]

        if BookingDB.objects.filter(pick_up_date=pick_up_date).exists() and BookingDB.objects.filter(pick_up_time_hour=pick_up_time_hour).exists() and BookingDB.objects.filter(pick_up_time_mins=pick_up_time_mins).exists():
            messages.info(request, 'This Time has already been booked')
            return redirect('home')

        else:
            bookingForm = BookingDB.objects.get_or_create(
                service_detail = service_detail, 
                pick_up_date = pick_up_date,
                pick_up_time_hour = pick_up_time_hour, 
                pick_up_time_mins = pick_up_time_mins,
                number_of_passenger = number_of_passenger, 
                number_of_luggages = number_of_luggages,
                pick_up_address = pick_up_address, 
                drop_off_address = drop_off_address,
                airline = airline,
                work_hour = work_hour,
                flight_number = flight_number,


                way_point_1 = way_point_1,
                way_point_2 = way_point_2,
            )
            messages.info(request, "let's proceed")
            print('Booking saved')
            return redirect('complete_booking')
        
    context = {
	    "google_api_key": settings.GOOGLE_API_KEY,
        "base_country": settings.BASE_COUNTRY
        }
    return render(request, 'passenger/index.html', context)






def car_selection(request):
    return render(request, 'passenger/select.html')




def complete_booking(request):
    # if request.method == "POST":
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     phone_number = request.POST['phone_number']
    #     email = request.POST['email']

    
    #     completeBooking = PersonalInfoBooking.objects.get_or_create(
    #         first_name = first_name,
    #         last_name = last_name,
    #         phone_number = phone_number,
    #         email = email
    #     )
    #     #messages.info(request, "let's proceed")
    #     print('Booking Placed')
    return render(request, 'passenger/user_details.html')



#subcriber logic for newsletter
def home(request):
    if request.method == "POST":
        #if request.POST.get("form_type") == 'subcribe_form':
        email = request.POST['email']

        # if get_user_model().objects.filter(email=email).first():
        #     messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
        #     return redirect('/')

        if Subcriber.objects.filter(email=email).first():
            messages.error(request, f'{email} is already a subcriber')
            return redirect('home_subcribe')
        
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            print('Error')
            return redirect("home_subcribe")
        
        subcriber = Subcriber.objects.get_or_create(email=email)
        messages.success(request, f'{email} successfully subscribed to our newsletter!')
        print('succesfull')
        return redirect('home_subcribe')
    return render(request, 'home.html')



def galleryPage(request):
    return render(request, 'passenger/gallery.html')
