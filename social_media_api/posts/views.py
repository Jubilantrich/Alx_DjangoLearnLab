from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import LikeSerializer
from notifications.models import Notification
from rest_framework.generics import get_object_or_404


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

class LikePostView(generics.GenericAPIView):
    """
    View for liking a post.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Fetch the post or return 404
        post = get_object_or_404(Post, pk=pk)

        # Create or retrieve the like object
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post author
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target=post
            )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_200_OK)


class UnlikePostView(generics.GenericAPIView):
    """
    View for unliking a post.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Fetch the post or return 404
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has already liked the post
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the like object
        like.delete()

        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)