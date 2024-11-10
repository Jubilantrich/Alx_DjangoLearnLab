from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
# Create your views here.

#1. Function-Based view for listing Books
#This view will pull all book records and send them to the list_books.html template for display.
def list_books(request):
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html', {'books': books})



#use DetailView to display details of specific library and its books
class LibraryDetailView (DetailView):
    model = Library
    Template = 'relationship_app/library_detail.html'
    context_object_name='library'