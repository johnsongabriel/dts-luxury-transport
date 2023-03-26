from django.shortcuts import get_object_or_404, render
from .models import Rentals, RentForm, Active_orders
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
import stripe
import json
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required
def rents(request):
	#rent = Rentals.objects.all()
	rent = Rentals.objects.filter(is_active=True)
	print(rent)
	context = {'rent': rent}

	return render(request,'rentals/index.html', context) 

@login_required
def rents_det(request, id):
	product = get_object_or_404(Rentals, id=id, is_active=True)

	if request.method == "POST":
		car_ids = request.POST.get('rentNameId', None)
		Days = request.POST.get('rent_days', False)
		#price = request.POST.get('rent_price', False)
		price = product.price
		print(Days,price )
		print(car_ids)
		user_id = request.POST['rent_car_name']
		user_names = request.POST.get('rent_car_uname', False)
		email_user = request.POST.get('rent_car_email', False)
		hourss = request.POST.get('rent_hrs',False)

		car_rent_name = request.POST.get('car_user_name',False)
		car_rent_model = request.POST.get('car_name_model', False)



		RentForm.objects.get_or_create(
			car_id = car_ids, 
			user_id = user_id,
			user_names = user_names, 
			email_user = email_user,
			hourss = hourss, 
			Days = Days,
			price = price,
			car_rent_name=car_rent_name,
			car_rent_model=car_rent_model,
			)

		user_ids = request.user.id
		rrr_id = product.id

		paths = '/rentals/car_forms/' + str(rrr_id) +'/'+ str(user_ids) + '/'
		print (paths)

		return redirect(paths)

	context = {'rents': product,}
	return render(request, 'rentals/car_det.html', context )


@login_required
def proceed_rent(request, slug, user):
	product = RentForm.objects.filter(car_id=slug, user_id=request.user.id).order_by('-date').first()
	re_h = product.calculate_total_price_hours()
	re_d = product.calculate_total_price_days()
	res = re_h * re_d
	ire = res * 100
	
	if request.POST.get('action') == 'POST':
		order_key = request.POST.get('order_key')
		active = Active_orders.objects.create(order_key=order_key, booking_id=request.user.id)
	stripe.api_key = 'sk_test_51MlxVxA82DOnA7aGjkIu860CpiBrititfiqNFpWCqShjdquSvRL3NJq1Yumk5lmvMsNnE5A94zMPAinZzGISg2IU00bCF3uMPR'
	intent = stripe.PaymentIntent.create( amount=ire, currency='usd', metadata={'userid': request.user.id})
	context = {'rents': product, 'client_secret': intent.client_secret, 'res':res } #
    

	return render(request, 'rentals/rent_form.html', context)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded': #payment_intent.succeeded
        payment_confirmation(event.data.object.client_secret)

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)

def payment_confirmation(data):
    Active_orders.objects.filter(order_key=data).update(billing_status=True)

