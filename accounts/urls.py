from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/login', views.LoginPage, name='Login'),
    path('accounts/signup', views.SignupPage, name='account_signup'),
    path('accounts/logout', views.LogoutPage, name='Logout'),
]
