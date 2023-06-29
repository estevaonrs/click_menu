from django.contrib.auth.models import User
from django.db import models

from core.models import BaseSuperModel


class Orders(BaseSuperModel):
    enable = models.BooleanField(
        verbose_name="Habilitar botão de pedidos pelo Whatsapp",
        default=False, db_index=True
    )

    OrdersPhone = models.CharField(
        verbose_name="Telefone que irá atender os pedidos",
        max_length=11)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.OrdersPhone

    class Meta:
        verbose_name_plural = 'Orders'
