from order.api.serializers import WishlistSerializer, Wishlist
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from product.models import Product
from django.http import JsonResponse

class WishlistDestroyView(DestroyAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()

class WishlistAPIView(ListCreateAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()

    def post(self, request, *args, **kwargs):
        productId = request.data.get('productId')
        product = Product.objects.filter(id = productId).first()
        wishlist = Wishlist.objects.filter(product = product, user = request.user).first()
        if wishlist:
            wishlist.delete()
            return JsonResponse('Item was deleted', safe=False)
        Wishlist.objects.create(product = product, user = request.user)
        return JsonResponse('Item was added', safe=False)