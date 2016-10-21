from django.test import TestCase
from fjfundo.core.models import MyUser
from django.shortcuts import resolve_url as r
from fjfundo.mensalidades.models import Turma, Fundo
from datetime import date


class DashboardTest(TestCase):
    def setUp(self):
        self.fundo = Fundo.objects.create(
            nome_fundo='fundo de formatura',
            data_inicial=date(2016, 1, 1),
            data_final=date(2016, 12, 31),
            cnpj='00000000000000'
        )

        self.turma = Turma.objects.create(
            fundo=self.fundo,
            nome_turma='nome da turma',
            dia_venc='10',
            data_formatura=date(2016, 12, 31),
            valor_multa=2.0,
            valor_juros=6.0
        )

        self.user = MyUser.objects.create_user(email='user@email.com', password='senha@123', nivel=2,
                                               turma=self.turma)
        self.client.login(email='user@email.com', password='senha@123')
        self.response = self.client.get(r('dashboard'))

    def test_get(self):
        """ GET/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use dashboard.html """
        self.assertTemplateUsed(self.response, 'dashboard.html')

    def test_html(self):
        """ Html must contain input tags"""
        self.assertContains(self.response, '<section class="content"')
        self.assertContains(self.response, 'Início')
        self.assertContains(self.response, '<li class="active">Início')

    def test_context_user(self):
        """ User (MyUser) must be in context"""
        user = self.response.context['user']
        self.assertIsInstance(user, MyUser)

    def test_context_turma(self):
        """ Turma must be in context"""
        turma = self.response.context['turma']
        self.assertIsInstance(turma, Turma)
