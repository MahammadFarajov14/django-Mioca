from rest_framework import serializers
from order.models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = (
            'user',
            'product',
        )
