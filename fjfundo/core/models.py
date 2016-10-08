from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from fjfundo.mensalidades.models import Turma


class MyUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs["email"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:
            raise ValueError(_('Informe o endereço de email.'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('Email'),
        unique=True
    )
    turma = models.ForeignKey(Turma, null=True)
    cpf = models.CharField(verbose_name='cpf', max_length=14, null=True)
    identidade = models.CharField(verbose_name='identidade', max_length=20, null=True)
    nome = models.CharField(verbose_name='nome', max_length=50, null=True)
    logradouro = models.CharField(verbose_name='logradouro', max_length=70, null=True)
    numero = models.CharField(verbose_name='número', max_length=10, null=True)
    complemento = models.CharField(verbose_name='complemento', max_length=10, null=True)
    bairro = models.CharField(verbose_name='bairro', max_length=70, null=True)
    cidade = models.CharField(verbose_name='cidade', max_length=70, null=True)
    uf = models.CharField(verbose_name='uf', max_length=2, null=True)
    cep = models.CharField(verbose_name='cep', max_length=8, null=True)
    fone1 = models.CharField(verbose_name='telefone', max_length=14, null=True)
    fone2 = models.CharField(verbose_name='celular', max_length=14, null=True, blank=True)
    nivel = models.IntegerField(verbose_name='nível', null=True)
    # nivel= 0.Associado, 1.Associado Administrador 2.Coloborador

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'