# Generated by Django 3.0 on 2020-09-14 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cumpleanio',
        ),
        migrations.AddField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(null=True, verbose_name='Año de Nacimiento'),
        ),
    ]
