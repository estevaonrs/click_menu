from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    full_name = models.CharField(
        max_length=50, null=True, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, null=True, verbose_name="CPF")
    cellphone = models.CharField(
        max_length=16, null=True, verbose_name="Celular com DDD")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
