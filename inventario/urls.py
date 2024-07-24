from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet)



urlpatterns = [
    #path('contact/<str:name>/', views.contact, name='contact'),
    # path('productos', views.productos, name='productos'),
    #path('saludo/', views.index),
    #path('productos/', views.productoFormView, name='productos'),
    #path('', include(router.urls))
    path('productos/', views.ProductoCreateView.as_view()),
    path('productos/cantidad/', views.producto_count),
    path('productos/filrar/unidades/', views.productos_en_unidades),
    path('productos/reporte/', views.reporte_productos),

]