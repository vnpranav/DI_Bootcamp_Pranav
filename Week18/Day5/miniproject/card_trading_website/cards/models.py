from django.db import models
from django.contrib.auth.models import AbstractUser
import random

# Create your models here.
class User(models.Model):
   id = models.IntegerField(unique=True, primary_key=True)
   username = models.CharField(max_length=100, unique=True)
   email = models.EmailField(unique=True)
   amount_of_money = models.IntegerField(default=10000)
   points = models.IntegerField(default=0)

class Card(models.Model):
   id = models.IntegerField(unique=True, primary_key=True)
   name_character = models.CharField(max_length=100)
   species = models.CharField(max_length=100)
   house = models.CharField(max_length=100)
   image_url = models.URLField()
   date_of_birth = models.DateField(null=True, blank=True)
   patronus = models.CharField(max_length=100)
   price = models.IntegerField(default=random.randint(200, 2000))
   xp_points = models.PositiveIntegerField(default=random.randint(1, 10))
   current_owner = models.ForeignKey(User, related_name='current_cards', on_delete=models.SET_NULL, null=True, blank=True)
   previous_owner = models.ForeignKey(User, related_name='previous_cards', on_delete=models.SET_NULL, null=True, blank=True)