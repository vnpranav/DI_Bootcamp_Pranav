from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Author(models.Model):
   name = models.CharField(max_length=100, blank=False)

   def __str__(self):
      return self.name

class Category(models.Model):
   name = models.CharField(max_length=100, blank=False)

   def __str__(self):
      return self.name
   
   def clean(self):
      if 'sunny' in self.name.lower():
         raise ValidationError("Can't have 'sunny' in category name")

   def save(self, *args, **kwargs):
      self.full_clean()
      super().save(*args, **kwargs)
class Book(models.Model):
   title = models.CharField(max_length=200, blank=False)
   author = models.ManyToManyField(Author)
   published_date = models.DateField(blank=False)
   description = models.TextField(blank=False)
   page_count = models.IntegerField(validators=[MinValueValidator(1)])
   categories = models.ManyToManyField(Category)
   thumbnail_url = models.URLField(blank=True)

   def __str__(self):
      return self.title
   
class BookReview(models.Model):
   book = models.ForeignKey(Book, on_delete=models.CASCADE)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
   review_text = models.TextField(blank=False, validators=[MaxValueValidator(10)])   

   def __str__(self):
      return f'Review of {self.book.title} by {self.user.username}'
   



   