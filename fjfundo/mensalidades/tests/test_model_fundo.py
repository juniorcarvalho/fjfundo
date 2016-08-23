from django.test import TestCase
from datetime import date
from fjfundo.mensalidades.models import Fundo


class FundoModelTest(TestCase):
    def setUp(self):
        self.fundo = Fundo.objects.create(
            nomefundo='fundo de formatura',
            dtinicial=date(2016, 1, 1),
            dtfinal=date(2016, 12, 31),
            vlrmensalidade=100.00,
            diavencimento='10',
            gestor=0,
            email='joseadolfojr@gmail.com',
            cnpj='00000000000000',
            multa=2.0,
            juro=6.0
        )

    def test_create(self):
        self.assertTrue(Fundo.objects.exists())

    def test_str(self):
        self.assertEqual('fundo de formatura', str(self.fundo))
