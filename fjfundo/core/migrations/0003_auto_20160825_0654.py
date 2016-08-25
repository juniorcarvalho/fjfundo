# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-25 06:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160825_0449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': 'usuário', 'verbose_name_plural': 'usuários'},
        ),
        migrations.AlterField(
            model_name='myuser',
            name='cpf',
            field=models.CharField(max_length=14, null=True, verbose_name='cpf'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='identidade',
            field=models.CharField(max_length=20, null=True, verbose_name='identidade'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mensalidades.Turma'),
        ),
    ]
