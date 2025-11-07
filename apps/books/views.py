from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .serializers import BooksSerializer
from .models import Books


class CreateBookAPIView(CreateAPIView):
    serializer_class = BooksSerializer


""" class GetBooksAPIView(ListAPIView):
    serializer_class = BooksSerializer

    def get_queryset(self):
        autor = self.request.query_params.get('autor', None)
        anio_publicacion = self.request.query_params.get('anio_publicacion', None)

        if anio_publicacion:
            anio_publicacion = int(anio_publicacion)
        
        return Books.objects.filter_by_author_or_year(autor=autor, anio_publicacion=anio_publicacion) """

class GetBooksAPIView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter('autor', str, description='Filtrar libros por autor', required=False),
            OpenApiParameter('anio_publicacion', int, description='Filtrar libros por año de publicación', required=False),
        ]
    )

    def get(self, request, *args, **kwargs):
        autor = self.request.query_params.get('autor', None)
        anio_publicacion = self.request.query_params.get('anio_publicacion', None)

        if anio_publicacion:
            anio_publicacion = int(anio_publicacion)
        
        queryset = Books.objects.filter_by_author_or_year(autor=autor, anio_publicacion=anio_publicacion)

        serializer = BooksSerializer(queryset, many=True)

        return Response(serializer.data)
        

class UpdateBookAPIView(RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    lookup_field = 'uuid'

class DeleteBookAPIView(DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    lookup_field = 'uuid'


class GetBookByAuthorTitleAPIView(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter('search_term', str, description='Filtrar libros por autor o titulo', required=True),
        ]
    )
    def get(self, request, *args, **kwargs):
        search_term = request.query_params.get('search_term', None)

        books = Books.objects.search(search_term)

        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data, status=200)



