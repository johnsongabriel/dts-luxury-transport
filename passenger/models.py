from django.db import models
from datetime import datetime
# Create your models here.

class BookingDB(models.Model):
    service_detail = models.CharField(max_length=50)
    pick_up_date = models.DateField(auto_now=False, blank=False)
    pick_up_time = models.TimeField(auto_now=False, blank=False)
    number_of_passenger = models.IntegerField()
    number_of_luggages = models.IntegerField()
    pick_up_address = models.CharField(max_length=100)
    drop_off_address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.service_detail}"
