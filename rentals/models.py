from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Rentals(models.Model):
	#id = models.AutoField(primary_key=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
	name = models.CharField(max_length=50, blank=False, null=False)
	car_model = models.CharField(max_length=50, blank=False, null=False)
	car_rent_img = models.ImageField(upload_to='rents/', null=False)
	car_rent_img_1 = models.ImageField(upload_to='rents/', null=False)
	car_rent_img_2 = models.ImageField(upload_to='rents/', null=False)
	car_rent_img_3= models.ImageField(upload_to='rents/', null=False)
	car_rent_img_4 = models.ImageField(upload_to='rents/', null=False)
	car_rent_img_5 = models.ImageField(upload_to='rents/', null=False)
	price = models.IntegerField()
	description = models.CharField(max_length=255, null=False, blank=False)

	is_active = models.BooleanField(default=True)

	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.name}'

	def get_absolute_url(self):
		return reverse('rentals:rents_detail', args=[self.id])

	def get_total_price(self):
		total = self.price

		return total

	class Meta:
		verbose_name = "Rents"
		ordering = ['-timestamp']
		verbose_name_plural = "Rents"


class RentForm(models.Model):
	id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
	car_id = models.CharField(max_length=60, blank=False, null=False)
	user_id = models.CharField(max_length=60, blank=False, editable=False, null=False)
	user_names = models.CharField(max_length=60, blank=False, null=False)
	email_user = models.EmailField(max_length=100, blank=False, null=False)

	hourss = models.CharField(max_length=15)
	Days = models.CharField(max_length=15)
	price = models.IntegerField()
	total = models.IntegerField(null=True, blank=True)

	car_rent_name = models.CharField(max_length=50, blank=False, null=False)
	car_rent_model = models.CharField(max_length=50, blank=False, null=False)
	date = models.DateTimeField(auto_now_add=True, editable=False)



	is_active =  models.BooleanField(default=True)
	ordered = models.BooleanField(default=False)

	def calculate_total_price_hours(self):
		total = 1
		if self.hourss == '':
			pass
		else:
			total = int(self.price) * int(self.hourss)
		return total

	def calculate_total_price_days(self):
		total = 1
		if self.Days == '':
			pass
		else:
			cal_c = int(self.Days) * 24
			total = int(self.price) * cal_c
		return total

	class Meta:
		verbose_name = "Rents Form"
		ordering = ['-date']
		verbose_name_plural = "Rents Form"

class Active_orders(models.Model):
    user_id = models.CharField(max_length=50)
    billing_status = models.BooleanField(default=False)
    order_key = models.CharField(max_length=150)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking_id 

    class Meta:
        verbose_name = "Active Orders"
        ordering = ['-date']
        verbose_name_plural = "Active Orders"