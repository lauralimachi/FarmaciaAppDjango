from django.db import models
from .validators import validar_par
from django.core.validators import EmailValidator
from inventario import validators

# Create your models here.
# class Proveedores(models.Model):
#     nombre_prov = models.CharField(max_length=255) not null
#     direccion_prov = models.CharField(max_length=255)
#     telefono_prov = models.CharField(max_length=255)


#     def __str__(self):
#         return f'Proveedor {self.id}: {self.nombre_prov} {self.telefono_prov}'

class Producto(models.Model):
    nombre_pro = models.CharField(max_length=255)
    descripcion_pro = models.TextField()
    precio_pro = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_pro = models.IntegerField()
    created_pro = models.DateTimeField(auto_now_add=True)
    update_pro = models.DateTimeField(auto_now=True)
    # proveedor_id_pro = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Producto {self.id}: {self.nombre_pro} {self.precio_pro}'

class Inventario(models.Model):
    cantidad_inv = models.IntegerField()
    producto_id_inv = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)


class Cliente(models.Model):
    nombre_cli = models.CharField(max_length=255)
    documento_cli = models.CharField(max_length=255)
    correo_cli =  models.EmailField(null=True, blank=True)

class MonedaUnits(models.TextChoices):
    Bol = 'BS', 'Bolivianos'
    Dol = 'USD', 'Dolares'

class Venta(models.Model):
    fecha_vta = models.DateTimeField(auto_now_add=True)
    cliente_id = models.ForeignKey(Cliente,on_delete=models.SET_NULL, null=True)
    total_vta = models.DecimalField(max_digits=10, decimal_places=2)
    moneda_vta = models.CharField(
        max_length=3,
        choices=MonedaUnits.choices,
        default=MonedaUnits.Bol
    )


class DetalleVenta(models.Model):
    cantidad_dv = models.IntegerField()
    precio_unitario_dv = models.DecimalField(max_digits=10, decimal_places=2) 
    producto_id_dv = models.ForeignKey(Producto,on_delete=models.SET_NULL, null=True)
    venta_id_dv = models.ForeignKey(Venta,on_delete=models.SET_NULL, null=True)
    
    