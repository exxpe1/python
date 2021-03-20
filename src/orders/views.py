from django.shortcuts import render
from .models import OrderItem, Customer, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect


def order_create(request):
    cart = Cart(request)
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
    else:
        customer = 'anonym'
    print(customer) 
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         )
            # очистка корзины
            cart.clear()
            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get()
            context = {
                'object' : order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("/")