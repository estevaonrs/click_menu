# Generated by Django 4.1.2 on 2022-10-19 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='establishmentsadress',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='establishmentsadress',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='establishmentscategories',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='establishmentscategories',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='establishmentscontacts',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='establishmentscontacts',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='establishmentsopeninghours',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='establishmentsopeninghours',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='establishmentsprofile',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='establishmentsprofile',
            name='deleted_at',
        ),
    ]
