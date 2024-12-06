from django.urls import path
from .views import BlogLoginView, BlogLogoutView, register, userProfile

urlpatterns = [
    path('login/', BlogLoginView.as_view(), name='login'),
    path('logout/', BlogLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', userProfile, name='profile'),

]