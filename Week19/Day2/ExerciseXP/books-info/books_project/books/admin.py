from django.contrib import admin
from .models import Book, BookReview, Author
# Register your models here.
admin.site.register(Book)
admin.site.register(BookReview)
admin.site.register(Author)
