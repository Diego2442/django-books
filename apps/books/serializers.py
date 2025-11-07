from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
from .utilities import validar_anio_publicacion

class BooksSerializer(serializers.ModelSerializer):
    anio_publicacion = serializers.IntegerField(validators=[validar_anio_publicacion])

    class Meta:
        model = Books
        fields = [
            'uuid',
            'titulo',
            'autor',
            'anio_publicacion',
            'isbn',
        ]