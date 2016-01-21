# -*- coding: utf-8 -*-
__author__ = 'eldio'

from django import forms


class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))

    class Meta:
        fields = ('username', 'password')