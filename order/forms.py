from order.models import Order
from django import forms

class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'name',
            'lname',
            'country',
            'email',
            'address',
            'phone',
            'zip',
            'city',
            'state',
            'note',
        )
        widgets = {
            'email': forms.EmailInput(attrs={
            })
        }