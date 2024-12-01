from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from api.models import Book
from api.serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

"""
    API view to retrieve the list of books with filtering, searching, and ordering capabilities.
    
    Filtering fields:
    - title
    - author
    - publication_year
    
    Search fields:
    - title
    - author (partial matches allowed)
    
    Ordering fields:
    - title (ascending by default, use -title for descending)
    - publication_year (ascending by default, use -publication_year for descending)
    """

#List View
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    fliter_backends = [DjangoFilterBackend]
    filterset_fields = ["title", "author", "publication_year"]
    search_fields = ["title", "author"] #fileds to search by
    ordering_fields = ["title", "publication_year"] #fileds to order

#DatailView
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListView

#CreateView
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#updateView
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#DeleteView
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

