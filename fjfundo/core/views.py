from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, resolve_url as r
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from fjfundo.core.forms import LoginForm, EditAccountForm, PasswordResetForm
from fjfundo.core.models import MyUser


def inicio(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['email'], password=form.cleaned_data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['turma_id'] = MyUser.getTurmaId(user)
                    return HttpResponseRedirect(r('dashboard'))
    else:
        form = LoginForm()
    return render_to_response('index.html', {
        'form': form,
    }, context_instance=RequestContext(request))


def fim(request):
    logout(request)
    try:
        del request.session['turma_id']
    except KeyError:
        pass
    return HttpResponseRedirect(r('inicio'))

@login_required
def dashboard(request):
    turma = MyUser.getTurma(request.user, request)
    return render(request, 'dashboard.html', {'turma': turma})


@login_required
def account_edit(request, id):
    user = get_object_or_404(MyUser, pk=id)

    # proteções
    # usuário nivel 0, so pode editar seu próprio cadastro
    if request.user.nivel == 0:
        if request.user.id != user.id:
            return HttpResponseRedirect(r('dashboard'))
    # usuário nivel 1, so pode editar cadastros da propria turma
    elif request.user.nivel == 1:
        if user.turma.id != request.user.turma.id:
            return HttpResponseRedirect(r('account_list'))

    turma = MyUser.getTurma(request.user, request)

    context = {}
    context['turma'] = turma
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=user)
    context['form'] = form
    return render(request, 'account_edit.html', context)


@login_required
def account_list(request):
    turma = MyUser.getTurma(request.user, request)
    context = {}
    context['turma'] = turma
    users = MyUser.objects.filter(turma=turma).order_by('nome')
    context['users'] = users
    return render(request, 'account_list.html', context)


def password_reset(request):
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, 'password_reset.html', context)


# def password_reset_confirm(request, key):
#     pass
