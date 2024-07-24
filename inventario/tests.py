from django.test import TestCase
from .models import Producto
from django.core.exceptions import ValidationError

# Create your tests here.


class TestProducto(TestCase);

    def test_grabacion(self):
        with self.assertRaises(ValidationError) as qv:
            q = Producto.objects.create(nombre_pro='No permitido')
            q.full_clean()

        mensaje_error = dict(qv.exception)
        self.assertEqual(mensaje_error["nombre_pro"][0], "No es una opcion permitida")


