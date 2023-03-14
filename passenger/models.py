from django.db import models
from datetime import datetime
# Create your models here.

class BookingDB(models.Model):
    service_detail = models.CharField(max_length=50, blank=False)
    pick_up_date = models.DateField(auto_now=False, blank=False)
    pick_up_time = models.CharField(max_length=50,blank=False)
    number_of_passenger = models.IntegerField(blank=False)
    number_of_luggages = models.IntegerField(blank=False)
    pick_up_address = models.CharField(max_length=150, blank=False)
    drop_off_address = models.CharField(max_length=150, blank=False)

    way_point_1 = models.CharField(max_length=250, blank=True)
    way_point_2 = models.CharField(max_length=250, blank=True)

    #eazy-creator
    airline = models.CharField(max_length=200)
    flight_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.service_detail}"
