from django.urls import path
from .views import RegisterView, LoginView

# Define URLs for the accounts app
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # User registration endpoint
    path('login/', LoginView.as_view(), name='login'),          # User login endpoint
]
