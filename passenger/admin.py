from django.contrib import admin
from .models import BookingDB, Subscriber, ContactFeedback, BookingDb_part2, BookngDb_final, CarsAvailable, Carselection, Active_Bookings, Active_orders

# Register your models here.
    
#admin.site.register(BookingDB)
admin.site.register(Subscriber)
admin.site.register(ContactFeedback)
#admin.site.register(BookingDb_part2)
#admin.site.register(BookngDb_final)
#admin.site.register(Carselection)


@admin.register(CarsAvailable)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'car_model','car_name','price','booked',]
    list_editable = ['price', 'booked']
    list_filter = ['booked', 'car_name']

@admin.register(Active_Bookings)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'booking_id','first_name','email','phone_number','completed']
    list_editable = ['completed']
    list_filter = ['booking_id']


@admin.register(Active_orders)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'order_key', 'billing_status']
    list_filter = ['booking_id']
