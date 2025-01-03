"""LibraryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from .views import list_books
from django.urls import path
from .views import LoginView
from .views import LogoutView
from .views import register
from .views import admin_view
from .views import librarian_view
from .views import member_view


urlpatterns = [
    path('books/', views.list_books, name='/templates/list_books'),
    path('library/<int:pk>', views.LibraryDetailView.as_view(), name='templates/library_details'),
    path('login/', LoginView.as_view(template_name="login"), template_name='login'),
    path('logout/', LogoutView.as_view(template_name="logout"), template_name='logout'),
    path('register/', views.register(), template_name='register'),
    path('', include('relationship_app.urls')),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
    
]
