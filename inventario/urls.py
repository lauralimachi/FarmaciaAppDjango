from django.urls import path
from . import views

urlpatterns = [
    path('contact/<str:name>/', views.contact, name='contact'),
    # path('productos', views.productos, name='productos'),
    path('saludo/', views.index),
    path('productos/', views.productoFormView, name='productos')
]