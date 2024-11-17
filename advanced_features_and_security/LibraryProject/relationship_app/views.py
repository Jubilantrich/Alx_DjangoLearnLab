from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from  django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm  # Assuming you have a BookForm for handling form data
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

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

    class LoginView(LoginView):
        template_name = 'relationship_app/login.hhml'
    
    class LogoutView(LogoutView):
        template_name = 'relationship_app/login.html'

    #Registration View
    def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user) # log in the user after registration
                return redirect('home') #Redirect to a home page or another page
        else:
            form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form':form})
        
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to a book list or success page
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'
# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
