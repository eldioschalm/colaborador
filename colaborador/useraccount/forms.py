# -*- coding: utf-8 -*-
__author__ = 'eldio'

from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'}), label=u'Usuário')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}), label=u'Senha')

    class Meta:
        fields = ('username', 'password')


class UserCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}), label=u'Nome')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}), label=u'Sobrenome')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'}), label=u'Usuário')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}), label=u'Senha')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), label=u'Email')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')