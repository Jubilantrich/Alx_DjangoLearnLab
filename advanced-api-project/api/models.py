from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Represents an author of a book.

    This model maps to a table called 'Author' in the database 'NewLibrary'.
    The table will have one attribute:
        - name: A string representing the author's name (max length: 100).
    """
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Book(models.Model):
    """
    Represents a book in the library.

    This model maps to a table called 'Book' in the database 'NewLibrary'.
    The table will have two attributes:
        - title: A string representing the book's title (max length: 200).
        - author: A foreign key referencing the Author model, representing the author of the book.
                  If the referenced author is deleted, all related books will also be deleted (CASCADE).
    """
    title = models.CharField(max_length=200)
    publication_year =models.IntegerField()
    author = models.ForeignKey(Author, many=True, read_only=True, on_delete=models.CASCADE, related_name='books')

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}"

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),           
            ('can_change_book', 'Can change book'),      
            ('can_delete_book', 'Can delete book'), 
            ] 
