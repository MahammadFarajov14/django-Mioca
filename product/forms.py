from django import forms
from .models import Product, ProductReview

class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            '__all__'
        )
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

class ProductReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = (
            'message',
        )
        widgets = {
            'message': forms.Textarea(attrs={
                'placeholder': 'Message my message'
            })
        }