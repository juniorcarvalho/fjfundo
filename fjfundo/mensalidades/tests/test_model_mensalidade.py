from datetime import date
from django.test import TestCase
from fjfundo.mensalidades.models import Associado, Turma, Fundo, Mensalidade


class MensalidadeModelTest(TestCase):
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
            diavenc='10',
            ativa='SIM',
            dtformatura=date(2016, 12, 31),
            multa=2.0,
            juros=6.0,
            entrada=1.0,
            saida=1.0
        )

        self.associado = Associado.objects.create(
            controle=1,
            id_associado=1,
            id_fundo=1,
            nomeassociado='Junior',
            logradouro='Rua',
            numero='numero',
            complemento='complemen',
            bairro='bairro',
            cidade='cidade',
            uf='uf',
            cep='12345678',
            email='joseadolfojr@gmail.com',
            cpf='00000000000',
            identidade='identidade',
            fone1='1111111111111',
            fone2='11111111111111',
            ctrl_turma=self.turma,
            id_turma=1,
            ativo='SIM',
            ctrl_perfil=1,
            codbanco='123'
        )

        self.mensalidade = Mensalidade.objects.create(
            id_mens=1,
            id_fundo=1,
            controle=self.associado,
            id_associado=1,
            historico='historico',
            parcela=1,
            numparcela='1',
            valor=1.0,
            vlrextra=1.1,
            acresdesc=1.0,
            vlrliquido=3.1,
            jurosdescbanco=0.0,
            vencimento=date(2016, 12, 31),
            controlebanco='controlebanco',
            pagamento=date(2016, 12, 31),
            formapagamento='forma de pagamento',
            lote='lote',
            baixa=date(2016, 12, 31),
            lotebaixa='lote baixa',
            codbarras='123',
            linhadigitavel='123',
            dtprocessamento=date(2016, 12, 31),
            id_contafd=1,
            despesabanco=1.0,
            funcbaixa=1
        )


    def test_create(self):
        self.assertTrue(Mensalidade.objects.exists())


    def test_str(self):
        self.assertEqual('historico', str(self.mensalidade))
