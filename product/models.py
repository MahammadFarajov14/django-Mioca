from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class ProductTag(AbstractModel):
    title = models.CharField('title', max_length=200)

    def __str__(self):
        return self.title
    

class ProductCategory(AbstractModel):
    parent = models.ForeignKey('self', related_name='child', on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=200)


    def __str__(self):
        if self.parent:
            return f'{self.parent} - {self.title}'
        return self.title
    

    class Meta:
        verbose_name_plural = 'Product Categories'


class ProductColor(AbstractModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Product Colors'
    
class ProductSize(AbstractModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Product Sizes'

class Product(AbstractModel):
    category = models.ForeignKey(ProductCategory, related_name='product', on_delete=models.CASCADE)
    color = models.ForeignKey(ProductColor, related_name='product', on_delete=models.CASCADE)
    tag = models.ManyToManyField(ProductTag, related_name='product', blank=True)
    size = models.ForeignKey(ProductSize, related_name='product', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=200)
    descriptiton = models.TextField('description', null=True, blank=True)
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    rating = models.DecimalField('rating', max_digits=10, decimal_places=2, null=True, blank=True)
    cover_image = models.ImageField(upload_to='product_images/')
    quantity = models.IntegerField('quantity')
    type = models.CharField('type', max_length=200, null=True, blank=True)
    slug = models.SlugField('slug', null=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.category} - {self.title}'
    
    def ratingrange(self):
        return range(int(self.rating))
    
    def reviewlen(self):
        return len(self.productReview.all())
class ProductImage(AbstractModel):
    product = models.ForeignKey(Product, related_name='productImage', on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='product_images_add/')


    def __str__(self):
        return self.product.title
    

class ProductReview(AbstractModel):
    product = models.ForeignKey(Product, related_name='productReview', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='productReview', on_delete=models.CASCADE)

    rating = models.IntegerField('rating', default=1, null=True, blank = True)
    message = models.TextField('message', null=True, blank=True)


    def __str__(self):
        return self.user.username
    

class PropertyValue(AbstractModel):
    product = models.ForeignKey(Product, related_name='propertyValue', on_delete=models.CASCADE)

    title = models.CharField('title', max_length=200)
    
    def __str__(self):
        return self.product.title
    
    
class Property(AbstractModel):
    propertyValue = models.ForeignKey(PropertyValue, related_name='property', on_delete=models.CASCADE)

    title = models.CharField('title', max_length=200)
    
    def __str__(self):
        return self.propertyValue.title
    
    class Meta:
        verbose_name_plural = 'Properties'
    
