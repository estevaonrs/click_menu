# Generated by Django 4.1.3 on 2023-01-05 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('establishments', '0015_alter_establishmentscategories_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Establishments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado às')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado às')),
                ('EstablishmentsCategory', models.CharField(blank=True, default='', max_length=30, verbose_name='Categoria do estabelecimento')),
                ('Establishment', models.CharField(max_length=100, verbose_name='Nome do estabelecimento')),
                ('description', models.CharField(max_length=500, verbose_name='Descreva seu estabelecimento')),
                ('image', models.ImageField(blank=True, default='', upload_to='establishments_images/%Y/%m/', verbose_name='Imagem')),
                ('adress', models.CharField(max_length=50, verbose_name='Endereço')),
                ('house_number', models.CharField(max_length=5, verbose_name='Número')),
                ('complement', models.CharField(max_length=100, verbose_name='Complemento')),
                ('district', models.CharField(max_length=30, verbose_name='Bairro')),
                ('zip_code', models.CharField(max_length=8, verbose_name='CEP')),
                ('city', models.CharField(max_length=30, verbose_name='Cidade')),
                ('state', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='SP', max_length=2, verbose_name='estado')),
                ('cellphone', models.CharField(max_length=11, verbose_name='Celular com DDD')),
                ('telephone', models.CharField(blank=True, default='', max_length=8, verbose_name='Telefone')),
                ('email', models.CharField(blank=True, default='', max_length=50, verbose_name='E-mail')),
                ('days', models.CharField(choices=[('Domingo', 'Domingo'), ('Segunda-feira', 'Segunda-feira'), ('Terça-feira', 'Terça-feira'), ('Quarta-feira', 'Quarta-feira'), ('Quinta-feira', 'Quinta-feira'), ('Sexta-feira', 'Sexta-feira'), ('Sábado', 'Sábado'), ('Segunda a sexta', 'Segunda a sexta'), ('Segunda a sábado', 'Segunda a sábado'), ('Todos os dias', 'Todos os dias')], default='Escolha', max_length=16, verbose_name='Dias da semana')),
                ('opening_time', models.TimeField(verbose_name='Abertura')),
                ('closing_time', models.TimeField(verbose_name='Fechamento')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='EstablishmentsAdress',
        ),
        migrations.RemoveField(
            model_name='establishmentscategories',
            name='user',
        ),
        migrations.DeleteModel(
            name='EstablishmentsContacts',
        ),
        migrations.DeleteModel(
            name='EstablishmentsOpeningHours',
        ),
        migrations.RemoveField(
            model_name='establishmentsprofile',
            name='author',
        ),
        migrations.RemoveField(
            model_name='establishmentsprofile',
            name='establishmentscategories',
        ),
        migrations.DeleteModel(
            name='EstablishmentsCategories',
        ),
        migrations.DeleteModel(
            name='EstablishmentsProfile',
        ),
    ]
