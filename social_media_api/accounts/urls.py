from django.urls import path
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView


# Define URLs for the accounts app
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # User registration endpoint
    path('login/', LoginView.as_view(), name='login'),          # User login endpoint
     path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]
