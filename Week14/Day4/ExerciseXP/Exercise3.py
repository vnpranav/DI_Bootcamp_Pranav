from Exercise2 import Dog
import random

class PetDog(Dog):
   def __init__(self, name, age, weight):
      Dog.__init__(self,name, age, weight)
      self.trained = False

   def train(self):
      self.trained = True
      self.bark()

   def play(self, *dogs):
      print(f"{','.join(dogs)} all play together")
   
   def do_a_trick(self):
      tricks = [
         "does a barrel roll",
         "shakes your hand",
         "stands on his back legs",
         "plays dead"
      ]

      if self.trained:
         print(f"{self.name} {random.choice(tricks)}")