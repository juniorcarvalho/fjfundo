from django.conf.urls import url, include
from fjfundo.core.views import dashboard, inicio, account_edit, account_list
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', inicio, name='inicio'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^sair/$', logout,
        {'next_page': 'inicio'}, name='logout'),
    url(r'^account_edit/(?P<id>\d+)/$', account_edit, name='account_edit'),
    url(r'^account_list/$', account_list, name='account_list'),
    url(r'', include('fjfundo.mensalidades.urls')),
]


