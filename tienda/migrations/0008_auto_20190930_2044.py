# Generated by Django 2.2 on 2019-10-01 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_maquinaria_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinaria',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
