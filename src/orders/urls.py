from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('order-summary', views.OrderSummaryView.as_view(),name='order-summary'),
]