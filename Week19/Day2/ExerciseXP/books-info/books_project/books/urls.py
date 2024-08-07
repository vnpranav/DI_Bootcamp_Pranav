from django.urls import path
from . import views

urlpatterns = [
   path('books/', views.list_books, name='list_books'),
   path('books/<int:id>/', views.book_detail, name='book_detail'),
   path('books/create/', views.create_book, name='create_book'),
   path("books/review/create/", views.create_review, name="create_review"),
   path('books/review/edit/<int:id>/', views.edit_review, name='edit_review'),
   path('books/review/delete/<int:id>/', views.delete_review, name='delete_review'),
]
