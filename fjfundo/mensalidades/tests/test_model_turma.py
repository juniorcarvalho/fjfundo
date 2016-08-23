from datetime import date
from django.test import TestCase
from fjfundo.mensalidades.models import Turma, Fundo


class TurmaModelTest(TestCase):
    def setUp(self):
        self.fundo = Fundo.objects.create(
            id_fundo=1,
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

        self.turma = Turma.objects.create(
            ctrl_turma=1,
            id_fundo=self.fundo,
            id_turma=1,
            nometurma='nome da turma',
            email='joseadolfojr@gmail.com',
            diavenc= '10',
            ativa='SIM',
            dtformatura=date(2016,12,31),
            multa=2.0,
            juros=6.0,
            entrada=1.0,
            saida=1.0
        )

    def test_create(self):
        self.assertTrue(Turma.objects.exists())

    def test_str(self):
        self.assertEqual('nome da turma', str(self.turma))
