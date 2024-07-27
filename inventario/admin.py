from django.contrib import admin
from .models import Inventario,Producto,Cliente,Venta,DetalleVenta
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_pro','descripcion_pro', 'precio_pro','cantidad_pro')
    list_filter = ('precio_pro','cantidad_pro',)
    search_fields = ('nombre_pro',)
    list_per_page = 10
    ordering = ('precio_pro',)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_cli','documento_cli', 'correo_cli')
    list_filter = ('documento_cli',)
    search_fields = ('nombre_cli',)
    list_per_page = 10
    ordering = ('documento_cli',)

class VentaAdmin(admin.ModelAdmin):
    list_display = ('fecha_vta','total_vta','moneda_vta')
    list_filter = ('fecha_vta',)
    search_fields = ('fecha_vta',)
    list_per_page = 10
    ordering = ('fecha_vta',)

class DetalleAdmin(admin.ModelAdmin):
    list_display = ('cantidad_dv','precio_unitario_dv','producto_id_dv','venta_id_dv')
    list_filter = ('precio_unitario_dv',)
    search_fields = ('precio_unitario_dv',)
    list_per_page = 10
    ordering = ('precio_unitario_dv',)

class DetalleInventario(admin.ModelAdmin):
    list_display = ('cantidad_inv','producto_id_inv')
    list_filter = ('cantidad_inv','producto_id_inv',)
    search_fields = ('producto_id_inv',)
    list_per_page = 10
    ordering = ('cantidad_inv',)

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Venta,VentaAdmin)
admin.site.register(DetalleVenta,DetalleAdmin)
admin.site.register(Inventario,DetalleInventario)
