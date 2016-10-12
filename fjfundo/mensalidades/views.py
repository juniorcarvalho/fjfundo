from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from fjfundo.mensalidades.models import Fundo, Turma
from fjfundo.mensalidades.forms import TrocaTurmaForm


@login_required
def fundo_list(request):
    if request.user.nivel == 3:
        fundo = Fundo.objects.all().order_by('nome_fundo')
        return render(request, 'fundo_list.html', {'fundos': fundo})
    else:
        return render(request, 'dashboard.html')

@login_required
def turma_list(request):
    if request.user.nivel == 3:
        turma = Turma.objects.all().order_by('fundo', 'nome_turma')
        return render(request, 'turma_list.html', {'turmas': turma})
    else:
        return render(request, 'dashboard.html')

@login_required
def turma_select(request):
    form = TrocaTurmaForm()
