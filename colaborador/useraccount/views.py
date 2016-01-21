# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from colaborador.useraccount.forms import UserForm
from django.forms.forms import NON_FIELD_ERRORS


# Create your views here.

def auth_login(request):
    if request.user.is_authenticated():
        return redirect('colaborador.core.views.landinpage')
    else:
        if request.method == 'POST':
            # print request.POST.getlist #imprime lista de variáveis do método post do formulário
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            form = UserForm(request.POST)

            try:
                user = authenticate(username=username, password=password)
            except AssertionError:
                form.full_clean()
                form._errors[NON_FIELD_ERRORS] = u'Erro na autenticação'
                return render(request, 'useraccount/login.html', {'form': form})

            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('colaborador.core.views.landinpage')
                else:
                    # Return a 'disabled account' error message
                    form.full_clean()
                    form._errors[NON_FIELD_ERRORS] = u'Usuário bloqueado'
                    return render(request, 'useraccount/login.html', {'form': form})
            else:
                # Return an 'invalid login' error message.
                form.full_clean()
                form._errors[NON_FIELD_ERRORS] = u'Usuário ou senha incorretos'
                return render(request, 'useraccount/login.html', {'form': form})
        else:
            form = UserForm()
            return render(request, 'useraccount/login.html', {'form': form})


def auth_logout(request):
    logout(request) #desloga
    return redirect('colaborador.core.views.landinpage')
    # tipos de mensagem: alert-success, alert-info, alert-warning, alert-danger