from django.http.response import Http404
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'proj/index.html', context)

def shop(request):
    return render(request, 'proj/shop.html')