# Generated by Django 4.1.2 on 2022-11-17 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebFinal', '0005_alter_empleado_legajo_carrito'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carrito',
            new_name='Ventas',
        ),
        migrations.AlterField(
            model_name='empleado',
            name='legajo',
            field=models.IntegerField(),
        ),
    ]
