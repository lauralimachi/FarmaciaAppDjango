from django.core.exceptions import ValidationError
import re

regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


def validation_numero(value):
    if value < 0:
        raise ValidationError("%(valor)s no es un numero positivo", params={'valor': value}) 

def validarEmail(email):
    if re.fullmatch(regex, email) is None:
        raise ValidationError(
            "El correo electrónico '%(email)s' es inválido",
            params={'email': email}
        )