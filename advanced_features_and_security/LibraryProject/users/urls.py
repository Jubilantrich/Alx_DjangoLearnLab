from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_mymodel, name='view_mymodel'),
    path('edit/<int:pk>/', views.edit_mymodel, name='edit_mymodel'),
    path('create/', views.create_mymodel, name='create_mymodel'),
]