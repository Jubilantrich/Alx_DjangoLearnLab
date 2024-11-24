from django.urls import path
from django.urls import include
from .views import BookList
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

# Create a router instance
router = DefaultRouter()

router.register(r"books_all", BookViewSet, basename="book_all")
urlpatterns = [
#Router for the BookList view (ListAPIView)
path("books", BookList.as_view(), name="book-list"),

#Include the route URLs for BookViewsSet (all CRUD Operationa)
path("", include(router.urls)), # This include all routes registered with the route

]