from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class RentBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    returned_date = models.CharField(max_length=55)

    def __str__(self):
        return self.book
