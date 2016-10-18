from datetime import date
from django.test import TestCase
from fjfundo.mensalidades.models import Fundo, Turma
from fjfundo.mensalidades.forms import TrocaTurmaForm

class TrocaTurmaFormTest(TestCase):
    def setUp(self):
        self.form = TrocaTurmaForm()

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

    def test_str_turma(self):
        field = self.form.fields['turmas']
        self.assertEqual('nome da turma', field.choices.queryset[0].nome_turma)

    def test_as_p(self):
        str_form_as_p = self.form.as_p()
        str_as_p= '<p><label for="id_turmas">Turmas:</label> <select id="id_turmas" name="turmas">\n<option value="1">nome da turma</option>\n</select></p>'
        self.assertEqual(str_as_p, str_form_as_p)
