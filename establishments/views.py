from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from establishments.models import Establishment


@login_required(login_url="/accounts/login")
def GeralEstablishments(request):
    establishment = Establishment.objects.all()
    context = {
        'establishment': establishment
    }
    return render(request, 'establishment.html', context)


class EstablishmentCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    model = Establishment
    fields = ['establishments_category', 'establishment', 'description',
              'adress', 'house_number', 'complement', 'district',
              'zip_code', 'city', 'state', 'cellphone', 'telephone',
              'email', 'days', 'opening_time', 'closing_time']
    success_url = reverse_lazy('establishment:list_establishment')

    def form_valid(self, form):
        form.instance.user = self.request.user

        url = super().form_valid(form)

        return url


class EstablishmentUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('accounts:login')
    model = Establishment
    fields = ['establishments_category', 'establishment', 'description',
              'adress', 'house_number', 'complement', 'district',
              'zip_code', 'city', 'state', 'cellphone', 'telephone',
              'email', 'days', 'opening_time', 'closing_time']
    success_url = reverse_lazy('establishment:list_establishment')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Establishment, pk=self.kwargs['pk'], user=self.request.user)
        return self.object


class EstablishmentList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('accounts:login')
    model = Establishment
    template_name = 'establishments/list_establishment.html'

    def get_queryset(self):
        self.object_list = Establishment.objects.filter(user=self.request.user)
        return self.object_list


class EstablishmentDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('accounts:login')
    queryset = Establishment.objects.all()
    success_url = reverse_lazy('establishment:list_establishment')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Establishment, pk=self.kwargs['pk'], user=self.request.user)
        return self.object
