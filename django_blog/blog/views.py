from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django import forms
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

#Custom Registration form
class RegisterationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Registration View
def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterationForm()
    return render(request,  'blog/register.html', {'form':form})

#Profile View
@login_required
def userProfile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        return HttpResponse("Profile updated successfully.")
    return render(request, 'blog/accounts/profile.html', {'user': request.user})

class BlogLoginView(LoginView):
    template_name = 'blog/login.html'

class BlogLogoutView(LogoutView):
    template_name = 'blog/logout.html'

#list View
class Post_ListView(ListView):
    model =Post
    template_name = 'blog/post_list.html' #custom template
    context_object_name = 'posts'
    ordering = ['-published_date']

#Detail View
class Post_DetailView(DetailView):
    model =Post
    template_name = 'blog/post_details.html' #custom template

#Creat View
class Post_CreateView(LoginRequiredMixin, CreateView):
    model =Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html' #custom template

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
   
#update view
class Post_UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model =Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html' #custom template

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post =self.get_object()
        return self.request.user == post.author
    
#Delete View
class Post_DeteteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author