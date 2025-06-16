from django.shortcuts import render, HttpResponse, redirect
from blog.models import Blog
from product.models import Product
from .tasks import export_data
from core.forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from order.models import Basket

# Create your views here.
def export_view(request):
    export_data.delay()
    return HttpResponse()

def home(request):
    allbaskets = Basket.objects.all()
    blogs = Blog.objects.all()
    products = Product.objects.all()
    context = {
        'products': products,
        'allbaskets': allbaskets
    }
    return render(request, 'index.html', context)

class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Successfully sent!')
        return super().form_valid(form)

def contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            print('validation')
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully sent!')
            return redirect(reverse_lazy('home'))
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def about(request):
    return render(request, 'about.html')

def p404(request):
    return render(request, '404.html')

def faq(request):
    return render(request, 'faq.html')

def compare(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'compare.html', context)