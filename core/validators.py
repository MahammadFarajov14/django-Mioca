from django.core.exceptions import ValidationError

def email_validation(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError('Email is incorrect! Please try again')