import random 

class MyList:
   def __init__(self, letters):
      self.letters = letters
   
   def reverse_list(self):
      return self.letters[::-1]
   
   def sort_list(self):
      return sorted(self.letters)
   
   def generate_random_list(self):
      return [random.randint(0, 100) for i in range(len(self.letters))]