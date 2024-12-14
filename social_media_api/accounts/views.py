from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RegisterSerializer
from .models import CustomUser


# API View for user registration
class RegisterView(APIView):
    def post(self, request):
        # Deserialize incoming data for registration
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new user and generate a token
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        # Return validation errors if any
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API View for user login
class LoginView(APIView):
    def post(self, request):
        from django.contrib.auth import authenticate  # Import authenticate function

        # Extract username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Verify credentials
        user = authenticate(username=username, password=password)
        if user:
            # Generate or retrieve an authentication token for the user
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        # Return error if authentication fails
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class FollowUserView(APIView):
    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        if request.user == target_user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(target_user)
        return Response({"message": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)
        if request.user == target_user:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.remove(target_user)
        return Response({"message": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)