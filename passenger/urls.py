from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('gallery', views.galleryPage, name="gallery"),
    path('select_car', views.car_selection, name="select_car"),
    path('complete_booking', views.complete_booking, name="complete_booking"),
]