from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import BookingDB, Subscriber, ContactFeedback
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# Create your views here.



def homePage(request):
    if request.method == "POST":
        service_details = request.POST['service_details']
        pick_up_date = request.POST['pick_up_date']
        pick_up_time_hour = request.POST['pick_up_time_hour']
        pick_up_time_mins = request.POST['pick_up_time_mins']
        number_of_passenger = request.POST['number_of_passenger']
        number_of_luggages = request.POST['number_of_luggages']
        pick_up_address = request.POST['google_address_a']
        dropoff_address = request.POST['google_address_b']
        pickup_airport = request.POST['pickup_airport']
        dropoff_airport = request.POST['dropoff_airport']
        distance = request.POST['distance']


        # way_point_1 = request.POST['google_address_c']
        # way_point_2 = request.POST['google_address_d']


        airline = request.POST["airline"]
        #work_hour = request.POST["work_hour", False]
        work_hour = request.POST.get('work_hour', False)
        flight_number = request.POST.get('flight_number', False)

        if BookingDB.objects.filter(pick_up_date=pick_up_date).exists() and BookingDB.objects.filter(pick_up_time_hour=pick_up_time_hour).exists() and BookingDB.objects.filter(pick_up_time_mins=pick_up_time_mins).exists():
            messages.info(request, 'This Time has already been booked')
            return redirect('home')

        else:
            bookingForm = BookingDB.objects.get_or_create(
                service_details = service_details, 
                pick_up_date = pick_up_date,
                pick_up_time_hour = pick_up_time_hour, 
                pick_up_time_mins = pick_up_time_mins,
                number_of_passenger = number_of_passenger, 
                number_of_luggages = number_of_luggages,
                pick_up_address = pick_up_address, 
                dropoff_address = dropoff_address,
                pickup_airport = pickup_airport,
                dropoff_airport = dropoff_airport,
                distance = distance,
                airline = airline,
                work_hour = work_hour,
                flight_number = flight_number,


                # way_point_1 = way_point_1,
                # way_point_2 = way_point_2,
            )
            messages.info(request, "let's proceed")
            print('Booking saved')
            return redirect('home')
        
    context = {
	    "google_api_key": settings.GOOGLE_API_KEY,
        "base_country": settings.BASE_COUNTRY
        }
    return render(request, 'passenger/index.html', context)



def car_selection(request):
    return render(request, 'passenger/select.html')



#subcriber logic for newsletter
# Helper Functions
def home(request):
    if request.method == "POST":
        #get the email from the input field
        email = request.POST['email']

        #if already a subcriber dont notify and dont safe
        if Subscriber.objects.filter(email=email).first():
            messages.error(request, f'{email} is already a subcriber')
            return redirect('home_subcribe')
        
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            print('Error')
            return redirect("home_subcribe")
        
        #if pass all condition save to the database
        subcriber,_ = Subscriber.objects.get_or_create(email=email)
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=[subcriber.email],
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for our email newsletter!'
            )
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print('successful')
        return render(request, 'home.html', {'email': subcriber.email, 'action': 'added'})
        # return redirect('home_subcribe')
    return render(request, 'home.html')



#Logic for contact form
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact,_ = ContactFeedback.objects.get_or_create(
            name=name,
            email=email,
            message=message
        )
        email_subject = f"New Contact: {contact.name}: {contact.email}"
        email_message = contact.message
        message = Mail(
            from_email=settings.CONTACT_EMAIL,
            to_emails=settings.ADMIN_EMAILS,
            subject=email_subject,
            html_content=email_message
        )
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print('thanks for contacting us')
        return redirect('contact')
    return render(request, 'passenger/contact.html')


def galleryPage(request):
    return render(request, 'passenger/gallery.html')
