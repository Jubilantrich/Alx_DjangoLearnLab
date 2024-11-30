from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

current_datetime = datetime.now()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def validate(self, data):
        if data['publication_year']>current_datetime:
            raise serializers.ValidationError('publication year can not be in the future')
        return data
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name"]