# Generated by Django 4.1.2 on 2022-10-19 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0010_establishmentsprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishmentsprofile',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='cardapio-online-novo/covers/%Y/%m/%d/', verbose_name='Imagem'),
        ),
    ]