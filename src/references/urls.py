from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexList.as_view(), name='home'),
    path('catalog/', views.shop, name='catalog'),
    path('catalog/<int:pk>', views.product_page, name='product'),
    path('catalog-cbv/<int:pk>', views.ProductDetail.as_view(), name='product-cbv'),
    path('catalog-delete/<int:pk>', views.ProductDelete.as_view(), name='catalog-delete'),
    path('product-create/', views.ProductCreate.as_view(), name='product-create'),
    path('catalog-update/<int:pk>', views.ProductUpdate.as_view(), name='product-update')
]