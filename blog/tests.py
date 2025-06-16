from django.test import TestCase
from .models import BlogReview

# Create your tests here.
class TestBlogReviewModel(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'name': 'Test',
            'email': 'wefefwsa2313@gmail.com',
            'subject': 'Things',
            'message': 'yes nice good but no yes i like it'
        }
        cls.review = BlogReview.objects.create(**cls.data)

    def test_post(self):
        review = BlogReview.objects.first()
        self.assertEqual(self.review, review)
    
    @classmethod
    def tearDownClass(cls):
        pass