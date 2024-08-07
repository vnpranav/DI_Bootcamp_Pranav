from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Book, BookReview
from django.contrib.auth.models import User
import json

# Create your views here.
def list_books(request):
   books = Book.objects.all()
   return JsonResponse(list(books), safe=False)

def book_detail(request, id):
   # Book.objects.get(id=id)
   book = get_object_or_404(Book, id=id)
   return JsonResponse({
      'title' : book.title,
      'author' : book.author,
      'published_date' : book.published_date,
      'description' : book.description,
      'page_count': book.page_count,
      'categories': book.categories,
      'thumbnail_url': book.thumbnail_url,     
   })

@csrf_exempt
def create_book(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      book = Book(
         title=data.get('title'),
         author=data.get('author'),
         published_date=data.get('published_date'),
         description=data.get('description'),
         page_count=data.get('page_count'),
         categories=data.get('categories'),
         thumbnail_url=data.get('thumbnail_url')
      )
      book.save()
      return JsonResponse({
         # 'id': book.id,
         'title': book.title,
         'author': book.author,
         'published_date': book.published_date,
         'description': book.description,
         'page_count': book.page_count,
         'categories': book.categories,
         'thumbnail_url': book.thumbnail_url,
      })
   return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

def create_review(request):
   if request.method == "POST":
      data = json.loads(request.body)
      book = get_object_or_404(Book, id=data.get("book_id"))
      user = get_object_or_404(User, id=data.get("user_id"))
      review = BookReview(
         book=book,
         user=user,
         rating=data.get("rating"),
         review_text=data.get("review")
      )
      review.save()
      return JsonResponse({
            'book': review.book.title,
            'user': review.user.username,
            'rating': review.rating,
            'review_text': review.review_text,})
   return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
   
@csrf_exempt
def edit_review(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        review = get_object_or_404(BookReview, id=id)
        review.rating = data.get('rating')
        review.review_text = data.get('review_text')
        review.save()
        return JsonResponse({
            'book': review.book.title,
            'user': review.user.username,
            'rating': review.rating,
            'review_text': review.review_text,
        })
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def delete_review(request, id):
    if request.method == 'POST':
        review = get_object_or_404(BookReview, id=id)
        review.delete()
        return JsonResponse({'success': 'Review deleted'})
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
