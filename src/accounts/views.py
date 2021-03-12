  
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import views


class UserLoginView(views.LoginView):
    template_name = 'accounts/login.html'


class UserLogoutView(views.LogoutView):
    pass