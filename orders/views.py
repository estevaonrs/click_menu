from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from orders.models import Orders


@login_required(login_url="/accounts/login")
def GeralOrders(request):
    orders = Orders.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'orders.html', context)


class OrdersCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    model = Orders
    fields = ['enable', 'OrdersPhone']
    success_url = reverse_lazy('orders:list_orders')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        return url


class OrdersUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('accounts:login')
    model = Orders
    fields = ['enable', 'OrdersPhone']
    success_url = reverse_lazy('orders:list_orders')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Orders, pk=self.kwargs['pk'], user=self.request.user)
        return self.object


class OrdersList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('accounts:login')
    model = Orders
    template_name = 'orders/list_orders.html'

    def get_queryset(self):
        self.object_list = Orders.objects.filter(user=self.request.user)
        return self.object_list


class OrdersDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('accounts:login')
    queryset = Orders.objects.all()
    success_url = reverse_lazy('orders:list_orders')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Orders, pk=self.kwargs['pk'], user=self.request.user)
        return self.object
