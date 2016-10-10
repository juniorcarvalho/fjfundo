from datetime import date
from django.test import TestCase
from fjfundo.mensalidades.models import Turma, Fundo


class TurmaModelTest(TestCase):
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

    def test_create(self):
        self.assertTrue(Turma.objects.exists())

    def test_str(self):
        self.assertEqual('nome da turma', str(self.turma))
