# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Banco(models.Model):
    numero = models.IntegerField(verbose_name='Número do Banco', unique=True)
    nome = models.CharField(max_length=200, blank=False, null=False, verbose_name='Nome do Banco')

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'

    def __unicode__(self):
        return self.nome