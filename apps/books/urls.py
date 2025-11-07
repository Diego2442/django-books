from django.urls import path
from .views import *

urlpatterns = [
    path('create', CreateBookAPIView.as_view()),    
    path('list', GetBooksAPIView.as_view()),
    path('update/<uuid:uuid>', UpdateBookAPIView.as_view()),
    path('delete/<uuid:uuid>', DeleteBookAPIView.as_view()),
    path('search', GetBookByAuthorTitleAPIView.as_view())
]