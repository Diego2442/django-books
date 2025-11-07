import pytest
from unittest.mock import patch, MagicMock
from rest_framework.test import APIClient
from rest_framework import status
from apps.books.models import Books
import uuid

@pytest.mark.django_db(transaction=True)
class TestBooksViews:

    # Test para la creación de un libro (CreateBookAPIView)
    @patch('apps.books.views.Books.objects.create')
    def test_create_book(self, mock_create):
        mock_create.return_value = Books(titulo='Libro Mock', autor='Autor Mock', anio_publicacion=2023, isbn='3333333333333')

        client = APIClient()
        data = {
            'titulo': 'Libro Mock',
            'autor': 'Autor Mock',
            'anio_publicacion': 2023,
            'isbn': '3333333333333'
        }

        response = client.post('/api/books/create', data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        mock_create.assert_called_once_with(titulo='Libro Mock', autor='Autor Mock', anio_publicacion=2023, isbn='3333333333333')
        assert Books.objects.count() == 0

    # Test para obtener libros con filtros (GetBooksAPIView)
    @patch('apps.books.views.Books.objects.filter_by_author_or_year')
    def test_get_books(self, mock_filter):
        mock_filter.return_value = [
            Books(titulo='Libro Mock 1', autor='Autor Mock', anio_publicacion=2023, isbn='3333333333'),
            Books(titulo='Libro Mock 2', autor='Autor Mock', anio_publicacion=2023, isbn='3333333334')
        ]

        client = APIClient()
        response = client.get('/api/books/list', {'autor': 'Autor Mock'}, format='json')

        assert response.status_code == status.HTTP_200_OK
        mock_filter.assert_called_once_with(autor='Autor Mock', anio_publicacion=None)
        assert len(response.data) == 2

    # Test para actualizar un libro (UpdateBookAPIView)
    """ @patch('apps.books.views.Books.objects.get')
    def test_update_book_queryset_mock(self, mock_books_get):
        uuid_libro = '12345678-1234-5678-1234-567812345678'
        
        # Mock del libro con todos los atributos necesarios
        mock_book = MagicMock()
        mock_book.pk = 1
        mock_book.id = 1
        mock_book.uuid = uuid.UUID(uuid_libro)
        mock_book.titulo = 'Libro Original'
        mock_book.autor = 'Autor Original'
        mock_book.anio_publicacion = 2020
        mock_book.isbn = '1111111111111'
        mock_book.save = MagicMock()
        
        mock_books_get.return_value = mock_book

        client = APIClient()
        data = {
            'titulo': 'Libro Actualizado',
            'autor': 'Autor Actualizado',
            'anio_publicacion': 2022,
            'isbn': '2222222222222'
        }

        # También mockeamos el serializer para evitar el error anterior
        with patch('apps.books.views.BooksSerializer') as mock_serializer_class:
            mock_serializer = MagicMock()
            mock_serializer.is_valid.return_value = True
            mock_serializer.save.return_value = mock_book
            mock_serializer.data = data
            mock_serializer_class.return_value = mock_serializer
            
            response = client.put(f'/api/books/update/{uuid_libro}', data, format='json')

        assert response.status_code == status.HTTP_200_OK
        mock_books_get.assert_called_once_with(uuid=uuid.UUID(uuid_libro))
        mock_book.save.assert_called_once() """

    # Test para eliminar un libro (DeleteBookAPIView)
    @patch('apps.books.views.DeleteBookAPIView.get_object')
    def test_delete_book(self, mock_get_object):
        uuid_libro = '12345678-1234-5678-1234-567812345678'
        
        mock_book = MagicMock(spec=Books)
        mock_book.uuid = uuid.UUID(uuid_libro)
        mock_book.delete = MagicMock()
        
        mock_get_object.return_value = mock_book

        client = APIClient()
        response = client.delete(f'/api/books/delete/{uuid_libro}')

        assert response.status_code == status.HTTP_204_NO_CONTENT
        mock_get_object.assert_called_once()
        mock_book.delete.assert_called_once()


    # Test para obtener libros por autor o título (GetBookByAuthorTitleAPIView)
    @patch('apps.books.views.Books.objects.search')
    def test_get_book_by_author_or_title(self, mock_search):
        mock_search.return_value = [
            Books(titulo='Libro 1', autor='Autor Test', anio_publicacion=2021, isbn='1111111111111'),
            Books(titulo='Libro 2', autor='Autor Test', anio_publicacion=2021, isbn='1111111112222')
        ]

        client = APIClient()
        response = client.get('/api/books/search', {'search_term': 'Autor Test'}, format='json')

        assert response.status_code == status.HTTP_200_OK
        mock_search.assert_called_once_with('Autor Test')
        assert len(response.data) == 2

    # Tests adicionales para casos edge
    def test_update_book_not_found(self):
        """Test para verificar el comportamiento cuando el libro no existe"""
        client = APIClient()
        non_existent_uuid = uuid.uuid4()
        
        data = {
            'titulo': 'Libro Inexistente',
            'autor': 'Autor Test',
            'anio_publicacion': 2023,
            'isbn': '9999999999999'
        }
        
        response = client.put(f'/api/books/update/{non_existent_uuid}', data, format='json')
        
        # Dependiendo de tu implementación, podría ser 404 o otro código
        assert response.status_code in [status.HTTP_404_NOT_FOUND, status.HTTP_400_BAD_REQUEST]

    def test_delete_book_not_found(self):
        """Test para verificar el comportamiento al eliminar un libro que no existe"""
        client = APIClient()
        non_existent_uuid = uuid.uuid4()
        
        response = client.delete(f'/api/books/delete/{non_existent_uuid}')
        
        assert response.status_code in [status.HTTP_404_NOT_FOUND, status.HTTP_400_BAD_REQUEST]