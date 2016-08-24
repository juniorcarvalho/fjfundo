from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import resolve_url as r
from django.template import RequestContext


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def inicio(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['id_username'], password=form.cleaned_data['id_password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(r('dashboard'))
    else:
        form = login
    return render_to_response('index.html', {
        'form': form,
    }, context_instance=RequestContext(request))
