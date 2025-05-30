from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views

class TestUrls(SimpleTestCase):
    def test_inicio_url_resolves(self):
        url = reverse('inicio')
        self.assertEqual(resolve(url).func, views.inicio_view)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, views.login_view)

    def test_cadastro_url_resolves(self):
        url = reverse('cadastro')
        self.assertEqual(resolve(url).func, views.cadastro)

    # Adicione outros testes para as demais URLs conforme necessário