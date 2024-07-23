from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
   template = loader.get_template('mytestsubapp/home.html')
   return HttpResponse(template.render({}, request=request))

def welcome(request):
   return HttpResponse("Welcome to the main app")


