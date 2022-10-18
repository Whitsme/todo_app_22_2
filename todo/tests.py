from django.test import TestCase
from django.urls import reverse

from .models import Todo

# Create your tests here.
class PostTests(TestCase):
    """"post tests"""

    @classmethod
    def setUpTestData(cls):
        """"set up test data"""
        cls.post = Todo.objects.create(text='just a test')

    def test_text_content(self):
        """test model content"""
        self.assertEqual(self.post.text, 'just a test')

    def test_view_url_exists_at_proper_location(self):
        """test view url exists at proper location"""
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_homepage(self):
        """test homepage"""
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(str(resp.context['object_list'][0]), 'just a test')