# Generated by Django 3.0 on 2020-09-16 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autoevaluacion', '0003_remove_autoevaluaciones_relacion_usuario'),
        ('usuarios', '0003_auto_20200914_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='autoevaluacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test', to='autoevaluacion.Autoevaluaciones'),
        ),
    ]