from django.db import models


class Fundo(models.Model):
    id_fundo = models.IntegerField(primary_key=True)
    id_empresa = models.IntegerField(null=True)
    nomefundo = models.CharField(max_length=80, null=True)
    dtinicial = models.DateField(null=True)
    dtfinal = models.DateField(null=True)
    vlrmensalidade = models.FloatField(null=True)
    diavencimento = models.CharField(max_length=2, null=True)
    gestor = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    cnpj = models.CharField(max_length=18, null=True)
    multa = models.FloatField(null=True)
    juro = models.FloatField(null=True)

    class Meta:
        verbose_name = 'fundo'
        verbose_name_plural = 'fundos'

    def __str__(self):
        return self.nomefundo


class Turma(models.Model):
    SIMNAO = (
        ('SIM', 'SIM'),
        ('NAO', 'NAO')
    )

    ctrl_turma = models.IntegerField(primary_key=True)
    id_fundo = models.ForeignKey('Fundo')
    id_turma = models.IntegerField(null=True)
    nometurma = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True)
    diavenc = models.CharField(max_length=2, null=True)
    ativa = models.CharField(max_length=3, choices=SIMNAO)
    dtformatura = models.DateField(null=True)
    multa = models.FloatField(null=True)
    juros = models.FloatField(null=True)
    entrada = models.FloatField(null=True)
    saida = models.FloatField(null=True)

    class Meta:
        verbose_name = 'turma'
        verbose_name_plural = 'turmas'

    def __str__(self):
        return self.nometurma


class Associado(models.Model):
    SIMNAO = (
        ('SIM', 'SIM'),
        ('NAO', 'NAO')
    )

    controle = models.IntegerField(primary_key=True)
    id_associado = models.IntegerField(null=True)
    id_fundo = models.IntegerField(null=True)
    nomeassociado = models.CharField(max_length=50, null=True)
    logradouro = models.CharField(max_length=70, null=True)
    numero = models.CharField(max_length=10, null=True)
    complemento = models.CharField(max_length=10, null=True)
    bairro = models.CharField(max_length=70, null=True)
    cidade = models.CharField(max_length=70, null=True)
    uf = models.CharField(max_length=2, null=True)
    cep = models.CharField(max_length=8, null=True)
    email = models.EmailField(null=True)
    cpf = models.CharField(max_length=14, null=True)
    identidade = models.CharField(max_length=20, null=True)
    fone1 = models.CharField(max_length=13)
    fone2 = models.CharField(max_length=14)
    ctrl_turma = models.ForeignKey('Turma')
    id_turma = models.IntegerField(null=True)
    ativo = models.CharField(max_length=3, choices=SIMNAO)
    ctrl_perfil = models.IntegerField(null=True)
    codbanco = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'associado'
        verbose_name_plural = 'associados'

    def __str__(self):
        return self.nomeassociado


class Mensalidade(models.Model):
    id_mens = models.IntegerField(primary_key=True)
    id_fundo = models.IntegerField(null=True)
    controle = models.ForeignKey('Associado')
    id_associado = models.IntegerField(null=True)
    historico = models.CharField(max_length=60, null=True)
    parcela = models.IntegerField(null=True)
    numparcela = models.CharField(max_length=10)
    valor = models.FloatField(null=True)
    vlrextra = models.FloatField(null=True)
    acresdesc = models.FloatField(null=True)
    vlrliquido = models.FloatField(null=True)
    jurosdescbanco = models.FloatField(null=True)
    vencimento = models.DateField(null=True)
    controlebanco = models.CharField(max_length=30, null=True)
    pagamento = models.DateField(null=True)
    formapagamento = models.CharField(max_length=30)
    lote = models.CharField(max_length=20)
    baixa = models.DateField(null=True)
    lotebaixa = models.CharField(max_length=20, null=True)
    codbarras = models.CharField(max_length=54, null=True)
    linhadigitavel = models.CharField(max_length=54, null=True)
    dtprocessamento = models.DateField(null=True)
    id_contafd = models.IntegerField(null=True)
    despesabanco = models.FloatField(null=True)
    funcbaixa = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'associado'
        verbose_name_plural = 'associados'

    def __str__(self):
        return self.historico

