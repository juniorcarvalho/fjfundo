from rest_framework import authentication, permissions, viewsets, filters
from fjfundo.mensalidades.models import Fundo
from fjfundo.api.serializers import FundoSerializer


class DefaultMixin(object):
    """configurações default para autenticacao, permissoes, filtragem e paginacao da view"""

    authentication_classes =(
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
    )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


class FundoViewSet(DefaultMixin, viewsets.ModelViewSet):
    """ EndPoint da API para listar e criar Fundos"""
    queryset = Fundo.objects.all()
    serializer_class = FundoSerializer
    search_fields = ('id', 'cnpj')


