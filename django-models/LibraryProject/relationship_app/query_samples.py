# relationship_app/query_samples.py

from relationship_app.models import Book, Author, Library, Librarian

def query_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books

def list_all_books_in_library(library_name):
    try:
        Library.objects.get(name=library_name)
        books = books.all()
        for book in books:
            print(f"Title: {book.title}, Author: {book.author.name}")
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
        return []

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian: {librarian.name}")
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None

# Example usage
#if _name_ == "_main_":
   # print("Querying all books by author 'George Orwell':")
   # query_books_by_author("George Orwell")

   # print("\nListing all books in 'Central Library':")
    #list_all_books_in_library("Central Library")

    #print("\nRetrieving the librarian for 'Central Library':")
    #retrieve_librarian_for_library("Central Library")