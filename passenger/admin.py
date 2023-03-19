from django.contrib import admin
from .models import BookingDB, Subscriber, ContactFeedback

# Register your models here.
    
admin.site.register(BookingDB)
admin.site.register(Subscriber)
admin.site.register(ContactFeedback)
