import uuid
from audioop import reverse

from django.contrib.auth.models import User
from django.db import models


class MenuName(models.Model):

    id = models.AutoField(
        primary_key=True,
    )

    slug = models.SlugField(
        max_length=150,
        unique=True,
        default='page-slug'
    )
    title = models.CharField(verbose_name="Nome do cardápio",
                             max_length=100,
                             blank=True,)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cardápios'

    def save(self, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4()
        super().save(**kwargs)


class Menu(models.Model):

    image_item = models.ImageField(verbose_name='Imagem do item',
                                   upload_to='menus_images/%Y/%m/',
                                   blank=False, default='')
    item_name = models.CharField(verbose_name="Nome do item", max_length=100,
                                 blank=True,)
    category = models.CharField(verbose_name='Categoria', max_length=100)
    value = models.FloatField(verbose_name="Valor",
                              blank=True,)
    item_description = models.CharField(
        verbose_name="Descrição", max_length=200,
        blank=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Menus'
        ordering = ['category']

    def get_absolute_url(self):
        return reverse("editar", kwargs={"menu_pk": self.id})

    def __str__(self):
        return self.item_name
