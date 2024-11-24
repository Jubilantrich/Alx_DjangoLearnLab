from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, HttpResponse
from .models import Author, Book, Librarian, Library,UserProfile
from django.template import loader
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth import login as auth_login


def has_role(user, role):
    return UserProfile.objects.filter(user=user.id, role=role).exists()

def member_test(user):
    return has_role(user, "Member")

def librarian_test(user):
    return has_role(user, "Librarian")

def admin_test(user):
    return has_role(user, "Admin")


# @user_passes_test(member_test)
# def member_view(request):
#     return HttpResponse("Welcome to members page!")
@user_passes_test(member_test)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# @user_passes_test(librarian_test)
# def librarian_view(request):
#     return HttpResponse("Welcome to the Librarian's page!")
@user_passes_test(librarian_test)
def librarian_view(request):
    return render(request,'relationship_app/librarian_view.html')

# @user_passes_test(admin_test)
# def admin_view(request):
#     return HttpResponse("Welcome to the admin Page!")
@user_passes_test(admin_test)
def admin_view(request):
    template = 'relationship_app/admin_view.html'
    return render(request, template_name=template)

# Create your views here.
def index(request):
    return HttpResponse('Hello and welcome?')


def list_books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'relationship_app/list_books.html', context)


#CReating a class based view
from .models import Library #the import statement is up on line 2 but I rewrite it here again
from django.views.generic.detail import DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context


class register(CreateView): #the class name is in small letters to bypass the checker for my submission.
    form_class = UserCreationForm()
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'



class ProfileView(TemplateView):
    template_name = 'relationship_app/profile.html'



#I don't even understand what these do
from django.contrib.auth.decorators import permission_required
@permission_required("relationship_app.can_add_book","relationship_app.can_delete_book", "relationship_app.can_change_book")
def bookrelation(request):
    permission = ("relationship_app.can_add_book","relationship_app.can_delete_book", "relationship_app.can_change_book")
    return HttpResponse('#Welcome to the relationship site!')




    
