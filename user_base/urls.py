from django.urls import path
from . import views

from django.contrib.auth import views as auth_views	
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm #,PwdResetForm,PwdResetConfirmForm


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
    path("password_reset", views.password_reset_request, name="password_reset"),
]