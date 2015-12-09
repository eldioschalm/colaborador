# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from colaborador.userprofile.models import UserProfile
from colaborador.userprofile.forms import UserProfileForm


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    form = UserProfileForm
    verbose_name_plural = 'Perfis'


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)