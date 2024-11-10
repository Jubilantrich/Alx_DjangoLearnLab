from django.db import models

# Create your models here.

#Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Book Model
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.name
    
#Optimising queries with prefetching
books = Book.objects.prefetch_related('Author')

    
#Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, on_delete=models.CASCADE, related_name='libraries')

    def __str__(self):
        return self.name
    
#Optimising queries with prefetching
libraries = Library.objects.prefetch_related('Book')

#Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarians')

    def __str__(self):
        return self.name

#Optimising queries with prefetching
librarians = Librarian.objects.prefetch_related('Library')

class Meta:
    permissions=[
        ("can_add_book", "can add a book"),
        ("can_change_book", "can change a book"),
        ("can_delete_book", "can delete a book"),

    ]