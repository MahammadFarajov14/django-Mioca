from django.test import TestCase, Client
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import ProductCategory, ProductTag
from django.conf import settings
import os

# Create your tests here.

class TestProductView(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = reverse_lazy('shop')
        cls.client = Client()

    def testurl(self):
        self.assertEqual(self.url, '/en/shop/')

    def test_response_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_response_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'shop-left-sidebar.html')

    @classmethod
    def tearDownClass(cls):
        pass


class TestProductApi(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = reverse_lazy('products')
        user = User.objects.create_user(username='john', email='js@js.com', password='js.sj')
        cls.client = APIClient()
        category = ProductCategory.objects.create(title = 'Category #1')
        tag = ProductTag.objects.create(title = 'Tag #1')
        refresh = RefreshToken.for_user(user)
        cls.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        file_path = os.path.join(settings.MEDIA_ROOT, 'product_images/2.jpg')
        cls.data = {
            'title': 'Product1',
            'cover_image': (open(file_path, 'rb'),),
            'tags': tag.id,
            'category': category.id,
            'price': 45,
            'quantity': 15,
        }
        cls.post_valid = cls.client.post(cls.url, data = cls.data)

    def test_product_api_url(self):
        self.assertEqual(self.url, '/en/api/products/')

    def test_product_post_status(self):
        self.assertEqual(self.post_valid.status_code, 201)

    def test_response_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        pass