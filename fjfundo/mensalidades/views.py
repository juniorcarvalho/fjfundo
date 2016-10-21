from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from fjfundo.mensalidades.models import Fundo, Turma
from fjfundo.mensalidades.forms import TrocaTurmaForm
from fjfundo.core.models import MyUser


@login_required
def fundo_list(request):
    if request.user.nivel == 3:
        fundo = Fundo.objects.all().order_by('nome_fundo')
        return render(request, 'fundo_list.html', {'fundos': fundo})
    else:
        return render(request, 'dashboard.html', {'turma': MyUser.getTurma(request.user)})


@login_required
def turma_list(request):
    if request.user.nivel == 3:
        turma = Turma.objects.all().order_by('fundo', 'nome_turma')
        return render(request, 'turma_list.html', {'turmas': turma})
    else:
        return render(request, 'dashboard.html', {'turma': MyUser.getTurma(request.user, request)})


@login_required
def turma_select(request):
    if request.method == 'POST':
        form = TrocaTurmaForm(request.POST)
        if form.is_valid():
            turma = form.cleaned_data['turmas']
            request.session['turma_id'] = turma.id
            return render(request, 'dashboard.html', {'turma': MyUser.getTurma(request.user, request)})

    if request.method == 'GET':
        form = TrocaTurmaForm()
        return HttpResponse(form)
