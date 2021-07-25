from accounts.forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.template import RequestContext

# Create your views here.


def LoginPage(request):
    return render(request, 'login.html')


def SignupPage(request):
    return render(request, 'signup.html')


def LogoutPage(request):
    return render(request, 'logout.html')
