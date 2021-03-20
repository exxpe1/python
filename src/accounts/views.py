from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render
from django.contrib.auth import forms as auth_forms, views as auth_views, models as auth_models, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from . import urls, forms, models


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})



@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'section': 'dashboard'})

class MyLoginView(LoginView):
    template_name='accounts/login.html'

class MyLogoutView(LogoutView):
   template_name='accounts/logged_out.html'

class MyPasswordChangeView(PasswordChangeView):
    template_name='registration/password_change_form.html'

class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name='registration/password_change_done.html'

class MyPasswordResetView(PasswordResetView):
    template_name='registration/password_reset_form.html'

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name='registration/password_reset_done.html'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name='registration/password_reset_confirm.html'

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name='registration/password_reset_complete.html'


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'accounts/registration_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {'user_form': user_form})

class UserCreateView(generic.CreateView):
    model = auth_models.User
    form_class = auth_forms.UserCreationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('shop:home')

    def get_success_url(self, *args, **kwargs):
        username=self.request.POST.get('username')
        password=self.request.POST.get('password1')
        user = authenticate(self.request, username=username, password=password)
        user.groups.add(auth_models.Group.objects.get(name='Customers'))
        user.save()
        
        if user is not None:
            login(self.request, user)        

        return str(self.success_url)

class UserLoginView(auth_views.LoginView):
    template_name='accounts/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()

        if url in ['/accounts/login/', '', None]:
            url = reverse_lazy('shop:home')  
        return url


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('shop:home')    


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = auth_models.User
    form_class = forms.UserProfileForm
    template_name = 'accounts/update_user.html'
    success_url = reverse_lazy('accounts:update-user')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        ext_user_data, created = models.UserExtend.objects.get_or_create(pk=self.request.user.pk)
        ext_user_data.save()
        context['form_ext'] = forms.UserProfileExtForm(instance=ext_user_data)
        return context

    def form_valid(self, form):
        self.object = form.save()
        object_ext = models.UserExtend.objects.get(pk=self.request.user.pk)
        form_ext = forms.UserProfileExtForm(self.request.POST, instance=object_ext)

        if form_ext.is_valid():
            object_ext = form_ext.save()

        return super().form_valid(form)

    def get_object(self, **kwargs):
        return self.request.user