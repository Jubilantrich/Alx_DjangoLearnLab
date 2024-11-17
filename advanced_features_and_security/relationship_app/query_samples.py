from .models import Book
from .models import Library
from .models import Librarian

#Quert all books by specific author
author = Book.objects.complex_filter('Name of Author')

# List all books in a Library
books = Library.Book.objects.all()

#Retirve the lirarian for a libary
lirarians = Library.Librarian.objects.all()