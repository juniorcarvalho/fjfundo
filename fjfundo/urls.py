from django.conf.urls import url, include
from fjfundo.core.views import dashboard, inicio, account_edit, account_list, fim, password_reset, \
     password_reset_confirm


urlpatterns = [

    url(r'^$', inicio, name='inicio'),
    url(r'', include('fjfundo.mensalidades.urls')),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^sair/$', fim, name='logout'),
    url(r'^conta-edita/(?P<id>\d+)/$', account_edit, name='account_edit'),
    url(r'^conta-lista/$', account_list, name='account_list'),
    url(r'^nova-senha/$', password_reset, name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', password_reset_confirm,  name='password_reset_confirm'),



]


