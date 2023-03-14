from django.contrib import admin
from .models import BookingDB, Subcriber, ContactFeedback #, PersonalInfoBooking

# Register your models here.
admin.site.register(BookingDB)
admin.site.register(Subcriber)
admin.site.register(ContactFeedback)
#admin.site.register(PersonalInfoooking)
