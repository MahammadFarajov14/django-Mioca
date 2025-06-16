from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Basket, BasketItem, Wishlist
from order.forms import CheckoutForm
from django.views.generic import CreateView
from django.http import JsonResponse
import json
from product.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

def update_item(request):
    data = json.loads(request.body)
    productid = data['productid']
    action = data['action']

    product = Product.objects.get(id = productid)

    basket, created = Basket.objects.get_or_create(user = request.user, is_active = True)
    basketItem, created = BasketItem.objects.get_or_create(basket = basket, product = product)

    if action == 'add':
        if not created:
            basketItem.quantity += 1

    if action == 'remove':
        basketItem.quantity -= 1

    basketItem.save()

    if basketItem.quantity <= 0:
        basketItem.delete()

    return JsonResponse('Item was added!', safe = False)

@login_required(login_url='login')
def cart(request):
    basket = Basket.objects.filter(user = request.user, is_active = True).first()
    context = {
        'basket': basket
    }
    return render(request, 'cart.html', context)

def emptyCart(request):
    return render(request, 'empty-cart.html')

@login_required(login_url='login')
def wishlist(request):
    wishlist = Wishlist.objects.filter(user = request.user)
    context = {
        'wishlist': wishlist
    }
    return render(request, 'wishlist.html', context)


class CheckoutListView(CreateView):
    # basket = Basket.objects.filter(user = request.user).first()
    # form = CheckoutForm
    # context = {
    #     'basket': basket,
    #     'form': form
    # }
    # return render(request, 'checkout.html', context)
    template_name = 'checkout.html'
    form_class = CheckoutForm
    model = Basket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['basket'] = Basket.objects.filter(user = self.request.user, is_active = True).first()

        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            order = form.save(False)
            order.user = self.request.user
            form.save()
            return redirect(reverse_lazy('checkout'))