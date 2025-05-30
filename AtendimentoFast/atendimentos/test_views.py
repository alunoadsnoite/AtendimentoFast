from django.test import TestCase, Client
from django.urls import reverse

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_inicio_view(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_cadastro_view(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)

    def test_menu_adm_view(self):
        response = self.client.get(reverse('menu_adm'))
        self.assertEqual(response.status_code, 200)

    def test_menu_cliente_view(self):
        response = self.client.get(reverse('menu_cliente'))
        self.assertEqual(response.status_code, 200)

    # Adicione outros testes para as views que desejar