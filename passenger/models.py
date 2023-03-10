from django.db import models
from django.utils import timezone

# Create your models here.

class BookingDB(models.Model):
    #id = models.AutoField(primary_key=True)
    service_detail = models.CharField(max_length=50, blank=False)
    pick_up_date = models.DateField(auto_now=False, blank=False)
    pick_up_time_hour = models.CharField(max_length=100, blank=False)
    pick_up_time_mins = models.CharField(max_length=100, blank=False)
    number_of_passenger = models.IntegerField(blank=False)
    number_of_luggages = models.IntegerField(blank=False)
    pick_up_address = models.CharField(max_length=150, blank=False)
    drop_off_address = models.CharField(max_length=150, blank=False)

    way_point_1 = models.CharField(max_length=250, blank=True)
    way_point_2 = models.CharField(max_length=250, blank=True)

    #eazy-creator
    airline = models.CharField(max_length=200)
    work_hour = models.CharField(max_length=100, blank=False)
    flight_number = models.IntegerField()

    # class Meta:
    #     db_table = "BookingDB"
    
    def __str__(self):
        return f"{self.service_detail} | {self.pick_up_date} | {self.pick_up_time_hour}:{self.pick_up_time_mins}"
    

# class PersonalInfoBooking(BookingDB):
#     first_name = models.CharField(max_length=200, blank=False)
#     last_name = models.CharField(max_length=200, blank=False)
#     phone_number = models.IntegerField()
#     email = models.EmailField(blank=False)

# class PersonalInfoBooking(models.Model):
#     id = models.AutoField(primary_key=True)
#     booking = models.OneToOneField(BookingDB, on_delete=models.CASCADE, parent_link=True)
#     first_name = models.CharField(max_length=200, blank=False)
#     last_name = models.CharField(max_length=200, blank=False)
#     phone_number = models.IntegerField()
#     email = models.EmailField(blank=False)

#     class Meta:
#         db_table = "PersonalInfoBooking"

#     def __str__(self):
#         return self.first_name



#newsletter and subcriber
class Subcriber(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.email