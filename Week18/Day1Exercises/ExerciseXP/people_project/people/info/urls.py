from django.urls import path
from . import views

urlpatterns = [
   path('', views.display_person, name='display_person'),
   path('people/', views.display_people, name='display_people'),
   path('all_people/', views.display_all_people, name='display_all_people')
]