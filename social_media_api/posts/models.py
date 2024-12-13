from django.db import models
from django.conf import settings

class Post(models.Model):
    # ForeignKey relationship linking Post to the User who created it
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the custom user model
        on_delete=models.CASCADE,  # Delete posts when the author is deleted
        related_name='account_posts'  # Allows reverse lookup (user.posts)
    )
    title = models.CharField(max_length=200)  # Title of the post
    content = models.TextField()  # Content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when post is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when post is last updated

    def __str__(self):
        return self.title  # String representation of the Post


class Comment(models.Model):
    # ForeignKey relationship linking Comment to a Post
    post = models.ForeignKey(
        'Post',  # Reference to the Post model
        on_delete=models.CASCADE,  # Delete comments when the post is deleted
        related_name='post_comments'  # Updated related_name to avoid conflict
    )
    # ForeignKey relationship linking Comment to the User who created it
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference to the custom user model
        on_delete=models.CASCADE,  # Delete comments when the author is deleted
        related_name='user_comments'  # Updated related_name to avoid conflict
    )
    content = models.TextField()  # Content of the comment
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when comment is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when comment is last updated

    def __str__(self):
        # String representation of the Comment
        return f"Comment by {self.author.username} on {self.post.title}"
    