# Generated by Django 4.1.3 on 2023-01-12 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0022_alter_establishment_adress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='days',
            field=models.CharField(choices=[('Domingo', 'Domingo'), ('Segunda-feira', 'Segunda-feira'), ('Terça-feira', 'Terça-feira'), ('Quarta-feira', 'Quarta-feira'), ('Quinta-feira', 'Quinta-feira'), ('Sexta-feira', 'Sexta-feira'), ('Sábado', 'Sábado'), ('Segunda a sexta', 'Segunda a sexta'), ('Segunda a sábado', 'Segunda a sábado'), ('Todos os dias', 'Todos os dias')], default='Escolha', max_length=16, verbose_name='Dias de funcionamento'),
        ),
    ]
