from order.api.views import WishlistAPIView, WishlistDestroyView
from django.urls import path

urlpatterns = [
    path('wishlist/', WishlistAPIView.as_view(), name='wishlist_api'),
    path('wishlist/<int:pk>/', WishlistDestroyView.as_view(), name='wishlist_del'),
]