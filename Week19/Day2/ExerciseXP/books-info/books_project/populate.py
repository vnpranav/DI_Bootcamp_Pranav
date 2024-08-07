import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_project.settings')

import django
django.setup()

from datetime import datetime
from books.models import Book
import requests

def fetch_books_from_google_books(query):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(url)
    return response.json()

def populate_books(data):
    for item in data.get('items', []):
        volume_info = item.get('volumeInfo', {})
        title = volume_info.get('title')
        authors = ', '.join(volume_info.get('authors', []))
        published_date = volume_info.get('publishedDate', '2000-01-01')
        description = volume_info.get('description', '')
        page_count = volume_info.get('pageCount', 0)
        categories = ', '.join(volume_info.get('categories', []))
        thumbnail_url = volume_info.get('imageLinks', {}).get('thumbnail', '')

        try:
            published_date = datetime.strptime(published_date, '%Y-%m-%d').date()
        except ValueError:
            published_date = datetime.strptime(published_date, '%Y-%m').date() if '-' in published_date else datetime.strptime(published_date, '%Y').date()

        book = Book(
            title=title,
            author=authors,
            published_date=published_date,
            description=description,
            page_count=page_count,
            categories=categories,
            thumbnail_url=thumbnail_url
        )
        book.save()
        print(f'Added book: {title}')

queries = ['python', 'django', 'machine learning']
for query in queries:
   data = fetch_books_from_google_books(query)
   populate_books(data)