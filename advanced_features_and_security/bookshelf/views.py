from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import MyModel


# Create your views here.

@permission_required('app_name.can_view', raise_exception=True)
def view_mymodel(request):
    objects = MyModel.objects.all()
    return render(request, 'app_name/view_mymodel.html', {'objects': objects})

@permission_required('app_name.can_edit', raise_exception=True)
def edit_mymodel(request, pk):
    obj = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title')
        obj.save()
    return render(request, 'app_name/edit_mymodel.html', {'object': obj})

@permission_required('app_name.can_create', raise_exception=True)
def create_mymodel(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        MyModel.objects.create(title=title, content=content)
    return render(request, 'app_name/create_mymodel.html')