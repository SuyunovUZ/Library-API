from django.contrib import admin
from .models import Book, User, RentBook


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class RentBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'user', 'created_at', 'returned_date']


admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(RentBook, RentBookAdmin)
