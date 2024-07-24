import json, os
file_path = os.path.join(os.path.dirname(__file__), 'datajson.json')

class Animal:
    def __init__(self, name, legs, weight, height, speed, family):
        self.name = name
        self.legs = legs
        self.weight = weight
        self.height = height
        self.speed = speed
        self.family = family

    def to_dict(self, animal_id):
        return {
            "id": animal_id,
            "name": self.name,
            "legs": self.legs,
            "weight": self.weight,
            "height": self.height,
            "speed": self.speed,
            "family": self.family
        }


class AnimalData:
    @staticmethod
    def load_data():
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def save_data(data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def add_animal(name, legs, weight, height, speed, family):
        data = AnimalData.load_data()
        animal_id = max(animal['id'] for animal in data['animals']) + 1
        new_animal = Animal(name, legs, weight, height, speed, family)
        data['animals'].append(new_animal.to_dict(animal_id))
        AnimalData.save_data(data)