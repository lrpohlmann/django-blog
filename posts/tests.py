from django.test import TestCase

from model_bakery import baker

# Create your tests here.
class TestPost(TestCase):
    def test_post_view(self):
        post = baker.make("Post")
        resposta = self.client.get(f"/post/{post.pk}")

        assert resposta.status_code == 200

    def test_post_grid(self):
        baker.make("Post")
        assert self.client.get("/post/grid").status_code == 200
