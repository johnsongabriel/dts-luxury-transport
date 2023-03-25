from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('next/', views.part_one, name="home_pt_2"),
    path('final/', views.final, name="home_final"),
    path('confirm_booking/', views.active_booking, name="booked"),
    path('select_car/', views.select_car, name="select_car"),

    path('payment/', views.payment, name="payment"),

    path('gallery', views.galleryPage, name="gallery"),
    path('home_subcribe', views.home, name="home_subcribe"),
    path('contact', views.contact, name='contact')
]