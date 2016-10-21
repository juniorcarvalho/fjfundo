from django.conf.urls import url, include
from fjfundo.core.views import dashboard, inicio, account_edit, account_list, fim


urlpatterns = [
    url(r'^$', inicio, name='inicio'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^sair/$', fim, name='logout'),
    url(r'^account_edit/(?P<id>\d+)/$', account_edit, name='account_edit'),
    url(r'^account_list/$', account_list, name='account_list'),
    url(r'', include('fjfundo.mensalidades.urls')),
]


