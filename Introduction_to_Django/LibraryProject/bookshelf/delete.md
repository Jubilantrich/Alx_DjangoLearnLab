In [11]: from bookshelf.models import Book

In [15]: bookintance = Book.objects.get(title="MY LOVE")
Book.objects.delete()