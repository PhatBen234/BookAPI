from rest_framework import serializers
from .models import Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer): #change data from model to JSON
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'price']

    # Ensure ISBN is unique
    def validate_isbn(self, value):
        if Book.objects.filter(isbn=value).exists():
            raise serializers.ValidationError("A book with this ISBN already exists.")
        return value

    # Ensure price is positive
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

    # Ensure published_date is in the correct format (YYYY-MM-DD)
    def validate_published_date(self, value):
        try:
            datetime.strptime(str(value), "%Y-%m-%d")
        except ValueError:
            raise serializers.ValidationError("Published date must be in YYYY-MM-DD format.")
        return value
