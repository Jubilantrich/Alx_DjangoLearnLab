from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.conf import settings

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username,email,password=None,**extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth =models.DateTimeField(null=True, blank=True)
    profile_photo = models.ImageField(null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
        
class Profile (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField()

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_view", "Can view MyModel"),
            ("can_create", "Can create MyModel"),
            ("can_edit", "Can edit MyModel"),
            ("can_delete", "Can delete MyModel"),
        ]
class Command(BaseCommand):
    help = "Set up default groups and permissions"

    def handle(self, *args, **kwargs):
        # Define groups
        groups_permissions = {
            "Editors": ["can_create", "can_edit"],
            "Viewers": ["can_view"],
            "Admins": ["can_create", "can_edit", "can_delete", "can_view"],
        }

        for group_name, permissions in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for permission_codename in permissions:
                permission = Permission.objects.get(codename=permission_codename)
                group.permissions.add(permission)

        self.stdout.write("Default groups and permissions set up successfully!")
