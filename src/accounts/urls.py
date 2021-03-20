#from django.contrib import admin
#from django.contrib.auth.views import logout_then_login
#from django.urls import path
#from django.conf.urls import url
#from django.contrib.auth import views as auth_views
#from . import views as myviews
#from django.contrib.auth import views
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    #path('login/', views.user_login, name='login'),
    #path('logout/', views.UserLogoutView.as_view(), name='logout'),    
    #path('login/', views.MyLoginView.as_view(), name='login'),
    #path('logout/', views.MyLogoutView.as_view(), name='logout'),
    #path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('password-change/', views.MyPasswordChangeView.as_view(), name='password_change'),
    #path('password-change/done/', views.MyPasswordChangeDoneView.as_view(), name='password_change_done'),
    #path('password-reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    #path('password-reset/done', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('password-reset/confirm', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('password-reset/complete', views.MyPasswordResetCompleteView.as_view(), name='password_reset_complete'), 

    #path('login/', views.LoginView.as_view(), name='login'),
    #path('logout/', views.LogoutView.as_view(), name='logout'),
    #path('logout-then-login/', logout_then_login, name='logout_then_login'),
    #path('dashboard/', myviews.dashboard, name='dashboard'),
    #path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    #path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    #path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),      
    #path('registration/', myviews.register, name='registraion'),  

    path('registration/', views.UserCreateView.as_view(), name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('update-user/', views.UserUpdateView.as_view(), name='update-user'),
    path('logout/', views.UserLogoutView.as_view(), name='logout')
]
