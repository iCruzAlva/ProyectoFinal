# Generated by Django 2.2 on 2019-10-01 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinaria',
            name='estado',
            field=models.CharField(choices=[('alq', 'alquilado'), ('dis', 'disponible')], default='dis', max_length=3),
        ),
    ]