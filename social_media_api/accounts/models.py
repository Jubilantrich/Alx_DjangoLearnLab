from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Custom user model extending Django's built-in AbstractUser
class CustomUser(AbstractUser):
    # Optional bio for user profile
    bio = models.TextField(blank=True, null=True)
    # Profile picture for the user
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    # Many-to-Many relationship for followers, non-symmetrical to allow one-sided follows
   # followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    # Many-to-Many relationship for following other users
    following = models.ManyToManyField(
        'self',
        symmetrical=False,  # Allows differentiation between followers and followees
        related_name='followers',  # Access followers using user.followers
        blank=True
    )

    def __str__(self):
        # String representation of the user, showing their username
        return self.username

# The post model
class Post(models.Model):
    # ForeignKey relationship linking Post to the User who created it
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the custom user model
        on_delete=models.CASCADE,  # Delete posts when the author is deleted
        related_name='posts'  # Allows reverse lookup (user.posts)
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
        Post, 
        on_delete=models.CASCADE,  # Delete comments when the post is deleted
        related_name='comments'  # Allows reverse lookup (post.comments)
    )
    # ForeignKey relationship linking Comment to the User who created it
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,  # Delete comments when the author is deleted
        related_name='comments'  # Allows reverse lookup (user.comments)
    )
    content = models.TextField()  # Content of the comment
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when comment is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when comment is last updated

    def __str__(self):
        # String representation of the Comment
        return f"Comment by {self.author.username} on {self.post.title}"
    