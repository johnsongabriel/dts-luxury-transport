from django.urls import path
from . import views

from django.contrib.auth import views as auth_views	
from django.views.generic import TemplateView

from .forms import UserLoginForm,PwdResetForm,PwdResetConfirmForm


app_name = "users"
urlpatterns = [
    
	path('sign-in/', auth_views.LoginView.as_view(template_name='user/sign_in.html', form_class=UserLoginForm), name='sign-in'),
    
    path('sign-out/', auth_views.LogoutView.as_view(next_page='/users/sign-in'), name='sign-out'),
	
	#path('account/', views.AccountView.as_view(), name="account"),
	path('profile/', views.dashboard, name="profile"),
	path('sign-up/', views.account_register, name="sign-up"),
	path('profile/edit/', views.profile_edit, name="edit_profiles"),
	path('profile/delete/', views.delete_user, name="delete_user"),
    path('profile/delete_confirm/', TemplateView.as_view(template_name="user/delete_confirm.html"), name='delete_confirmation'),
	path('activate/<slug:uidb64>/<slug:token>', views.account_activate, name="activate"),


	#path('password_reset/', auth_views.PasswordResetView.as_view(template_name="user/password_reset_form.html",success_url='password_reset_email_confirm',email_template_name='user/password_reset_email.html',form_class=PwdResetForm), name='pwdreset'),
#
	#path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',success_url='/users/password_reset_complete/', form_class=PwdResetConfirmForm),name="password_reset_confirm"),
    #path('password_reset/password_reset_email_confirm/',TemplateView.as_view(template_name="user/reset_status.html"), name='password_reset_done'),
    #path('password_reset_complete/',TemplateView.as_view(template_name="user/reset_status.html"), name='password_reset_complete'),




    # Reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="user/password_reset_form.html",
                                                                 success_url='password_reset_email_confirm',
                                                                 email_template_name='user/password_reset_email.html',
                                                                 form_class=PwdResetForm), name='pwdreset'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',
                                                                                                success_url="/users/password_reset_complete/", 
                                                                                                form_class=PwdResetConfirmForm),
         name="password_reset_confirm"),
    path('password_reset/password_reset_email_confirm/',
         TemplateView.as_view(template_name="user/reset_status.html"), name='password_reset_done'),
    path('password_reset_complete/',
         TemplateView.as_view(template_name="user/reset_status.html"), name='password_reset_complete'),


	]