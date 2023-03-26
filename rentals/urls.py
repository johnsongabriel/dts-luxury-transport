from django.urls import path, re_path
from . import views


app_name = "rentals"
urlpatterns = [
	path('cars_for_rents/', views.rents, name="rents"), #rents_detail
	path('webhook/', views.stripe_webhook), #rents_detail
	#path('car_forms/<slug:car_id>/<slug:user_id>/', views.proceed_rent, name='proceed_payment'), 
	path('cars_details/<slug:id>', views.rents_det, name="rents_detail"), 
	re_path(r'^car_forms/(?P<slug>[\w-]+)/(?P<user>[\w-]+)/$',views.proceed_rent, name="proceed_payment"),
]