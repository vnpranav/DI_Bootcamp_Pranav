import json, os
file_path = os.path.join(os.path.dirname(__file__), 'datajson.json')

def load_data():
   with open(file_path, 'r') as f:
      data = json.load(f)
   return data

def get_all_animals():
   data = load_data()
   animals = data['animals']
   families = {family['id']: family['name'] for family in data['families']}
   for animal in animals:
      animal['family_name'] = families.get(animal['family'], 'Unknown')
   return animals

def get_all_families():
    data = load_data()
    return [family['name'] for family in data['families']]


def get_one_animal(animal_id):
    data = load_data()
    animals = data['animals']
    families = {family['id']: family['name'] for family in data['families']}
    animal = next((a for a in animals if a['id'] == animal_id), None)
    if animal:
        animal['family_name'] = families.get(animal['family'], 'Unknown')
    return animal

def get_animals_per_family(family_id):
    data = load_data()
    animals = data['animals']
    families = {family['id']: family['name'] for family in data['families']}
    family_animals = [a for a in animals if a['family'] == family_id]
    for animal in family_animals:
        animal['family_name'] = families.get(animal['family'], 'Unknown')
    return family_animals