In [11]: from bookshelf.models import Book

In [14]: bookintance = Book.objects.get(title="1984")
Book.objects.title="MY LOVE"
Book.objects.save()