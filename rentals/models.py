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

	def calculate_total_ones(self):
		if self.Days and not self.hourss:
			con_v = int(self.Days) * 24
			total = self.price * con_v
		elif self.hourss != '' and self.Days == '':
			total = int(self.hourss) * self.price

			return total

	def calculate_total(self):
		if isinstance(self.price, str):
			self.price = int(self.price)
		if not isinstance(self.Days, str):
			self.Days = ''
			self.Days = str(self.Days)
		if not isinstance(self.hourss, str):
			self.hourss = str(self.hourss)
			self.hourss = ''
		if isinstance(self.Days, str):
			if self.Days == '':
				self.Days = '1'
			else:
				self.Days = int(self.Days)
			self.Days = int(self.Days) * 24
			total = self.Days * self.price
		if isinstance(self.hourss, str):
			if self.hourss == '':
				self.hourss = '1'
			else:
				self.hourss = int(self.hourss)
			total = self.hourss * self.price
		return total

	def calculate_total_one(self):
		if isinstance(self.price, str):
			self.price = int(self.price)
		if isinstance(self.Days, str):
			self.Days = int(self.Days) if self.Days else 0
		if isinstance(self.hourss, str):
			self.hourss = int(self.hourss) if self.hourss else 0
		if self.Days and not self.hourss:
			total = self.Days * self.price
		elif self.hourss and not self.Days:
			total = self.hourss * self.price
		else:
			total = 0
		return total

	def get_total_price(self):
		tota = self.price
		total = int(tota)
		return total

	def get_hours(self):
		hours = self.hourss
		return hours

	def dayes(self):
		daay = self.Days
		return daay

	class Meta:
		verbose_name = "Rents Form"
		ordering = ['-date']
		verbose_name_plural = "Rents Form"