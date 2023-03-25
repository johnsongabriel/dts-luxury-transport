from django.db import models
from django.utils import timezone
import uuid



# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
# Create your models here.

class LongUUIDField(models.UUIDField):
    default_uuid_length = 64

    def __init__(self, *args, **kwargs):
        super().__init__(default=uuid.uuid4, *args, **kwargs)

    def db_type(self, connection):
        return 'char({})'.format(self.default_uuid_length)

class CarsAvailable(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False,)
    car_name = models.CharField(null=False, max_length=100)
    car_model = models.CharField(null=False, max_length=100)
    car_image = models.ImageField(upload_to='images/cars/',default='default.jpg')
    car_seats = models.IntegerField(blank=False, null=False)
    car_luggage_space = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(default=00000)
    booked = models.BooleanField(default=False)

    boking_per_hour = models.IntegerField()

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = "Cars Available"
        verbose_name_plural = "Cars Available"
    
class Carselection(models.Model):
    car_id = models.CharField(max_length=100)
    booking_id = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking_id

    class Meta:
        verbose_name = "Booking Cars"
        ordering = ['-date']
        verbose_name_plural = "Booking Cars"

class BookingDB(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False,)
    booking_id = models.CharField(unique=True, null=False, blank=False, max_length=200)
    service_details = models.CharField(max_length=50, blank=False)
    pick_up_date = models.DateField(auto_now=False, blank=False)
    pick_up_time = models.TimeField(max_length=100, blank=False)
    number_of_passenger = models.IntegerField(blank=False)
    number_of_luggages = models.IntegerField(blank=False)

    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.service_details} | {self.pick_up_date} |"
    
    class Meta:
        verbose_name = "booking_part1"
        ordering = ['-date']
        verbose_name_plural = "booking_part1"


class BookingDb_part2(models.Model):
    pick_up_address = models.CharField(max_length=150, null=True, blank=True)
    dropoff_address = models.CharField(max_length=150, null=True, blank=True)
    dropoff_airport = models.CharField(max_length=150, null=True, blank=True)
    pickup_airport = models.CharField(max_length=150, null=True, blank=True)
    distance = models.CharField(max_length=150, null=True)
    airline = models.CharField(max_length=200)
    work_hour = models.CharField(max_length=100, blank=True, null=True)
    flight_number = models.CharField(max_length=200, blank=True, null=True)

    date = models.DateTimeField(auto_now_add=True)
    booking_id = models.CharField( null=False, blank=False, max_length=200)


    def __str__(self):
        return f"{self.pick_up_address} | {self.pickup_airport}:{self.work_hour}"

    class Meta:
        verbose_name = "booking_part2"
        ordering = ['-date']
        verbose_name_plural = "booking_part2"



class Active_Bookings(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False,)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    phone_number = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    service_details = models.CharField(max_length=50, blank=False)
    pick_up_date = models.DateField(auto_now=False, blank=False)
    pick_up_time = models.TimeField(max_length=100, blank=False)
    number_of_passenger = models.IntegerField(blank=False)
    number_of_luggages = models.IntegerField(blank=False)
    pick_up_address = models.CharField(max_length=150, null=True, blank=True)
    dropoff_address = models.CharField(max_length=150, null=True, blank=True)
    dropoff_airport = models.CharField(max_length=150, null=True, blank=True)
    pickup_airport = models.CharField(max_length=150, null=True, blank=True)
    distance = models.CharField(max_length=150, null=True)
    airline = models.CharField(max_length=200)
    work_hour = models.CharField(max_length=100, blank=True, null=True)
    flight_number = models.CharField(max_length=200, blank=True, null=True)
    car_name = models.CharField(null=True, max_length=100)
    car_model = models.CharField(null=False, max_length=100)
    payment = models.CharField(null=False, max_length=25)
    boking_per_hour = models.CharField(null=True, max_length= 10)
    price = models.CharField(null=True, max_length= 10)

    completed = models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=True)
    booking_id = models.CharField( null=False, blank=False, max_length=200)

    def __str__(self):
        return f"{self.booking_id} | {self.first_name}:{self.email}"
    
    def calculate_total_book_hrs(self):
        total = 1
        if self.work_hour == 'False':
            total = int(self.price)
        else:
            total = int(self.price) * int(self.boking_per_hour)
        return total
    

    class Meta:
        verbose_name = "Active Booking"
        ordering = ['-date']
        verbose_name_plural = "Active Booking"



class BookngDb_final(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    phone_number = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)


    date = models.DateTimeField(auto_now_add=True)
    booking_id = models.CharField( null=False, blank=False, max_length=200)

    def __str__(self):
        return f"{self.first_name} | {self.last_name}:{self.email}"

    class Meta:
        verbose_name = "booking_final"
        ordering = ['-date']
        verbose_name_plural = "booking_final"




#newsletter and subcriber
class Subscriber(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    confirmed = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.email


class Newsletter(models.Model):
    pass

#Contact/Feedback Model
class ContactFeedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=False)
    message = models.TextField(max_length=400)
    date_created = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return f"Name: {self.name} | Contact On: {self.date_created}"