from django.db import models
from core.models import AbstractModel
from product.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Wishlist(AbstractModel):
    user = models.ForeignKey(User, related_name='wishlist', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='wishlist', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Basket(AbstractModel):
    user = models.ForeignKey(User, related_name='basket', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username
    
    def total(self):
        total = 0
        for item in self.basketItem.all():
            total += item.price()
        
        return total
    
    def len(self):
        return len(self.basketItem.all())

class BasketItem(AbstractModel):
    basket = models.ForeignKey(Basket, related_name='basketItem', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='basketItem', on_delete=models.CASCADE)
    quantity = models.IntegerField('quantity', default=1)

    def __str__(self):
        return self.product.title
    
    def price(self):
        return self.quantity * self.product.price
    
    class Meta:
        ordering = '-created_date',

class Order(AbstractModel):
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE, null=True, blank=True)
    basket = models.ForeignKey(Basket, related_name='order', on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    country = models.CharField('country', max_length=200)
    address = models.CharField('address', max_length=200)
    city = models.CharField('city', max_length=200)
    state = models.CharField('state', max_length=200)
    zip = models.CharField('zip', max_length=200)
    phone = models.CharField('phone', max_length=200)
    email = models.EmailField(max_length=100)
    note = models.TextField()

    def __str__(self):
        return self.user.username