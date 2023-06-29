from django.contrib.auth.models import User
from django.db import models

from core.models import BaseSuperModel


class Establishment(BaseSuperModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    establishments_category = models.CharField(
        verbose_name='Categoria do estabelecimento',
        max_length=30, blank=True, default='')

    establishment = models.CharField(
        verbose_name="Nome do estabelecimento", max_length=100)

    description = models.CharField(
        verbose_name="Descreva seu estabelecimento", max_length=500)

    adress = models.CharField(verbose_name="Endereço", max_length=50)

    house_number = models.CharField(verbose_name="Número", max_length=5)

    complement = models.CharField(verbose_name="Complemento", max_length=100)

    district = models.CharField(verbose_name="Bairro", max_length=30)

    zip_code = models.CharField(verbose_name="CEP", max_length=9)

    city = models.CharField(verbose_name="Cidade", max_length=30)

    state = models.CharField(verbose_name="estado",
                             max_length=2,
                             default='SP',
                             choices=(
                                 ('AC', 'Acre'),
                                 ('AL', 'Alagoas'),
                                 ('AP', 'Amapá'),
                                 ('AM', 'Amazonas'),
                                 ('BA', 'Bahia'),
                                 ('CE', 'Ceará'),
                                 ('DF', 'Distrito Federal'),
                                 ('ES', 'Espírito Santo'),
                                 ('GO', 'Goiás'),
                                 ('MA', 'Maranhão'),
                                 ('MT', 'Mato Grosso'),
                                 ('MS', 'Mato Grosso do Sul'),
                                 ('MG', 'Minas Gerais'),
                                 ('PA', 'Pará'),
                                 ('PB', 'Paraíba'),
                                 ('PR', 'Paraná'),
                                 ('PE', 'Pernambuco'),
                                 ('PI', 'Piauí'),
                                 ('RJ', 'Rio de Janeiro'),
                                 ('RN', 'Rio Grande do Norte'),
                                 ('RS', 'Rio Grande do Sul'),
                                 ('RO', 'Rondônia'),
                                 ('RR', 'Roraima'),
                                 ('SC', 'Santa Catarina'),
                                 ('SP', 'São Paulo'),
                                 ('SE', 'Sergipe'),
                                 ('TO', 'Tocantins'),
                             )
                             )

    cellphone = models.CharField(verbose_name="Celular com DDD", max_length=16)

    telephone = models.CharField(
        verbose_name="Telefone", max_length=9, blank=True, default='')

    email = models.CharField(verbose_name="E-mail",
                             max_length=50, blank=True, default='')

    days = models.CharField(verbose_name="Dias de funcionamento",
                            max_length=16,
                            default='Escolha',
                            choices=(
                                ('Domingo', 'Domingo'),
                                ('Segunda-feira', 'Segunda-feira'),
                                ('Terça-feira', 'Terça-feira'),
                                ('Quarta-feira', 'Quarta-feira'),
                                ('Quinta-feira', 'Quinta-feira'),
                                ('Sexta-feira', 'Sexta-feira'),
                                ('Sábado', 'Sábado'),
                                ('Segunda a sexta', 'Segunda a sexta'),
                                ('Segunda a sábado', 'Segunda a sábado'),
                                ('Todos os dias', 'Todos os dias'),
                            )
                            )
    opening_time = models.TimeField(
        verbose_name='Abertura', auto_now_add=False)

    closing_time = models.TimeField(
        verbose_name='Fechamento', auto_now_add=False)
