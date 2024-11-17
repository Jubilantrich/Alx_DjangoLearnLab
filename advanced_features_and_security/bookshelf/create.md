In [11]: from bookshelf.models import Book

In [12]: bookintance = Book.objects.create(title="1984", author="George Orwell", published_year=1949)