from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.shortcuts import resolve_url as r
from django.template import RequestContext
from fjfundo.core.forms import LoginForm
from fjfundo.core.forms import EditAccountForm


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
def edit_account(request):
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, 'edit_account.html', context)
