# Generated by Django 4.1.3 on 2023-01-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0020_alter_establishment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='adress',
            field=models.CharField(max_length=500, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='cellphone',
            field=models.CharField(max_length=500, verbose_name='Celular com DDD'),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='city',
            field=models.CharField(max_length=500, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='complement',
            field=models.CharField(max_length=500, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='district',
            field=models.CharField(max_length=500, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='email',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='house_number',
            field=models.CharField(max_length=500, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='telephone',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='zip_code',
            field=models.CharField(max_length=500, verbose_name='CEP'),
        ),
    ]