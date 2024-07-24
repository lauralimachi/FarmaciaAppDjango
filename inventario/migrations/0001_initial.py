# Generated by Django 5.0.7 on 2024-07-23 01:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cli', models.CharField(max_length=255)),
                ('documento_cli', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pro', models.CharField(max_length=255)),
                ('descripcion_pro', models.CharField(max_length=255)),
                ('precio_pro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad_pro', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_inv', models.IntegerField()),
                ('producto_id_inv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vta', models.DateField()),
                ('total_vta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_dv', models.IntegerField()),
                ('precio_unitario_dv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_linea', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto_id_dv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.producto')),
                ('venta_id_dv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.venta')),
            ],
        ),
    ]