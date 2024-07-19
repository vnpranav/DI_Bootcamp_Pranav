class Farm:
   def __init__(self, name):
      self.name = name + "'s Farm" 
      self.animals = []

   def add_animal(self, animal_name, count):
      animal = {
         "name": animal_name,
         "count": count
      }
      self.animals.append(animal)

   def get_info(self):
      print(self.name + "\n\n")
      for animal in self.animals:
         print(f"{animal['name']} : {animal['count']}")

      print("\n\n\t E-I-E-I-O!")

   def get_animal_types(self):
      animal_types = []
      for animal in self.animals:
         if animal['count'] > 1:
            animal_types.append(animal['name'] + 's')
         else:
            animal_types.append(animal['name'])

      return sorted(animal_types)
   
   def get_short_info(self):
      animal_types = self.get_animal_types()
      print(f"{self.name} has {",".join(animal_types)}")

   


