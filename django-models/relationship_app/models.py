from django.db import models

# Create your models here.

#Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)

#Book Model
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

#Optimising queries with prefetching
books = Book.objects.prefetch_related('Author')


#Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, on_delete=models.CASCADE, related_name='libraries')

#Optimising queries with prefetching
libraries = Library.objects.prefetch_related('Book')

#Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarians')

#Optimising queries with prefetching
librarians = Librarian.objects.prefetch_related('Library')