from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

from .views import list_books, LibraryDetailView

urlpatterns = [
    path("relations/", views.bookrelation, name='bookrelation'),
    path("add_book/", views.bookrelation, name='add_book'),
    path("delete_book/", views.bookrelation, name='delete_book'),
    path("edit_book/", views.bookrelation, name='edit_book'),
    path('', views.index, name='index'),
    path('listbooks/',views.list_books, name='listbooks'),
    path('librarydetail/<int:pk>/', views.LibraryDetailView.as_view(), name='librarydetailview'),
    path('register/', views.register.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('members/', views.member_view, name='members'),
    path('librarian/', views.librarian_view, name='librarian'),
    path('admin/', views.admin_view, name="admin") 
]
