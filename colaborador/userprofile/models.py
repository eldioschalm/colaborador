# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from colaborador.banco.models import Banco

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, blank=False, null=False, verbose_name='CPF', unique=True)
    nit = models.CharField(max_length=14, verbose_name='NIT, antigo PIS/PASEP')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    banco = models.ForeignKey('banco.Banco')
    agencia = models.CharField(max_length=10, verbose_name='Agência Bancária')
    conta = models.CharField(max_length=10, verbose_name='Conta Corrente')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __unicode__(self):
        return self.user.first_name