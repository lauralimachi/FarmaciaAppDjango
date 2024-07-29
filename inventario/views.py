from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Producto, Cliente , DetalleVenta
from .form import ProductForm
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import ProductoSerializer, ClienteSerializer, DetalleVentaSerializer
from rest_framework import generics
from rest_framework.decorators import api_view


# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de hoy")

def productoFormView(request):
    form = ProductForm()
    producto = None
    id_producto = request.GET.get("id")
    if id_producto:
        # producto = Producto.objects.get(id=10011)
        producto = get_object_or_404(Producto, id=id_producto)
        form = ProductForm(instance=producto)

    if request.method == "POST":
        if producto:
            form = ProductForm(request.POST, instance=producto)
        else:
            form = ProductForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "productos.html", {"form": form})

# para productos 
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

@api_view(['GET'])
def producto_count(request):
    """
    Cuenta la cantidad de productos
    """

    try:
        cantidad = Producto.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )


@api_view(['GET'])
def productos_en_unidades(requesto):
    """
    Lista de productos filtrados por nombre
    """

    try:
        productos = Producto.objects.filter(nombre_pro='aspirina')
        return JsonResponse(
            ProductoSerializer(productos, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )


@api_view(['GET'])
def reporte_productos(request):
    """
    Reporte de productos por categoria
    """

    try:
        productos = Producto.objects.filter(nombre_pro='aspirina')
        cantidad = productos.count()
        return JsonResponse(
            ReporteProductosSerializer({
                "cantidad": cantidad,
                "productos": productos
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )

# para Cliente
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

@api_view(['GET'])
def cliente_count(request):
    """
    Cuenta la cantidad de clientes
    """

    try:
        cantidad = Cliente.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )


@api_view(['GET'])
def clientes_por_nombre(requesto):
    """
    Lista de clientes filtrados por nombre
    """

    try:
        clientes = Cliente.objects.filter(nombre_cli='Luis Lara')
        return JsonResponse(
            ClienteSerializer(clientes, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )


@api_view(['GET'])
def reporte_clientes(request):
    """
    Reporte de clientes por nombre
    """

    try:
        clientes = Cliente.objects.filter(nombre_cli='Luis Lara')
        cantidad = clientes.count()
        return JsonResponse(
            ReporteClientesSerializer({
                "cantidad": cantidad,
                "clientes": clientes
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )

# detalle venta
class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer


class DetalleVentaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer