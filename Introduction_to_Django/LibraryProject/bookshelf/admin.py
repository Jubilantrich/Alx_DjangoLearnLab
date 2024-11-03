from django.contrib import admin
from .models import Book
from .models import Product

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display =('title', 'author','published_date')
    search_fields=('title','author')
    list_fliter=('publication_year')
    
admin.site.register(Book, BookAdmin)