from datetime import datetime
from django.core.exceptions import ValidationError
import re

def validate_isbn(value):
    if not re.match(r'^\d{13}$|^\d{10}$', value):
        raise ValidationError(f'{value} no es un ISBN válido.')

def validar_anio_publicacion(value):
    current_year = datetime.now().year
    if value < 1000 or value > current_year:
        raise ValidationError(f"El año debe ser entre 1000 y {current_year}.")
    return value