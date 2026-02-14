from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Title", text="Content")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_title = f'{post.title}'
        expected_object_text = f'{post.text}'
        self.assertEqual(expected_object_title, "Title")
        self.assertEqual(expected_object_text, "Content")

class HomePageViewText(TestCase):
    def setUp(self):
        Post.objects.create(title="Title 2", text="Content 2")

    def test_views_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_users_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")
