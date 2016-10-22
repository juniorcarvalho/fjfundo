from django.conf.urls import url

from fjfundo.mensalidades.views import fundo_list, turma_list, turma_select, extrato

urlpatterns = [
    url(r'^fundo-lista/$', fundo_list, name='fundo_list'),
    url(r'^turma-lista/$', turma_list, name='turma_list'),
    url(r'^turma-seleciona/$', turma_select, name='turma_select'),
    url(r'^extrato/(?P<id_usr>\d+)/$', extrato, name='extrato')
]


