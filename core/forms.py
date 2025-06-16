from django import forms
from core.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name*'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email*'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject*'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your Message*'
            }),
        }

    def clean(self):
        value = self.cleaned_data['email']
        if not value.endswith('gmail.com'):
            raise forms.ValidationError('You must enter a gmail address!')
        return self.cleaned_data