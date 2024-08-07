import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_project.settings')

import django
django.setup()

from random import choice, sample
from books.models import Book, Author, Category

def create_authors_and_categories():
    author_names = ["Author 1", "Author 2", "Author 3", "Author 4", "Author 5"]
    category_names = ["Category 1", "Category 2", "Category 3", "Category 4", "Category 5"]

    authors = [Author.objects.get_or_create(name=name)[0] for name in author_names]
    categories = [Category.objects.get_or_create(name=name)[0] for name in category_names]

    for book in Book.objects.all():
        book.author.set(sample(authors, k=2))
        book.categories.set(sample(categories, k=3))
        book.save()
        print(f'Updated book: {book.title} with authors and categories')