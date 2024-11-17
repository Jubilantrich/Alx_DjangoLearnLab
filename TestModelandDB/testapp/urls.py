from django.urls import path
from .views import welcomepage

urlpatterns = [
    path("welcome/", view = welcomepage, name="welcome")
]