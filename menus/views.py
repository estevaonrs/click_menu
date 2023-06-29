from pathlib import Path

import qrcode
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from wkhtmltopdf.views import PDFTemplateResponse

from menus.models import Menu, MenuName
from menus.utils import GeraPDFMixin


def QrCode(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        url = request.POST.get('link')

        home = Path.home()
        path_imagem = home / "Downloads"

        if url != '':
            img = qrcode.make(url)

            img.save(f"{path_imagem}/{nome}.png")

    return render(request, 'menus/qrcode.html')


@login_required(login_url="/accounts/login")
def GeralMenu(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus
    }
    return render(request, 'menu.html', context)



class MenuCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    model = Menu
    fields = ['image_item', 'item_name',
              'category', 'value', 'item_description']
    success_url = reverse_lazy('menus:see_menuname')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        return url


class MenuUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('accounts:login')
    model = Menu
    fields = ['image_item', 'item_name',
              'category', 'value', 'item_description']
    success_url = reverse_lazy('menus:see_menuname')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Menu, pk=self.kwargs['pk'], user=self.request.user)
        return self.object


class MenuDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    queryset = Menu.objects.all()
    success_url = reverse_lazy('menus:see_menuname')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Menu, pk=self.kwargs['pk'], user=self.request.user)
        return self.object


@login_required(login_url="/accounts/login")
def SeeMenuName(request):
    all_menuname = MenuName.objects.filter(user=request.user)
    menus = Menu.objects.filter(user=request.user)

    context = {
        'menus': menus,
        'all_menuname': all_menuname
    }

    return render(request, 'menus/SeeMenuName.html', context)


class MenuNameCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    model = MenuName
    fields = ['title']
    success_url = reverse_lazy('menus:see_menuname')

    def form_valid(self, form):
        form.instance.user = self.request.user

        url = super().form_valid(form)

        return url


class MenuNameDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    queryset = MenuName.objects.all()
    success_url = reverse_lazy('menus:see_menuname')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            MenuName, slug=self.kwargs['slug'], user=self.request.user)
        return self.object


def post_detail(request, slug):
    all_menuname = MenuName.objects.filter(user=request.user.id)
    menus = Menu.objects.filter(user=request.user.id)
    unique_slug = get_object_or_404(MenuName, slug=slug)
    return render(request, "menus/menuname_detail.html", {"menunames": unique_slug, 'all_menuname': all_menuname, 'menus': menus})


def public_menu(request, slug):
    unique_slug = get_object_or_404(MenuName, slug=slug)
    menus = Menu.objects.filter(user=unique_slug.user)
    all_menuname = MenuName.objects.filter(user=unique_slug.user)
    return render(request, "menus/menuname_detail_public.html", {
        "all_menuname":all_menuname,
        "menunames": unique_slug,
        "menus": menus,
    })


