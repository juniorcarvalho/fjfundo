from django.db import models
from django.conf import settings


class Fundo(models.Model):
    nome_fundo = models.CharField(max_length=80, null=True)
    data_inicial = models.DateField(null=True)
    data_final = models.DateField(null=True)
    cnpj = models.CharField(max_length=18, null=True)

    class Meta:
        verbose_name = 'fundo'
        verbose_name_plural = 'fundos'

    def __str__(self):
        return self.nome_fundo


class Turma(models.Model):
    fundo = models.ForeignKey('Fundo')
    nome_turma = models.CharField(max_length=40, null=True)
    dia_venc = models.CharField(max_length=2, null=True)
    data_formatura = models.DateField(null=True)
    valor_multa = models.FloatField(null=True)
    valor_juros = models.FloatField(null=True)

    class Meta:
        verbose_name = 'turma'
        verbose_name_plural = 'turmas'

    def listaTurmas(self):
        return Turma.objects.all().order_by('nome_turma')

    def __str__(self):
        return self.nome_turma


class Financeiro(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Associado')
    nrodoc = models.CharField(max_length=10, null=True)
    parcela = models.IntegerField(null=True)
    valor = models.FloatField(null=True)
    valor_extra = models.FloatField(null=True)
    valor_acresdesc = models.FloatField(null=True)
    valor_liquido = models.FloatField(null=True)
    valor_jurdescbco = models.FloatField(null=True)
    valor_despbco = models.FloatField(null=True)
    data_vencimento = models.DateField(null=True)
    data_pagamento = models.DateField(null=True)
    data_proc = models.DateField(null=True)

    class Meta:
        verbose_name = 'Financeiro'
        verbose_name_plural = 'Financeiro'

    # def __str__(self):
    #     return self.historico

