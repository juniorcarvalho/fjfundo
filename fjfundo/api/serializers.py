from rest_framework import serializers
from fjfundo.mensalidades.models import Fundo


class FundoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundo
        fields = ('id', 'nome_fundo', 'data_inicial', 'data_final', 'cnpj')

