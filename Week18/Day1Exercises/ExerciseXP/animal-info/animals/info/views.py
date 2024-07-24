from django.shortcuts import render
from django.http import HttpResponse
from .data import animals, families
from .read_data import get_all_animals, get_all_families, get_one_animal, get_animals_per_family
from .animals_class import AnimalData

# Create your views here.
# def display_all_animals(request):
#    animals_list = '\n'.join([f"Name: {a['name']}, Legs: {a['legs']}, Weight: {a['weight']}, Height: {a['height']}, Speed: {a['speed']}" for a in animals])
#    return HttpResponse(animals_list)

# def display_all_families(request):
#    family_list = "\n".join([f"Family Name: {f['name']}" for f in families])
#    return HttpResponse(family_list)

# def display_one_animal(request, animal_id):
#    animal = next((a for a in animals if a['id'] == animal_id), None)
#    if animal:
#       animal_info = f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, Height: {animal['height']}, Speed: {animal['speed']}"
#       return HttpResponse(animal_info)
#    return HttpResponse("Animal not found")

# def display_animal_per_family(request, family_id):
#    family_animals = [a for a in animals if a['family'] == family_id]
#    if family_animals:
#       animal_list = "\n".join([f"Name: {a['name']}, Legs: {a['legs']}, Weight: {a['weight']}, Height: {a['height']}, Speed: {a['speed']}" for a in family_animals])
#       return HttpResponse(animal_list)
#    return HttpResponse("No animals found in this family")

def display_all_animals(request):
    animals = get_all_animals()
    animal_list = "\n".join([f"Name: {a['name']}, Legs: {a['legs']}, Weight: {a['weight']}, Height: {a['height']}, Speed: {a['speed']}, Family: {a['family_name']}" for a in animals])
    return HttpResponse(animal_list)

def display_all_families(request):
    families = get_all_families()
    family_list = "\n".join([f"Family Name: {f}" for f in families])
    return HttpResponse(family_list)

def display_one_animal(request, animal_id):
    animal = get_one_animal(animal_id)
    if animal:
        animal_info = f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, Height: {animal['height']}, Speed: {animal['speed']}, Family: {animal['family_name']}"
        return HttpResponse(animal_info)
    return HttpResponse("Animal not found")

def display_animal_per_family(request, family_id):
    family_animals = get_animals_per_family(family_id)
    if family_animals:
        animal_list = "\n".join([f"Name: {a['name']}, Legs: {a['legs']}, Weight: {a['weight']}, Height: {a['height']}, Speed: {a['speed']}, Family: {a['family_name']}" for a in family_animals])
        return HttpResponse(animal_list)
    return HttpResponse("No animals found in this family")

def add_animal(request):
    name = request.GET.get('name')
    legs = int(request.GET.get('legs', 0))
    weight = float(request.GET.get('weight', 0))
    height = float(request.GET.get('height', 0))
    speed = int(request.GET.get('speed', 0))
    family = int(request.GET.get('family', 0))

    if not all([name, legs, weight, height, speed, family]):
        return HttpResponse("Missing one or more parameters", status=400)

    AnimalData.add_animal(name, legs, weight, height, speed, family)
    return HttpResponse(f"Animal {name} added successfully")