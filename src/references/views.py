from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'proj/index.html', context)

def shop(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'proj/shop.html', context)
    
def product_page(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'object' : product, 'pk': pk}
    return render(request, 'proj/product_page.html', context)

def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    message = f'Продукт {product.name_product} удален'
    product.delete()
    context = {'message' : message}
    return render(request, 'proj/product_delete.html', context)


def product_create(request):
    if request.method == 'POST':
        name_product = request.POST.get('name_product')
        product = Product.objects.create(name_product=name_product)
        return HttpResponseRedirect(reverse('product', kwargs={'pk':product.pk}))
    context = {}
    return render(request, 'proj/product_create.html', context)


def product_update(request, pk):
    context = {}
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context = {'product': product}
    elif request.method == 'POST':
        name_product = request.POST.get('name_product')
        product = Product.objects.get(pk=pk).update(name_product=name_product)
        return HttpResponseRedirect(reverse('product', kwargs={'pk':product.pk}))
    
    return render(request, 'proj/product_update.html', context)