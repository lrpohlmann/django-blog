from django.test import TestCase

from model_bakery import baker

# Create your tests here.
class TestPost(TestCase):
    def test_post_view(self):
        post = baker.make("Post")
        resposta = self.client.get(f"/post/{post.pk}")

        self.assertEqual(resposta.status_code, 200)


class TestPostGridView(TestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make("Post", 20)

    def test_sem_pagina_indicada(self):
        self.assertEqual(self.client.get("/post/grid").status_code, 200)

    def test_com_pagina_indicada(self):
        for n in range(0, 10):
            with self.subTest(msg=f"Testando com página número {n}"):
                self.assertEqual(
                    self.client.get("/post/grid", data={"pagina": n}).status_code, 200
                )

    def test_paginador_apareceu(self):
        resposta = self.client.get("/post/grid", data={"pagina": 2})
        html = str(resposta.content).replace(" ", "").replace("\\n", "")
        self.assertIn("1</button>", html)
        self.assertIn("3</button>", html)
        self.assertIn("2</div>", html)
