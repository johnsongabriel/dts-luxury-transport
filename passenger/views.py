from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .models import BookingDB, Subscriber, ContactFeedback, BookingDb_part2, BookngDb_final, CarsAvailable, Active_Bookings, Carselection
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import uuid
import stripe
# Create your views here.



def homePage(request):
    if request.method == "POST":
        service_details = request.POST['service_details']
        pick_up_date = request.POST['pick_up_date']
        pick_up_time_hour = request.POST['pick_up_time']
        number_of_passenger = request.POST['number_of_passenger']
        number_of_luggages = request.POST['number_of_luggages']
        

        session_uuid = uuid.uuid4()
        booking_id = session_uuid
        
        request.session['booking_id'] = str(booking_id)
        print(booking_id)
        r = request.session.get('booking_id')
        print(r)


        #
        bookingForm = BookingDB.objects.get_or_create(
            service_details = service_details, 
            pick_up_date = pick_up_date,
            pick_up_time = pick_up_time_hour,
            number_of_passenger = number_of_passenger, 
            number_of_luggages = number_of_luggages,
            booking_id = booking_id
        )
        messages.info(request, "let's proceed")
        print('Booking saved')

        

        paths = '/select_car/'
        print (paths)
        return redirect(paths)
        
    context = {
	    "google_api_key": settings.GOOGLE_API_KEY,
        "base_country": settings.BASE_COUNTRY
        }
    return render(request, 'passenger/index.html', context)

def part_one(request):
    s = request.session.get('booking_id')
    product = BookingDB.objects.filter(booking_id=s).order_by('-date').first()
    car_available = CarsAvailable.objects.filter(booked=False )
    #product = get_object_or_404(BookingDB, booking_id=s,).order_by('-date').first()
    if request.method == "POST":
        pick_up_address = request.POST.get('pick_up_address', False)
        dropoff_address = request.POST.get('google_address_b', False)
        pickup_airport = request.POST.get('pickup_airport',False)
        dropoff_airport = request.POST.get('dropoff_airport', False)
        distance = request.POST.get('distance', False)
        airline = request.POST.get("airline", False)
        work_hour = request.POST.get('work_hour', False)
        flight_number = request.POST.get('flight_number', False)
        booking_id = s


        BookingDb_part2.objects.get_or_create( pick_up_address = pick_up_address, 
                dropoff_address = dropoff_address,
                pickup_airport = pickup_airport,
                dropoff_airport = dropoff_airport,
                distance = distance,
                airline = airline,
                work_hour = work_hour,
                flight_number = flight_number,
                booking_id=booking_id)


        paths = '/final/'
        print (paths)
        return redirect(paths)
        
        

    context = {'books_p': product, 'car_a': car_available, 's':s}
    return render(request, 'passenger/select.html', context)
        

def final(request):
    s = request.session.get('booking_id')
    product = BookingDb_part2.objects.filter(booking_id=s).order_by('-date').first()
    print(product)
    
    print(product.booking_id)
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']

        booking_id = s


        BookngDb_final.objects.get_or_create(
                first_name = first_name,
                last_name = last_name,
                phone_number = phone_number,
                email = email,
                booking_id = booking_id
                ) #confirm_booking
        
        paths = '/confirm_booking/'
        print (paths)
        return redirect(paths)
    context = {'user_det': product}
    return render(request, 'passenger/user_details.html', context)


def select_car(request):
    s = request.session.get('booking_id')
    c = CarsAvailable.objects.filter(booked=False)

    if request.method == 'POST':
        car_id = request.POST['car_id']
        booking_id = s

        Carselection.objects.get_or_create(
            car_id = car_id,
            booking_id = booking_id
        )

        paths = '/next/'
        print (paths)
        return redirect(paths)


    context = {'c': c}
    return render(request, 'passenger/select_car.html', context)


        


def active_booking(request):
    s = request.session.get('booking_id')
    part_one =  BookingDB.objects.filter(booking_id=s).order_by('-date').first()
    part_two =  BookingDb_part2.objects.filter(booking_id=s).order_by('-date').first()
    part_three =  BookngDb_final.objects.filter(booking_id=s).order_by('-date').first()
    car_s = Carselection.objects.filter(booking_id=s).order_by('-date').first()
    car_a = CarsAvailable.objects.filter(id=car_s.car_id).first()


    if request.method == 'POST':
        first_name = part_three.first_name
        last_name = part_three.last_name
        phone_number = part_three.phone_number
        email = part_three.email
        service_details = part_one.service_details
        pick_up_date = part_one.pick_up_date
        pick_up_time = part_one.pick_up_time
        number_of_passenger = part_one.number_of_passenger
        number_of_luggages = part_one.number_of_luggages
        pick_up_address = part_two.pick_up_address
        dropoff_address = part_two.dropoff_address
        dropoff_airport = part_two.dropoff_airport
        pickup_airport = part_two.pickup_airport
        distance = part_two.distance
        work_hour = part_two.work_hour
        flight_number = part_two.flight_number
        car_name = car_a.car_name
        boking_per_hour = car_a.boking_per_hour
        price = car_a.price
        payment = request.POST['payment']
        print(car_name)
        car_model = car_a.car_model

        booking_id = s

        Active_Bookings.objects.get_or_create(
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            email = email,
            service_details = service_details,
            pick_up_date = pick_up_date,
            pick_up_time = pick_up_time,
            number_of_passenger = number_of_passenger,
            number_of_luggages = number_of_luggages,
            pick_up_address = pick_up_address,
            dropoff_address = dropoff_address,
            dropoff_airport = dropoff_airport,
            pickup_airport = pickup_airport,
            distance = distance,
            work_hour = work_hour,
            flight_number = flight_number,
            car_name = car_name,
            car_model = car_model,
            payment = payment,
            boking_per_hour = boking_per_hour,
            price = price,

            booking_id = booking_id
            
        )

        paths = '/payment/'
        print (paths)
        return redirect(paths)
    
    context = {'p1': part_one, 'p2': part_two, 'p3': part_three, 'ca': car_a}
    return render(request, 'passenger/overview.html', context)


def payment(request):
    s = request.session.get('booking_id')
    active_p =  Active_Bookings.objects.filter(booking_id=s).order_by('-date').first()
    ire = active_p.calculate_total_book_hrs()
    print(ire)
    print(type(ire))

    res = ire * 100


    stripe.api_key = 'sk_test_51MlxVxA82DOnA7aGjkIu860CpiBrititfiqNFpWCqShjdquSvRL3NJq1Yumk5lmvMsNnE5A94zMPAinZzGISg2IU00bCF3uMPR'
    intent = stripe.PaymentIntent.create( amount=res, currency='usd', metadata={'userid': request.user.id})
    context = {'rents': active_p, 'client_secret': intent.client_secret, 'ire':ire} #
    
    return render(request, 'rentals/book_form.html', context)



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
        return render(request, 'passenger/index.html', {'email': subcriber.email, 'action': 'added'})
        # return redirect('home_subcribe')
    return render(request, 'passenger/index.html')



#Logic for contact form
def contact(request):
    r = request.session.get('booking_id')
    print(r)
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
