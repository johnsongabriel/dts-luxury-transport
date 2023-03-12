from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,SetPasswordForm)
from django.utils.translation import gettext_lazy as _

from .models import UserBase


STATUS_CHOICES = (
    ('',_('-- select --')),
    (1, _("Driver")),
    (2, _("Passenger"))
)


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'password mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'password mb-3', 'placeholder': 'Repeat New Password', 'id': 'form-new-pass2'}))

class PwdResetForm(PasswordResetForm):
    
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError('Unfortunatley we can not find that email address')
        return email

class UserLoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'password',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))



class RegistrationForm(forms.ModelForm):
    
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required',  widget=forms.TextInput(attrs={'placeholder': '*Username.'}))
    email = forms.EmailField(max_length=100, help_text='Required', widget=forms.EmailInput(attrs={'placeholder': '*Email ...'}), error_messages={'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={'placeholder': '*Type password', 'class':'password'}))
    password2 = forms.CharField( label='Repeat password',  widget=forms.PasswordInput(attrs={'placeholder': '*Repeat password', 'class': 'password'}))
    
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Your first name..'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Your last name..'}))
    is_driver = forms.ChoiceField(choices = STATUS_CHOICES, required=True)


    class Meta:
        model = UserBase
        #fields = ('user_name', 'email',)
        fields = ('user_name', 'email', 'first_name', 'last_name', 'password', 'password2','is_driver' )

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email
		


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(attrs={'class': '', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='user name', min_length=4, max_length=50, widget=forms.TextInput(attrs={'class': '', 'placeholder': 'Username', 'id':'form-firstname', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='First Name', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-lastname'}))

    last_name = forms.CharField(
        label='Last Name', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Last Name ', 'id': 'form-lastname'}))
    phone_number = forms.IntegerField(
        label='Phone number', widget=forms.NumberInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Phone number', 'id': 'form-lastname'}))
    
    car_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Car Name', 'id': 'form-lastname'}))
    #car_image = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class': '', 'placeholder': 'upload image of car', 'id': 'form-lastname'}))
    car_seats = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'placeholder': 'Number of seats'}))
    car_luggage_space = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'placeholder': 'noumber of luggage space'}))

    class Meta:
        model = UserBase
        fields = ('email', 'user_name', 'first_name','last_name', 'phone_number', 'car_name', 'car_image', 'car_seats', 'car_luggage_space')

    
    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            pass
        else:
            raise forms.ValidationError(
                'This email is not found in database')
        return email
    
    
    def clean_user_name(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            pass
        else:
            raise forms.ValidationError("Username not found")
        return user_name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True