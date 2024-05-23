from rest_framework import serializers
from .models import Book, User, RentBook


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class RentBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentBook
        fields = '__all__'
