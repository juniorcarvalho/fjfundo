from django.test import TestCase
from datetime import date
from fjfundo.mensalidades.models import Fundo


class FundoModelTest(TestCase):
    def setUp(self):
        self.fundo = Fundo.objects.create(
            nome_fundo='fundo de formatura',
            data_inicial=date(2016, 1, 1),
            data_final=date(2016, 12, 31),
            cnpj='00000000000000'
        )

    def test_create(self):
        self.assertTrue(Fundo.objects.exists())

    def test_str(self):
        self.assertEqual('fundo de formatura', str(self.fundo))
