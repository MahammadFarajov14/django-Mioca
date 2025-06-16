from django.template import Library
register = Library()
from blog.models import Blog
from product.models import ProductCategory, Product
from order.models import Basket, Wishlist
from django.contrib.auth import get_user_model
User = get_user_model()

@register.simple_tag
def get_categories():
    return ProductCategory.objects.filter(parent = None)

@register.inclusion_tag('includes/latest-blogs.html')
def get_blogs():
    recent_blogs = Blog.objects.order_by("-created_date")[:3]
    return {
        'blogs': recent_blogs
    }


@register.inclusion_tag('includes/recent-products.html')
def get_recent_products():
    recent_products = Product.objects.order_by("-created_date")[:4]
    return {
        'products': recent_products
    }

@register.inclusion_tag('includes/related-products.html')
def get_related_products(category):
    related_products = Product.objects.filter(category = category)
    return {
        'products': related_products
    }

@register.simple_tag
def get_basket(user):
    return Basket.objects.filter(user = user, is_active = True).first()

@register.simple_tag
def get_wishlist(user):
    return Wishlist.objects.filter(user = user)

# {% get_categories as categories %}