from django.core.exceptions import ValidationError

def validar_par(value):
    if value % 2 != 0:
        raise ValidationError("%(valor)s no es un numero par", params={'valor': value})

<<<<<<< HEAD
def validation_producto(value):
    if value == "No permitido":
        raise ValidationError("No es una opcion permitida")
=======
>>>>>>> 1394ab79238923f51650b24bdac26a562cd444f8
