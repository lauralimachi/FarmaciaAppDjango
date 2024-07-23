from django.contrib import admin
from .models import Inventario,Producto,Cliente,Venta,DetalleVenta
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_pro','descripcion_pro', 'precio_pro','cantidad_pro')
    list_filter = ('precio_pro','cantidad_pro',)
    search_fields = ('nombre_pro',)
    list_per_page = 10
    ordering = ('precio_pro',)


admin.site.register(Producto,ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Venta)
