# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-25 04:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mensalidades', '0007_auto_20160825_0436'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='last_name',
        ),
        migrations.AddField(
            model_name='myuser',
            name='bairro',
            field=models.CharField(max_length=70, null=True, verbose_name='bairro'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='cep',
            field=models.CharField(max_length=8, null=True, verbose_name='cep'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='cidade',
            field=models.CharField(max_length=70, null=True, verbose_name='cidade'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='complemento',
            field=models.CharField(max_length=10, null=True, verbose_name='complemento'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='cpf',
            field=models.CharField(editable=False, max_length=14, null=True, verbose_name='cpf'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='fone1',
            field=models.CharField(max_length=14, null=True, verbose_name='telefone'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='fone2',
            field=models.CharField(max_length=14, null=True, verbose_name='telefone'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='identidade',
            field=models.CharField(editable=False, max_length=20, null=True, verbose_name='identidade'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='logradouro',
            field=models.CharField(max_length=70, null=True, verbose_name='logradouro'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='nome',
            field=models.CharField(max_length=50, null=True, verbose_name='nome'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='numero',
            field=models.CharField(max_length=10, null=True, verbose_name='número'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='turma',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='mensalidades.Turma'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='uf',
            field=models.CharField(max_length=2, null=True, verbose_name='uf'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(editable=False, max_length=254, unique=True, verbose_name='Email'),
        ),
    ]
