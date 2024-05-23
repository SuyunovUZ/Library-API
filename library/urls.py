from django.urls import path
from .views import BookAPI, UserAPI, RentBookAPI
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'books', BookAPI, basename='books')
router.register(r'users', UserAPI, basename='users')
router.register(r'rent_books', RentBookAPI, basename='rent_books')
urlpatterns = router.urls

