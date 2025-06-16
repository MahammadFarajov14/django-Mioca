from django.urls import path
from product.api.views import categories, products, product_update, ProductListAPIView, ProductRetrieveView, SubscribeCreateAPIView, TagApiView

urlpatterns = [
    path('categories/', categories, name = 'categories'),
    path('products/', ProductListAPIView.as_view(), name = 'products'),
    path('tags/', TagApiView.as_view(), name = 'tags'),
    path('product/<int:pk>/', ProductRetrieveView.as_view(), name = 'product_update'),
    path('subscribers/', SubscribeCreateAPIView.as_view(), name = 'subscribers'),

]