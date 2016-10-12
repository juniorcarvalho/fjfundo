from django import forms
from fjfundo.mensalidades.models import Turma


class TrocaTurmaForm(forms.Form):

    turmas = forms.ModelChoiceField(queryset=Turma.objects.all().order_by('nome_turma').values('id', 'nome_turma'),
                                    required=True, label='Turmas', empty_label=None)
