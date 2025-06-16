from django.db import models
from core.validators import email_validation
# Create your models here.


class AbstractModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subscribe(AbstractModel):
    email = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.email

class Contact(AbstractModel):
    name = models.CharField('Name', max_length=200)
    email = models.CharField('Email', max_length=200, unique=True, validators=[email_validation])
    subject = models.CharField('Subject', max_length=200)
    message = models.TextField('Message')

    def __str__(self):
        return self.name