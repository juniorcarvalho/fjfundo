from django import forms
from fjfundo.mensalidades.models import Turma


class TrocaTurmaForm(forms.Form):

    turmas = forms.ChoiceField(choices=Turma.objects.all().order_by('nome_turma'),
                               required=True, label='Turmas')

