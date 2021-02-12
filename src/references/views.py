from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from .models import Product
from . import forms
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'references/index.html', context)

class IndexList(ListView):
    model=Product

def shop(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'references/shop.html', context)
    
def product_page(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'object' : product, 'pk': pk}
    return render(request, 'references/product_page.html', context)

class ProductDetail(DetailView):
    model=Product


def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    message = f'Продукт {product.name_product} удален'
    product.delete()
    context = {'message' : message}
    return render(request, 'references/product_delete.html', context)

class ProductDelete(DeleteView):
    success_url= reverse_lazy('catalog')
    model=Product
    

def product_create(request):
    context = {}
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return HttpResponseRedirect(reverse('product', kwargs={'pk':product.pk}))
        else:
            context['form'] = form
    else:
        context['form'] = forms.ProductForm()
    
    return render(request, 'references/product_create.html', context)

class ProductCreate(CreateView):
    success_url=reverse_lazy('catalog')
    model=Product
    fields=('name_product','price')

def product_update(request, pk):
    context = {}
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context = {'product': product}
    elif request.method == 'POST':
        name_product = request.POST.get('name_product')
        price = request.POST.get('price')
        product = Product.objects.get(pk=pk)
        product.name_product=name_product
        product.price=price
        product.save()

        return HttpResponseRedirect(reverse('product', kwargs={'pk':product.pk}))
    return render(request, 'references/product_update.html', context)

class ProductUpdate(UpdateView):
    success_url=reverse_lazy('catalog')
    model=Product
    fields=('name_product','price')
    template_name_suffix='_update_form'