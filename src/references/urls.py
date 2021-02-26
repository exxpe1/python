from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from account import urls as account_urls

urlpatterns = [
    path('', views.IndexList.as_view(), name='home'),
    path('catalog/', views.ProductView.as_view(), name='catalog'),
    #path('catalog/<int:pk>', views.product_page, name='product'),
    path('catalog/<int:pk>', views.ProductDetail.as_view(), name='product'),
    path('catalog-delete/<int:pk>', views.ProductDelete.as_view(), name='catalog-delete'),
    path('product-create/', views.ProductCreate.as_view(), name='product-create'),
    path('catalog-update/<int:pk>', views.ProductUpdate.as_view(), name='product-update'),

    path('account/', include(account_urls)),

    path('author/', views.AuthorView.as_view(), name='author'),
    path('author/<int:pk>', views.AuthorDetail.as_view(), name='author-page'),
    path('author-delete/<int:pk>', views.AuthorDelete.as_view(), name='author-delete'),
    path('author-create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author-update/<int:pk>', views.AuthorUpdate.as_view(), name='author-update'),

    path('genre/', views.GenreView.as_view(), name='genre'),
    path('genre/<int:pk>', views.GenreDetail.as_view(), name='genre-page'),
    path('genre-delete/<int:pk>', views.GenreDelete.as_view(), name='genre-delete'),
    path('genre-create/', views.GenreCreate.as_view(), name='genre-create'),
    path('genre-update/<int:pk>', views.GenreUpdate.as_view(), name='genre-update'),

    path('publisher/', views.PublisherView.as_view(), name='publisher'),
    path('publisher/<int:pk>', views.PublisherDetail.as_view(), name='publisher-page'),
    path('publisher-delete/<int:pk>', views.PublisherDelete.as_view(), name='publisher-delete'),
    path('publisher-create/', views.PublisherCreate.as_view(), name='publisher-create'),
    path('publisher-update/<int:pk>', views.PublisherUpdate.as_view(), name='publisher-update'),

    path('series/', views.SeriesView.as_view(), name='series'),
    path('series/<int:pk>', views.SeriesDetail.as_view(), name='series-page'),
    path('series-delete/<int:pk>', views.SeriesDelete.as_view(), name='series-delete'),
    path('series-create/', views.SeriesCreate.as_view(), name='series-create'),
    path('series-update/<int:pk>', views.SeriesUpdate.as_view(), name='series-update'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)