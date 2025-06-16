from django.urls import path
from core.views import home, contact, about, p404, faq, compare, export_view, ContactView

urlpatterns = [
    path('', home, name = 'home'),
    path('contact/', ContactView.as_view(), name = 'contact'),
    path('about/', about, name = 'about'),
    path('404/', p404, name = '404'),
    path('faq/', faq, name = 'faq'),
    path('compare/', compare, name = 'compare'),
    path('export/', export_view, name = 'export'),
]