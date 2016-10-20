from django.conf.urls import url

from fjfundo.mensalidades.views import fundo_list, turma_list, turma_select

urlpatterns = [
    url(r'^fundo_list/$', fundo_list, name='fundo_list'),
    url(r'^turma_list/$', turma_list, name='turma_list'),
    url(r'^turma_select/$', turma_select, name='turma_select'),
]


