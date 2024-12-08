from django.urls import path
from .views import BlogLoginView, BlogLogoutView, register, userProfile
from .views import (
    Post_CreateView,
    Post_DetailView,
    Post_ListView,
    Post_UpdateView,
    Post_DeteteView,
    add_comment, 
    CommentUpdateView, 
    CommentDeleteView

)

urlpatterns = [
    path('login/', BlogLoginView.as_view(), name='login'),
    path('logout/', BlogLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('accounts/profile/', userProfile, name='profile'),
    path('', Post_ListView.as_view(), name='post-list'),
    path('post/<int:pk>/', Post_DetailView.as_view(), name='post-detail'),
    path('post/new/', Post_CreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', Post_UpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', Post_DeteteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),


]
