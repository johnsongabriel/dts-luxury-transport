from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.conf import settings
from django.http import JsonResponse

from passenger.views import homePage

from .forms import RegistrationForm, UserEditForm
from .models import UserBase
from .token import account_activation_token

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import uuid
from django.conf import settings


# reset password
def password_reset_request(request):
    if request.method == "POST":
            password_reset_form = PasswordResetForm(request.POST)
            if password_reset_form.is_valid():
                data = password_reset_form.cleaned_data['email']
                associated_users = UserBase.objects.filter(Q(email=data))
                if associated_users.exists():                
                    for user in associated_users:
                        subject = "Password Reset Requested"
                        email_template_name = "user/password_reset_email.txt"
                        c = {
                            "email":user.email,
                            'domain':'127.0.0.1:8000',
                            'site_name': 'DTS Transport',
                            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                            "user": user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                        }
                        email = render_to_string(email_template_name, c)
                        message = Mail(from_email=settings.CONTACT_EMAIL,
                                        to_emails=user.email,
                                        subject=subject,
                                        html_content=email
                                        )
                        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                        response = sg.send(message)
                        print('password reset sent')
                        return redirect ("password_reset_done")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="user/password_reset.html", context={"password_reset_form":password_reset_form})



# Create your views here.
@login_required
def dashboard(request):
    users = UserBase.objects.get(user_name=request.user)
    orders = homePage(request)
    return render(request,'user/dashboard.html',{'section': 'profile','users': users,'orders': orders})

@login_required
def profile_edit(request):
    users = UserBase.objects.get(user_name=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, 'user/edit_profile.html', {'user_form': user_form, 'cars': users})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('users:profile')
    else:
        return render(request, 'user/activation_invalid.html')


def account_register(request):
    
    if request.user.is_authenticated:
        return redirect('/')


    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.user_name = registerForm.cleaned_data['user_name']
            user.first_name = registerForm.cleaned_data['first_name']
            user.last_name = registerForm.cleaned_data['last_name']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('user/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered succesfully and activation sent')
    else:
        registerForm = RegistrationForm()

    return render(request, 'user/sign_up.html', {'form': registerForm})


@login_required
def delete_user(request):
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('users:delete_confirmation')

