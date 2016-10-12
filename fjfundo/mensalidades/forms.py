from django import forms
from fjfundo.mensalidades.models import Turma


class TrocaTurmaForm(forms.Form):

    turmas = forms.ChoiceField(choices=Turma.listaTurmas, required=True, label='Turmas')
