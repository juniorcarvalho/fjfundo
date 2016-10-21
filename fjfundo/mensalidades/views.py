from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, resolve_url as r
from fjfundo.mensalidades.models import Fundo, Turma, Financeiro
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


@login_required
def extrato(request, id_usr):

    user = get_object_or_404(MyUser, pk=id_usr)

    # proteções
    # usuário nivel 0, so pode ver seu próprio extrato
    if request.user.nivel == 0:
        if request.user.id != user.id:
            return HttpResponseRedirect(r('dashboard'))
    # usuário nivel 1, so pode ver extratos da propria turma
    elif request.user.nivel == 1:
        if user.turma.id != request.user.turma.id:
            return HttpResponseRedirect(r('account_list'))


    turma = MyUser.getTurma(request.user, request)

    context = {}
    context['turma'] = turma

    financeiro = Financeiro.objects.filter(usuario=user).order_by('-data_vencimento')
    context['dados'] = financeiro

    return render(request, 'extrato.html', context)
