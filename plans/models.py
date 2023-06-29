from core.models import BaseSuperModel
from django.db import models


class Subscriber(BaseSuperModel):
    name = models.CharField(verbose_name="Nome",
                            max_length=32, null=False, blank=True)
    phone = models.CharField(verbose_name="Telefone",
                             max_length=11, null=True, blank=True)
    email = models.EmailField(verbose_name="E-mail", null=True, blank=True)
    plans = models.ForeignKey("Plano", on_delete=models.SET_NULL,
                              null=True,)
    start_date = models.DateField(
        verbose_name="Data da assinatura", null=False, blank=False)
    due_date = models.DateField(
        verbose_name="Vencimento", null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Subscribers"



class Plano(models.Model):
    TIPOS_PLANO = (
        ('gold', 'Gold'),
        ('platina', 'Platina'),
        ('diamante', 'Diamante'),
    )

    tipo = models.CharField(max_length=10, choices=TIPOS_PLANO)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    duracao_dias = models.PositiveIntegerField()
    
    def __str__(self):
        return self.tipo


