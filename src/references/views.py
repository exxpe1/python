from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from .models import Author, Product, Series, Publisher, Genre
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

class ProductView(ListView):
    model=Product
    template_name_suffix='_list'



def product_page(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'object' : product, 'pk': pk}
    return render(request, 'references/product_page.html', context)

class ProductDetail(DetailView):
    model=Product
    template_name_suffix='_page'



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

class AuthorView(ListView):
    model=Author
    template_name_suffix='_list'

class AuthorDetail(DetailView):
    model=Author
    template_name_suffix='_page'

class AuthorDelete(DeleteView):
    success_url= reverse_lazy('author')
    model=Author


class AuthorCreate(CreateView):
    success_url=reverse_lazy('author')
    model=Author
    fields=('name_author','desc_author')

class AuthorUpdate(UpdateView):
    success_url=reverse_lazy('author')
    model=Author
    fields=('name_author','desc_author')
    template_name_suffix='_update_form'


#genre cbv
class GenreView(ListView):
    model=Genre
    template_name_suffix='_list'

class GenreDetail(DetailView):
    model=Genre
    template_name_suffix='_page'

class GenreDelete(DeleteView):
    success_url= reverse_lazy('genre')
    model=Genre


class GenreCreate(CreateView):
    success_url=reverse_lazy('genre')
    model=Genre
    fields=('name_genre')

class GenreUpdate(UpdateView):
    success_url=reverse_lazy('genre')
    model=Genre
    fields=('name_genre','desc_genre')
    template_name_suffix='_update_form'
    
#publisher

class PublisherView(ListView):
    model=Publisher
    template_name_suffix='_list'

class PublisherDetail(DetailView):
    model=Publisher
    template_name_suffix='_page'

class PublisherDelete(DeleteView):
    success_url= reverse_lazy('publisher')
    model=Publisher


class PublisherCreate(CreateView):
    success_url=reverse_lazy('publisher')
    model=Publisher
    fields=('name_publisher','desc_publisher')

class PublisherUpdate(UpdateView):
    success_url=reverse_lazy('publisher')
    model=Publisher
    fields=('name_publisher')
    template_name_suffix='_update_form'

#serie

#publisher

class SeriesView(ListView):
    model=Series
    template_name_suffix='_list'

class SeriesDetail(DetailView):
    model=Series
    template_name_suffix='_page'

class SeriesDelete(DeleteView):
    success_url= reverse_lazy('series')
    model=Series


class SeriesCreate(CreateView):
    success_url=reverse_lazy('series')
    model=Series
    fields=('name_series','desc_series')

class SeriesUpdate(UpdateView):
    success_url=reverse_lazy('series')
    model=Series
    fields=('name_series','desc_series')
    template_name_suffix='_update_form'