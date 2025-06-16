from django.urls import path
from order.views import emptyCart, cart, wishlist, update_item, CheckoutListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('update-item/', update_item, name = 'updateitem'),
    path('emptyCart/', emptyCart, name = 'emptyCart'),
    path('cart/', cart, name = 'cart'),
    path('wishlist/', wishlist, name = 'wishlist'),
    path('checkout/', login_required(CheckoutListView.as_view(), login_url='login'), name = 'checkout'),

]
