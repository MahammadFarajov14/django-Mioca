from django.db import models
from core.models import AbstractModel
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
# from django.contrib.auth import get_user_model
# User = get_user_model()
# Create your models here.

class User(AbstractUser):
    image = models.ImageField('image', upload_to='user',  null=True, blank=True, default='images/default-profile.jpg')
    ips = ArrayField(models.GenericIPAddressField(), null=True, blank=True)



class UserProfile(AbstractModel):
    user = models.ForeignKey(User, related_name='userProfile', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='user_profile/')
    gender = models.CharField('gender', null=True, blank=True)


class UserAddress(AbstractModel):
    user = models.ForeignKey(User, related_name='address', on_delete=models.CASCADE)
    country = models.CharField('country', max_length=200)
    address = models.CharField('address', max_length=200)
    apartment = models.CharField('apartment', max_length=200)
    zipcode = models.CharField('zipcode', max_length=200)
    city = models.CharField('city', max_length=200)
    state = models.CharField('state', max_length=200)

class BlockUserIp(AbstractModel):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address