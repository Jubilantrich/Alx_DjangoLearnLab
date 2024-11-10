from django.shortcuts import render
from  django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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

    class CLoginView(LoginView):
        template_name = 'relationship_app/login.hhml'
    
    class CLogoutView(LogoutView):
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
            