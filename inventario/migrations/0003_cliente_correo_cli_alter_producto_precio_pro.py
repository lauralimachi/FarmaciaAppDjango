# Generated by Django 5.0.7 on 2024-07-27 01:48

import inventario.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_producto_created_pro_producto_update_pro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='correo_cli',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_pro',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[inventario.validators.validar_par]),
        ),
    ]
