# Generated by Django 5.0.7 on 2024-07-27 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_remove_detalleventa_producto_id_dv_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalleventa',
            old_name='producto',
            new_name='producto_id_dv',
        ),
        migrations.RenameField(
            model_name='detalleventa',
            old_name='venta',
            new_name='venta_id_dv',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='cliente',
            new_name='cliente_id',
        ),
    ]
