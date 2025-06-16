from django.urls import path
from blog.views import BlogView, blog

urlpatterns = [
    path('home/<int:pk>/', BlogView.as_view(), name = 'blog_single'),
    path('blogs/', blog, name='blogs')
]

