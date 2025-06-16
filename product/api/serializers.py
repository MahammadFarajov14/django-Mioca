from rest_framework import serializers
from product.models import ProductCategory, Product, ProductTag, ProductSize, ProductColor
from core.models import Subscribe

class SubscribeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = (
            'email',
        )

class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = (
            'id',
            'title',
            'parent'
        )

class ProductTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTag
        fields = (
            'id',
            'title'
        )

class ProductSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSize
        fields = (
            'id',
            'title'
        )

class ProductColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductColor
        fields = (
            'id',
            'title'
        )

class ProductSerializer(serializers.ModelSerializer):

    # category = serializers.CharField(source='category.title')
    category = ProductCategorySerializer()
    color = ProductColorSerializer()
    size = ProductSizeSerializer()
    tag = ProductTagSerializer(many = True) # bir nece tage sahib olan var deye tagde many True olacaq.

    class Meta:
        model = Product
        fields = (
            'id',
            'color',
            'size',
            'rating',
            'title',
            'cover_image',
            'tag',
            'category',
            'price',
            'quantity',
        )


class ProductCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = (
            'title',
            'color',
            'size',
            'cover_image',
            'tag',
            'category',
            'price',
            'quantity',
        )
