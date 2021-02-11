from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('catalog', views.shop, name='catalog'),
    path('catalog/<int:pk>', views.product_page, name='product'),
    path('catalog-delete/<int:pk>', views.product_delete, name='catalog-delete'),
    path('product-create/', views.product_create, name='product-create'),
    path('catalog-update/<int:pk>', views.product_update, name='product-update')
]