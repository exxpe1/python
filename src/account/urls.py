from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.MyLoginView.as_view(), name='login'),
]