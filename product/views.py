from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from product.models import Product, ProductCategory, ProductReview, ProductTag, ProductSize, ProductColor, ProductImage
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from product.forms import ProductReviewForm
from django.db.models import Min, Max
# Create your views here.


class ProductView(ListView):
    template_name = 'shop-left-sidebar.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['tags'] = ProductTag.objects.all()
        context['sizes'] = ProductSize.objects.all()
        context['colors'] = ProductColor.objects.all()       
        context['min_max_price'] = Product.objects.aggregate(Min('price'), Max('price'))
        return context
    
    def get_queryset(self):
        q_set = super().get_queryset()
        cat_id = self.request.GET.get('category')
        tag_id = self.request.GET.get('tag')
        color_id = self.request.GET.get('color')
        size_id = self.request.GET.get('size')

        if cat_id:
            q_set = q_set.filter(category = cat_id)
        if tag_id:
            q_set = q_set.filter(tag = tag_id)
        if color_id:
            q_set = q_set.filter(color = color_id)

        if size_id:
            q_set = q_set.filter(size = size_id)
        if cat_id and tag_id:
            q_set = q_set.filter(category = cat_id, tags = tag_id)
        return q_set

def shop(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {
        'products': products,
        'categories': categories

    }
    return render(request, 'shop-left-sidebar.html', context)

def productdetail(request, pk):
    product = get_object_or_404(Product, id = pk)
    recently_viewed_products = None

    if 'recently_viewed' in request.session:
        if pk in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(pk)

        products = Product.objects.filter(pk__in=request.session['recently_viewed'])
        recently_viewed_products = sorted(products, 
            key=lambda x: request.session['recently_viewed'].index(x.id)
            )
        request.session['recently_viewed'].insert(0, pk)
        if len(request.session['recently_viewed']) > 5:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = [pk]

    request.session.modified = True

    context = {'product': product, 'recently_viewed_products' : recently_viewed_products}
    return render(request, 'single-product.html', context)

class ShopDetailView(FormMixin, DetailView):
    template_name = 'single-product.html'
    model = Product
    form_class = ProductReviewForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = ProductReview.objects.filter(product = self.get_object())
        context['productImages'] = ProductImage.objects.filter(product = self.get_object())

        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            review = form.save(False)
            review.product = self.object
            review.user = self.request.user
            form.save()
            return redirect(reverse_lazy('productdetail', kwargs = {'slug': self.object.slug}))