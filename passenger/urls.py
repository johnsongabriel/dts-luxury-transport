from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('gallery', views.galleryPage, name="gallery"),
    path('select_car', views.car_selection, name="select_car"),
    path('complete_booking', views.complete_booking, name="complete_booking"),
    path('terms_and_conditions', views.terms_condition, name="terms_and_conditions"),
    path('privacy', views.privacy, name="privacy"),
    path('contact', views.contact_us, name="contact"),
]