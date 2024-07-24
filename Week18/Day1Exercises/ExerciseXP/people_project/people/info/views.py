from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
name = 'bob smith'
age = 35
country = 'usa'

def display_person(request):
   person_info = f"Name : {name} \n Age: {age}\n Country: {country}"
   return HttpResponse(person_info)


