class Zoo:
   def __init__(self, zoo_name):
      self.name = zoo_name
      self.animals = []

   def add_animal(self, new_animal):
      self.animals.append(new_animal)

   def get_animals(self):
      for animal in self.animals:
         print(animal)
      
   def sell_animal(self, animal_sold):
      self.animals.remove(animal_sold)

   def sort_animals(self):
      sorted_animals = {}

      for animal in sorted(self.animals):
         f_letter = animal[0].upper()
         if f_letter not in sorted_animals:
            sorted_animals[f_letter] = [animal]
         else:
            sorted_animals[f_letter].append(animal)

      return sorted_animals
   
   def get_groups(self):
      groups = self.sort_animals()

      for key, value in groups.items():
         print(f"{key} : {value}")


      