from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import ExampleForm


# Create your views here.

@permission_required('app_name.can_view', raise_exception=True)
def view_mymodel(request):
    book_list = Book.objects.all()
    return render(request, 'app_name/view_mymodel.html', {'objects': book_list})

@permission_required('app_name.can_edit', raise_exception=True)
def edit_mymodel(request, pk):
    books = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        books.title = request.POST.get('title')
        books.save()
    return render(request, 'app_name/edit_mymodel.html', {'object': books})

@permission_required('app_name.can_create', raise_exception=True)
def create_mymodel(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Book.objects.create(title=title, content=content)
    return render(request, 'app_name/create_mymodel.html')

from django.shortcuts import render
from .forms import ExampleForm

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data
            pass
    else:
        form = ExampleForm()
    return render(request, "form_example.html")