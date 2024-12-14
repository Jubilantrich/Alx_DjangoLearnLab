from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to ensure that only the author of a post or comment
    can modify it, while others have read-only access.
    """
    def has_object_permission(self, request, view, obj):
        # Grant read-only permissions for GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of the object
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations for posts.
    """
    queryset = Post.objects.all().order_by('-created_at')  # Retrieve posts ordered by creation date
    serializer_class = PostSerializer  # Use PostSerializer to serialize/deserialize data
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]  # Apply permissions

    def perform_create(self, serializer):
        """
        Automatically set the logged-in user as the author of the post during creation.
        """
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations for comments.
    """
    queryset = Comment.objects.all().order_by('-created_at')  # Retrieve comments ordered by creation date
    serializer_class = CommentSerializer  # Use CommentSerializer to serialize/deserialize data
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]  # Apply permissions

    def perform_create(self, serializer):
        """
        Automatically set the logged-in user as the author of the comment during creation.
        """
        serializer.save(author=self.request.user)

class FeedView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get posts from users the current user is following
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
