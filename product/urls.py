from django.urls import path
from product.views import ShopDetailView, ProductView

urlpatterns = [
    path('shop/', ProductView.as_view(), name = 'shop'),
    path('shop/<str:slug>/', ShopDetailView.as_view(), name = 'productdetail')
]