from django.contrib import auth, messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import UsuarioForm
from .models import Perfil


def GeralAccounts(request):
    user = User.objects.all()
    context = {
        'user': user
    }
    return render(request, 'accounts/GeralAccounts.html', context)


class AccountsCreate(CreateView):
    template_name = "accounts/accounts_form.html"
    form_class = UsuarioForm
    model = User
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        url = super().form_valid(form)
        self.object.save()
        Perfil.objects.create(user=self.object)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Crie a sua conta"
        context["botao"] = "Cadastre-se"

        return context


class AccountsUpdate(UpdateView):
    template_name = "accounts/accounts_form.html"
    model = Perfil
    fields = ['full_name', 'cpf', 'cellphone']
    success_url = reverse_lazy('accounts:list_accounts')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Perfil, user=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Meus dados pessoais"
        context["botao"] = "Atualizar"

        return context


def logout(request):
    auth.logout(request)
    messages.add_message(request, constants.WARNING,
                         'Faça login antes de acessar a plataforma')
    return redirect('/accounts/login/')


class AccountsList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'accounts/list_accounts.html'

    def get_queryset(self):
        self.object_list = User.objects.filter(username=self.request.user)
        return self.object_list


def PasswordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Sua senha foi alterada com sucesso!")
        else:
            messages.error(request, 'Por favor, corrija o erro abaixo')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, "accounts/change_password.html", {
        'form': form
    })
