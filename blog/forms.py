from django import forms
from blog.models import BlogReview
from django.core.exceptions import ValidationError
class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogReview
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )
        widgets = {
            'name': forms.TextInput(attrs= {
                'placeholder': 'Name *'
            }),
            'email': forms.EmailInput(attrs= {
                'placeholder': 'Email *'
            }),
            'subject': forms.TextInput(attrs= {
                'placeholder': 'Subject (Optinal)'
            }),
            'message': forms.Textarea(attrs= {
                'placeholder': 'Message'
            })
        }

    def clean_email(self):
        value = self.cleaned_data['email']
        if not value.endswith('gmail.com'):
            raise forms.ValidationError('You must enter gmail address!')
        return self.cleaned_data