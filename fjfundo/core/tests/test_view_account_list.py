from django.test import TestCase
from fjfundo.core.models import MyUser
from fjfundo.mensalidades.models import Turma, Fundo
from django.shortcuts import resolve_url as r
from datetime import date


class AccountListTest(TestCase):
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

        self.user = MyUser.objects.create_user(email='user@email.com', password='senha@123',
                                               nome='Usuario teste', nivel=0, fone1='1234567890',
                                               turma=self.turma)
        self.client.login(email='user@email.com', password='senha@123')
        self.response = self.client.get(r('account_list'))

    def test_get(self):
        """ GET/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use edit_account.html """
        self.assertTemplateUsed(self.response, 'account_list.html')

    def test_context(self):
        """User must be in context"""
        user = self.response.context['user']
        self.assertIsInstance(user, MyUser)

    def test_html(self):
        contents = [
            'Usuario teste',
            'user@email.com',
            '1234567890',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)
