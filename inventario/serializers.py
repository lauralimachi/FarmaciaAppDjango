from rest_framework import serializers
from .models import Producto, Cliente


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ReporteProductosSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    productos = ProductoSerializer(many=True)

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'   

class ReporteClientesSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    clientes = ClienteSerializer(many=True)