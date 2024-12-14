from rest_framework import serializers
from .models import Post, Comment, Like

class CommentSerializer(serializers.ModelSerializer):
    # Read-only field to display the username of the comment's author
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment  # Specify the model for this serializer
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']  # Fields that cannot be updated by the user


class PostSerializer(serializers.ModelSerializer):
    # Read-only field to display the username of the post's author
    author_username = serializers.ReadOnlyField(source='author.username')
    # Nested serializer to include comments in the post response
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post  # Specify the model for this serializer
        fields = ['id', 'author', 'author_username', 'title', 'content', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['author', 'created_at', 'updated_at']  # Fields that cannot be updated by the user

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']