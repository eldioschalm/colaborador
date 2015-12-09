# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpf', models.CharField(unique=True, max_length=14, verbose_name=b'CPF')),
                ('nit', models.CharField(max_length=14, verbose_name=b'NIT, antigo PIS/PASEP')),
                ('telefone', models.CharField(max_length=15, verbose_name=b'Telefone')),
                ('agencia', models.CharField(max_length=10, verbose_name=b'Ag\xc3\xaancia Banc\xc3\xa1ria')),
                ('conta', models.CharField(max_length=10, verbose_name=b'Conta Corrente')),
                ('banco', models.ForeignKey(to='banco.Banco')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
            },
        ),
    ]
