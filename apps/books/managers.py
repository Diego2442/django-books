from django.db import models 
from django.db.models import Q

class BookManger(models.Manager):
    def filter_by_author_or_year(self, autor=None, anio_publicacion=None):
        queryset = self.get_queryset()

        if autor:
            queryset = queryset.filter(autor__icontains=autor)
        if anio_publicacion:
            queryset = queryset.filter(anio_publicacion=anio_publicacion)
        
        return queryset
    
    def search(self, search_term=None):
        if search_term:
            return self.filter(
                Q(titulo__icontains=search_term) | Q(autor__icontains=search_term)
            )
        return self.all()