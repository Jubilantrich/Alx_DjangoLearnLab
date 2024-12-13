from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user model extending Django's built-in AbstractUser
class CustomUser(AbstractUser):
    # Optional bio for user profile
    bio = models.TextField(blank=True, null=True)
    # Profile picture for the user
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    # Many-to-Many relationship for followers, non-symmetrical to allow one-sided follows
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        # String representation of the user, showing their username
        return self.username
