from django.contrib import admin
from order.models import Wishlist, Basket, BasketItem, Order
# Register your models here.

admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(Basket)
admin.site.register(BasketItem)