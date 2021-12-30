from django.test import SimpleTestCase
from blog.views import (PostListView, PostDetailView, SearchListView,
                        PostCreateView, PostDeleteView, UserPostListView,
                        PostUpdateView, about)
from django.urls import reverse, resolve
class TestUrls(SimpleTestCase):

    def test_blog_about_url(self):
        url = reverse('blog-about')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, about)

    def test_blog_post_search_url(self):
        url = reverse('post-search')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, SearchListView)

    def test_blog_home_url(self):
        url = reverse('blog-home')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_blog_post_detail_url(self):
        url = reverse('post-detail', args=[1,])
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_blog_user_post_list_view_url(self):
        url = reverse('user-posts', args=["user",])
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UserPostListView)

    def test_blog_post_create_url(self):
        url = reverse('post-create')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_blog_post_update_url(self):
        url = reverse('post-update', args=[1,])
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_blog_post_delete_url(self):
        url = reverse('post-delete', args=[1,])
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)
