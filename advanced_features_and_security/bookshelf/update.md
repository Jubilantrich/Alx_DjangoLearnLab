In [11]: from bookshelf.models import Book

In [14]: bookintance = Book.objects.get(title="1984")
book.title="Nineteen Eighty-Four"
book.save()