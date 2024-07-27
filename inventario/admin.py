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

# class VentaAdmin(admin.ModelAdmin):
#     list_display = ('fecha_vta')
#     list_filter = ('fecha_vta',)
#     search_fields = ('fecha_vta',)
#     list_per_page = 10
#     ordering = ('fecha_vta',)

# class DetalleAdmin(admin.ModelAdmin):
#     list_display = ('cantidad_dv')
#     list_filter = ('cantidad_vd',)
#     search_fields = ('cantidad_vd',)
#     list_per_page = 10
#     ordering = ('cantidad_vd',)

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
