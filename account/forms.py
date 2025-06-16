from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()



class MyAccountForm(forms.ModelForm):

    fullname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Full Name(Format: firstname lastname)'
    }))

    class Meta:
        model = User
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            })
        }

    def save(self, commit = ...):
        fullname = self.cleaned_data['fullname']
        firstname = fullname.split()[0]
        lastname = fullname.split()[1]
        self.instance.first_name = firstname
        self.instance.last_name = lastname
        return super().save(commit)
        

class RegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password'
        )
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
        }
    
    def save(self, commit = ...):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.save()
        return user

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError("Confirm password didn't match with password")
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder' : 'Username'
    }))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        'placeholder' : 'Password'
    }))