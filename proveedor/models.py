from django.db import models

# Create your models here.



# class Proveedores(models.Model):
#     nombre_prov = models.CharField(max_length=255) not null
#     direccion_prov = models.CharField(max_length=255)
#     telefono_prov = models.CharField(max_length=255)


#     def __str__(self):
#         return f'Proveedor {self.id}: {self.nombre_prov} {self.telefono_prov}'

# class Productos(models.model):
#     nombre_pro = models.CharField(max_length=255)
#     descripcion_pro = models.CharField(max_length=255)
#     precio_pro = models.DecimalField(max_digits=10, decimal_places=2) not null
#     cantidad_pro = models.IntegerField() not null
#     proveedor_id_pro = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return f'Productos {self.id}: {self.nombre_pro} {self.precio_pro}'