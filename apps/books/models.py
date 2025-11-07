from django.db import models
import uuid
from .utilities import validate_isbn
from .managers import BookManger

# Create your models here.

class Books(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=255)
    anio_publicacion = models.IntegerField()
    isbn = models.CharField(max_length=15, validators=[validate_isbn], unique=True)

    objects = BookManger()

    def __str__(self):
        return self.titulo