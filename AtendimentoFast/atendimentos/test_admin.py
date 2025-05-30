from django.test import TestCase
from django.contrib import admin
from .models import Usuario, Cliente, Servico, HorarioAtendimento

class AdminSiteTest(TestCase):
    def test_usuario_registered(self):
        self.assertIn(Usuario, admin.site._registry)

    def test_cliente_registered(self):
        self.assertIn(Cliente, admin.site._registry)

    def test_servico_registered(self):
        self.assertIn(Servico, admin.site._registry)

    def test_horarioatendimento_registered(self):
        self.assertIn(HorarioAtendimento, admin.site._registry)