# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Banco(models.Model):
    numero = models.IntegerField(verbose_name='Número do Banco', unique=True)
    nome = models.CharField(max_length=200, blank=False, null=False, verbose_name='Nome do Banco')