from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('gallery', views.galleryPage, name="gallery"),
    path('home_subcribe', views.home, name="home_subcribe"),
    path('select_car', views.car_selection, name="select_car"),
    path('complete_booking', views.complete_booking, name="complete_booking"),
    path('contact', views.contact, name='contact')
]