# -*- coding: utf-8 -*-
__author__ = 'eldio'

from django import forms
from django.forms import ModelForm
from colaborador.userprofile.models import UserProfile

class UserProfileForm(ModelForm):
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js',
            '/static/js/jquery.maskedinput.min.js',
            '/static/js/fields_mask.js',
        )