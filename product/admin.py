from django.contrib import admin
from product.models import Product, ProductCategory, ProductImage, ProductReview, Property, PropertyValue, ProductTag, ProductColor, ProductSize
from product.forms import ProductAdminForm
from modeltranslation.admin import TranslationAdmin

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'category', 'price', 'quantity', 'get_tags']
    list_display_links = ['id', 'title']
    list_editable = ['category', 'quantity']
    list_filter = ['category']
    search_fields = ['title']
    inlines = [ProductImageInline]
    form = ProductAdminForm

    def get_tags(self, obj):
        tags = []
        for tag in obj.tag.all():
            tags.append(tag.title)
        return tags

# class ProductCategoryModelAdmin(TranslationAdmin):
#     list_display = ['title']
    
# admin.site.register(ProductCategory, ProductCategoryModelAdmin)

admin.site.register(ProductCategory)
admin.site.register(ProductReview)
admin.site.register(ProductTag)
admin.site.register(Property)
admin.site.register(PropertyValue) 
admin.site.register(ProductColor) 
admin.site.register(ProductSize) 