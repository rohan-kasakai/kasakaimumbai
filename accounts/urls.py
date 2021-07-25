from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/login', views.LoginPage, name='Login'),
    path('accounts/signup', views.SignupPage, name='Signup'),
    path('accounts/logout', views.LogoutPage, name='Logout'),
]
