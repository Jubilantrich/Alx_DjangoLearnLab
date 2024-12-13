from rest_framework import serializers
from rest_framework.authtoken.models import Token  # Import Token model for authentication
from django.contrib.auth import get_user_model  # Import to use the custom user model
from .models import CustomUser
from .models import Post, Comment

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()  # Password field should not be exposed in API responses

    class Meta:
        model = get_user_model()  # Dynamically fetch the custom user model
        fields = ['username', 'email', 'password']  # Fields required for registration

    def create(self, validated_data):
        """
        Create a new user instance with a hashed password and generate an auth token.
        """
        # Create the user with hashed password
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),  # Email can be optional based on the project
            password=validated_data['password']  # Password is hashed internally
        )
        # Create an authentication token for the user
        Token.objects.create(user=user)
        return user

# Serializer for the user profile and followers management
class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()  # Custom field to count followers

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'followers_count']

    def get_followers_count(self, obj):
        """
        Custom method to count the number of followers.
        """
        return obj.followers.count()
