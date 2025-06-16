from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Blog(AbstractModel):
    user = models.ForeignKey(User, related_name='blog', on_delete=models.CASCADE)

    title = models.CharField('title', max_length=200, blank=True, null=True)
    cover_image = models.ImageField(upload_to='blog_images/', default='blog_images/1.jpg' , blank=True, null=True)
    description = models.TextField('description', null=True, blank=True)
    
    def __str__(self):
        return self.title
    

class BlogReview(AbstractModel):
    name = models.CharField('name', max_length=200, unique=True)
    email = models.EmailField('email', max_length=200)
    subject = models.CharField('subject', max_length=200, null=True, blank=True)
    message = models.TextField('message')

    def len(self):
        return len(self.objects.all())


    def __str__(self):
        return self.name