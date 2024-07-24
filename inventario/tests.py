from django.test import TestCase
<<<<<<< HEAD
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


=======

# Create your tests here.
>>>>>>> 1394ab79238923f51650b24bdac26a562cd444f8
