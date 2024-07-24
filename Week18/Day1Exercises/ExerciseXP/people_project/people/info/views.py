from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
name = 'bob smith'
age = 35
country = 'usa'
people = ['bob','martha', 'fabio', 'john']

all_people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def display_person(request):
   person_info = f"Name : {name} \n Age: {age}\n Country: {country}"
   return HttpResponse(person_info)

def display_people(request):
   persons = "\n".join([p for p in people])
   return HttpResponse(persons)

def display_all_people(request):
   sorted_people = sorted(all_people, key=lambda x: x['age'])
   people_list = "\n".join([f"Name: {person['name']}, Age: {person['age']}, Country: {person['country']}" for person in sorted_people])
   return HttpResponse(people_list)
