from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import resolve_url as r
from django.template import RequestContext
from fjfundo.core.forms import LoginForm
from fjfundo.core.forms import EditAccountForm
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
                    return HttpResponseRedirect(r('dashboard'))
    else:
        form = LoginForm()
    return render_to_response('index.html', {
        'form': form,
    }, context_instance=RequestContext(request))


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def account_edit(request, id):
    context = {}
    user = get_object_or_404(MyUser, pk=id)
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
    users = MyUser.objects.filter(turma=request.user.turma).order_by('nome')
    return render(request, 'account_list.html', {'users': users})
