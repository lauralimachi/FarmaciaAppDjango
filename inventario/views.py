from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Producto
from .form import ProductForm
from django.shortcuts import get_object_or_404

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