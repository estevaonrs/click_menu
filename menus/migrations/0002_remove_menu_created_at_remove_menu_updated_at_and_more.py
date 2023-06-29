# Generated by Django 4.1.3 on 2023-01-18 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='updated_at',
        ),
        migrations.CreateModel(
            name='MenuName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(default='page-slug', max_length=150, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Nome do cardápio')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cardápios',
            },
        ),
    ]
