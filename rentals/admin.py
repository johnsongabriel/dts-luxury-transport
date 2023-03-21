from django.contrib import admin
from .models import Rentals, RentForm

# Register your models here.
#admin.site.register(Rentals)
#admin.site.register(RentForm)

@admin.register(Rentals)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_model','price', 'is_active']
    list_editable = ['price', 'is_active']
    list_filter = ['name', 'is_active']
    prepopulated_fields = {'name':('name',),}


@admin.register(RentForm)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['car_rent_name', 'car_rent_model', 'date']
    list_filter = ['ordered', 'is_active']
    prepopulated_fields = {'user_names': ('car_rent_model',)}