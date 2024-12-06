from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django import forms

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
    return render(request, 'blog/profile.html', {'user': request.user})

class BlogLoginView(LoginView):
    template_name = 'blog/login.html'

class BlogLogoutView(LogoutView):
    template_name = 'blog/logout.html'