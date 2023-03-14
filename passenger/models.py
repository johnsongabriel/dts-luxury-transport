from django.db import models
from django.utils import timezone

# Create your models here.

class BookingDB(models.Model):
    #id = models.AutoField(primary_key=True)
    service_details = models.CharField(max_length=50, blank=False)
    pick_up_date = models.DateField(auto_now=False, blank=False)
    pick_up_time_hour = models.CharField(max_length=100, blank=False)
    pick_up_time_mins = models.CharField(max_length=100, blank=False)
    number_of_passenger = models.IntegerField(blank=False)
    number_of_luggages = models.IntegerField(blank=False)
    pick_up_address = models.CharField(max_length=150, null=True, blank=True)
    dropoff_address = models.CharField(max_length=150, null=True, blank=True)
    dropoff_airport = models.CharField(max_length=150, null=True, blank=True)
    pickup_airport = models.CharField(max_length=150, null=True, blank=True)
    


    way_point_1 = models.CharField(max_length=250, blank=True)
    way_point_2 = models.CharField(max_length=250, blank=True)

    #eazy-creator
    airline = models.CharField(max_length=200)
    work_hour = models.CharField(max_length=100, blank=True, null=True)
    flight_number = models.IntegerField(blank=True)

    # Personal Information
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    phone_number = models.IntegerField()
    email = models.EmailField(blank=False)
    
    def __str__(self):
        return f"{self.service_detail} | {self.pick_up_date} | {self.first_name}:{self.last_name}"
    


#newsletter and subcriber
class Subcriber(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.email


#Contact/Feedback Model
class ContactFeedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=False)
    message = models.TextField(max_length=400)
    date_created = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return f"Name: {self.name} | Contact On: {self.date_created}"