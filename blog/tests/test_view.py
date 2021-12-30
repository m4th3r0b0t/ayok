from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.about_url = reverse('blog-about')
        self.home_url = reverse('blog-home')

    def test_blog_about_GET(self):

        response = self.client.get(self.about_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    def test_blog_home_GET(self):

        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')
