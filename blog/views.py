from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from blog.models import Blog, BlogReview
from blog.forms import BlogForm
from django.contrib import messages
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _
# Create your views here.

class BlogView(CreateView):
    template_name = 'blog-single.html'
    form_class = BlogForm
    success_url = reverse_lazy('home')
    def form_invalid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _("Succesfully Sent!"))
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = BlogReview.objects.all()
        return context

def blog_single(request, pk):
    form = BlogForm
    if request.method == 'POST':
        form = BlogForm(data = request.POST)   
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Succesfully Sent!")
            return redirect(reverse_lazy('home'))
    blog = get_object_or_404(Blog, id = pk)
    context = {
        'blog': blog,
        'form': form
    }
    return render(request, 'blog-single.html', context)

def blog(request):
    blog = Blog.objects.all()
    context = {
        'blogs': blog,
    }
    return render(request, 'blog.html', context)
