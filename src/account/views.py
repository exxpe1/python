from django.contrib.auth import views
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from . import forms


def login_view(request):
    template_name ='account/login.html'
    if request.method == 'GET':
        login_form = forms.LoginForm()
        return render(
            request,
            template_name=template_name, context={'form':login_form}        )
    elif request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('catalog'))
        else:
            return render(
            request,
            template_name=template_name, context={'form':login_form}        )

class MyLoginView(views.LoginView):
    template_name = 'account/login.html'