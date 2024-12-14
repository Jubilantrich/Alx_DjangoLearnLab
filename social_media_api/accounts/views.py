from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import generics, status  # For GenericAPIView and status codes
from rest_framework import permissions  # For user authentication
from rest_framework.response import Response  # For sending API responses
from django.shortcuts import get_object_or_404  # For safely retrieving objects
from .models import CustomUser  # Import the CustomUser model
from .serializers import UserSerializer  # Import UserSerializer if needed for validation or serialization


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

class FollowUserView(generics.GenericAPIView):
    """
    View to allow a user to follow another user.
    """
    queryset = CustomUser.objects.all()  # Required for GenericAPIView
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access
    
    def post(self, request, user_id):
        # Retrieve the user to be followed
        target_user = get_object_or_404(self.get_queryset(), id=user_id)
        
        # Prevent the user from following themselves
        if request.user == target_user:
            return Response(
                {"error": "You cannot follow yourself."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Add the target user to the following list of the current user
        request.user.following.add(target_user)
        
        return Response(
            {"message": f"You are now following {target_user.username}."}, 
            status=status.HTTP_200_OK
        )

class UnfollowUserView(generics.GenericAPIView):
    """
    View to allow a user to unfollow another user.
    """
    queryset = CustomUser.objects.all()  # Required for GenericAPIView
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access
    
    def post(self, request, user_id):
        # Retrieve the user to be unfollowed
        target_user = get_object_or_404(self.get_queryset(), id=user_id)
        
        # Prevent the user from unfollowing themselves
        if request.user == target_user:
            return Response(
                {"error": "You cannot unfollow yourself."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Remove the target user from the following list of the current user
        request.user.following.remove(target_user)
        
        return Response(
            {"message": f"You have unfollowed {target_user.username}."}, 
            status=status.HTTP_200_OK
        )
