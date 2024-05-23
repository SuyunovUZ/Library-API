from .models import Book, User, RentBook
from .serializers import BookSerializer, UserSerializer, RentBookSerializer
from rest_framework import viewsets


class BookAPI(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RentBookAPI(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer