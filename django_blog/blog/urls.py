from django.urls import path
from .views import BlogLoginView, BlogLogoutView, register, userProfile
from .views import (
    Post_CreateView,
    Post_DetailView,
    Post_ListView,
    Post_UpdateView,
    Post_DeteteView
)

urlpatterns = [
    path('login/', BlogLoginView.as_view(), name='login'),
    path('logout/', BlogLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('accounts/profile/', userProfile, name='profile'),
    path('', Post_ListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', Post_DetailView.as_view(), name='post-detail'),
    path('posts/new/', Post_CreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', Post_UpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', Post_DeteteView.as_view(), name='post-delete'),

]